#!/usr/bin/env python3
"""Search the Arc pack index. RUN this script; do not read it as reference.

Usage:
  python3 scripts/find-item.py "emoji picker" [--tier free|pro|shared] [--kind component|block] [--limit 10]

Prints ranked matches: name, tier/kind, what it does, and where its code
(free bundle path) or spec (pro bundle markdown) lives.
"""
import argparse, json, re, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("query")
ap.add_argument("--tier", default=None)
ap.add_argument("--kind", default=None)
ap.add_argument("--limit", type=int, default=10)
a = ap.parse_args()

idx_path = Path(__file__).resolve().parents[1] / "data" / "index.json"
if not idx_path.exists():
    sys.exit(f"ERROR: index not found at {idx_path}. The skill folder is incomplete; "
             "data/index.json must sit next to SKILL.md.")
items = json.loads(idx_path.read_text())
terms = [t for t in re.split(r"[^a-z0-9]+", a.query.lower()) if t]

def score(it):
    s = 0
    name = it["name"].lower()
    hay = {
        "name": name.replace("-", " "),
        "title": it["title"].lower(),
        "keywords": " ".join(it.get("keywords", [])).lower(),
        "desc": it["description"].lower(),
        "use": " ".join(it.get("whenToUse", [])).lower(),
        "variants": " ".join(v["name"].replace("-", " ") for v in it.get("variants", [])),
    }
    for t in terms:
        if t == name or t in name.split("-"):
            s += 10
        if t in hay["name"] or t in hay["variants"]:
            s += 5
        if t in hay["title"]:
            s += 4
        if t in hay["keywords"]:
            s += 3
        if t in hay["desc"]:
            s += 2
        if t in hay["use"]:
            s += 1
    return s

rows = []
for it in items:
    if a.tier and it["tier"] != a.tier:
        continue
    if a.kind and it["kind"] != a.kind:
        continue
    sc = score(it)
    if sc > 0:
        rows.append((sc, it))
rows.sort(key=lambda r: (-r[0], r[1]["name"]))
if not rows:
    print("No matches. Try broader words (a job, not a name): e.g. 'date picker', 'table', 'dashboard', 'chat'.")
    sys.exit(0)
for sc, it in rows[: a.limit]:
    where = ("spec: uiarc-pro-markdowns/" + it["markdown"]) if it["tier"] == "pro" else \
        ("code: " + "; ".join("uiarc-free-code/" + f["bundle_path"] for f in it["files"][:4]))
    var = (" variants: " + ", ".join(v["name"] for v in it["variants"])) if it.get("variants") else ""
    print(f"{it['name']} [{it['tier']}/{it['kind']}] - {it['title']}: {it['description']}")
    print(f"    {where}{var}")
