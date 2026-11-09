#!/usr/bin/env python3
"""Install free Arc items into a project, in the exact layout the code expects.
RUN this script; do not read it as reference. It never guesses: unknown items,
missing bundles and conflicting files are explicit errors.

Usage:
  python3 scripts/install-item.py --project /path/to/app --item button [--item hero-section]
                                  [--components-dir src/components] [--free-dir /path/to/uiarc-free-code]
                                  [--dry-run] [--force]

Layout produced (the pack's relative imports depend on it):
  <components>/arc/<component>/<files>          free components
  <components>/arc/blocks/<block>/<files>       free blocks
  <components>/arc/lib/<shared lib files>       from any item's lib/* files
  <components>/arc/foundation.css               shared, once (--no-shared to skip)
  <components>/arc/motion-tokens.ts             shared, once
  <components>/arc/lib/motion-tokens.ts         shared, once
Registry dependencies of an item are installed recursively (e.g. hero-section
pulls button, avatar, ...). npm dependencies are only PRINTED, never installed.
"""
import argparse, json, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--project", required=True)
ap.add_argument("--item", action="append", required=True)
ap.add_argument("--components-dir", default="components",
                help="components root inside the project (default: components; use src/components for src/ layouts)")
ap.add_argument("--free-dir", default=None)
ap.add_argument("--dry-run", action="store_true")
ap.add_argument("--force", action="store_true", help="overwrite conflicting existing files")
ap.add_argument("--no-shared", action="store_true")
a = ap.parse_args()

skill_dir = Path(__file__).resolve().parents[1]
idx_path = skill_dir / "data" / "index.json"
if not idx_path.exists():
    sys.exit(f"ERROR: {idx_path} missing; the skill folder is incomplete.")
index = {it["name"]: it for it in json.loads(idx_path.read_text())}

def find_free_dir():
    cands = []
    if a.free_dir:
        cands.append(Path(a.free_dir))
    import os
    if os.environ.get("UIARC_FREE_DIR"):
        cands.append(Path(os.environ["UIARC_FREE_DIR"]))
    cands += [skill_dir.parent / "uiarc-free-code", Path.cwd() / "uiarc-free-code",
              skill_dir / "uiarc-free-code"]
    for c in cands:
        if (c / "INDEX.md").exists() or (c / "components").exists():
            return c
    sys.exit("ERROR: free bundle (uiarc-free-code/) not found. Looked in: "
             + ", ".join(str(c) for c in cands)
             + ". Unzip uiarc-free-code.zip next to the skill folder or pass --free-dir.")

free_dir = find_free_dir()
project = Path(a.project)
arc_root = project / a.components_dir / "arc"

def target_for(bundle_path):
    parts = bundle_path.split("/")
    if parts[0] == "shared":
        rest = parts[2:]
        if rest[0] == "lib":
            return arc_root / "lib" / rest[1]
        return arc_root / rest[0]
    kind_dir, name, rest = parts[0], parts[1], parts[2:]
    if rest[0] == "lib":
        return arc_root / "lib" / rest[1]
    base = arc_root / ("blocks" if kind_dir == "blocks" else "") / name if kind_dir == "blocks" else arc_root / name
    return base.joinpath(*rest)

# resolve closure
todo, seen, missing = list(a.item), [], []
while todo:
    n = todo.pop()
    if n in seen:
        continue
    it = index.get(n)
    if it is None:
        missing.append(n); continue
    if it["tier"] == "pro":
        sys.exit(f"ERROR: '{n}' is a Pro item. Pro source is not in the free bundle; "
                 "build it from its spec instead (see SKILL.md workflow C): uiarc-pro-markdowns/" + (it["markdown"] or ""))
    seen.append(n)
    todo += [d for d in it["registryDependencies"] if d not in seen]
if missing:
    sys.exit("ERROR: unknown item(s): " + ", ".join(sorted(set(missing)))
             + ". Find names with scripts/find-item.py.")
plan = []  # (src, dst)
for n in seen:
    for f in index[n]["files"]:
        plan.append((free_dir / f["bundle_path"], target_for(f["bundle_path"])))
if not a.no_shared:
    for shared_name in ("arc-motion-tokens", "arc-foundation"):
        for f in index[shared_name]["files"]:
            plan.append((free_dir / f["bundle_path"], target_for(f["bundle_path"])))

copied = skipped = 0
conflicts = []
npm = sorted({d for n in seen for d in index[n]["dependencies"]})
for src, dst in plan:
    if not src.exists():
        sys.exit(f"ERROR: bundle file missing: {src}")
    if dst.exists():
        if dst.read_bytes() == src.read_bytes():
            skipped += 1; continue
        if not a.force:
            conflicts.append(str(dst)); continue
    if a.dry_run:
        print(f"WOULD COPY {src.name} -> {dst}")
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
    copied += 1
if conflicts:
    print("CONFLICTS (existing files differ; re-run with --force to overwrite):")
    for c in conflicts:
        print("  " + c)
    sys.exit(2)
print(f"{'DRY RUN: ' if a.dry_run else ''}items: {', '.join(seen)}")
print(f"files {'to copy' if a.dry_run else 'copied'}: {copied}, already identical: {skipped}")
if npm:
    print("npm dependencies to install in the project: " + ", ".join(npm))
print("Reminder: import foundation.css once in the root layout: "
      "import \"<components>/arc/foundation.css\" (per your alias), and set data-theme on <html>.")
