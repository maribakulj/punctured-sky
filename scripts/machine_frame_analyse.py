#!/usr/bin/env python3
"""The machine's frame — summary. Step 1: where detectors put the edge of "the work" (content
alone, frame included, wider, elsewhere), per word and frame. Step 2: what Claude says of the
machine's crop compared with the whole image (price, place read as a museum, institutional owner).
Writes results/machine_frame/summary.json."""

from __future__ import annotations

import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median

spec = importlib.util.spec_from_file_location("sa", "scripts/social_analyse.py")
sa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sa)


def step1() -> dict:
    rows = [json.loads(l) for l in open("data/machine_frame/boxes.jsonl")]
    out = defaultdict(dict)
    for r in rows:
        if r["frame"] == "none":  # content and object coincide: the verdict says nothing
            continue
        out[f"{r['model']}|{r['prompt']}"].setdefault(r["space"], Counter())[r["verdict"]] += 1
    sam = Counter(r["sam_verdict"] for r in rows if r.get("sam_verdict") and r["frame"] != "none")
    return {"detectors": {k: {s: dict(c) for s, c in v.items()} for k, v in out.items()},
            "sam_on_painting_box": dict(sam)}


def step2() -> dict:
    whole = sa.load("claude")
    crops = defaultdict(dict)
    for l in open("data/annotations/machine_frame_readings.jsonl"):
        r = json.loads(l)
        crops[r["item"].replace("mf|", "soc|")][r["which"]] = r
    res = {}
    for k, c in crops.items():
        if "social" not in c:
            continue
        w = whole[k]["social"]
        res[k] = {"price_whole": sa.price(w.get("prix_euros")),
                  "price_crop": sa.price(c["social"].get("prix_euros")),
                  "museum_whole": bool(sa.MUSEUM.search(str(w.get("lieu", "")))),
                  "museum_crop": bool(sa.MUSEUM.search(str(c["social"].get("lieu", "")))),
                  "owner_inst_whole": bool(sa.INSTIT.search(str(w.get("proprietaire", "")))),
                  "owner_inst_crop": bool(sa.INSTIT.search(str(c["social"].get("proprietaire", "")))),
                  "lieu_crop": c["social"].get("lieu"), "subject_crop": c.get("subject_only", {}).get("subject")}
    by = defaultdict(list)
    for k, v in res.items():
        _, content, frame, space = k.split("|")
        by[(space, frame)].append(v)
    table = {}
    for (space, frame), vs in sorted(by.items()):
        table[f"{space}|{frame}"] = {
            "n": len(vs),
            "price_whole_median": median([v["price_whole"] for v in vs if v["price_whole"] is not None]),
            "price_crop_median": median([v["price_crop"] for v in vs if v["price_crop"] is not None]),
            "museum_whole": sum(v["museum_whole"] for v in vs), "museum_crop": sum(v["museum_crop"] for v in vs),
            "owner_inst_whole": sum(v["owner_inst_whole"] for v in vs),
            "owner_inst_crop": sum(v["owner_inst_crop"] for v in vs)}
    return {"per_image": res, "by_space_frame": table}


def main() -> None:
    out = {"step1": step1(), "step2": step2()}
    Path("results/machine_frame").mkdir(parents=True, exist_ok=True)
    json.dump(out, open("results/machine_frame/summary.json", "w"), indent=1, ensure_ascii=False)
    print("SAM sur la boîte « a painting » (images encadrées) :", out["step1"]["sam_on_painting_box"])
    print("\nespace|cadre   n  prix entier → découpé   musée entier → découpé   propriétaire institution")
    for k, v in out["step2"]["by_space_frame"].items():
        print(f"{k:18s} {v['n']}  {v['price_whole_median']:>10.2f} → {v['price_crop_median']:<10.2f}"
              f"   {v['museum_whole']} → {v['museum_crop']}            {v['owner_inst_whole']} → {v['owner_inst_crop']}")


if __name__ == "__main__":
    main()
