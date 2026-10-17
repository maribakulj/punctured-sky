#!/usr/bin/env python3
"""Part B of notes/prereg-chien-2.md: SmolVLM-500M-Instruct reads the 120 images of the first
dog test (P0, W1-W5, T0-T4) and the 48 English quarantine images (E0/E1/E3/E4).
Two samples per question (temperature 0.7, fixed seed). Resumable: data/chien2/smolvlm.jsonl.
Heavy: run through ~/outils-seg/lourd.sh."""
import json
from pathlib import Path

import torch
from PIL import Image
from transformers import AutoModelForImageTextToText, AutoProcessor

MID = "HuggingFaceTB/SmolVLM-500M-Instruct"
Q = {"q_present": "Is there a dog in this room? Answer yes or no.",
     "q_vivants": "How many living beings (humans or animals) are present in this room? Answer with a number."}
OUT = Path("data/chien2/smolvlm.jsonl")
dev = "mps" if torch.backends.mps.is_available() else "cpu"
proc = AutoProcessor.from_pretrained(MID)
model = AutoModelForImageTextToText.from_pretrained(MID, torch_dtype=torch.bfloat16).to(dev).eval()

jobs = []
for it in json.loads(Path("data/chien/items.json").read_text()):
    qs = ["q_present"] if it["cond"].startswith("T") else list(Q)
    jobs += [(f"data/chien/img/{it['file']}", it, q) for q in qs]
for it in json.loads(Path("data/chien2/items.json").read_text()):
    if it["part"] == "B":
        jobs.append((f"data/chien2/img/{it['file']}", it, "q_present"))

done = set()
if OUT.exists():
    done = {(r["path"], r["which"]) for r in map(json.loads, OUT.open())}
with OUT.open("a") as fo:
    for path, it, q in jobs:
        for rep in (1, 2):
            which = f"{q}#{rep}"
            if (path, which) in done:
                continue
            msgs = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": Q[q]}]}]
            prompt = proc.apply_chat_template(msgs, add_generation_prompt=True)
            inp = proc(text=prompt, images=[Image.open(path).convert("RGB")], return_tensors="pt").to(dev)
            torch.manual_seed(20261017 + rep)
            with torch.no_grad():
                g = model.generate(**inp, max_new_tokens=20, do_sample=True, temperature=0.7)
            ans = proc.batch_decode(g[:, inp["input_ids"].shape[1]:], skip_special_tokens=True)[0].strip()
            row = {"path": path, "file": Path(path).name, "which": which, "cond": it["cond"], "dog": it["dog"],
                   "kind": it["kind"], "space": it["space"], "model": MID, "answer": ans}
            fo.write(json.dumps(row, ensure_ascii=False) + "\n"); fo.flush()
            print(row["file"], which, repr(ans), flush=True)
