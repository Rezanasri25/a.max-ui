---
name: uiarc-pack
description: Builds and refactors React and Next.js interfaces with the owner's local Arc UI (uiarc.dev) bundles: 143 free items with full source code (uiarc-free-code) and 233 Pro items as markdown specs (uiarc-pro-markdowns). Use when asked to build a project, page, dashboard, settings screen, pricing, auth, form, table, chart, dialog, AI chat or composer, or any UI with the Arc pack instead of custom UI, and when asked to audit an existing project (custom components, shadcn/ui, MUI, Chakra, Tailwind) and replace its components with pack equivalents: copy free source directly, rebuild Pro items from their specs. Use whenever the two bundle folders are present, or the user mentions the Arc pack, the uiarc bundles, or swapping project components for pack ones.
license: Free bundle content is MIT (Arc). Pro markdown specs are Arc Pro reference documentation; rebuilt code must follow the spec, not claim to be Arc's original source.
compatibility: Needs a filesystem coding agent, the two bundles unzipped (uiarc-free-code/, uiarc-pro-markdowns/), and Python 3 for the bundled scripts (optional but recommended). Targets React 19 / Next.js projects.
metadata:
  version: "1.0.0"
  bundles: "uiarc-free-code (143 items, 334 files) + uiarc-pro-markdowns (233 specs)"
  source: "uiarc.dev catalog and registry, captured 2026-11-05"
---

# Arc UI pack: build with it, or replace a project's UI with it

This skill operates two local bundles of the Arc UI library (uiarc.dev). It does
not contain the library itself; it tells you where everything is, what each item
does, and the exact workflows for using it. Arc's own agent skill (name `arc`)
also exists and is bundled inside the free bundle: it is the authority for
Arc's design rules. This skill is the authority for the bundles: inventories,
offline installation, and replacement work. If both are installed, use both.

## First: locate the bundles (do this before anything else)

Find two folders, `uiarc-free-code/` and `uiarc-pro-markdowns/`, next to this
skill folder, in the project, or in the working directory. If either is missing,
stop and tell the user exactly which folder is missing and where you looked.
Never invent a component, prop, or file that is not in the bundles.

What is inside:

| Bundle | Contents | Truth |
| --- | --- | --- |
| `uiarc-free-code/` | 121 components + 22 blocks with COMPLETE source (.tsx + .module.css + helpers), plus shared foundation, motion tokens, and Arc's own skill files | Real, copyable code (MIT) |
| `uiarc-pro-markdowns/` | 119 Pro components + 114 Pro block pages as markdown specs (props, usage, keyboard, accessibility, motion, responsive, performance) | Specs only. Pro source is token-gated and is NOT in the pack |

## Hard rules

1. **Read before you use.** For a free item, read its actual .tsx in the bundle
   before wiring it. For a Pro item, read its full markdown spec before building
   it. Use only documented props and exports.
2. **Free means copy, not rewrite.** Copy the item's files (use
   scripts/install-item.py) and adapt only data, copy, and the documented
   adaptation points. Never restyle a copied item's internals or its CSS module.
3. **Pro means spec rebuild.** Implement the item from its markdown spec,
   following its documented API, motion, accessibility and responsive behavior.
   Call it a spec-based rebuild in your report; never present it as Arc's
   original source, and never claim to have the Pro source.
4. **Layout is exact.** Installed files live under `<components>/arc/` in the
   layout in references/integration.md. The pack's relative imports depend on
   it. Low freedom here: reproduce, do not improvise.
5. **Verify before you finish.** Run the gates at the bottom of this file on
   every task. A task is not done because files were copied.

## Find an item

- By job: `references/replacement-map.md` (job table) or run
  `python3 scripts/find-item.py "<job words>"` (for example "emoji picker",
  "data table", "dashboard", "model picker"). Add `--tier free` or `--tier pro`
  to filter.
- Full inventories (every item, its files, exports, dependencies, when to use
  and when not to): `references/free-components.md`,
  `references/free-blocks-and-shared.md`, `references/pro-components.md`,
  `references/pro-blocks.md`. These are large; search within them, read the
  entry you need.
- Machine-readable everything: `data/index.json` (grep it; do not read it whole).
- Choosing between close candidates: also check
  `uiarc-free-code/shared/arc-skill/components.md` and the quick-decision rules
  in Arc's bundled SKILL.md.

## Workflow A: build something new with the pack

Copy this checklist and tick it off:

```
- [ ] 1. Plan regions: break the requested screen into regions (shell, header,
         content regions, overlays, states). For each region find a pack item:
         blocks first (they cover whole regions), then components.
- [ ] 2. Foundation: install shared items once (foundation.css, motion tokens)
         via scripts/install-item.py with any first item; import foundation.css
         once in the root layout; set data-theme (and data-accent if asked).
- [ ] 3. Install: scripts/install-item.py --project <app> --item <name> ...
         for every free item chosen (registry dependencies resolve
         automatically). Note the npm dependencies it prints and install them.
- [ ] 4. Rebuild: for every Pro item chosen, read its spec fully and implement
         it under components/arc/ in the same layout, following the spec.
- [ ] 5. Wire: documented props only, real project data, callbacks that are
         typed void | Promise<...> return the promise. Replace every *-data.ts
         sample dataset with real data or clearly-marked placeholders.
- [ ] 6. Compose and style by Arc's rules: read the arc-skill files the task
         needs (composition, design, copy, motion, accessibility, responsive)
         in uiarc-free-code/shared/arc-skill/.
- [ ] 7. States: every data region gets loading, empty, error and success
         states (skeleton, empty-state, inline alert from the pack).
- [ ] 8. Verify: run the gates below.
```

