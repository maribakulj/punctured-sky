#!/usr/bin/env python3
"""Analyse Gemini's blind readings of the YCBA pilot views (data/ycba/gemini/readings.jsonl).

Per view (cropped / unframed / framed / verso / sheet, and SAM crops crop_<view>): median price,
share read as art, museum named as place or owner, artist recognised (surname of the YCBA
creator in the title or subject), separately for well-known painters and the others.
Writes results/ycba/gemini_summary.json.
"""
import json, re, statistics
from collections import defaultdict
from pathlib import Path

FAMOUS = ["Turner", "Constable", "Gainsborough", "Stubbs", "Hogarth", "Reynolds", "Wright",
          "Lawrence", "Zoffany", "Canaletto", "Gheeraerts", "Blake"]
MUSEUM = re.compile(r"mus[ée]e|museum|galerie|gallery|yale|institution|collection publique", re.I)

mp = {json.loads(l)["file"]: json.loads(l)["key"] for l in open("data/blind/map.jsonl") if "ycba|" in l}
pilot = json.loads(Path("data/ycba/pilot.json").read_text())
meta = pilot["meta"]
prints = {str(o) for o in pilot["prints"]}
rd = defaultdict(dict)
for l in open("data/ycba/gemini/readings.jsonl"):
    r = json.loads(l)
    if "file" in r and r.get("answer") and r["file"] in mp:
        rd[mp[r["file"]]][r["which"]] = r["answer"]


def num(x):
    try:
        return float(re.sub(r"[^\d.]", "", str(x)) or "nan")
    except ValueError:
        return float("nan")


groups = defaultdict(list)
for key, ans in rd.items():
    _, obj, view = key.split("|")
    if "social" not in ans:
        continue
    m = meta.get(obj) or meta.get(int(obj)) or {}
    creator = (m.get("creator") or "").split(",")[0]
    surname = creator.split()[-1] if creator else "??"
    fam = "print" if obj in prints else ("famous" if any(f in creator for f in FAMOUS) else "other")
    s = ans["social"]
    text = " ".join(str(v) for v in list(s.values()) + list(ans.get("subject_only", {}).values()))
    groups[(view, fam)].append({
        "obj": obj, "price": num(s.get("prix_euros")),
        "art": str(s.get("art", "")).lower().startswith("oui"),
        "museum_place": bool(MUSEUM.search(str(s.get("lieu", "")))),
        "museum_owner": bool(MUSEUM.search(str(s.get("proprietaire", "")))),
        "artist_named": surname.lower() in text.lower(),
        "frame_mentioned": bool(re.search(r"cadre|frame|dor", text, re.I)),
    })

out = {}
for (view, fam), rows in sorted(groups.items()):
    prices = [r["price"] for r in rows if r["price"] == r["price"]]
    out[f"{view}|{fam}"] = {
        "n": len(rows), "price_median": statistics.median(prices) if prices else None,
        **{k: sum(r[k] for r in rows) for k in ("art", "museum_place", "museum_owner", "artist_named", "frame_mentioned")}}
Path("results/ycba").mkdir(parents=True, exist_ok=True)
Path("results/ycba/gemini_summary.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
for k, v in out.items():
    print(f"{k:28s}", v)

# Paired comparisons: each object against itself across views.
by_obj = defaultdict(dict)
for (view, fam), rows in groups.items():
    for r in rows:
        by_obj[(r["obj"], fam)][view] = r
pairs = {}
for a, b in [("framed", "unframed"), ("framed", "cropped"), ("unframed", "cropped"),
             ("crop_framed", "framed"), ("crop_framed", "cropped"), ("verso", "framed"),
             ("sheet", "cropped"), ("crop_sheet", "sheet")]:
    for fam in ("famous", "other", "print"):
        rat = []
        for (obj, f), v in by_obj.items():
            if f == fam and a in v and b in v and v[a]["price"] > 0 and v[b]["price"] > 0:
                rat.append(v[a]["price"] / v[b]["price"])
        if rat:
            pairs[f"{a}/{b}|{fam}"] = {"n": len(rat), "median_ratio": round(statistics.median(rat), 2),
                                      "higher": sum(x > 1 for x in rat), "equal": sum(x == 1 for x in rat),
                                      "lower": sum(x < 1 for x in rat)}
out["_paired_price"] = pairs
Path("results/ycba/gemini_summary.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print()
for k, v in pairs.items():
    print(f"{k:32s}", v)
