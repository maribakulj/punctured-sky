#!/usr/bin/env python3
"""FSA pilot: what the film edge changes to Gemini's blind reading (full scan vs YOLO crop).

Per object, full vs crop: dated year (first 4-digit year or century), read as art, archive /
library / museum named, the support named (negative, film, archive...), price ratio.
Writes results/fsa/summary.json.
"""
import json, re, statistics
from collections import defaultdict
from pathlib import Path

mp = {json.loads(l)["file"]: json.loads(l) for l in open("data/fsa/map.jsonl")}
meta = json.loads(Path("data/fsa/sample.json").read_text())
rd = defaultdict(dict)
for l in open("data/fsa/gemini/readings.jsonl"):
    r = json.loads(l)
    if r.get("answer") and r.get("file") in mp:
        m = mp[r["file"]]
        rd[(m["obj"], m["view"])][r["which"]] = r["answer"]

SUPPORT = re.compile(r"n[ée]gatif|negative|pellicule|film|planche[- ]contact|diapositive|transparen|kodachrome|archive|tirage|scan|perforation", re.I)
INST = re.compile(r"archive|biblioth|library|mus[ée]e|museum|congr[eè]s|collection|fonds|institution", re.I)


def year(s):
    s = str(s)
    m = re.search(r"(1[89]\d\d|20\d\d)", s)
    if m:
        return int(m.group(1))
    m = re.search(r"ann[ée]es\s*(\d0)", s)
    if m:
        return 1900 + int(m.group(1))
    return None


def price(x):
    try:
        return float(re.sub(r"[^\d.]", "", str(x)))
    except ValueError:
        return None


def row(a):
    s, sub = a.get("social", {}), a.get("subject_only", {})
    text = json.dumps(a, ensure_ascii=False)
    return {"year": year(s.get("epoque")), "price": price(s.get("prix_euros")),
            "art": str(s.get("art", "")).lower().startswith("oui"),
            "inst_owner": bool(INST.search(str(s.get("proprietaire", "")))),
            "inst_place": bool(INST.search(str(s.get("lieu", "")))),
            "support_named": bool(SUPPORT.search(text)),
            "support_in_subject": bool(SUPPORT.search(json.dumps(sub, ensure_ascii=False))),
            "photo_object": bool(re.search(r"photograph|photo", str(sub), re.I))}


out = {}
for kind in ("bw", "colour"):
    objs = [o for o, v in meta.items() if v["kind"] == kind and (o, "full") in rd and (o, "crop") in rd
            and "social" in rd[(o, "full")] and "social" in rd[(o, "crop")]]
    R = {v: [row(rd[(o, v)]) for o in objs] for v in ("full", "crop")}
    res = {"n": len(objs)}
    for v, rows in R.items():
        ys = [r["year"] for r in rows if r["year"]]
        ps = [r["price"] for r in rows if r["price"]]
        res[v] = {"year_median": statistics.median(ys) if ys else None,
                  "price_median": statistics.median(ps) if ps else None,
                  **{k: sum(r[k] for r in rows) for k in ("art", "inst_owner", "inst_place", "support_named", "support_in_subject")}}
    rat = [f["price"] / c["price"] for f, c in zip(R["full"], R["crop"]) if f["price"] and c["price"]]
    dy = [f["year"] - c["year"] for f, c in zip(R["full"], R["crop"]) if f["year"] and c["year"]]
    res["price_full_over_crop"] = {"median": statistics.median(rat) if rat else None,
                                   "higher": sum(x > 1 for x in rat), "equal": sum(x == 1 for x in rat), "lower": sum(x < 1 for x in rat)}
    res["year_full_minus_crop"] = {"median": statistics.median(dy) if dy else None,
                                   "older": sum(x < 0 for x in dy), "same": sum(x == 0 for x in dy), "younger": sum(x > 0 for x in dy)}
    out[kind] = res
Path("results/fsa").mkdir(parents=True, exist_ok=True)
Path("results/fsa/summary.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(json.dumps(out, indent=1, ensure_ascii=False))