## Workflow B: audit an existing project and replace its UI with the pack

This is a batch, destructive operation: use plan-validate-execute.

```
- [ ] 1. Audit: inventory the project's UI (component folders, routes,
         package.json UI libraries). List every distinct element with its
         path, behavior, props and states. Method: references/replacement-map.md.
- [ ] 2. Match: for each element find pack candidates (find-item.py, the job
         table, inventories). Grade each: direct / adaptable / none.
- [ ] 3. Plan: write arc-replacement-plan.md in the project root (one row per
         element: element + path, pack item or "keep", grade, files/spec,
         adaptations, behavior to preserve). VALIDATE the plan: every pack
         name exists in data/index.json, every free file path exists in the
         bundle, every Pro spec path exists in the pro bundle. Fix until valid.
         Show the plan to the user if the scope is large or any grade is
         "adaptable" with behavior changes.
- [ ] 4. Execute row by row: install (free) or rebuild (Pro), rewire imports
         and props, keep the old code until the row is verified. After each
         row the element must render, interact, and type-check.
- [ ] 5. Sweep: grep the project for leftovers of replaced components and old
         library imports; confirm nothing references deleted code.
- [ ] 6. Verify: run the gates below. Report by plan row: replaced (free,
         copied), replaced (Pro, spec rebuild), kept (no equivalent), kept
         (out of scope).
```

Never replace an element whose behavior the pack item cannot reproduce; grade
it "keep" and say why. Never delete project code before its replacement is
verified. Match by behavior and props surface, not by name.

## Workflow C: use one Pro item

1. Find its spec: `references/pro-blocks.md` / `references/pro-components.md`,
   or find-item.py. Two specs are grouped pages: `sidebar` (4 Pro variants:
   sidebar-rail, workspace-sidebar, inbox-sidebar, docs-sidebar) and `login`
   (Pro variants login-split and login-immersive, plus 3 free variants whose
   real source is in the free bundle).
2. Read the ENTIRE spec file in uiarc-pro-markdowns/ before writing code.
3. Implement under components/arc/ using the pack's tokens and motion presets,
   with the spec's documented props as the public API, its keyboard and
   accessibility behavior, and a reduced-motion branch.
4. If the spec's usage example imports sibling Arc items, install the free ones
   from the bundle and rebuild the Pro ones the same way.
5. Report it as a spec-based rebuild.

## Routing: which file to read when

| Task moment | Read |
| --- | --- |
| Choosing items for a screen or a job | references/replacement-map.md, then the inventory entry |
| Anything about a free component | references/free-components.md, then the item's .tsx in the bundle |
| Anything about a free block or the shared items | references/free-blocks-and-shared.md |
| Anything about a Pro component | references/pro-components.md, then its spec in uiarc-pro-markdowns/components/ |
| Anything about a Pro block | references/pro-blocks.md, then its spec in uiarc-pro-markdowns/blocks/ |
| Installing, layout, imports, deps, theming, fonts | references/integration.md |
| Design, copy, motion, accessibility, responsive rules | the matching file in uiarc-free-code/shared/arc-skill/ (see integration.md table) |
| Final review | uiarc-free-code/shared/arc-skill/checklist.md (always) |

All references are one level from this file on purpose: follow the links here,
not chains inside other files.

## Scripts (run them; do not read them as reference)

- `python3 scripts/find-item.py "date picker"` — ranked search over all 379
  indexed entries (143 free items, 233 Pro specs, 3 shared).
- `python3 scripts/install-item.py --project <app> --item button --item hero-section [--dry-run]`
  — copies free items + recursive registry dependencies + shared foundation and
  motion tokens into the exact arc/ layout; refuses Pro items with a pointer to
  workflow C; reports conflicts instead of overwriting; prints npm dependencies.

## Degrees of freedom

- Low (exact): bundle layout, file names, copying free code, plan validation.
- Medium (spec-bound): Pro rebuilds: the spec fixes the API and behavior; you
  choose internal implementation that satisfies it with pack tokens.
- High (judgment): composition, which item fits a region, copy, data wiring,
  within Arc's rules and the item's documented "when not to use".

## Verification gates (every workflow, in order)

1. The project type check and build pass (or the project's own equivalent).
2. Every pack item used appears in data/index.json; every copied file is
   byte-identical to the bundle except adaptations you list; every Pro item
   used has its spec read and is reported as a rebuild.
3. foundation.css imported exactly once; no raw hex or Tailwind color classes
   on Arc surfaces; no edited internals of copied items.
4. Run uiarc-free-code/shared/arc-skill/checklist.md against the result; fix
   every failing line; run it again.
5. Widths 390, 768, 1024, 1440 checked; loading, empty, error and success
   states present for data regions; keyboard path works for interactive items;
   reduced-motion branch exists for animations you added.

## Report format

End every task with: items used (name, free-copied or Pro-rebuilt, files
touched), adaptations made and why, npm dependencies added, gates run and
their results, and anything kept or skipped with the reason. For workflow B,
report per plan row.

## When not to use this pack

- The project is not React (the pack is React 19 + CSS modules + Motion).
- A region needs behavior no item documents (check "Avoid when" first).
- The user asks for Arc Pro SOURCE code: it is not in the pack and must not be
  fabricated; offer a spec rebuild (workflow C) or a free alternative.
- Arc's separate Pro skills (full-page generation, refactor-to-Arc, audits)
  are account-gated services of uiarc.dev, not files in these bundles; do not
  claim they are included.
