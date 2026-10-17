#!/usr/bin/env python3
"""Contact sheets of the chien-2 images (one per dog, 20 numbered thumbnails in shuffled order)
for Gemini's inspection, before any reading."""
import json, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

D = Path("data/chien2"); O = D / "inspect_build"
items = json.loads((D / "items.json").read_text())
f = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 30)
key = {}
for dog in sorted({i["dog"] for i in items}):
    its = [i for i in items if i["dog"] == dog]; random.Random(dog).shuffle(its)
    sheet = Image.new("RGB", (5 * 400, 4 * 300), "white")
    for k, it in enumerate(its):
        im = Image.open(D / "img" / it["file"]); im.thumbnail((392, 292))
        x, y = (k % 5) * 400 + 4, (k // 5) * 300 + 4
        sheet.paste(im, (x, y)); d = ImageDraw.Draw(sheet)
        d.rectangle([x, y, x + 50, y + 38], fill="yellow"); d.text((x + 6, y + 2), str(k + 1), font=f, fill="black")
        key[f"{dog}#{k + 1}"] = it["file"]
    sheet.save(O / "img" / f"planche_{dog}.jpg", quality=88)
(O / "keymap.json").write_text(json.dumps(key, indent=1))
