#!/usr/bin/env python3
"""SAM 3 on the YCBA views: where does a concept-prompted segmenter put the edge of the work?

Prompts "painting", "picture frame", "artwork" (framed / unframed views) and "print", "artwork"
(whole sheet). For each, the best-scoring instance box against the museum's image box
(SIFT-registered, data/ycba/pilot.json). Writes data/ycba/sam3.json.
Run as a heavy job: ~/outils-seg/lourd.sh .venv/bin/python scripts/sam3_frame.py [limit]
"""
import json, sys
from pathlib import Path

import torch
from PIL import Image
from transformers import Sam3Model, Sam3Processor


def iou(a, b):
    x0, y0, x1, y1 = max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x1 - x0) * max(0, y1 - y0)
    ar = lambda r: (r[2] - r[0]) * (r[3] - r[1])
    return inter / max(1e-9, ar(a) + ar(b) - inter)


dev = "mps" if torch.backends.mps.is_available() else "cpu"
proc = Sam3Processor.from_pretrained("facebook/sam3")
model = Sam3Model.from_pretrained("facebook/sam3").to(dev).eval()
sel = json.loads(Path("data/ycba/pilot.json").read_text())
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10**9
outp = Path("data/ycba/sam3.json")
out = json.loads(outp.read_text()) if outp.exists() else []
seen = {r["obj"] for r in out}
for obj in (sel["paintings"] + sel["prints"])[:limit]:
    if obj in seen:
        continue
    for v in ("framed", "unframed", "sheet"):
        p = Path(f"data/ycba/img/{obj}__{v}.jpg")
        if not p.exists():
            continue
        im = Image.open(p).convert("RGB")
        mus = sel["museum_image_box"].get(f"{obj}|{v}")
        prompts = ["print", "artwork"] if v == "sheet" else ["painting", "picture frame", "artwork"]
        for pr in prompts:
            inp = proc(images=im, text=pr, return_tensors="pt").to(dev)
            with torch.no_grad():
                o = model(**inp)
            r = proc.post_process_instance_segmentation(o, threshold=0.4, mask_threshold=0.5,
                                                        target_sizes=inp.get("original_sizes").tolist())[0]
            row = {"obj": obj, "view": v, "prompt": pr, "n": len(r["scores"]), "size": list(im.size)}
            if len(r["scores"]):
                i = int(r["scores"].argmax())
                box = [float(x) for x in r["boxes"][i]]
                row.update(score=float(r["scores"][i]), box=box)
                if mus:
                    row["iou_museum_image"] = iou(box, mus[:4])
                    row["area_ratio"] = (box[2] - box[0]) * (box[3] - box[1]) / max(1.0, (mus[2] - mus[0]) * (mus[3] - mus[1]))
            out.append(row)
    print(obj, flush=True)
    Path("data/ycba/sam3.json").write_text(json.dumps(out, indent=1))
print("done")
