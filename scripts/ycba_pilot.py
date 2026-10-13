#!/usr/bin/env python3
"""YCBA pilot — the museum's edges against the machine's.

From the census (data/ycba/census.jsonl): 30 public-domain paintings with the four views (recto
cropped to image, recto unframed, recto framed, verso framed), a third by well-known painters,
and 10 prints with the image alone and the whole sheet. Steps (no language model here):
  build    download the views (IIIF, at most 1200 px), resumable;
  register find the museum's "image" edge inside the framed, unframed and whole-sheet views by
           SIFT keypoints + homography (RANSAC) from the cropped view;
  detect   Grounding DINO, OWLv2 ("a painting", "an artwork", "a picture", "a print") and SAM 2.1
           draw their own edge on the framed, unframed and whole-sheet views.
Writes data/ycba/pilot.json and data/ycba/img/<obj>__<view>.jpg.

Run detect as a heavy job: ~/outils-seg/lourd.sh uv run python scripts/ycba_pilot.py detect
"""

from __future__ import annotations

import importlib.util
import json
import random
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np

CENSUS = Path("data/ycba/census.jsonl")
IMG = Path("data/ycba/img")
PILOT = Path("data/ycba/pilot.json")
UA = {"User-Agent": "punctured-sky/0.1 (research; github.com/maribakulj/punctured-sky)"}
VIEWS = {"recto, cropped to image": "cropped", "recto, unframed": "unframed",
         "recto, framed": "framed", "verso, framed": "verso", "recto": "sheet"}
FAMOUS = ["Turner", "Constable", "Gainsborough", "Stubbs", "Hogarth", "Reynolds", "Wright",
          "Lawrence", "Zoffany", "Canaletto", "Gheeraerts", "Blake"]


def select() -> dict:
    rows = [json.loads(l) for l in CENSUS.open() if '"views"' in l]
    pd = [r for r in rows if (r.get("rights") or "").startswith("Public")]
    def has(r, need):
        labs = {v["label"] for v in r["views"]}
        return all(n in labs for n in need)
    paint = [r for r in pd if r.get("collection") == "Paintings and Sculpture"
             and "oil" in (r.get("medium") or "").lower() and has(
                 r, ["recto, cropped to image", "recto, unframed", "recto, framed", "verso, framed"])]
    prints = [r for r in pd if r.get("collection") != "Paintings and Sculpture"
              and has(r, ["recto, cropped to image", "recto"])]
    rng = random.Random(20261013)
    fam = [r for r in paint if any(f in (r.get("creator") or "") for f in FAMOUS)]
    oth = [r for r in paint if r not in fam]
    chosen = rng.sample(fam, min(10, len(fam))) + rng.sample(oth, min(30 - min(10, len(fam)), len(oth)))
    return {"paintings": [r["obj"] for r in chosen], "prints": [r["obj"] for r in rng.sample(prints, min(10, len(prints)))],
            "counts": {"census": len(rows), "public_domain": len(pd), "paintings_4views": len(paint),
                       "famous_4views": len(fam), "prints_2views": len(prints)}}


def build() -> None:
    sel = select()
    rows = {json.loads(l)["obj"]: json.loads(l) for l in CENSUS.open() if '"views"' in l}
    IMG.mkdir(parents=True, exist_ok=True)
    for obj in sel["paintings"] + sel["prints"]:
        for v in rows[obj]["views"]:
            name = VIEWS.get(v["label"])
            if not name:
                continue
            p = IMG / f"{obj}__{name}.jpg"
            if p.exists():
                continue
            url = v["image"].replace("/full/full/0/", "/full/!1200,1200/0/")
            time.sleep(1.2)
            p.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read())
    sel["meta"] = {o: {k: rows[o].get(k) for k in ("title", "creator", "medium", "call")}
                   for o in sel["paintings"] + sel["prints"]}
    PILOT.write_text(json.dumps(sel, indent=1, ensure_ascii=False))
    print(sel["counts"], len(sel["paintings"]), "paintings,", len(sel["prints"]), "prints")


