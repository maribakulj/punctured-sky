#!/usr/bin/env python3
"""Sources for the "dog in the painting" test: dog photographs from Wikimedia Commons (quality
images, free licences) and dog paintings from the Met (public domain). Downloads to
data/chien/src/ (>= 2 s between requests) and writes data/chien/src/sources.json."""
import json, time, urllib.parse, urllib.request
from pathlib import Path

UA = {"User-Agent": "punctured-sky/0.1 (research; github.com/maribakulj/punctured-sky)"}
OUT = Path("data/chien/src")
PHOTOS = ["File:Beagle sleeping in Hautmont (DSC07212).jpg",
          "File:20110425 German Shepherd Dog 8505.jpg",
          "File:Benasque - Anciles - Labrador Retriever.jpg",
          "File:Dülmen, Hausdülmen, Golden Retriever -- 2022 -- 5945.jpg",
          "File:Benasque - Linsoles - Galgo 01.jpg",
          "File:Bronco the Beagle.JPG"]
PAINTINGS = [435704, 782306, 437234]  # Bonheur, Landseer, Oudry (Met, public domain)


def get(url):
    time.sleep(2.1)
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src = []
    for i, t in enumerate(PHOTOS):
        q = ("https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo"
             "&iiprop=url|extmetadata&iiurlwidth=1400&titles=" + urllib.parse.quote(t))
        p = next(iter(json.loads(get(q))["query"]["pages"].values()))["imageinfo"][0]
        m = p["extmetadata"]
        name = f"photo{i + 1}.jpg"
        (OUT / name).write_bytes(get(p["thumburl"]))
        src.append({"file": name, "kind": "photo", "title": t, "page": p["descriptionurl"],
                    "licence": m.get("LicenseShortName", {}).get("value"),
                    "author": m.get("Artist", {}).get("value")})
        print(name, src[-1]["licence"])
    for i, oid in enumerate(PAINTINGS):
        o = json.loads(get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}"))
        name = f"painting{i + 1}.jpg"
        (OUT / name).write_bytes(get(o["primaryImageSmall"] or o["primaryImage"]))
        src.append({"file": name, "kind": "painting", "title": o["title"], "artist": o.get("artistDisplayName"),
                    "date": o.get("objectDate"), "page": o.get("objectURL"), "licence": "CC0 (Met Open Access)"})
        print(name, o["title"])
    (OUT / "sources.json").write_text(json.dumps(src, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    import urllib.parse  # noqa: F401
    main()
