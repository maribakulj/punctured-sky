#!/usr/bin/env python3
"""Judge Gemini's subject answers (social pilot) with the same blind Haiku judge as Claude's."""

import importlib.util
from concurrent.futures import ThreadPoolExecutor

from punctured_sky.blind import _call
from punctured_sky.claude_vision import Cache

spec = importlib.util.spec_from_file_location("sr", "scripts/social_readings.py")
sr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sr)
spec = importlib.util.spec_from_file_location("sa", "scripts/social_analyse.py")
sa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sa)
JUDGED = Cache("data/annotations/social_judged_gemini.jsonl")


def one(k: str, desc: str) -> None:
    if k in JUDGED:
        return
    for _ in range(3):
        try:
            ans, mid = _call(sr.JUDGE.format(what=sr.WHAT[k.split("|")[1]], desc=desc), "haiku")
            JUDGED.add(k, {"model": mid, **ans})
            return
        except Exception as e:  # noqa: BLE001
            if "limit" in str(e).lower():
                raise


rows = sa.load("gemini")
with ThreadPoolExecutor(2) as ex:
    list(ex.map(lambda kv: one(kv[0], kv[1]["subject"]), rows.items()))
print("judged", len(JUDGED.data))
