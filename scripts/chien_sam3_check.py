#!/usr/bin/env python3
"""H1 of notes/prereg-chien.md: does SAM 3 ("dog") find the dog in every test image?
Writes results/chien/sam3_check.json. Heavy: run through ~/outils-seg/lourd.sh."""
import json
from pathlib import Path

import torch
from PIL import Image
from transformers import Sam3Model, Sam3Processor

dev = "mps" if torch.backends.mps.is_available() else "cpu"
proc = Sam3Processor.from_pretrained("facebook/sam3")
model = Sam3Model.from_pretrained("facebook/sam3").to(dev).eval()
out = {}
for it in json.loads(Path("data/chien/items.json").read_text()):
    im = Image.open(f"data/chien/img/{it['file']}").convert("RGB")
    inp = proc(images=im, text="dog", return_tensors="pt").to(dev)
    with torch.no_grad():
        o = model(**inp)
    r = proc.post_process_instance_segmentation(o, threshold=0.4, mask_threshold=0.5,
                                                target_sizes=inp.get("original_sizes").tolist())[0]
    out[it["file"]] = {"n": int(len(r["scores"])), "score": float(r["scores"].max()) if len(r["scores"]) else 0.0}
    print(it["file"], out[it["file"]], flush=True)
Path("results/chien").mkdir(parents=True, exist_ok=True)
Path("results/chien/sam3_check.json").write_text(json.dumps(out, indent=1))
