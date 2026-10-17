#!/usr/bin/env python3
"""FSA-OWI pilot — the archive's support (film edge) with and without, read by Gemini.

Dialogue with Arnold & Tilton 2026 (Humanités numériques 13): they remove the "frame" (film edges,
mounts) as noise and assert, without measuring, that it disturbs the models. Here we measure what
the support changes to a reading. Public-domain scans from tile.loc.gov (LoC "v" reference JPEGs).
  sample   random b&w negatives (fsa 8a-8e) and colour transparencies (fsac 1a), resumable;
  crop     the photographic area by Arnold & Tilton's own YOLOv8 (data/fsa/project-4.pt);
  blind    opaque copies of full/crop views into data/fsa/gemini/img + data/fsa/map.jsonl.
"""
import hashlib, json, random, shutil, sys, time, urllib.request
from pathlib import Path

D = Path("data/fsa"); IMG = D / "img"
UA = {"User-Agent": "Mozilla/5.0 (punctured-sky research; github.com/maribakulj/punctured-sky)"}
RANGES = {"bw": ("fsa", "8", "abcde", 1, 40000), "colour": ("fsac", "1a", None, 34000, 35999)}


def url(col, id_):
    a, n = id_[:2], int(id_[2:])
    return (f"https://tile.loc.gov/storage-services/service/pnp/{col}/{a}{n // 1000 * 1000:05d}/"
            f"{a}{n // 500 * 500:05d}/{id_}v.jpg")


def sample(n_per=30):
    IMG.mkdir(parents=True, exist_ok=True)
    rng = random.Random(20261017)
    meta = json.loads((D / "sample.json").read_text()) if (D / "sample.json").exists() else {}
    for kind, (col, pre, letters, lo, hi) in RANGES.items():
        tries = 0
        while sum(v["kind"] == kind for v in meta.values()) < n_per and tries < 400:
            tries += 1
            n = rng.randint(lo, hi)
            id_ = (pre + rng.choice(letters) if letters else pre) + f"{n:05d}"
            if id_ in meta:
                continue
            time.sleep(2)
            try:
                b = urllib.request.urlopen(urllib.request.Request(url(col, id_), headers=UA), timeout=60).read()
            except Exception:
                continue
            (IMG / f"{id_}__full.jpg").write_bytes(b)
            meta[id_] = {"kind": kind, "url": url(col, id_)}
            (D / "sample.json").write_text(json.dumps(meta, indent=1))
            print(kind, id_, flush=True)


def crop():
    from ultralytics import YOLO
    from PIL import Image
    m = YOLO(str(D / "project-4.pt"))
    meta = json.loads((D / "sample.json").read_text())
    for id_, v in meta.items():
        im = Image.open(IMG / f"{id_}__full.jpg").convert("RGB")
        r = m.predict(im, verbose=False)[0]
        boxes = [(float(c), [float(x) for x in b]) for b, c in zip(r.boxes.xyxy.tolist(), r.boxes.conf.tolist())]
        v["yolo"] = sorted(boxes, reverse=True)
        v["size"] = list(im.size)
        if boxes:
            c, b = max(boxes)
            v["box"], v["conf"] = b, c
            v["area_kept"] = (b[2] - b[0]) * (b[3] - b[1]) / (im.size[0] * im.size[1])
            im.crop([int(x) for x in b]).save(IMG / f"{id_}__crop.jpg", quality=92)
        print(id_, v.get("conf"), v.get("area_kept"), flush=True)
    (D / "sample.json").write_text(json.dumps(meta, indent=1))
    print(m.names)


def blind():
    g = D / "gemini" / "img"; g.mkdir(parents=True, exist_ok=True)
    rows = []
    for p in sorted(IMG.glob("*.jpg")):
        h = hashlib.sha256(b"fsa-pilot-2026" + p.name.encode()).hexdigest()[:12]
        shutil.copy(p, g / f"{h}.jpg")
        id_, view = p.stem.split("__")
        rows.append({"file": f"{h}.jpg", "obj": id_, "view": view})
    (D / "map.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    shutil.copy("data/ycba/gemini/PROMPTS.md", D / "gemini" / "PROMPTS.md")
    print(len(rows), "images")


if __name__ == "__main__":
    {"sample": sample, "crop": crop, "blind": blind}[sys.argv[1]]()
