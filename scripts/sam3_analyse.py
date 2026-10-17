#!/usr/bin/env python3
"""Summarise data/ycba/sam3.json: per view and prompt, where SAM 3 puts the edge.

area_ratio = detected box / museum image box. ~1 = the canvas alone (or the image of the print);
>1.3 = frame (or sheet margin) included; <0.8 = part only (or something else). Writes
results/ycba/sam3_summary.json.
"""
import json, statistics
from collections import defaultdict
from pathlib import Path

rows = json.loads(Path("data/ycba/sam3.json").read_text())
g = defaultdict(list)
for r in rows:
    g[(r["view"], r["prompt"])].append(r)
out = {}
for (v, p), rs in sorted(g.items()):
    ar = [r["area_ratio"] for r in rs if "area_ratio" in r]
    out[f"{v}|{p}"] = {
        "n": len(rs), "found": sum(r["n"] > 0 for r in rs),
        "median_area_ratio": round(statistics.median(ar), 2) if ar else None,
        "canvas_only (0.8-1.3)": sum(0.8 <= a <= 1.3 for a in ar),
        "frame_or_margin (>1.3)": sum(a > 1.3 for a in ar),
        "part_or_other (<0.8)": sum(a < 0.8 for a in ar),
        "median_iou_museum_image": round(statistics.median([r["iou_museum_image"] for r in rs if "iou_museum_image" in r]), 2) if ar else None}
Path("results/ycba/sam3_summary.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
for k, v in out.items():
    print(f"{k:24s}", v)
