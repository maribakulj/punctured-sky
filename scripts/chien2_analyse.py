#!/usr/bin/env python3
"""Analysis of notes/prereg-chien-2.md. Part A: Gemini readings in data/chien2/gemini.
Part B: SmolVLM readings in data/chien2/smolvlm.jsonl. Writes results/chien2/summary.json."""
import importlib.util, json, re
from collections import defaultdict
from pathlib import Path

src = Path("scripts/chien_analyse.py").read_text().split("\nrows = defaultdict")[0]
ca = {}; exec(compile(src.replace('M = {json.loads(l)["opaque"]: json.loads(l) for l in open("data/chien/map.jsonl")}', ""), "ca", "exec"), ca)
wilson, code = ca["wilson"], ca["code"]


def stat(v):
    return {"pct": round(100 * sum(v) / len(v), 1), "ci": wilson(sum(v), len(v)), "n": len(v)} if v else None


def verdict(a, b):
    """a - b in points, with the preregistered rule."""
    if not a or not b:
        return None
    d = a["pct"] - b["pct"]
    sep = a["ci"][0] > b["ci"][1] or b["ci"][0] > a["ci"][1]
    v = "retenu" if abs(d) >= 15 and sep else "négligeable" if abs(d) < 5 else "indéterminé"
    return {"diff": round(d, 1), "verdict": v}


out = {}
# ---- part A
M = {json.loads(l)["opaque"]: json.loads(l) for l in open("data/chien2/map.jsonl")}
A = defaultdict(list)
p = Path("data/chien2/gemini/readings.jsonl")
for l in (p.open() if p.exists() else []):
    r = json.loads(l); it = M.get(r["file"])
    if not it or not r.get("answer"):
        continue
    q = r["which"].split("#")[0]; c = code(q, r["answer"])
    if c is None:
        continue
    for k in [(q, it["cond"]), (q, it["cond"], it["kind"]), (q, it["cond"], it["space"])]:
        A[k].append(c)
SA = {"|".join(k): stat(v) for k, v in A.items()}
g = lambda c, q="q_present": SA.get(f"{q}|{c}")
out["A"] = {"stats": SA, "tests": {
    "A0_W1>=90": g("W1") and g("W1")["pct"] >= 90, "A0_W5_20-80": g("W5") and 20 <= g("W5")["pct"] <= 80,
    "A1_B2<W1": verdict(g("W1"), g("B2")), "A2_B1-W1": verdict(g("B1"), g("W1")),
    "A3_B3<B1": verdict(g("B1"), g("B3")), "A4_B4<W1": verdict(g("W1"), g("B4")),
    "e_B2>=90": g("B2") and g("B2")["pct"] >= 90, "f_B3>=90": g("B3") and g("B3")["pct"] >= 90}}
# ---- part B
B = defaultdict(list); OB = defaultdict(list); raw = defaultdict(lambda: defaultdict(int))
p = Path("data/chien2/smolvlm.jsonl")
for l in (p.open() if p.exists() else []):
    r = json.loads(l); q = r["which"].split("#")[0]; a = r["answer"].lower(); c = r["cond"]
    raw[c][a[:20]] += 1
    if c[0] in "TE":
        OB[c].append(int(("apple" if c[0] == "E" else "pomme") in a)); OB[(c, r["kind"])].append(OB[c][-1])
        continue
    if q == "q_present":
        v = 1 if re.match(r"\W*no\b", a) else 0 if re.match(r"\W*yes\b", a) else None
    else:
        m = re.search(r"\d+", a); words = {"zero": 0, "none": 0, "one": 1, "two": 2, "three": 3}
        n = int(m.group()) if m else next((v for w, v in words.items() if re.search(rf"\b{w}\b", a)), None)
        v = None if n is None else int(n == 0)
    if v is not None:
        B[(q, c)].append(v); B[(q, c, r["kind"])].append(v)
SB = {"|".join(k): stat(v) for k, v in B.items()}
SO = {(k if isinstance(k, str) else "|".join(k)): stat(v) for k, v in OB.items()}
h = lambda c: SB.get(f"q_present|{c}")
p0 = h("P0")
out["B"] = {"stats": SB, "obeissance": SO, "raw": {k: dict(v) for k, v in raw.items()}, "tests": {
    "B0_P0_yes>=80": p0 and (100 - p0["pct"]) >= 80,
    "B1_W3-W1": verdict(h("W3"), h("W1")), "B1_order": [h(c) and h(c)["pct"] for c in ("W1", "W2", "W3")],
    "B2_W3-W4": verdict(h("W3"), h("W4")),
    "B3_T0>=30": {"FR": SO.get("T0") and SO["T0"]["pct"] >= 30, "EN": SO.get("E0") and SO["E0"]["pct"] >= 30},
    "B3_T0-T3": verdict(SO.get("T0"), SO.get("T3")), "B3_E0-E3": verdict(SO.get("E0"), SO.get("E3")),
    "B3_E1-E3": verdict(SO.get("E1"), SO.get("E3"))}}
Path("results/chien2").mkdir(parents=True, exist_ok=True)
Path("results/chien2/summary.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
for part in ("A", "B"):
    print(f"== {part}")
    for k, v in sorted(out[part]["stats"].items()):
        if k.count("|") == 1:
            print(f"  {k:16s} {v['pct']:5.1f} {v['ci']} n={v['n']}")
    print("  tests:", json.dumps(out[part]["tests"], ensure_ascii=False))
print("obéissance B:", {k: v["pct"] for k, v in SO.items() if "|" not in k})
