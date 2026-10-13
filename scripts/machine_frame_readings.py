#!/usr/bin/env python3
"""The machine's frame, step 2 — what the crop does to meaning.

For the 30 images where the frame mattered most in the social pilot (child's drawing, beach
snapshot, receipt; five frames; grey and living room), Claude Sonnet reads, blind, the crop that
Grounding DINO + SAM 2.1 drew for "a painting", with the same two questions as before (subject
alone; indirect questions). The answers are compared with the readings of the whole image."""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from punctured_sky.blind import read
from punctured_sky.claude_vision import Cache

CROPS = Path("data/machine_frame/crops")
READS = Cache("data/annotations/machine_frame_readings.jsonl")
CONTENTS = ["child", "beach", "receipt"]
FRAMES = ["none", "modern", "classic", "ebonized", "rococo"]
SPACES = ["grey", "salon"]


def main(threads: int = 2) -> None:
    jobs = []
    for c in CONTENTS:
        for f in FRAMES:
            for s in SPACES:
                p = CROPS / f"{c}__{f}__{s}.jpg"
                if p.exists():
                    for w in ("subject_only", "social"):
                        k = f"mf|{c}|{f}|{s}"
                        if f"{k}#{w}" not in READS:
                            jobs.append((k, p, w))
    print(len(jobs), "readings to do", flush=True)
    with ThreadPoolExecutor(threads) as ex:
        list(ex.map(lambda j: read(j[0], j[1], READS, j[2]), jobs))
    print("done", flush=True)


if __name__ == "__main__":
    main()