def locate(small: Path, big: Path) -> list[float] | None:
    """Box of the cropped view inside another view, by SIFT + homography."""
    import cv2
    a = cv2.imread(str(small), cv2.IMREAD_GRAYSCALE)
    b = cv2.imread(str(big), cv2.IMREAD_GRAYSCALE)
    sift = cv2.SIFT_create(4000)
    ka, da = sift.detectAndCompute(a, None)
    kb, db = sift.detectAndCompute(b, None)
    if da is None or db is None:
        return None
    m = cv2.BFMatcher().knnMatch(da, db, k=2)
    good = [x for x, y in (p for p in m if len(p) == 2) if x.distance < 0.75 * y.distance]
    if len(good) < 12:
        return None
    src = np.float32([ka[g.queryIdx].pt for g in good]).reshape(-1, 1, 2)
    dst = np.float32([kb[g.trainIdx].pt for g in good]).reshape(-1, 1, 2)
    H, inl = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
    if H is None or inl.sum() < 12:
        return None
    h, w = a.shape
    pts = cv2.perspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]).reshape(-1, 1, 2), H)
    xs, ys = pts[:, 0, 0], pts[:, 0, 1]
    return [float(xs.min()), float(ys.min()), float(xs.max()), float(ys.max()), int(inl.sum())]


def register() -> None:
    sel = json.loads(PILOT.read_text())
    reg = {}
    for obj in sel["paintings"] + sel["prints"]:
        c = IMG / f"{obj}__cropped.jpg"
        for v in ("framed", "unframed", "sheet"):
            p = IMG / f"{obj}__{v}.jpg"
            if c.exists() and p.exists():
                reg[f"{obj}|{v}"] = locate(c, p)
    sel["museum_image_box"] = reg
    PILOT.write_text(json.dumps(sel, indent=1, ensure_ascii=False))
    ok = sum(v is not None for v in reg.values())
    print(ok, "/", len(reg), "views registered")


def detect() -> None:
    spec = importlib.util.spec_from_file_location("mf", "scripts/machine_frame.py")
    mf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mf)
    from PIL import Image
    sel = json.loads(PILOT.read_text())
    models, sam = [mf.GDino(), mf.Owl()], mf.Sam()
    out = []
    for obj in sel["paintings"] + sel["prints"]:
        for v in ("framed", "unframed", "sheet"):
            p = IMG / f"{obj}__{v}.jpg"
            if not p.exists():
                continue
            im = Image.open(p).convert("RGB")
            mus = sel["museum_image_box"].get(f"{obj}|{v}")
            prompts = ["a print", "an artwork", "a picture"] if v == "sheet" else \
                ["a painting", "an artwork", "a picture"]
            for m in models:
                for pr in prompts:
                    box, score = m.best(im, pr)
                    row = {"obj": obj, "view": v, "model": m.name, "prompt": pr, "box": box,
                           "score": score, "size": list(im.size), "museum_image": mus}
                    if box and mus:
                        row["iou_museum_image"] = mf.iou(box, mus[:4])
                        row["area_ratio"] = ((box[2] - box[0]) * (box[3] - box[1])) / max(
                            1.0, (mus[2] - mus[0]) * (mus[3] - mus[1]))
                    if m.name == "grounding-dino-base" and pr == prompts[0] and box:
                        mk = sam.mask(im, box)
                        ys, xs = np.nonzero(mk)
                        if len(xs):
                            sb = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]
                            row["sam_box"] = sb
                            if mus:
                                row["sam_iou_museum_image"] = mf.iou(sb, mus[:4])
                            (IMG.parent / "crops").mkdir(exist_ok=True)
                            im.crop(sb).save(IMG.parent / "crops" / f"{obj}__{v}.jpg", quality=92)
                    out.append(row)
        print(obj, flush=True)
    Path("data/ycba/detections.json").write_text(json.dumps(out, indent=1))
    print("done")


if __name__ == "__main__":
    {"build": build, "register": register, "detect": detect}[sys.argv[1]]()
