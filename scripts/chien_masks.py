#!/usr/bin/env python3
"""SAM 3 masks for the dog test: the dog in each source (prompt "dog", best instance) and the
floor of the salon (prompt "floor"). Writes data/chien/masks/<name>.png and masks.json.
Heavy: ~/outils-seg/lourd.sh .venv/bin/python scripts/chien_masks.py"""
import json
from pathlib import Path

import numpy as np
import torch
from PIL import Image
from transformers import Sam3Model, Sam3Processor

dev = "mps" if torch.backends.mps.is_available() else "cpu"
proc = Sam3Processor.from_pretrained("facebook/sam3")
model = Sam3Model.from_pretrained("facebook/sam3").to(dev).eval()
OUT = Path("data/chien/masks"); OUT.mkdir(parents=True, exist_ok=True)
jobs = [(f"data/chien/src/{n}.jpg", "dog", n) for n in
        ["photo2", "photo3", "photo6", "painting1", "painting2", "painting3"]]
jobs.append(("data/social/src/hi/space_salon.jpg", "floor", "salon_floor"))
meta = {}
for path, prompt, name in jobs:
    im = Image.open(path).convert("RGB")
    inp = proc(images=im, text=prompt, return_tensors="pt").to(dev)
    with torch.no_grad():
        o = model(**inp)
    r = proc.post_process_instance_segmentation(o, threshold=0.4, mask_threshold=0.5,
                                                target_sizes=inp.get("original_sizes").tolist())[0]
    if not len(r["scores"]):
        meta[name] = {"found": 0}; print(name, "none"); continue
    if prompt == "floor":
        m = (r["masks"].float().sum(0) > 0).cpu().numpy()
    else:
        m = r["masks"][int(r["scores"].argmax())].cpu().numpy().astype(bool)
    Image.fromarray((m * 255).astype(np.uint8)).save(OUT / f"{name}.png")
    ys, xs = np.nonzero(m)
    meta[name] = {"found": int(len(r["scores"])), "score": float(r["scores"].max()),
                  "bbox": [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())],
                  "area_frac": float(m.mean()), "size": list(im.size)}
    print(name, meta[name])
(OUT / "masks.json").write_text(json.dumps(meta, indent=1))
