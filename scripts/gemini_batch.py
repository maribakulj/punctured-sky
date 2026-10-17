#!/usr/bin/env python3
"""Blind readings by Gemini (agy print mode), one fresh session per image and per question.

Usage: python scripts/gemini_batch.py <dir with img/ PROMPTS.md readings.jsonl> [shard nshards]
Resumable: skips (file, which) pairs already in readings.jsonl.
"""
import json, re, subprocess, sys
from pathlib import Path

d = Path(sys.argv[1]).resolve()
prompts = {}
for block in (d / "PROMPTS.md").read_text().split("\n## ")[1:]:
    name, _, body = block.partition("\n")
    prompts[name.strip()] = body.strip()
out = d / "readings.jsonl"
done = set()
if out.exists():
    for l in out.open():
        try:
            r = json.loads(l)
            done.add((r.get("file"), r.get("which")))
        except Exception:
            pass
shard, nsh = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (0, 1)
for i, f in enumerate(sorted((d / "img").glob("*.jpg"))):
    if i % nsh != shard:
        continue
    for which in prompts:
        if (f.name, which) in done:
            continue
        q = prompts[which] + f"\n\nImage : @{f.relative_to(d)}\nNe lis aucun autre fichier."
        ans = None
        for _ in range(3):
            try:
                p = subprocess.run(["agy", "-p", q, "--print-timeout", "180s"], cwd=d,
                                   capture_output=True, text=True, timeout=240)
            except subprocess.TimeoutExpired:
                continue
            m = re.search(r"\{.*\}", p.stdout, re.S)
            if m:
                try:
                    ans = json.loads(m.group(0)); break
                except Exception:
                    pass
        row = {"file": f.name, "which": which, "model": "gemini-3.8-flash (agy -p)",
               "answer": ans}
        if ans is None:
            print(f.name, which, "FAILED", flush=True); continue
        with out.open("a") as fh:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f.name, which, "ok" if ans else "RAW", flush=True)
