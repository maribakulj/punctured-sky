#!/usr/bin/env python3
"""The machine's frame — where do detectors and segmenters put the edge of "the work"?

On the 100 images of the social pilot, whose content box and framed-object box are known exactly,
each open-vocabulary detector (Grounding DINO base, OWLv2 base) is given five words ("a painting",
"an artwork", "a picture", "a picture frame", "the main subject"); its best box is compared with
the content alone and with the whole framed object. SAM 2.1 then cuts the mask inside the
"a painting" box: that crop is the machine's frame, kept for the next step (what the crop does
to meaning). Writes data/machine_frame/boxes.jsonl and data/machine_frame/crops/.

Run as a heavy job: ~/outils-seg/lourd.sh uv run python scripts/machine_frame.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import torch
from PIL import Image

PROMPTS = ["a painting", "an artwork", "a picture", "a picture frame", "the main subject"]
ITEMS = json.loads(Path("data/social/items.json").read_text())["items"]
OUT = Path("data/machine_frame")
DEV = "mps" if torch.backends.mps.is_available() else "cpu"


def iou(a, b) -> float:
    x0, y0, x1, y1 = max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x1 - x0) * max(0, y1 - y0)
    ua = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter
    return inter / ua if ua > 0 else 0.0


def verdict(box, content, obj) -> str:
    if box is None:
        return "rien"
    ic, io = iou(box, content), iou(box, obj)
    area = (box[2] - box[0]) * (box[3] - box[1])
    oarea = (obj[2] - obj[0]) * (obj[3] - obj[1])
    if io >= 0.75 and io >= ic:
        return "cadre inclus"
    if ic >= 0.75:
        return "contenu seul"
    contains = box[0] <= obj[0] + 5 and box[1] <= obj[1] + 5 and box[2] >= obj[2] - 5 and box[3] >= obj[3] - 5
    if contains and area > 1.3 * oarea:
        return "plus large"
    return "ailleurs"


class GDino:
    name = "grounding-dino-base"

    def __init__(self):
        from transformers import AutoModelForZeroShotObjectDetection, AutoProcessor
        self.p = AutoProcessor.from_pretrained("IDEA-Research/grounding-dino-base")
        self.m = AutoModelForZeroShotObjectDetection.from_pretrained(
            "IDEA-Research/grounding-dino-base").to(DEV).eval()

    @torch.no_grad()
    def best(self, im: Image.Image, prompt: str):
        inp = self.p(images=im, text=prompt + ".", return_tensors="pt").to(DEV)
        out = self.m(**inp)
        r = self.p.post_process_grounded_object_detection(
            out, inp.input_ids, threshold=0.1, text_threshold=0.1, target_sizes=[im.size[::-1]])[0]
        if len(r["scores"]) == 0:
            return None, 0.0
        i = int(r["scores"].argmax())
        return [float(v) for v in r["boxes"][i]], float(r["scores"][i])


class Owl:
    name = "owlv2-base"

    def __init__(self):
        from transformers import Owlv2ForObjectDetection, Owlv2Processor
        self.p = Owlv2Processor.from_pretrained("google/owlv2-base-patch16-ensemble")
        self.m = Owlv2ForObjectDetection.from_pretrained(
            "google/owlv2-base-patch16-ensemble").to(DEV).eval()

    @torch.no_grad()
    def best(self, im: Image.Image, prompt: str):
        inp = self.p(text=[[prompt]], images=im, return_tensors="pt").to(DEV)
        out = self.m(**inp)
        side = max(im.size)  # OWLv2 pads to a square
        r = self.p.post_process_object_detection(out, threshold=0.0, target_sizes=[(side, side)])[0]
        if len(r["scores"]) == 0:
            return None, 0.0
        i = int(r["scores"].argmax())
        b = [float(v) for v in r["boxes"][i]]
        b = [max(0, b[0]), max(0, b[1]), min(im.width, b[2]), min(im.height, b[3])]
        return b, float(r["scores"][i])


class Sam:
    name = "sam2.1-hiera-base-plus"

    def __init__(self):
        from transformers import Sam2Model, Sam2Processor
        self.p = Sam2Processor.from_pretrained("facebook/sam2.1-hiera-base-plus")
        self.m = Sam2Model.from_pretrained("facebook/sam2.1-hiera-base-plus").to(DEV).eval()

    @torch.no_grad()
    def mask(self, im: Image.Image, box) -> np.ndarray:
        inp = self.p(images=im, input_boxes=[[box]], return_tensors="pt").to(DEV)
        out = self.m(**inp, multimask_output=False)
        m = self.p.post_process_masks(out.pred_masks.cpu(), inp["original_sizes"].cpu())[0]
        return m[0, 0].numpy() > 0


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "crops").mkdir(exist_ok=True)
    done = set()
    path = OUT / "boxes.jsonl"
    if path.exists():
        done = {(r["file"], r["model"], r["prompt"]) for r in map(json.loads, path.open())}
    models = [GDino(), Owl()]
    sam = Sam()
    with path.open("a") as fh:
        for n, it in enumerate(ITEMS):
            im = Image.open(Path("data/social/img") / it["file"]).convert("RGB")
            for m in models:
                for p in PROMPTS:
                    if (it["file"], m.name, p) in done:
                        continue
                    box, score = m.best(im, p)
                    row = {"file": it["file"], "content": it["content"], "frame": it["frame"],
                           "space": it["space"], "model": m.name, "prompt": p, "box": box,
                           "score": score,
                           "iou_content": iou(box, it["content_box"]) if box else 0.0,
                           "iou_object": iou(box, it["object_box"]) if box else 0.0,
                           "verdict": verdict(box, it["content_box"], it["object_box"])}
                    if m.name == "grounding-dino-base" and p == "a painting" and box:
                        mk = sam.mask(im, box)
                        ys, xs = np.nonzero(mk)
                        if len(xs):
                            mb = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]
                            row["sam_box"] = mb
                            row["sam_iou_content"] = iou(mb, it["content_box"])
                            row["sam_iou_object"] = iou(mb, it["object_box"])
                            row["sam_verdict"] = verdict(mb, it["content_box"], it["object_box"])
                            im.crop(mb).save(OUT / "crops" / it["file"], quality=92)
                    fh.write(json.dumps(row) + "\n")
                    fh.flush()
            print(n + 1, "/", len(ITEMS), flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    sys.exit(main())
