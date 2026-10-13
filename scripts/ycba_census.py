#!/usr/bin/env python3
"""Census of the Yale Center for British Art IIIF manifests: which objects have the four views
(recto cropped to image, recto unframed, recto framed, verso framed) — the museum's own three
edges of the work. One request per 1.2 s; resumable. Writes data/ycba/census.jsonl."""

import json
import sys
import time
import urllib.request
from pathlib import Path

OUT = Path("data/ycba/census.jsonl")
UA = {"User-Agent": "punctured-sky/0.1 (research; github.com/maribakulj/punctured-sky)"}


def meta(d: dict) -> dict:
    m = {}
    for x in d.get("metadata", []):
        k = x["label"]["en"][0]
        m[k] = " | ".join(x["value"].get("en", []))
    return m


def main(lo: int, hi: int) -> None:
    done = set()
    if OUT.exists():
        done = {json.loads(l)["obj"] for l in OUT.open()}
    with OUT.open("a") as fh:
        for i in range(lo, hi):
            if i in done:
                continue
            time.sleep(1.2)
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(
                    f"https://manifests.collections.yale.edu/ycba/obj/{i}", headers=UA), timeout=60))
            except Exception as e:  # noqa: BLE001
                fh.write(json.dumps({"obj": i, "error": str(e)[:80]}) + "\n")
                continue
            m = meta(d)
            views = []
            for c in d.get("items", []):
                try:
                    img = c["items"][0]["items"][0]["body"].get("id")
                except (IndexError, KeyError):
                    img = None
                views.append({"label": ((c.get("label") or {}).get("en") or [""])[0], "image": img})
            fh.write(json.dumps({"obj": i, "collection": m.get("Collection"), "title": m.get("Title"),
                                 "creator": m.get("Creator"), "medium": m.get("Medium"),
                                 "date": m.get("Date"), "rights": m.get("Copyright Statement"),
                                 "call": m.get("Call Number"), "views": views}, ensure_ascii=False) + "\n")
            fh.flush()


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
