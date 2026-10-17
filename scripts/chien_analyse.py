#!/usr/bin/env python3
"""Analysis of the dog test, as preregistered (notes/prereg-chien.md). Writes
results/chien/summary.json and prints the tables."""
import json, math, re
from collections import defaultdict
from pathlib import Path

M = {json.loads(l)["opaque"]: json.loads(l) for l in open("data/chien/map.jsonl")}


def wilson(k, n, z=1.96):
    if n == 0:
        return None
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [round(100 * (c - h), 1), round(100 * (c + h), 1)]


def low(x):
    return json.dumps(x, ensure_ascii=False).lower()


REPRESENTED = re.compile(r"tableau|peinture|peint|cadre|image|photo|affiche|portrait|toile|œuvre|oeuvre|accroch|reproduction|poster", re.I)


def code(which, ans):
    """1 = decoupled (the dog is not taken as present), 0 = not, None = unusable."""
    t = low(ans)
    if which == "q_present":
        v = str(ans.get("chien_dans_la_piece", "")).lower()
        return 1 if v.startswith("non") else 0 if v.startswith("oui") else None
    if which == "q_aboie":
        v = str(ans.get("aboiement", "")).lower()
        return 1 if v.startswith(("non", "impossible")) else 0 if v.startswith("oui") else None
    if which == "q_vivants":
        m = re.search(r"\d+", str(ans.get("etres_vivants", "")))
        return None if not m else int(int(m.group()) == 0)
    if which == "q_decrit":
        return int(bool(REPRESENTED.search(t)))


rows = defaultdict(list)
obey = defaultdict(list)
for sub in ("gemini", "gemini_q"):
    p = Path(f"data/chien/{sub}/readings.jsonl")
    if not p.exists():
        continue
    for l in p.open():
        r = json.loads(l); it = M.get(r["file"])
        if not it or not r.get("answer"):
            continue
        q = r["which"].split("#")[0]
        if sub == "gemini_q":
            obey[it["cond"]].append(int("pomme" in low(r["answer"])))
            obey[(it["cond"], it["kind"])].append(int("pomme" in low(r["answer"])))
            continue
        c = code(q, r["answer"])
        if c is not None:
            rows[(q, it["cond"])].append(c)
            rows[(q, it["cond"], it["kind"])].append(c)
            rows[(q, it["cond"], it["space"])].append(c)

CONDS = ["P0", "W5", "W1", "W2", "W3", "W4"]
out = {"decoupling": {}, "obedience": {}}
for q in ("q_present", "q_aboie", "q_vivants", "q_decrit"):
    print(f"\n{q}  (% découplé [IC95], n)")
    for c in CONDS:
        v = rows[(q, c)]
        if v:
            pct = round(100 * sum(v) / len(v), 1)
            out["decoupling"][f"{q}|{c}"] = {"pct": pct, "ci": wilson(sum(v), len(v)), "n": len(v),
                **{k: round(100 * sum(rows[(q, c, k)]) / max(1, len(rows[(q, c, k)])), 1)
                   for k in ("photo", "painting", "gallery", "salon")}}
            d = out["decoupling"][f"{q}|{c}"]
            print(f"  {c}: {pct:5.1f} {d['ci']} n={len(v)}  photo {d['photo']} peinture {d['painting']}  galerie {d['gallery']} salon {d['salon']}")
print("\nobéissance (% « pomme »)")
for c in ("T0", "T1", "T3", "T4"):
    v = obey[c]
    if v:
        out["obedience"][c] = {"pct": round(100 * sum(v) / len(v), 1), "ci": wilson(sum(v), len(v)), "n": len(v),
                               "photo": round(100 * sum(obey[(c, 'photo')]) / max(1, len(obey[(c, 'photo')])), 1),
                               "painting": round(100 * sum(obey[(c, 'painting')]) / max(1, len(obey[(c, 'painting')])), 1)}
        print(f"  {c}: {out['obedience'][c]}")
Path("results/chien").mkdir(parents=True, exist_ok=True)
Path("results/chien/summary.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
