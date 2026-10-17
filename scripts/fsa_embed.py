#!/usr/bin/env python3
"""FSA pilot, encoders: does the film edge disturb image embeddings (Arnold & Tilton's claim)?

For CLIP, SigLIP, DINOv2 (src encoders, letterboxed) and DINOv3 ViT-B (CLS token):
  self_sim      cosine(full, crop) of the same photo;
  other_full    mean cosine between full scans of different photos (same kind);
  other_crop    the same between crops: if other_full > other_crop, the edge makes photos alike;
  top1          share of crops whose nearest full scan is their own.
Writes results/fsa/embed.json.
"""
import json, sys
from pathlib import Path

import numpy as np
import torch
from PIL import Image

sys.path.insert(0, "src")
from punctured_sky.encoders import Encoder, letterbox  # noqa: E402

meta = json.loads(Path("data/fsa/sample.json").read_text())
objs = [o for o, v in meta.items() if (v.get("conf") or 0) >= 0.9 and (v.get("area_kept") or 0) >= 0.5]
kinds = np.array([meta[o]["kind"] for o in objs])
full = [Image.open(f"data/fsa/img/{o}__full.jpg").convert("RGB") for o in objs]
crop = [Image.open(f"data/fsa/img/{o}__crop.jpg").convert("RGB") for o in objs]


def dinov3(ims):
    from transformers import AutoImageProcessor, AutoModel
    repo = "facebook/dinov3-vitb16-pretrain-lvd1689m"
    proc, m = AutoImageProcessor.from_pretrained(repo), AutoModel.from_pretrained(repo).eval()
    out = []
    with torch.no_grad():
        for im in ims:
            o = m(**proc(images=letterbox(im), return_tensors="pt"))
            out.append(o.last_hidden_state[0, 0].numpy())
    return np.array(out)


res = {"n": len(objs), "n_bw": int((kinds == "bw").sum())}
for name in ("clip", "siglip", "dinov2", "dinov3"):
    if name == "dinov3":
        F, C = dinov3(full), dinov3(crop)
    else:
        e = Encoder(name)
        F, C = e.images(full), e.images(crop)
    F = F / np.linalg.norm(F, axis=1, keepdims=True)
    C = C / np.linalg.norm(C, axis=1, keepdims=True)
    S = C @ F.T
    r = {"self_sim": float(np.mean(np.diag(S))),
         "top1": float(np.mean(S.argmax(1) == np.arange(len(objs))))}
    for k in ("bw", "colour"):
        idx = np.where(kinds == k)[0]
        off = ~np.eye(len(idx), dtype=bool)
        r[f"other_full_{k}"] = float((F[idx] @ F[idx].T)[off].mean())
        r[f"other_crop_{k}"] = float((C[idx] @ C[idx].T)[off].mean())
    res[name] = r
    print(name, {k: round(v, 3) for k, v in r.items()}, flush=True)
Path("results/fsa/embed.json").write_text(json.dumps(res, indent=1))
