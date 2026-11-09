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


---

# STANDALONE APPENDIX — all references inline

This standalone edition contains the full text of every reference file of the
folder edition, appended below, for models that cannot load a skill folder.
The folder edition (uiarc-pack/) is canonical; content is identical.


---

<!-- references/replacement-map.md -->

# Replacement map — matching existing UI to the pack

## Contents

- Find by job (table below)
- Mapping from other libraries and hand-rolled UI
- The audit method (used by SKILL.md workflow B)

## Find by job

Free = real source in the free bundle, copy it. Pro = markdown spec in the pro
bundle, rebuild from the spec. Before choosing, read the item's "Use when /
Avoid when" in its inventory entry (references/) or its arc-skill components.md
entry (`uiarc-free-code/shared/arc-skill/components.md`), and prefer a block
over assembling components when a block matches the whole region.

| Job | Free (copy source) | Pro (rebuild from spec) |
| --- | --- | --- |
| Buttons and primary actions | `button`, `action-button`, `split-button`, `button-group`, `floating-button-group`, `expanding-button-group`, `copy-button` | `action-morph` |
| Destructive confirmation | `confirm-morph`, `hold-to-confirm` | — |
| Menus (dropdown, context, user) | `dropdown-menu`, `context-menu`, `user-menu` | `mega-menu-morph`, `glass-menu`, `orbit-menu` |
| Theme switching | `theme-switch`, `theme-switch-eclipse`, `theme-switch-split`, `theme-switch-rise` | — |
| Text inputs and forms | `input`, `textarea`, `password-field`, `password-strength`, `search-field`, `expanding-search`, `inline-edit`, `number-field`, `money-input`, `phone-input`, `scrub-input`, `tag-input`, `mention-input`, `shortcut-recorder` | `smart-form-fill`, `multi-step-form` |
| Selects and choice controls | `select`, `combobox`, `multi-select`, `morph-select`, `chip-group`, `radio-cards`, `radio-group`, `checkbox`, `switch`, `segmented-control`, `toggle-group`, `billing-toggle` | `availability-picker` |
| Sliders and ratings | `slider`, `elastic-slider`, `range-histogram-slider`, `ruler-slider`, `rating` | — |
| Date and time | `calendar`, `date-picker`, `date-range-picker`, `time-picker` | `week-calendar` |
| Pickers (color, emoji, avatar) | `color-picker` | `emoji-picker`, `avatar-upload` |
| File upload | `file-dropzone` | — |
| Rich text and chat input | `rich-text-editor`, `chat-thread`, `comment-thread` | `ai-composer` |
| Overlays: dialog, drawer, sheets | `dialog`, `drawer`, `bottom-sheet`, `popover`, `hover-card`, `tooltip` | `sheet-stack`, `share-sheet`, `confirm-popover` |
| Navigation: tabs, breadcrumb, pagination | `tabs`, `breadcrumb`, `pagination`, `accordion`, `scroll-area` | `toc-progress`, `morph-nav` |
| App shell and sidebars | — | `sidebar`, `metrics-dashboard` |
| Tables and data grids | `sortable-data-table`, `tree-table`, `tree-view`, `filter-toolbar` | `team-directory`, `project-board`, `kanban-board` |
| Charts | `bar-chart`, `line-chart`, `donut-chart`, `sparkline`, `streamgraph`, `brush-chart`, `ridgeline`, `treemap`, `waffle-chart`, `slope-chart`, `gauge`, `activity-heatmap` | `horizon-chart`, `funnel-chart`, `race-bar-chart`, `radar-chart` |
| Cards and metrics | `card`, `metric-card`, `expandable-card`, `empty-state` | `ai-insight-card`, `metric-ticker` |
| Feedback: toast, alert, progress, loading | `toast`, `toast-stack`, `alert`, `skeleton`, `progress`, `usage-meter`, `countdown`, `announcement-bar`, `cookie-consent` | `undo-toast` |
| Avatars and people | `avatar`, `avatar-group` | `presence-stack`, `team-members`, `team-switcher` |
| Text effects | `text-reveal`, `text-morph`, `text-shimmer`, `slot-text`, `expandable-text`, `in-view-title` | — |
| Media: carousel, compare, galleries | `carousel`, `image-compare`, `card-stack` | `lightbox-gallery`, `product-gallery`, `media-player` |
| Auth pages | `sign-in`, `login-centered`, `signup-form` | `login` |
| Marketing sections | `hero-section`, `faq-section`, `plan-comparison`, `comparison-table`, `logo-marquee`, `blog-grid`, `stats-band`, `cta-section`, `newsletter-signup`, `contact-section`, `site-header`, `site-footer`, `page-header` | `pricing-calculator`, `hero-signup` |
| Dashboards and admin | `metric-card`, `empty-states` | `metrics-dashboard`, `settings-page`, `security-settings`, `profile-page`, `billing-overview`, `invoice-studio` |
| Inbox, notifications, commands | `notification-center`, `command-palette`, `otp-input`, `file-upload`, `changelog-feed` | `inbox-triage`, `settings-command` |
| AI product UI | — | `ai-composer`, `ai-chat`, `model-picker`, `model-arena`, `ai-search-bar`, `ai-answer`, `ai-side-panel`, `ai-command`, `context-window` |
| Onboarding | `onboarding-checklist` | `onboarding-survey`, `ai-setup-wizard` |
| Steps and timelines | `stepper`, `timeline` | — |
| Code and data display | `code-block`, `json-viewer` | — |

## Mapping from other libraries and hand-rolled UI

Match by BEHAVIOR AND PROPS SURFACE, not by name. Common translations:

| Existing | Pack equivalent | Notes |
| --- | --- | --- |
| shadcn/ui button, MUI Button, hand-rolled `<button>` | `button` (free) | variant primary/secondary/ghost/danger; loading state built in |
| shadcn dialog / radix dialog / modal divs | `dialog` (free) | drawer for side detail, bottom-sheet for phone-first tasks |
| shadcn dropdown-menu, context menu | `dropdown-menu`, `context-menu` (free) | user-menu for account menus |
| shadcn select, native `<select>` | `select` / `combobox` (free) | combobox when the list is searchable or long |
| shadcn table, MUI DataGrid (simple), hand tables | `sortable-data-table` (free) | tree-table for hierarchical rows |
| shadcn toast / sonner | `toast` or `toast-stack` (free) | never the only confirmation for a foreground action |
| shadcn skeleton, spinners as page loading | `skeleton` (free) | plus empty-state and inline alert for the other states |
| shadcn tabs | `tabs` (free); `segmented-control` for 2-5 views of the same data | Arc's own quick-decision rule, see arc-skill SKILL.md |
| shadcn switch / checkbox | `switch` for immediate on/off, `checkbox` for submit forms (free) | Arc's own quick-decision rule |
| Recharts / hand SVG charts | free chart components by chart type | match chart TYPE and data shape, not just "a chart" |
| Custom sidebar layouts | Pro `sidebar` spec (4 variants) or free blocks for narrower shells | sidebar is a grouped spec page |
| Custom AI chat / model switchers | Pro `ai-composer`, `ai-chat`, `model-picker` specs | spec rebuilds; keep the project's data wiring |
| Pricing tables (custom or MUI) | free `plan-comparison`; worked example in arc-skill example-pricing.md | Pro pricing-calculator / usage-pricing for interactive pricing |
| Auth screens (custom) | free `sign-in`, `login-centered`, `signup-form`; Pro `login` grouped spec | login page also documents the free variants |

Anything with no equivalent in the table or inventories: leave it as is and
list it under "no equivalent" in the replacement plan. Do not force a match.

## The audit method (used by SKILL.md workflow B)

1. Inventory the project's UI: components folder(s), page/route files, and the
   UI library (if any) in package.json. List every distinct UI element with
   its file path and what it does (behavior, props, states).
2. For each element, find pack candidates: run scripts/find-item.py with the
   JOB words, check the table above, then read the candidate's inventory entry
   and its source (free) or spec (pro). Record match quality: direct (same job
   and props surface), adaptable (same job, minor prop/data adaptation), or
   none.
3. Write the plan BEFORE touching code (plan-validate-execute): a file
   `arc-replacement-plan.md` in the project root with one row per element:
   project element + path, pack item or "keep", match quality, files to copy
   or spec to follow, adaptations, and the state/behavior that must be
   preserved. Validate the plan: every named pack item exists in
   data/index.json, every free file path exists in the bundle, every pro spec
   path exists in the pro bundle. Fix the plan until it validates.
4. Execute row by row. After each row: the element renders, its interactions
   and states work, and the project's type check passes. Keep a row's old code
   until its replacement is verified.
5. Finish with the verification gates in SKILL.md and delete the plan file
   only after the final report is delivered (or keep it if the user wants the
   audit trail).


---

<!-- references/integration.md -->

# Integration — installing the pack into a project

## Contents

- The installed layout (exact, non-negotiable)
- Why the layout is exact: the import graph
- Setup, step by step
- npm dependencies
- Theming and fonts
- Design, motion, accessibility and copy rules (routed, not duplicated)
- Framework notes (Next.js vs plain React)
- Verification after installing

## The installed layout (exact, non-negotiable)

```
<components>/arc/
  foundation.css            from shared/arc-foundation (install once)
  motion-tokens.ts          from shared/arc-motion-tokens (install once)
  lib/
    motion-tokens.ts        from shared/arc-motion-tokens/lib (re-export used by items)
    use-today.ts            lib helper, copied from the items that list it
    use-copy-feedback.ts    lib helper
    media.ts                lib helper
    arc-provider.tsx        lib helper
  <component-name>/         one folder per free component: <name>.tsx + <name>.module.css (+ extra files)
  blocks/
    <block-name>/           one folder per free block (same pattern)
```

`<components>` is the project's components root: `components/` or `src/components/`
in src-layout projects. Two files in the pack import the provider through the
project alias (`@/components/arc/lib/arc-provider`), so the project's `@/` alias
must resolve so that `@/components/...` reaches that components root (the standard
shadcn/tsconfig setup). If it does not, fix the two imports to relative paths and
note the change in your report.

Use `scripts/install-item.py` to produce this layout; it resolves registry
dependencies recursively, never overwrites a differing file without --force, and
prints the npm dependencies. Manual copying is acceptable only if you reproduce
the layout exactly.

## Why the layout is exact: the import graph

The copied code imports with RELATIVE paths that assume the layout above:
- A component imports motion tokens as `../lib/motion-tokens`; a block as `../../lib/motion-tokens`.
- Blocks import components as `../../button/button`, `../../avatar/avatar`, etc.
- An item's CSS module is imported as `./<name>.module.css` from its own folder.
- Shared helpers are imported as `../lib/use-today`, `../../lib/media`, and so on.
Move or rename a folder and every one of these imports breaks. This is a
low-freedom step: reproduce the layout, do not improvise it.

## Setup, step by step

1. Install the shared items once: foundation.css, motion tokens (both files).
2. Import foundation.css exactly once in the root layout, before page content renders.
3. Set `data-theme="dark"` or `"light"` on `<html>`; optionally `data-accent` =
   neutral, violet, blue, green, amber, orange, coral, or rose.
4. Load the fonts the tokens expect (Geist for large headings, Inter for the rest)
   as `--font-geist` and `--font-inter`, per Arc's own skill.
5. Install the items the task needs (script, or the shadcn CLI if the project
   prefers it and has network: `npx shadcn@latest add @uiarc/<name>` with the
   `@uiarc` registry registered in components.json). The bundle and the CLI
   deliver identical files.
6. Install the npm dependencies the installed items require (table below).
7. Wire items with documented props only. Selection items take `value` and
   `onValueChange`; pickers and editors (`date-picker`, `calendar`, `time-picker`)
   take `value` and `onChange`. When a callback is typed `void | Promise<...>`,
   return the promise so the item can show its pending, success and error states.

## npm dependencies

Across the 143 free items, only these npm packages appear. An item's own list is
in data/index.json and in its inventory entry; install only what installed items need.

| Package | Items using it |
| --- | --- |
| `motion` | 139 |
| `lucide-react` | 89 |
| `@radix-ui/react-dropdown-menu` | 5 |
| `@radix-ui/react-popover` | 4 |
| `@radix-ui/react-dialog` | 4 |
| `@radix-ui/react-tabs` | 2 |
| `@radix-ui/react-tooltip` | 2 |
| `@radix-ui/react-accordion` | 1 |
| `@radix-ui/react-checkbox` | 1 |
| `@radix-ui/react-select` | 1 |
| `@radix-ui/react-switch` | 1 |

`motion` is the Motion package (imports from `motion/react`). React 19 is the
pack's runtime target (the site metadata declares it); Next.js is only required
by the items listed under Framework notes.

## Theming and fonts

Semantic tokens only, from foundation.css: `--background`, `--surface`,
`--surface-muted`, `--foreground`, `--text-secondary`, `--text-muted`, `--border`,
`--accent`, `--success`, `--warning`, `--danger`, `--radius-*`, `--text-*`,
`--space-*`. Never raw hex values or Tailwind color classes on Arc surfaces.
Weights 400 and 500 only. Accent marks active, selected, progress and emphasized
data; status colors only for real status, always with a label.

## Design, motion, accessibility and copy rules (routed, not duplicated)

Arc's own agent skill ships INSIDE the free bundle and is the authority for
these rules. Read the file the task needs; do not rely on summaries:

| Need | Read (in the free bundle) |
| --- | --- |
| Always-on short rules | `uiarc-free-code/shared/arc-skill/INSTRUCTIONS.md` |
| Choosing an item by job | `uiarc-free-code/shared/arc-skill/components.md` |
| Page composition, states, dashboards, marketing | `uiarc-free-code/shared/arc-skill/composition.md` |
| Color, type, surfaces, radii, spacing, icons | `uiarc-free-code/shared/arc-skill/design.md` |
| Visible copy (headings, buttons, errors, empty states) | `uiarc-free-code/shared/arc-skill/copy.md` |
| Springs, motion tokens, reduced motion | `uiarc-free-code/shared/arc-skill/motion.md` |
| Semantics, keyboard, announcements | `uiarc-free-code/shared/arc-skill/accessibility.md` |
| Widths, overflow, touch targets | `uiarc-free-code/shared/arc-skill/responsive.md` |
| Final review loop (run, fix, re-run) | `uiarc-free-code/shared/arc-skill/checklist.md` |
| Worked examples | `uiarc-free-code/shared/arc-skill/example-settings.md`, `example-pricing.md`, `example-dashboard.md` |

Essentials that apply even before you open those files: one h1 and one primary
button per surface; sentence-case copy; no eyebrow labels; no em dashes in copy;
no hand-made focus rings (foundation.css provides the keyboard ring); every
animation gets a reduced-motion branch; every data region gets loading
(skeleton), empty (empty-state), error (inline alert) and success states;
check 390, 768, 1024 and 1440 px widths; touch targets at least 44 px.

## Framework notes (Next.js vs plain React)

Most items are framework-agnostic React with `"use client"` at the top. These
items import `next/image` or `next/link` and assume Next.js:
`avatar`, `breadcrumb`, `changelog-feed`, `hover-card`, `newsletter-signup`, `site-header`.
In a non-Next project, adapt only those imports (an `img`/`a` or the router's
link component), keep the rest of the file untouched, and list the adaptation
in your report.

## Verification after installing

- The project's type check and build pass.
- No import points outside the arc/ layout; no item file was edited except
  documented adaptations (Next.js imports, alias fix).
- foundation.css is imported exactly once; dark and light both render correctly.
- Run the bundled review loop: `uiarc-free-code/shared/arc-skill/checklist.md`,
  fix every failing line, run it again.


---

<!-- references/free-components.md -->

# Free components — ready source code (121)

## Contents

- `accordion` — Accordion
- `action-button` — Action button
- `action-swap` — Action swap
- `activity-heatmap` — Activity heatmap
- `alert` — Alert
- `animated-counter` — Animated counter
- `announcement-bar` — Announcement bar
- `avatar` — Avatar
- `avatar-group` — Avatar group
- `badge` — Badge
- `bar-chart` — Bar chart
- `billing-toggle` — Billing toggle
- `bottom-sheet` — Bottom sheet
- `breadcrumb` — Breadcrumb
- `brush-chart` — Brush chart
- `button` — Button
- `button-group` — Button group
- `calendar` — Calendar
- `card` — Card
- `card-stack` — Card stack
- `carousel` — Carousel
- `chat-thread` — Chat thread
- `checkbox` — Checkbox
- `chip-group` — Chip group
- `code-block` — Code block
- `color-picker` — Color picker
- `combobox` — Combobox
- `comment-thread` — Comment thread
- `confirm-morph` — Confirm morph
- `context-menu` — Context menu
- `cookie-consent` — Cookie consent
- `copy-button` — Copy button
- `countdown` — Countdown
- `date-picker` — Date picker
- `date-range-picker` — Date range picker
- `dialog` — Dialog
- `donut-chart` — Donut chart
- `drawer` — Drawer
- `dropdown-menu` — Dropdown menu
- `elastic-slider` — Elastic slider
- `empty-state` — Empty state
- `expandable-card` — Expandable card
- `expandable-text` — Expandable text
- `expanding-button-group` — Expanding button group
- `expanding-search` — Expanding search
- `file-dropzone` — File dropzone
- `filter-toolbar` — Filter toolbar
- `floating-button-group` — Floating button group
- `gauge` — Gauge
- `hold-to-confirm` — Hold to confirm
- `hover-card` — Hover card
- `icon-morph` — Icon morph
- `image-compare` — Image compare
- `in-view-title` — In-view title
- `inline-edit` — Inline edit
- `input` — Input
- `json-viewer` — JSON viewer
- `line-chart` — Line chart
- `mention-input` — Mention input
- `metric-card` — Metric card
- `money-input` — Money input
- `morph-select` — Morph select
- `multi-select` — Multi-select
- `number-field` — Number field
- `onboarding-checklist` — Onboarding checklist
- `pagination` — Pagination
- `password-field` — Password field
- `password-strength` — Password strength
- `phone-input` — Phone input
- `popover` — Popover
- `progress` — Progress
- `radio-cards` — Radio cards
- `radio-group` — Radio group
- `range-histogram-slider` — Range histogram slider
- `rating` — Rating
- `reactions` — Reactions
- `reorderable-list` — Reorderable list
- `resizable-panels` — Resizable panels
- `rich-text-editor` — Rich text editor
- `ridgeline` — Ridgeline
- `ruler-slider` — Ruler slider
- `scroll-area` — Scroll area
- `scrub-input` — Scrub input
- `search-field` — Search field
- `segmented-control` — Segmented control
- `select` — Select
- `shortcut-recorder` — Shortcut recorder
- `signature-pad` — Signature pad
- `skeleton` — Skeleton
- `slider` — Slider
- `slope-chart` — Slope chart
- `slot-text` — Slot text
- `sortable-data-table` — Sortable data table
- `sparkline` — Sparkline
- `split-button` — Split button
- `stepper` — Stepper
- `streamgraph` — Streamgraph
- `swipe-actions` — Swipe actions
- `switch` — Switch
- `tabs` — Tabs
- `tag-input` — Tag input
- `text-morph` — Text morph
- `text-reveal` — Text reveal
- `text-shimmer` — Text shimmer
- `textarea` — Textarea
- `theme-switch` — Theme switcher
- `theme-switch-eclipse` — Eclipse
- `theme-switch-rise` — Rise
- `theme-switch-split` — Split
- `time-picker` — Time picker
- `timeline` — Timeline
- `toast` — Toast
- `toast-stack` — Toast stack
- `toggle-group` — Toggle group
- `tooltip` — Tooltip
- `tree-table` — Tree table
- `tree-view` — Tree view
- `treemap` — Treemap
- `usage-meter` — Usage meter
- `user-menu` — User menu
- `waffle-chart` — Waffle chart
Every item below is a free (MIT) Arc component whose COMPLETE source is in the
free bundle at the listed paths (.tsx logic + .module.css styles + any lib helper).
Copy the files, do not rewrite them from this summary. Props and behavior live in
the .tsx itself; read it before use. Install with scripts/install-item.py.

### `accordion` — Accordion [Disclosure]
Progressively reveal supporting information in place.
- Files: uiarc-free-code/components/accordion/accordion.tsx; uiarc-free-code/components/accordion/accordion.module.css
- Exports: Accordion
- npm: @radix-ui/react-accordion, lucide-react, motion · also copy: arc-motion-tokens
- Use when: FAQ sections where only one answer should be open at a time.; Settings or help pages that group long content under short, scannable questions.; Page-level FAQs that need larger type, via size="lg".
- Avoid when: Use expandable-card for a single standalone disclosure such as a plan or order summary.

### `action-button` — Action button [Actions]
A compact button for frequent toolbar actions.
- Files: uiarc-free-code/components/action-button/action-button.tsx; uiarc-free-code/components/action-button/action-button.module.css
- Exports: ActionButton
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: A single async commit such as Save, Publish, or Submit where the result should appear on the button.; Call-to-action buttons where a trailing arrow invites the next step.; Flows where the button should reset to idle on its own after success, via resetAfterMs.
- Avoid when: Use button with loading for plain form submits that do not need a success state.

### `action-swap` — Action swap [Actions]
Swap an action label while preserving its place and intent.
- Files: uiarc-free-code/components/action-swap/action-swap.tsx; uiarc-free-code/components/action-swap/action-swap.module.css
- Exports: ActionSwap, ActionSwapState
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: One control that cycles through related states, like Follow and Following or Send and Sent.; Toggles that run async work on press and should show a working phase and a failure message in place.; Short confirmations that should revert on their own after a mome…
- Avoid when: Use action-button for a single save or publish that ends in a success tick.

### `activity-heatmap` — Activity heatmap [Data]
See a year of activity at a glance, one square per day.
- Files: uiarc-free-code/components/activity-heatmap/activity-heatmap.tsx; uiarc-free-code/components/activity-heatmap/activity-heatmap.module.css
- Exports: ActivityHeatmap
- npm: motion · also copy: arc-motion-tokens
- Use when: Daily rhythm over a long range, like contributions or workouts.; Views where streaks and quiet weeks matter more than exact comparison.
- Avoid when: Use bar-chart when the exact comparison is the point.

### `alert` — Alert [Feedback]
A persistent message that helps people recover or continue.
- Files: uiarc-free-code/components/alert/alert.tsx; uiarc-free-code/components/alert/alert.module.css
- Exports: Alert
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Persistent, in-flow messages about a page or form, such as an expiring card.; Status that changes over time, where one alert should morph between tones.; Dismissible notices that should collapse and close the gap below them.
- Avoid when: Use toast or toast-stack for transient results of an action.

### `animated-counter` — Animated counter [Data]
Give changing totals a clear sense of movement.
- Files: uiarc-free-code/components/animated-counter/animated-counter.tsx; uiarc-free-code/components/animated-counter/animated-counter.module.css
- Exports: AnimatedCounter
- npm: motion · also copy: arc-motion-tokens
- Use when: Standalone numbers that change, such as totals, prices, or live counts.; Hero stats that roll up from zero when they scroll into view, via animateOnView.
- Avoid when: Use metric-card or stat-card when the number needs a card around it.

### `announcement-bar` — Announcement bar [Feedback]
A top banner that rotates messages, counts down, and collapses smoothly when dismissed.
- Files: uiarc-free-code/components/announcement-bar/announcement-bar.tsx; uiarc-free-code/components/announcement-bar/announcement-bar.module.css
- Exports: AnnouncementBar, clearAnnouncementDismissal
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Site-wide promotions, launches, or maintenance notices at the top of every page.; Rotating two to four short announcements in one slim bar.; A sale banner with a live countdown to its end.
- Avoid when: Use alert for a message tied to one section or form.

### `avatar` — Avatar [Data]
A compact identity marker for people and accounts.
- Files: uiarc-free-code/components/avatar/avatar.tsx; uiarc-free-code/components/avatar/avatar.module.css; uiarc-free-code/components/avatar/lib/arc-provider.tsx
- Exports: Avatar
- npm: motion · also copy: arc-motion-tokens
- Use when: Showing one person next to their name, comment, or record.; Presence in a header or list, via the online or offline status dot.; Places where a photo may be missing and initials should stand in.
- Avoid when: Use avatar-group for several people with an overflow count.

### `avatar-group` — Avatar group [Data]
Show a team or set of contributors in a small space.
- Files: uiarc-free-code/components/avatar-group/avatar-group.tsx; uiarc-free-code/components/avatar-group/avatar-group.module.css
- Exports: AvatarGroup
- npm: motion · also copy: arc-motion-tokens, avatar
- Use when: Showing who owns or edits something in a header, card, or table cell.; Collaborator stacks where people join and leave while the page is open.; Long member lists that should collapse into a +N chip.
- Avoid when: Use avatar for a single person.

### `badge` — Badge [Data]
A small label for status, category, or metadata.
- Files: uiarc-free-code/components/badge/badge.tsx; uiarc-free-code/components/badge/badge.module.css
- Exports: Badge
- npm: motion · also copy: arc-motion-tokens
- Use when: Short statuses next to titles or in table cells, such as Live, Draft, or Failed.; Counts or states that change in place and should morph instead of jump.; Tagging a row with one tone plus an optional icon.
- Avoid when: Use alert or toast when the message needs a full sentence.

### `bar-chart` — Bar chart [Data]
Compare one measure across days and scrub any bar for its value.
- Files: uiarc-free-code/components/bar-chart/bar-chart.tsx; uiarc-free-code/components/bar-chart/bar-chart.module.css
- Exports: BarChart
- npm: motion · also copy: arc-motion-tokens
- Use when: One measure across days, weeks, or months, with an average line.; Charts with a range switch, where stable keys let bars morph between ranges.
- Avoid when: Use sparkline for a compact trend.

### `billing-toggle` — Billing toggle [Inputs]
A monthly and yearly switch with a savings badge and prices that roll to the new amount.
- Files: uiarc-free-code/components/billing-toggle/billing-toggle.tsx; uiarc-free-code/components/billing-toggle/billing-toggle.module.css
- Exports: BillingToggle, BillingToggleOption, BillingPrice
- npm: motion · also copy: arc-motion-tokens, animated-counter
- Use when: The billing period switch at the top of a pricing page.; Any price display that should roll to a new amount when a period or plan changes, using BillingPrice.; A small plan picker with a savings note, such as yearly versus lifetime.
- Avoid when: Use segmented-control for switching views or filters with no pricing meaning.

### `bottom-sheet` — Bottom sheet [Disclosure]
A sheet that rests at a peek or full height and follows your finger.
- Files: uiarc-free-code/components/bottom-sheet/bottom-sheet.tsx; uiarc-free-code/components/bottom-sheet/bottom-sheet.module.css
- Exports: BottomSheet, BottomSheetClose
- npm: @radix-ui/react-dialog, lucide-react, motion · also copy: arc-motion-tokens
- Use when: Mobile-first secondary tasks such as details, filters, or share options.; Content that benefits from a peek height before expanding to nearly full screen.; Maps and media views where the sheet should be dragged between detents.
- Avoid when: Use dialog for interrupting decisions on any screen size.

### `breadcrumb` — Breadcrumb [Disclosure]
Show where a page sits in a hierarchy.
- Files: uiarc-free-code/components/breadcrumb/breadcrumb.tsx; uiarc-free-code/components/breadcrumb/breadcrumb.module.css; uiarc-free-code/components/breadcrumb/lib/arc-provider.tsx
- Exports: Breadcrumb
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Showing where a page sits in a hierarchy, such as Workspace, Settings, Billing.; Client-side paths like a file browser, where crumbs call onClick instead of navigating.; Paths that grow as people drill in, where new crumbs should slide in.
- Avoid when: Use tree-view when people need to browse the whole hierarchy.

### `brush-chart` — Brush chart [Data]
A dense time series with an overview strip: drag a window to zoom, resize it by its handles, and read events in place.
- Files: uiarc-free-code/components/brush-chart/brush-chart.tsx; uiarc-free-code/components/brush-chart/brush-chart.module.css
- Exports: BrushChart
- npm: motion · also copy: arc-motion-tokens
- Use when: Product analytics with a year or more of daily data.; Incident reviews where events need to be read against a metric.; Any chart where people ask to zoom into a stretch without losing context.
- Avoid when: Use line-chart for a few weeks of data or several series.

### `button` — Button [Actions]
A clear, responsive action with quiet secondary states.
- Files: uiarc-free-code/components/button/button.tsx; uiarc-free-code/components/button/button.module.css
- Exports: Button
- npm: motion · also copy: arc-motion-tokens
- Use when: Any single action on a page, form, or dialog, such as Save, Continue, or Cancel.; Actions whose label changes in place, like Save to Saved, where the width should spring instead of jump.; Short async work where a spinner on the button is enough feedback, via…
- Avoid when: Use action-button when the button itself should show pending and success states after an async commit.

### `button-group` — Button group [Actions]
Related actions joined into one surface with hairline dividers: a hover highlight glides between segments, the pressed one answers in place, and an attached menu can close the row.
- Files: uiarc-free-code/components/button-group/button-group.tsx; uiarc-free-code/components/button-group/button-group.module.css
- Exports: ButtonGroup
- npm: @radix-ui/react-dropdown-menu, lucide-react, motion · also copy: arc-motion-tokens
- Use when: A small set of related actions on the same object, shown together in a header, toolbar or card footer.; Compact tool clusters such as zoom out, the current level and zoom in, or stacked map controls.; A primary action row, such as Reply, Reply all and Forward…
- Avoid when: Use toggle-group or segmented-control when the segments are options that stay selected.

### `calendar` — Calendar [Inputs]
Browse dates in a clear, compact month view.
- Files: uiarc-free-code/components/calendar/calendar.tsx; uiarc-free-code/components/calendar/lib/use-today.ts; uiarc-free-code/components/calendar/calendar.module.css
- Exports: Calendar, useToday
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Inline date picking where the month should stay visible, such as booking pages.; Picking one date with blocked days via minDate, maxDate, and disabledDates.
- Avoid when: Use date-picker for a form field that opens a calendar popover.

### `card` — Card [Data]
A contained group of related content and actions.
- Files: uiarc-free-code/components/card/card.tsx; uiarc-free-code/components/card/card.module.css
- Exports: Card
- npm: @radix-ui/react-dialog, lucide-react, motion · also copy: arc-motion-tokens
- Use when: Browsable items in a grid, such as projects, listings, or posts.; Items that should open into a larger quick look dialog without leaving the page, via details.; Content with media, an owner byline, and a status line that updates in place.
- Avoid when: Use expandable-card for inline disclosure without a dialog.

### `card-stack` — Card stack [Data]
Review a deck one card at a time, with a throw and an undo.
- Files: uiarc-free-code/components/card-stack/card-stack.tsx; uiarc-free-code/components/card-stack/card-stack.module.css
- Exports: CardStack
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: One-by-one triage such as shortlisting, review queues, or onboarding picks.; Decks where swiping left or right should be undoable.
- Avoid when: Use a list or sortable-data-table when people compare items side by side.

### `carousel` — Carousel [Data]
Browse a row of slides by dragging, flicking, or arrowing through them.
- Files: uiarc-free-code/components/carousel/carousel.tsx; uiarc-free-code/components/carousel/carousel.module.css
- Exports: Carousel
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: A short set of peer items where neighbouring slides hint at more.; Galleries browsed by drag, flick, trackpad swipe, or keys.; Rotating highlights with a visible pause control, via interval.
- Avoid when: Use cover-flow for a showpiece gallery and photo-grid to show everything at once.

### `chat-thread` — Chat thread [Data]
A chat thread with grouped messages, reactions, read receipts, typing, and a composer with attachments.
- Files: uiarc-free-code/components/chat-thread/chat-thread.tsx; uiarc-free-code/components/chat-thread/chat-thread.module.css
- Exports: ChatThread, ChatThreadHandle, ChatComposer, ChatMessage, formatBytes
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Customer support or in-app messaging with read receipts and typing state.; Team or DM threads that need reactions and image or file attachments.; Comment threads on an object where replies arrive live.
- Avoid when: Use log-stream for streaming system or build output.

### `checkbox` — Checkbox [Inputs]
A binary choice with a precise, legible state.
- Files: uiarc-free-code/components/checkbox/checkbox.tsx; uiarc-free-code/components/checkbox/checkbox.module.css
- Exports: Checkbox
- npm: @radix-ui/react-checkbox, motion · also copy: arc-motion-tokens
- Use when: Independent on and off choices confirmed by a submit, such as accepting terms.; Parent rows that show a partial selection through the indeterminate state.
- Avoid when: Use switch for settings that apply immediately.

### `chip-group` — Chip group [Inputs]
Filter by a few facets with chips that morph as you pick them.
- Files: uiarc-free-code/components/chip-group/chip-group.tsx; uiarc-free-code/components/chip-group/chip-group.module.css
- Exports: ChipGroup
- npm: motion · also copy: arc-motion-tokens
- Use when: Facet filters people toggle often, like topics or categories.; Single clearable choices shown as chips, via multiple={false}.; Long option sets folded behind a +N more chip with maxVisible.
- Avoid when: Use multi-select when space is tight.

### `code-block` — Code block [Data]
Present code with legible hierarchy and copy access.
- Files: uiarc-free-code/components/code-block/code-block.tsx; uiarc-free-code/components/code-block/code-block.module.css
- Exports: CodeBlock
- npm: lucide-react, motion · also copy: arc-motion-tokens, copy-button
- Use when: Documentation snippets and install commands with a copy button.; Long files that should collapse to a few lines with Show all, via maxLines.
- Avoid when: Use copy-button alone for a one-line value such as an API key.

### `color-picker` — Color picker [Inputs]
A swatch that grows into a picker with format morphing, eyedropper, saved swatches, and contrast readout.
- Files: uiarc-free-code/components/color-picker/color-picker.tsx; uiarc-free-code/components/color-picker/color-picker.module.css
- Exports: ColorPicker, parseColor, toHex
- npm: lucide-react, motion · also copy: arc-motion-tokens, text-morph
- Use when: Theme editors and brand settings where users choose an exact color.; Design tools that need hex, RGB, HSL, and OKLCH input plus opacity.; Any color choice where contrast against a background should be visible while picking.
- Avoid when: Use segmented-control or radio-group when the choice is between a few fixed colors.

### `combobox` — Combobox [Inputs]
Search and select from a list without leaving the field.
- Files: uiarc-free-code/components/combobox/combobox.tsx; uiarc-free-code/components/combobox/combobox.module.css
- Exports: Combobox
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Single-choice fields with long lists, such as time zones or countries.; Lists where people know the name and want to type, including aliases via keywords.
- Avoid when: Use select for a short list where typing adds nothing.

### `comment-thread` — Comment thread [Data]
Threaded comments with replies, reactions, mentions, inline edit, and resolve.
- Files: uiarc-free-code/components/comment-thread/comment-thread.tsx; uiarc-free-code/components/comment-thread/comment-thread.module.css
- Exports: CommentThread, ThreadComment
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Review threads on documents, designs, tickets, or pull requests.; Discussions that need replies, reactions, mentions, and a resolved state.; Sidebars of feedback attached to one object.
- Avoid when: Use chat-thread for real-time back-and-forth conversation.

### `confirm-morph` — Confirm morph [Actions]
A destructive button that morphs into an inline confirmation, a spinner, and a result with undo.
- Files: uiarc-free-code/components/confirm-morph/confirm-morph.tsx; uiarc-free-code/components/confirm-morph/confirm-morph.module.css
- Exports: ConfirmMorph
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Deleting a selection in a table or file list, right where the button sits.; Revoking access, removing a member, or discarding a draft.; Actions that should offer Undo in place after they finish.
- Avoid when: Use dialog when the consequence needs more than one line, or when typing a name to confirm is required.

### `context-menu` — Context menu [Actions]
Secondary actions kept close to the selected object.
- Files: uiarc-free-code/components/context-menu/context-menu.tsx; uiarc-free-code/components/context-menu/context-menu.module.css
- Exports: ContextMenu
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Secondary actions on a file, card, or row where a visible menu button would add clutter.; Desktop-style right-click menus that also open from the keyboard with Shift+F10 or the ContextMenu key.; Short flat lists of item actions with one destructive option.
- Avoid when: Use dropdown-menu when the actions deserve a visible trigger.

### `cookie-consent` — Cookie consent [Feedback]
A consent bar that morphs into preferences and folds into a reopen button.
- Files: uiarc-free-code/components/cookie-consent/cookie-consent.tsx; uiarc-free-code/components/cookie-consent/cookie-consent.module.css
- Exports: CookieConsent, readCookieConsent, defaultCookieCategories
- npm: lucide-react, motion · also copy: arc-motion-tokens, button, switch
- Use when: Asking for cookie or tracking consent on a marketing site or app.; Sites that need per-category choices with a way to reopen them later.
- Avoid when: Use announcement-bar for a site-wide promotion or notice that needs no choice.

### `copy-button` — Copy button [Actions]
Copy a value with immediate confirmation.
- Files: uiarc-free-code/components/copy-button/copy-button.tsx; uiarc-free-code/components/copy-button/copy-button.module.css; uiarc-free-code/components/copy-button/lib/use-copy-feedback.ts
- Exports: CopyButton
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Next to API keys, install commands, links, or code snippets.; Icon-only copy controls in dense rows, with an accessible label.; Any copy action that should confirm Copied or Could not copy in place.
- Avoid when: Use split-button when copying has alternatives, such as Copy link and Copy as Markdown.

### `countdown` — Countdown [Feedback]
A launch countdown with rolling digits that morphs into a live state at zero.
- Files: uiarc-free-code/components/countdown/countdown.tsx; uiarc-free-code/components/countdown/countdown.module.css
- Exports: Countdown, toEpoch
- npm: motion · also copy: arc-motion-tokens
- Use when: A launch page or event hero counting to a keynote.; A compact deadline pill in a table row or banner.; Sale or registration windows that should flip to a Live now state on their own.
- Avoid when: Use stopwatch for time counting up from a start.

### `date-picker` — Date picker [Inputs]
Choose a date without losing context.
- Files: uiarc-free-code/components/date-picker/date-picker.tsx; uiarc-free-code/components/date-picker/date-picker.module.css
- Exports: DatePicker
- npm: lucide-react, motion · also copy: arc-motion-tokens, calendar
- Use when: A date field in a form, such as a start or due date.; Dates with limits or blocked days, shown in a locale format.
- Avoid when: Use calendar inline when the grid should stay visible.

### `date-range-picker` — Date range picker [Inputs]
A range picker that grows from its trigger into two months with presets and a stretching range highlight.
- Files: uiarc-free-code/components/date-range-picker/date-range-picker.tsx; uiarc-free-code/components/date-range-picker/lib/use-today.ts; uiarc-free-code/components/date-range-picker/date-range-picker.module.css
- Exports: DateRangePicker, useToday
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Analytics and reporting filters that need presets like Last 7 days or This quarter.; Booking or leave requests where a start and end day are picked together.; Toolbars where the picker must stay compact until opened.
- Avoid when: Use date-picker for a single date.

### `dialog` — Dialog [Disclosure]
A focused surface for decisions that need attention.
- Files: uiarc-free-code/components/dialog/dialog.tsx; uiarc-free-code/components/dialog/dialog.module.css
- Exports: Dialog, DialogTrigger, DialogContent, DialogClose
- npm: @radix-ui/react-dialog, lucide-react, motion · also copy: arc-motion-tokens
- Use when: Confirmations and decisions that must interrupt, such as Delete project.; Short forms like rename or invite that fit in one focused panel.; Flows where the dialog title changes between steps and should crossfade in place.
- Avoid when: Use drawer for long forms or detail panels that keep the page in context.

### `donut-chart` — Donut chart [Data]
A donut whose arcs morph between datasets, with the active value rolling into the center.
- Files: uiarc-free-code/components/donut-chart/donut-chart.tsx; uiarc-free-code/components/donut-chart/donut-chart.module.css
- Exports: DonutChart
- npm: motion · also copy: arc-motion-tokens
- Use when: Traffic by source, spend by category, or storage by file type.; A dashboard card where the total and one highlighted share matter most.; Switching between datasets, such as this month and last month, with the same categories.
- Avoid when: Use bar-chart when precise comparison between parts matters or there are many parts.

### `drawer` — Drawer [Disclosure]
A temporary side surface for focused work.
- Files: uiarc-free-code/components/drawer/drawer.tsx; uiarc-free-code/components/drawer/drawer.module.css
- Exports: Drawer, DrawerTrigger, DrawerContent, DrawerClose
- npm: @radix-ui/react-dialog, lucide-react, motion · also copy: arc-motion-tokens
- Use when: Side panels for filters, settings, or record details that keep the page in context.; Forms that are too long for a dialog but should not leave the current view.; Panels from any edge, via side, with drag-to-dismiss on the header.
- Avoid when: Use dialog for short decisions and confirmations.

### `dropdown-menu` — Dropdown menu [Actions]
A focused list of actions anchored to a trigger.
- Files: uiarc-free-code/components/dropdown-menu/dropdown-menu.tsx; uiarc-free-code/components/dropdown-menu/dropdown-menu.module.css
- Exports: DropdownMenu
- npm: @radix-ui/react-dropdown-menu, lucide-react, motion · also copy: arc-motion-tokens
- Use when: A list of commands behind a labelled button, such as Rename, Duplicate, and Delete.; Row or card actions where a visible trigger is clearer than right-click.; Short grouped menus with separators and one destructive item at the end.
- Avoid when: Use split-button when one command is the default.

### `elastic-slider` — Elastic slider [Inputs]
A slider that stretches like rubber past its ends, with a swaying value tag and detents the thumb clicks into.
- Files: uiarc-free-code/components/elastic-slider/elastic-slider.tsx; uiarc-free-code/components/elastic-slider/elastic-slider.module.css
- Exports: ElasticSlider
- npm: motion · also copy: arc-motion-tokens
- Use when: A single setting people drag to taste, such as volume, brightness, or opacity.; Media and creative tools where a physical, tactile control fits the product.; Values with a few common stops that should feel like detents.
- Avoid when: Use slider for dense forms and settings pages where a quiet control fits better.

### `empty-state` — Empty state [Data]
A useful next step when there is nothing to show yet.
- Files: uiarc-free-code/components/empty-state/empty-state.tsx; uiarc-free-code/components/empty-state/empty-state.module.css
- Exports: EmptyState
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Empty lists, zero search results, and first-run views.; A view that should morph between states, such as empty and success, by changing props.
- Avoid when: Use skeleton while data is still loading.

### `expandable-card` — Expandable card [Disclosure]
Give a dense card more room when requested.
- Files: uiarc-free-code/components/expandable-card/expandable-card.tsx; uiarc-free-code/components/expandable-card/expandable-card.module.css
- Exports: ExpandableCard
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: A single summary card with optional details, like a plan, order, or log entry.; Cards whose summary line updates and should roll changed words in place.
- Avoid when: Use accordion for a list of mutually exclusive sections.

### `expandable-text` — Expandable text [Disclosure]
Long text clamped to a few lines with a soft fade that glides open with Read more and closes with Show less, shown only when the text overflows.
- Files: uiarc-free-code/components/expandable-text/expandable-text.tsx; uiarc-free-code/components/expandable-text/expandable-text.module.css
- Exports: ExpandableText
- npm: lucide-react, motion
- Use when: A list of user reviews or comments where some entries are long.; A product, listing, or profile description that should not push the rest of the page down.; Any card where long text would make the cards uneven.
- Avoid when: Use accordion for a set of titled sections or an FAQ.

### `expanding-button-group` — Expanding button group [Actions]
Icon buttons in a compact group: the one you point at or focus grows to reveal its label while its neighbours slide aside, and an action confirms in place.
- Files: uiarc-free-code/components/expanding-button-group/expanding-button-group.tsx; uiarc-free-code/components/expanding-button-group/expanding-button-group.module.css
- Exports: ExpandingButtonGroup
- npm: motion · also copy: arc-motion-tokens
- Use when: A compact action bar on a message, file, or card where space is tight but labels should be one glance away.; Toolbars where actions finish in place and deserve a confirmation without a toast, such as Archive or Copy link.
- Avoid when: Use toggle-group or segmented-control when the buttons select a value instead of running an action.

### `expanding-search` — Expanding search [Inputs]
An icon that morphs into a search field with results beneath it.
- Files: uiarc-free-code/components/expanding-search/expanding-search.tsx; uiarc-free-code/components/expanding-search/expanding-search.module.css
- Exports: ExpandingSearch
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Header or toolbar search where a full field would crowd the layout.; Quick navigation across local items with grouped results and recent suggestions.
- Avoid when: Use search-field to filter a visible list in place.

### `file-dropzone` — File dropzone [Inputs]
A generous target for dropping one or more files.
- Files: uiarc-free-code/components/file-dropzone/file-dropzone.tsx; uiarc-free-code/components/file-dropzone/file-dropzone.module.css
- Exports: FileDropzone, FileDropzoneItem
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Attachments and uploads with drag and drop plus a file picker.; Uploads that need per-file progress, retry, and cancel through onUpload.
- Avoid when: Use input with type file only when a native picker with no list is enough.

### `filter-toolbar` — Filter toolbar [Data]
Keep collection filters close and easy to reset.
- Files: uiarc-free-code/components/filter-toolbar/filter-toolbar.tsx; uiarc-free-code/components/filter-toolbar/filter-toolbar.module.css
- Exports: FilterToolbar, FilterMenu
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Faceted filtering above tables and lists, with removable chips.; Adding filters through a two step field then value menu.; Views that pair with sortable-data-table and pagination for a full list page.
- Avoid when: Use chip-group for a fixed set of toggles.

### `floating-button-group` — Floating button group [Actions]
Separate soft buttons in a quiet tray, with one shared highlight that morphs from button to button as you move, and a pressed state that settles in place.
- Files: uiarc-free-code/components/floating-button-group/floating-button-group.tsx; uiarc-free-code/components/floating-button-group/floating-button-group.module.css
- Exports: FloatingButtonGroup
- npm: @radix-ui/react-tooltip, motion · also copy: arc-motion-tokens, tooltip
- Use when: A floating editor or canvas toolbar with undo, redo, share and present.; A selection toolbar that appears over text or objects.; A vertical tools rail with zoom and insert actions.
- Avoid when: Use toggle-group for formatting toggles or alignment where the choice stays pressed.

### `gauge` — Gauge [Data]
Show a value against a known range.
- Files: uiarc-free-code/components/gauge/gauge.tsx; uiarc-free-code/components/gauge/gauge.module.css
- Exports: Gauge
- npm: motion · also copy: arc-motion-tokens
- Use when: One value against a known range, such as disk quota or health score.; Values with labelled bands, like Healthy, Filling up, and Critical.
- Avoid when: Use progress for task completion.

### `hold-to-confirm` — Hold to confirm [Actions]
Confirm a destructive action by holding, not tapping.
- Files: uiarc-free-code/components/hold-to-confirm/hold-to-confirm.tsx; uiarc-free-code/components/hold-to-confirm/hold-to-confirm.module.css
- Exports: HoldToConfirm
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Destructive actions like delete or revoke where the consequence is already visible on screen.; Replacing a confirm dialog with a deliberate press in compact settings rows.; Actions that should not fire on an accidental tap on touch devices.
- Avoid when: Use dialog when people need to read what will happen before confirming.

### `hover-card` — Hover card [Disclosure]
Preview a person or link on hover or focus without leaving the page.
- Files: uiarc-free-code/components/hover-card/hover-card.tsx; uiarc-free-code/components/hover-card/hover-card.module.css
- Exports: HoverCard, HoverCardProfile
- npm: @radix-ui/react-popover, motion · also copy: arc-motion-tokens
- Use when: Previews of people behind mentions, avatars, or author names.; Link or reference previews where the click must stay free for navigation.; Dense lists where moving between triggers should open cards almost instantly.
- Avoid when: Use tooltip for a plain text label.

### `icon-morph` — Icon morph [Actions]
Icons that morph between states: menu to close, play to pause, copy to check, and more.
- Files: uiarc-free-code/components/icon-morph/icon-morph.tsx; uiarc-free-code/components/icon-morph/icon-morph.module.css
- Exports: IconMorph, MenuIcon, PlayPauseIcon, PlusCheckIcon, CopyCheckIcon, SunMoonIcon, ChevronIcon, BellIcon, HeartIcon
- npm: motion · also copy: arc-motion-tokens
- Use when: Icon buttons that toggle between two states, such as a hamburger menu or a play control.; Copy and add actions that should confirm with a check in place.; Like and notify toggles that deserve a small moment of delight.
- Avoid when: Use copy-button for a complete copy-to-clipboard control with its own feedback.

### `image-compare` — Image compare [Data]
Drag a divider across two images to see what changed.
- Files: uiarc-free-code/components/image-compare/image-compare.tsx; uiarc-free-code/components/image-compare/image-compare.module.css
- Exports: ImageCompare
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Before and after visuals such as photo edits, redesigns, or cleanup results.; Top and bottom comparisons, via orientation vertical.
- Avoid when: Use carousel to browse many images.

### `in-view-title` — In-view title [Text]
Bring a section title in as it scrolls into view.
- Files: uiarc-free-code/components/in-view-title/in-view-title.tsx; uiarc-free-code/components/in-view-title/in-view-title.module.css
- Exports: InViewTitle
- npm: motion · also copy: arc-motion-tokens
- Use when: Section headings that should animate once they scroll into view.; Feature pages where each section title needs a consistent entrance style.; Headings that should replay on each entry, via once={false}.
- Avoid when: Use text-reveal for hero copy that animates on load.

### `inline-edit` — Inline edit [Inputs]
Rename in place: the text becomes a field without moving.
- Files: uiarc-free-code/components/inline-edit/inline-edit.tsx; uiarc-free-code/components/inline-edit/inline-edit.module.css
- Exports: InlineEdit
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Titles and descriptions read far more often than edited, like a project name.; Single fields that save on their own with optimistic updates and rollback.
- Avoid when: Use input or textarea in a form when several fields save together.

### `input` — Input [Inputs]
A single line field with clear labels and useful states.
- Files: uiarc-free-code/components/input/input.tsx; uiarc-free-code/components/input/input.module.css
- Exports: Input
- npm: motion · also copy: arc-motion-tokens
- Use when: Any single-line text value in a form, such as name, email, or URL.; Fields whose helper or error copy changes as the person types, where the message should reword in place.; Plain form posts, since it forwards name and every native input attribute.
- Avoid when: Use textarea for multi-line text.

### `json-viewer` — JSON viewer [Data]
A collapsible JSON tree with search, paging for long arrays, and copy value or path.
- Files: uiarc-free-code/components/json-viewer/json-viewer.tsx; uiarc-free-code/components/json-viewer/json-viewer.module.css
- Exports: JsonViewer
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Inspecting a JSON payload in a developer dashboard, such as webhooks or API logs.; Large nested objects where search and copy path save time.; Arrays with hundreds of items, which load in pages of pageSize.
- Avoid when: Use code-block to show JSON as formatted source for copying whole.

### `line-chart` — Line chart [Data]
A multi-series line chart with a gliding crosshair, legend toggles, and paths that morph between ranges.
- Files: uiarc-free-code/components/line-chart/line-chart.tsx; uiarc-free-code/components/line-chart/line-chart.module.css
- Exports: LineChart
- npm: motion · also copy: arc-motion-tokens
- Use when: Traffic, revenue, or latency over days or weeks in a dashboard card.; Comparing this period against a previous period or target with a dashed series.; Charts that switch ranges (7d, 30d, 90d) and should morph rather than redraw.
- Avoid when: Use sparkline for a tiny inline trend with no axes or tooltip.

### `mention-input` — Mention input [Inputs]
A textarea with @people and #channel mentions that act as single tokens, with suggestions at the caret.
- Files: uiarc-free-code/components/mention-input/mention-input.tsx; uiarc-free-code/components/mention-input/mention-input.module.css
- Exports: MentionInput, MentionInputHandle, serializeMentions, mentionText
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Comment and reply boxes where people are tagged with @ and should be notified by id.; Chat or task composers that link #channels or projects inline.; Any text field whose stored value needs structured references alongside the plain text.
- Avoid when: Use textarea for plain notes with no references.

### `metric-card` — Metric card [Data]
A compact summary for a number that needs context.
- Files: uiarc-free-code/components/metric-card/metric-card.tsx; uiarc-free-code/components/metric-card/metric-card.module.css
- Exports: MetricCard
- npm: motion · also copy: arc-motion-tokens, animated-counter
- Use when: A single plain number with odometer style rolling digits, such as uptime or orders.; Numbers that update live and should roll in the direction they moved.
- Avoid when: Use stat-card for preformatted strings, trend arrows, tones, and icons.

### `money-input` — Money input [Inputs]
A currency field with live grouping, stable width, rolling digits, and minor-unit output.
- Files: uiarc-free-code/components/money-input/money-input.tsx; uiarc-free-code/components/money-input/money-input.module.css
- Exports: MoneyInput
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Payment, tip, transfer, or budget amounts entered by hand.; Invoice and expense forms where the currency may change.; Amount fields that benefit from quick add chips such as +$10.
- Avoid when: Use number-field for quantities and non currency numbers.

### `morph-select` — Morph select [Inputs]
A select whose trigger grows into the list, with a gliding highlight and type-ahead.
- Files: uiarc-free-code/components/morph-select/morph-select.tsx; uiarc-free-code/components/morph-select/morph-select.module.css
- Exports: MorphSelect
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Form fields and property panels where one value is picked from a known list.; Grouped lists like time zones, assignees, or projects, with optional icons and meta.; Compact toolbars where the picker should look like a pill until opened.
- Avoid when: Use combobox when users type free text or the list is very long and remote.

### `multi-select` — Multi-select [Inputs]
Select several values while keeping the field readable.
- Files: uiarc-free-code/components/multi-select/multi-select.tsx; uiarc-free-code/components/multi-select/multi-select.module.css
- Exports: MultiSelect
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Picking several values from a fixed list in a compact field, such as labels or assignees.; Filters where the chosen values should show in the field with a +N overflow.
- Avoid when: Use chip-group when every option should stay visible.

### `number-field` — Number field [Inputs]
Enter a bounded number with clear increment controls.
- Files: uiarc-free-code/components/number-field/number-field.tsx; uiarc-free-code/components/number-field/number-field.module.css
- Exports: NumberField
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Bounded quantities like seats, items, or prices where the exact number matters.; Values people nudge with steppers, arrow keys, or by dragging the label with scrub.; Numbers with units, using a prefix or a pluralizing suffix function.
- Avoid when: Use slider when the approximate position matters more than the exact number.

### `onboarding-checklist` — Onboarding checklist [Feedback]
Guide a new workspace through setup, one step at a time.
- Files: uiarc-free-code/components/onboarding-checklist/onboarding-checklist.tsx; uiarc-free-code/components/onboarding-checklist/onboarding-checklist.module.css
- Exports: OnboardingChecklist
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: A one-time getting-started card with three to eight loosely ordered steps.; Setup steps that run async actions, like Connect GitHub, and check off when they resolve.; Checklists people can hide and come back to, with state persisted through callbacks.
- Avoid when: Use stepper when the order is strict and steps map to screens.

### `pagination` — Pagination [Data]
Move through a long collection with clear bounds.
- Files: uiarc-free-code/components/pagination/pagination.tsx; uiarc-free-code/components/pagination/pagination.module.css
- Exports: Pagination
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Paged server results and long tables.; Lists where the page should live in the URL or state and fetch on change.
- Avoid when: Use carousel for browsing slides.

### `password-field` — Password field [Inputs]
Capture sensitive text with a visible reveal control.
- Files: uiarc-free-code/components/password-field/password-field.tsx; uiarc-free-code/components/password-field/password-field.module.css
- Exports: PasswordField
- npm: motion · also copy: arc-motion-tokens
- Use when: Sign in forms and password confirmation fields.; Any secret the person may want to check by revealing it.
- Avoid when: Use password-strength when creating or changing a password.

### `password-strength` — Password strength [Inputs]
Show how strong a new password is while it is typed.
- Files: uiarc-free-code/components/password-strength/password-strength.tsx; uiarc-free-code/components/password-strength/password-strength.module.css
- Exports: PasswordStrength
- npm: motion · also copy: arc-motion-tokens
- Use when: Sign up and change password forms.; Password rules that should check off live as the person types.
- Avoid when: Use password-field for sign in.

### `phone-input` — Phone input [Inputs]
A phone field with a country picker, formatting as you type, and E.164 output.
- Files: uiarc-free-code/components/phone-input/phone-input.tsx; uiarc-free-code/components/phone-input/phone-input.module.css
- Exports: PhoneInput, parsePhoneNumber / formatPhoneNumber / formatNational, PHONE_COUNTRIES / flagOf
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Sign up, checkout, and contact forms that need a phone number in E.164.; International audiences where the country and calling code must be clear.; Two factor setup before sending an SMS code.
- Avoid when: Use input with type="tel" when you only store free text and never dial or text the number.

### `popover` — Popover [Disclosure]
A small anchored surface for contextual information.
- Files: uiarc-free-code/components/popover/popover.tsx; uiarc-free-code/components/popover/popover.module.css
- Exports: Popover, PopoverTrigger, PopoverContent, PopoverClose
- npm: @radix-ui/react-popover
- Use when: Click-opened panels with interactive content, like share settings or a small filter form.; Non-modal helpers that should stay open while people interact with the rest of the page.; Custom pickers built from your own controls anchored to a button.
- Avoid when: Use tooltip for short hover labels.

### `progress` — Progress [Feedback]
Show how much of a known task is complete.
- Files: uiarc-free-code/components/progress/progress.tsx; uiarc-free-code/components/progress/progress.module.css
- Exports: Progress
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Determinate progress for uploads, imports, or long tasks.; Progress with a visible percentage and a check at completion, via showValue.
- Avoid when: Use skeleton while content is loading with no progress to report.

### `radio-cards` — Radio cards [Inputs]
Selectable option cards with a sliding selection ring, price and description slots, and radio keyboard behavior.
- Files: uiarc-free-code/components/radio-cards/radio-cards.tsx; uiarc-free-code/components/radio-cards/radio-cards.module.css
- Exports: RadioCards
- npm: motion · also copy: arc-motion-tokens
- Use when: Choices where each option needs a description, price, or estimate to decide.; Plan, shipping, region, or size pickers inside checkout and setup flows.; Options that may be unavailable and need a visible reason.
- Avoid when: Use radio-group for short text-only options.

### `radio-group` — Radio group [Inputs]
Choose one option from a visible set.
- Files: uiarc-free-code/components/radio-group/radio-group.tsx; uiarc-free-code/components/radio-group/radio-group.module.css
- Exports: RadioGroup
- npm: motion · also copy: arc-motion-tokens
- Use when: Two to six mutually exclusive options that need descriptions, such as plans.; Form choices that should submit natively through name.
- Avoid when: Use segmented-control for short inline view options.

### `range-histogram-slider` — Range histogram slider [Inputs]
A price range over a live histogram of the data, lighting the bars inside the range and settling on bar edges.
- Files: uiarc-free-code/components/range-histogram-slider/range-histogram-slider.tsx; uiarc-free-code/components/range-histogram-slider/range-histogram-slider.module.css
- Exports: RangeHistogramSlider, histogram
- npm: motion · also copy: arc-motion-tokens
- Use when: Marketplace and search filters for price, size, or distance where the distribution guides the choice.; Analytics filters that trim outliers from a numeric column.; Any min and max choice where people benefit from seeing how many results fall inside.
- Avoid when: Use slider for a plain range without data behind it.

### `rating` — Rating [Inputs]
A simple, accessible way to capture a numeric opinion.
- Files: uiarc-free-code/components/rating/rating.tsx; uiarc-free-code/components/rating/rating.module.css
- Exports: Rating
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Collecting a 1 to N score in reviews or feedback forms.; Displaying average scores, with readOnly and allowHalf.; Forms that submit natively, via name.
- Avoid when: Use slider for continuous values.

### `reactions` — Reactions [Actions]
Acknowledge a post in one tap, with counts that roll.
- Files: uiarc-free-code/components/reactions/reactions.tsx; uiarc-free-code/components/reactions/reactions.module.css
- Exports: Reactions
- npm: @radix-ui/react-popover, lucide-react, motion · also copy: arc-motion-tokens
- Use when: Lightweight acknowledgement on comments, posts, or release notes.; Slack-style reaction pills with counts and a picker for new reactions.
- Avoid when: Use a reply field such as ai-composer when people need to say something specific.

### `reorderable-list` — Reorderable list [Data]
Organize items with direct drag and drop.
- Files: uiarc-free-code/components/reorderable-list/reorderable-list.tsx; uiarc-free-code/components/reorderable-list/reorderable-list.module.css
- Exports: ReorderableList
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Short user-ordered lists such as priorities or a playlist.; Lists that must be reorderable by keyboard as well as by drag.
- Avoid when: Use sortable-data-table when order comes from a column.

### `resizable-panels` — Resizable panels [Disclosure]
Trade space between panes by dragging the divider between them.
- Files: uiarc-free-code/components/resizable-panels/resizable-panels.tsx; uiarc-free-code/components/resizable-panels/resizable-panels.module.css
- Exports: ResizablePanels, ResizablePanel
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Editor, mail, or dashboard layouts where people trade space between side-by-side panes.; Sidebars that should collapse by dragging or flicking toward the edge.; Layouts whose pane sizes should persist between visits via onLayoutChange.
- Avoid when: Use drawer for a panel that slides over the page.

### `rich-text-editor` — Rich text editor [Inputs]
A lightweight editor with markdown shortcuts, a floating toolbar, a slash menu, and HTML and markdown output.
- Files: uiarc-free-code/components/rich-text-editor/rich-text-editor.tsx; uiarc-free-code/components/rich-text-editor/rich-text-editor.module.css
- Exports: RichTextEditor, RichTextEditorHandle, markdownToHtml, htmlToMarkdown, sanitizeHtml, normalizeUrl
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Comments, notes, and posts where people expect markdown shortcuts and a selection toolbar.; Forms that need Markdown or clean HTML out without pulling in a full editor framework.; Short to medium documents with headings, lists, quotes, and code blocks.
- Avoid when: Use textarea for plain text, or mention-input when the only rich part is tagging people.

### `ridgeline` — Ridgeline [Data]
Overlapping distributions, one ridge per group: hover to lift a ridge and read its quartiles, switch datasets and every curve morphs.
- Files: uiarc-free-code/components/ridgeline/ridgeline.tsx; uiarc-free-code/components/ridgeline/ridgeline.module.css
- Exports: Ridgeline
- npm: motion · also copy: arc-motion-tokens
- Use when: Seasonal or categorical distributions such as temperatures by month or response times by region.; Showing where two groups differ in shape, such as bimodal winters.
- Avoid when: Use beeswarm when each individual observation matters.

### `ruler-slider` — Ruler slider [Inputs]
A tape of ticks that slides under a fixed needle, with momentum, snapping, and a rolling readout.
- Files: uiarc-free-code/components/ruler-slider/ruler-slider.tsx; uiarc-free-code/components/ruler-slider/ruler-slider.module.css
- Exports: RulerSlider
- npm: motion · also copy: arc-motion-tokens
- Use when: Onboarding and profile flows that ask for body measurements or goals.; Mobile-first inputs where dragging a scale is easier than typing.; Wide ranges with fine steps that a short slider track cannot resolve.
- Avoid when: Use number-field when people know the exact number and prefer to type it.

### `scroll-area` — Scroll area [Disclosure]
A native scroll container with thin overlay scrollbars and edge fades that appear only when content overflows.
- Files: uiarc-free-code/components/scroll-area/scroll-area.tsx; uiarc-free-code/components/scroll-area/scroll-area.module.css
- Exports: ScrollArea
- Use when: Panels, sidebars, and popovers whose content can outgrow their box.; Horizontal strips of cards or chips that need mouse-wheel scrolling and snap points.; Places where platform scrollbars look heavy but native scrolling must be kept.
- Avoid when: Use carousel when items should page one at a time with controls.

### `scrub-input` — Scrub input [Inputs]
A Figma-style number field: drag the label to scrub, or type values, units, and arithmetic.
- Files: uiarc-free-code/components/scrub-input/scrub-input.tsx; uiarc-free-code/components/scrub-input/scrub-input.module.css
- Exports: ScrubInput, evaluateScrubExpression
- npm: motion · also copy: arc-motion-tokens
- Use when: Position, size, rotation, and opacity fields in an inspector panel.; Dense settings where typing exact values and dragging both matter.; Values with units such as px, %, or deg that people type mixed.
- Avoid when: Use number-field for a normal form with stepper buttons and a visible label.

### `search-field` — Search field [Inputs]
A recognizable search entry point with clear affordances.
- Files: uiarc-free-code/components/search-field/search-field.tsx; uiarc-free-code/components/search-field/search-field.module.css
- Exports: SearchField
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Filtering a visible list or table in place.; Toolbar search where the query should be clearable with one click.
- Avoid when: Use expanding-search for compact header search with results.

### `segmented-control` — Segmented control [Inputs]
Switch between a small set of related views.
- Files: uiarc-free-code/components/segmented-control/segmented-control.tsx; uiarc-free-code/components/segmented-control/segmented-control.module.css
- Exports: SegmentedControl
- npm: motion · also copy: arc-motion-tokens
- Use when: Two to five short view options like Day, Week, and Month.; Toolbar toggles between layouts or modes that apply immediately.
- Avoid when: Use tabs when each option swaps a panel of content.

### `select` — Select [Inputs]
A compact choice field with a keyboard friendly menu.
- Files: uiarc-free-code/components/select/select.tsx; uiarc-free-code/components/select/select.module.css
- Exports: Select
- npm: @radix-ui/react-select, lucide-react, motion · also copy: arc-motion-tokens
- Use when: A short fixed list where typing is not needed, such as region or sort order.; Form fields that should submit natively through Radix's hidden select via name.
- Avoid when: Use combobox for long or searchable lists.

### `shortcut-recorder` — Shortcut recorder [Inputs]
Record key combinations into key caps, with conflict warnings, Kbd, and a searchable cheatsheet.
- Files: uiarc-free-code/components/shortcut-recorder/shortcut-recorder.tsx; uiarc-free-code/components/shortcut-recorder/shortcut-recorder.module.css
- Exports: ShortcutRecorder, ShortcutList, ShortcutKeys, ShortcutKbd, matchesShortcut / formatShortcut / usePlatform / usePressedKeys
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Settings pages where people remap keyboard shortcuts.; A keyboard shortcut cheatsheet or help dialog, with ShortcutList.; Inline key hints in menus, tooltips, and docs, with ShortcutKbd or ShortcutKeys.
- Avoid when: Use ShortcutKbd alone when shortcuts are fixed and only need to be shown.

### `signature-pad` — Signature pad [Inputs]
Smooth ink that thins with speed, with undo, replay, and PNG or SVG export.
- Files: uiarc-free-code/components/signature-pad/signature-pad.tsx; uiarc-free-code/components/signature-pad/signature-pad.module.css
- Exports: SignaturePad, signatureToSvg, signatureToPng
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Contracts, delivery confirmations, and consent forms that need a drawn signature.; Initials or quick sketches where pen pressure and natural stroke width matter.; Flows that need a clean, cropped PNG or SVG of the signature.
- Avoid when: Use input for a typed name when a legal drawn signature is not required.

### `skeleton` — Skeleton [Feedback]
Reserve space while content is still loading.
- Files: uiarc-free-code/components/skeleton/skeleton.tsx; uiarc-free-code/components/skeleton/skeleton.module.css
- Exports: Skeleton
- npm: motion · also copy: arc-motion-tokens
- Use when: Loading states for content whose shape is known, like a profile or comment.; Swapping a placeholder into real content with a crossfade and height spring.
- Avoid when: Use progress when you can report a percentage.

### `slider` — Slider [Inputs]
Pick a value or a range on a track that follows your finger.
- Files: uiarc-free-code/components/slider/slider.tsx; uiarc-free-code/components/slider/slider.module.css
- Exports: Slider
- npm: motion · also copy: arc-motion-tokens
- Use when: Approximate values like volume, opacity, or a price range.; Ranges with two thumbs, labelled marks, and a formatted readout.
- Avoid when: Use number-field when the exact number matters.

### `slope-chart` — Slope chart [Data]
Before and after on two axes: lines draw in, rank moves sit beside each value, and switching datasets slides every line to its new slope.
- Files: uiarc-free-code/components/slope-chart/slope-chart.tsx; uiarc-free-code/components/slope-chart/slope-chart.module.css
- Exports: SlopeChart
- npm: motion · also copy: arc-motion-tokens
- Use when: Showing which items rose, which fell, and how the order changed between two periods.; Replacing a grouped bar chart when the change is the story.
- Avoid when: Use line-chart for three or more moments.

### `slot-text` — Slot text [Special]
Text and numbers that spin into their new value on staggered slot machine reels.
- Files: uiarc-free-code/components/slot-text/slot-text.tsx; uiarc-free-code/components/slot-text/slot-text.module.css
- Exports: SlotText
- npm: motion
- Use when: Pricing toggles, KPI cards, dashboards changing period.; Launch moments, raffles, and reveals.
- Avoid when: Values that update several times a second.

### `sortable-data-table` — Sortable data table [Data]
Compare structured records with sortable columns.
- Files: uiarc-free-code/components/sortable-data-table/sortable-data-table.tsx; uiarc-free-code/components/sortable-data-table/sortable-data-table.module.css
- Exports: SortableDataTable
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Tabular records people sort and select, such as projects, invoices, or users.; Tables that need Shift-click range selection and a count line with Clear.
- Avoid when: Use data-grid when people edit cells like a spreadsheet.

### `sparkline` — Sparkline [Data]
Show a compact trend beside a value.
- Files: uiarc-free-code/components/sparkline/sparkline.tsx; uiarc-free-code/components/sparkline/sparkline.module.css
- Exports: Sparkline
- npm: motion · also copy: arc-motion-tokens
- Use when: A compact trend inside a card, table row, or KPI tile.; Small charts people can scrub by pointer or keyboard to read past values.
- Avoid when: Use bar-chart for comparing discrete periods with axes.

### `split-button` — Split button [Actions]
A primary action with a menu of nearby alternatives.
- Files: uiarc-free-code/components/split-button/split-button.tsx; uiarc-free-code/components/split-button/split-button.module.css
- Exports: SplitButton
- npm: @radix-ui/react-dropdown-menu, lucide-react, motion · also copy: arc-motion-tokens
- Use when: One default action with a few close variants, like Merge with Squash and Rebase.; Export or share actions where one format is the usual pick and others sit behind the chevron.; Copy actions that swap the label to Copied in place while offering alternatives.
- Avoid when: Use dropdown-menu when there is no default action and every option is equal.

### `stepper` — Stepper [Feedback]
Show where a person is in a multi-step flow and what is done.
- Files: uiarc-free-code/components/stepper/stepper.tsx; uiarc-free-code/components/stepper/stepper.module.css
- Exports: Stepper
- npm: motion · also copy: arc-motion-tokens
- Use when: Showing position in a strict multi-step flow like checkout or account setup.; Flows where people can jump back to completed steps, via onStepSelect.; Vertical timelines of steps with descriptions and error states.
- Avoid when: Use multi-step-form when you also want the step content, navigation, and success state.

### `streamgraph` — Streamgraph [Data]
Layered streams on a wiggle baseline that morph between ranges, with a layer you can isolate and read week by week.
- Files: uiarc-free-code/components/streamgraph/streamgraph.tsx; uiarc-free-code/components/streamgraph/streamgraph.module.css
- Exports: Streamgraph
- npm: motion · also copy: arc-motion-tokens
- Use when: Showing the changing share of topics, channels, or genres week by week.; Storytelling dashboards where the shape of seasonality and spikes is the point.; Comparing ranges where a morph between them explains what changed.
- Avoid when: Use line-chart when exact values or comparisons between series matter.

### `swipe-actions` — Swipe actions [Actions]
Reveal row actions with a swipe, or from the same actions in a menu.
- Files: uiarc-free-code/components/swipe-actions/swipe-actions.tsx; uiarc-free-code/components/swipe-actions/swipe-actions.module.css
- Exports: SwipeActions, SwipeActionsRow, SwipeAction
- npm: @radix-ui/react-dropdown-menu, lucide-react, motion · also copy: arc-motion-tokens
- Use when: Touch-first triage lists such as mail, notifications, or tasks.; Rows with one or two quick actions per side, like Archive and Mark unread.; Lists where a full swipe should commit the main action and the row should animate away.
- Avoid when: Use context-menu or dropdown-menu for desktop-first tables.

### `switch` — Switch [Inputs]
A tactile toggle for settings that take effect immediately.
- Files: uiarc-free-code/components/switch/switch.tsx; uiarc-free-code/components/switch/switch.module.css
- Exports: Switch
- npm: @radix-ui/react-switch, motion · also copy: arc-motion-tokens
- Use when: Settings that take effect as soon as they are flipped, like notifications.; Settings lists where each row is one on and off preference.
- Avoid when: Use checkbox when the choice waits for a submit button.

### `tabs` — Tabs [Disclosure]
Switch between related content in the same context.
- Files: uiarc-free-code/components/tabs/tabs.tsx; uiarc-free-code/components/tabs/tabs.module.css
- Exports: Tabs, TabsList, TabsTrigger, TabsContent
- npm: @radix-ui/react-tabs, lucide-react, motion · also copy: arc-motion-tokens
- Use when: Peer views of the same object, such as Overview, Activity, and Settings.; Panels with different heights, where the container should spring between them.; Long tab sets that need to scroll horizontally with edge buttons.
- Avoid when: Use segmented-control for a compact value toggle not tied to panels.

### `tag-input` — Tag input [Inputs]
Turn short text values into removable tags.
- Files: uiarc-free-code/components/tag-input/tag-input.tsx; uiarc-free-code/components/tag-input/tag-input.module.css
- Exports: TagInput
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Free-form lists of short values like tags, keywords, or emails.; Fields where people add values by pressing Enter or comma.
- Avoid when: Use multi-select or chip-group when values come from a fixed list.

### `text-morph` — Text morph [Text]
Morph a label into its next state, letter by letter.
- Files: uiarc-free-code/components/text-morph/text-morph.tsx; uiarc-free-code/components/text-morph/text-morph.module.css
- Exports: TextMorph
- npm: motion · also copy: arc-motion-tokens
- Use when: Status words that change a few letters at a time, such as Follow and Following.; Custom buttons or badges that need a morphing label without the rest of the button.; Inline counters or short state labels that should glide instead of jump.
- Avoid when: Use word-rotate for a sentence with one cycling word.

### `text-reveal` — Text reveal [Text]
Reveal a short piece of content with restrained motion.
- Files: uiarc-free-code/components/text-reveal/text-reveal.tsx; uiarc-free-code/components/text-reveal/text-reveal.module.css
- Exports: TextReveal
- also copy: arc-motion-tokens
- Use when: Above-the-fold hero headlines that animate on page load.; Landing page intros where text must appear on first paint even if scripts are slow.
- Avoid when: Use in-view-title for section titles further down the page.

### `text-shimmer` — Text shimmer [Text]
Show ongoing work with a calm light across the words.
- Files: uiarc-free-code/components/text-shimmer/text-shimmer.tsx; uiarc-free-code/components/text-shimmer/text-shimmer.module.css
- Exports: TextShimmer
- npm: motion · also copy: arc-motion-tokens
- Use when: AI thinking or loading labels such as Generating summary.; Short status lines that should show ongoing work and settle when done.
- Avoid when: Use text-stream for the response text itself.

### `textarea` — Textarea [Inputs]
A multiline field for notes, descriptions, and longer text.
- Files: uiarc-free-code/components/textarea/textarea.tsx; uiarc-free-code/components/textarea/textarea.module.css
- Exports: Textarea
- npm: motion · also copy: arc-motion-tokens
- Use when: Free-form multi-line text like bios, comments, or feedback.; Fields with a live character count, which rolls its digits in the helper row.
- Avoid when: Use input for single-line values.

### `theme-switch` — Theme switcher [Actions]
Four smooth ways to move between light and dark appearance.
- Files: uiarc-free-code/components/theme-switch/theme-switch.tsx; uiarc-free-code/components/theme-switch/theme-switch.module.css
- Exports: ThemeSwitch
- npm: lucide-react, motion · also copy: arc-motion-tokens, button
- Use when: A single light and dark toggle in an app or marketing top bar.; Pages that want to run their own view transition from the button's position.
- Avoid when: Use user-menu when theme choice, including system, belongs inside an account menu.

### `theme-switch-eclipse` — Eclipse [Actions]
The next appearance crosses the page like an eclipse.
- Files: uiarc-free-code/components/theme-switch-eclipse/theme-switch.tsx; uiarc-free-code/components/theme-switch-eclipse/theme-switch.module.css
- Exports: ThemeSwitch
- npm: lucide-react, motion · also copy: arc-motion-tokens, button
- Use when: Marketing or showcase pages where the theme change should feel like an event.; Layouts where a directional sweep across the page reads naturally.
- Avoid when: Use theme-switch-rise for everyday product chrome where a calmer change fits.

### `theme-switch-rise` — Rise [Actions]
The next appearance rises into place.
- Files: uiarc-free-code/components/theme-switch-rise/theme-switch.tsx; uiarc-free-code/components/theme-switch-rise/theme-switch.module.css
- Exports: ThemeSwitch
- npm: lucide-react, motion · also copy: arc-motion-tokens, button
- Use when: Product chrome and dashboards where the theme change should be calm.; Icon-only toggles in a top bar, as the library's own header uses it.
- Avoid when: Use theme-switch-eclipse for a dramatic change on a showcase page.

### `theme-switch-split` — Split [Actions]
The next appearance opens from a slim center seam.
- Files: uiarc-free-code/components/theme-switch-split/theme-switch.tsx; uiarc-free-code/components/theme-switch-split/theme-switch.module.css
- Exports: ThemeSwitch
- npm: lucide-react, motion · also copy: arc-motion-tokens, button
- Use when: Centered layouts where the theme should open symmetrically from a middle seam.; Pages where the switch position varies, since the split does not depend on where the button sits.
- Avoid when: Use theme-switch for a reveal that grows from the button itself.

### `time-picker` — Time picker [Inputs]
Choose a time with sensible keyboard behavior.
- Files: uiarc-free-code/components/time-picker/time-picker.tsx; uiarc-free-code/components/time-picker/time-picker.module.css
- Exports: TimePicker
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Picking a time of day at a fixed interval, such as meetings or reminders.; Fields that show 12-hour times but store 24-hour HH:mm values.
- Avoid when: Use date-picker for dates, pairing the two for a timestamp.

### `timeline` — Timeline [Data]
Follow what happened, newest first, grouped by day.
- Files: uiarc-free-code/components/timeline/timeline.tsx; uiarc-free-code/components/timeline/timeline.module.css
- Exports: Timeline
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Project history, audit logs, and deploy streams where recency matters.; Live feeds where new updates slide in at the top.; Rows that expand in place to show logs or detail.
- Avoid when: Use sortable-data-table when people sort or compare.

### `toast` — Toast [Feedback]
Brief confirmation for a completed background action.
- Files: uiarc-free-code/components/toast/toast.tsx; uiarc-free-code/components/toast/toast.module.css
- Exports: Toast
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: A single success confirmation, like Changes saved, controlled with local state.; Demos or small apps that do not need a toast queue.
- Avoid when: Use toast-stack for app-wide notifications with types, actions, updates, and stacking.

### `toast-stack` — Toast stack [Feedback]
Stack short results at the edge until you reach for them.
- Files: uiarc-free-code/components/toast-stack/toast-stack.tsx; uiarc-free-code/components/toast-stack/toast-stack.module.css
- Exports: ToastStackProvider, ToastStack, useToastStack
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: App-wide notifications for async results, errors, and undo.; Loading toasts that morph into success or error when work finishes.; Toasts with an action button, like View or Undo.
- Avoid when: Use toast for a single locally controlled confirmation.

### `toggle-group` — Toggle group [Inputs]
A row of icon or text toggles, single or multiple: one pressed fill glides between options, or each fades in on its own and neighbours join, as in a formatting toolbar.
- Files: uiarc-free-code/components/toggle-group/toggle-group.tsx; uiarc-free-code/components/toggle-group/toggle-group.module.css
- Exports: ToggleGroup, ToggleGroupItem
- npm: motion · also copy: arc-motion-tokens
- Use when: Formatting toolbars: bold, italic and underline as multiple, alignment as single.; Compact view options on a canvas, map or editor, such as grid or list, or which layers to show.; Any short row of icon toggles that apply immediately.
- Avoid when: Use segmented-control for switching between views, ranges or tabs of content.

### `tooltip` — Tooltip [Disclosure]
Short supporting text for unfamiliar controls.
- Files: uiarc-free-code/components/tooltip/tooltip.tsx; uiarc-free-code/components/tooltip/tooltip.module.css
- Exports: Tooltip
- npm: @radix-ui/react-tooltip, motion · also copy: arc-motion-tokens
- Use when: One-line labels on icon-only buttons in toolbars.; Revealing the full text of truncated labels on hover or focus.; Dense toolbars where moving between icons should show labels instantly after the first one.
- Avoid when: Use popover for anything with links or controls inside.

### `tree-table` — Tree table [Data]
A table with nested rows, tri-state selection, hierarchy-preserving sort, and lazy-loaded children.
- Files: uiarc-free-code/components/tree-table/tree-table.tsx; uiarc-free-code/components/tree-table/tree-table.module.css
- Exports: TreeTable, collectExpandableIds
- npm: lucide-react, motion · also copy: arc-motion-tokens, checkbox
- Use when: File or folder listings with size, owner, and modified columns.; Budgets, org charts, or accounts where totals roll up through nested rows.; Large trees whose deeper levels should load from the server on demand.
- Avoid when: Use tree-view for navigation trees without columns.

### `tree-view` — Tree view [Data]
Navigate nested folders and structured content.
- Files: uiarc-free-code/components/tree-view/tree-view.tsx; uiarc-free-code/components/tree-view/tree-view.module.css
- Exports: TreeView
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Files, folders, and nested categories people expand and select.; Side panels next to code-block or a detail view where selection drives content.; Hierarchies that need full keyboard navigation with arrow keys.
- Avoid when: Use accordion for a few collapsible sections of content.

### `treemap` — Treemap [Data]
A squarified treemap: click to drill and the tiles grow to fill the view, with a breadcrumb back and metrics that morph every tile.
- Files: uiarc-free-code/components/treemap/treemap.tsx; uiarc-free-code/components/treemap/treemap.module.css
- Exports: Treemap
- npm: motion · also copy: arc-motion-tokens
- Use when: Many parts where the biggest ones matter and people drill for detail.; Showing size and a second measure at once.
- Avoid when: Use bar-chart when exact comparisons between similar values matter.

### `usage-meter` — Usage meter [Feedback]
Show what fills an allowance and how close it is to the limit.
- Files: uiarc-free-code/components/usage-meter/usage-meter.tsx; uiarc-free-code/components/usage-meter/usage-meter.module.css
- Exports: UsageMeter
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Quota against a fixed allowance, such as storage, seats, or API calls.; Billing pages that should show what takes the space and how close the plan is to full.; Plans that can go over the limit, where the overage should be clear without relying on color.
- Avoid when: Use progress for task completion.

### `user-menu` — User menu [Actions]
Your account, settings, theme, and sign out behind the avatar. Opens as a bottom sheet on phones.
- Files: uiarc-free-code/components/user-menu/user-menu.tsx; uiarc-free-code/components/user-menu/user-menu.module.css
- Exports: UserMenu, PresenceDot
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: The single account entry point in an app top bar.; Menus that combine presence status, theme preference, account links, and sign out.; Apps that want async sign out with a spinner in the menu.
- Avoid when: Use dropdown-menu for generic command lists.

### `waffle-chart` — Waffle chart [Data]
A ten by ten unit chart where every cell is one percent, and cells fly to their new group when the data changes.
- Files: uiarc-free-code/components/waffle-chart/waffle-chart.tsx; uiarc-free-code/components/waffle-chart/waffle-chart.module.css
- Exports: WaffleChart
- npm: motion · also copy: arc-motion-tokens
- Use when: Showing shares of one whole where people should be able to count units.; Comparing the same categories across a few datasets, such as countries or years.; Replacing a pie or donut when small shares need to stay visible.
- Avoid when: Use line-chart or streamgraph for how shares change over time.


---

<!-- references/free-blocks-and-shared.md -->

# Free blocks and shared foundation (22 + 3)

## Contents

- `blog-grid` — Blog grid
- `changelog-feed` — Changelog feed
- `command-palette` — Command palette
- `comparison-table` — Comparison table
- `contact-section` — Contact section
- `cta-section` — CTA section
- `empty-states` — Empty states
- `faq-section` — FAQ section
- `file-upload` — File upload
- `hero-section` — Hero section
- `login-centered` — Centered login
- `logo-marquee` — Logo marquee
- `newsletter-signup` — Newsletter signup
- `notification-center` — Notification center
- `otp-input` — OTP input
- `page-header` — Page header
- `plan-comparison` — Plan comparison
- `sign-in` — Sign in
- `signup-form` — Sign up form
- `site-footer` — Site footer
- `site-header` — Site header
- `stats-band` — Stats band
- `arc-foundation` — Arc foundation
- `arc-motion-tokens` — Arc motion tokens
- `arc-skill` — Arc agent skill
Free blocks are complete interface sections. Their files may include *-data.ts
sample-data files (replace the sample data with real data) and extra sub-components
in the same folder. Blocks compose free components: their registry dependencies
are listed per item and scripts/install-item.py resolves them recursively.
The 3 shared items at the end are required infrastructure, installed once per project.

### `blog-grid` — Blog grid
A blog index with a featured post, category filter, post cards, pagination and an in-place reader.
- Files: uiarc-free-code/blocks/blog-grid/blog-grid.tsx; uiarc-free-code/blocks/blog-grid/blog-grid-data.ts; uiarc-free-code/blocks/blog-grid/blog-grid.module.css
- Exports: BlogGrid, BlogPost
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: A marketing site blog or journal index.; Resource hubs with a few categories and a featured story.
- Avoid when: Use changelog-page for release notes with versions.

### `changelog-feed` — Changelog feed
Release notes you can filter, open in place, and scroll through month by month.
- Files: uiarc-free-code/blocks/changelog-feed/changelog-feed.tsx; uiarc-free-code/blocks/changelog-feed/changelog-feed.module.css; uiarc-free-code/blocks/changelog-feed/lib/media.ts
- Exports: ChangelogFeed
- npm: lucide-react, motion · also copy: arc-motion-tokens, copy-button
- Use when: A product changelog or release notes page grouped by month.; Release notes with type filters such as features, fixes, and improvements.; Changelogs that should offer an email subscribe action in the header.
- Avoid when: Use timeline for a short vertical list of events without filters.

### `command-palette` — Command palette
A complete keyboard driven action surface with search, grouped results, and shortcuts.
- Files: uiarc-free-code/blocks/command-palette/command-palette.tsx; uiarc-free-code/blocks/command-palette/command-palette.module.css
- Exports: CommandPalette, CommandItem
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: App-wide command search opened with Cmd or Ctrl plus K.; Jumping to pages, creating items, and running actions from one input.; Inline search panels that group results with shortcuts.
- Avoid when: Use combobox to pick a value inside a form.

### `comparison-table` — Comparison table
An us versus them table with a sticky header, a highlighted column, and a stacked phone view.
- Files: uiarc-free-code/blocks/comparison-table/comparison-table.tsx; uiarc-free-code/blocks/comparison-table/comparison-table-data.ts; uiarc-free-code/blocks/comparison-table/comparison-table.module.css
- Exports: ComparisonTable
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Showing how your product stacks up against named alternatives.; Feature matrices with three to five columns and grouped rows.
- Avoid when: Use plan-comparison to compare your own pricing tiers.

### `contact-section` — Contact section
A validated contact form that morphs into a confirmation, support channels, and office cards with local times.
- Files: uiarc-free-code/blocks/contact-section/contact-section.tsx; uiarc-free-code/blocks/contact-section/contact-section.module.css; uiarc-free-code/blocks/contact-section/lib/media.ts
- Exports: ContactSection, ContactSectionBlock
- npm: lucide-react, motion · also copy: arc-motion-tokens, avatar, button, copy-button, input, segmented-control, textarea
- Use when: Contact pages and sections on marketing sites.; Sales or support pages that list several channels with response times.; Companies with offices in several time zones.
- Avoid when: Use support-widget for an in-app help launcher.

### `cta-section` — CTA section
A call to action as a centered closing section, a split beside a setup card that completes itself, or a dismissible banner.
- Files: uiarc-free-code/blocks/cta-section/cta-section.tsx; uiarc-free-code/blocks/cta-section/cta-section-data.ts; uiarc-free-code/blocks/cta-section/lib/media.ts; uiarc-free-code/blocks/cta-section/cta-section.module.css
- Exports: CtaSection
- npm: lucide-react, motion · also copy: arc-motion-tokens, button, segmented-control
- Use when: The last section of a landing page, asking for a trial or demo.; An in-page prompt beside a product visual that shows the outcome.; A slim promotional banner above content.
- Avoid when: The first screen of a page. Use Hero section.

### `empty-states` — Empty states
Four empty states in one illustration whose shapes morph between scenes as you switch tabs.
- Files: uiarc-free-code/blocks/empty-states/empty-states.tsx; uiarc-free-code/blocks/empty-states/empty-states.module.css; uiarc-free-code/blocks/empty-states/empty-states-art.ts
- Exports: EmptyStates
- npm: motion · also copy: arc-motion-tokens, button
- Use when: A reference for no results, offline, inbox zero, and 404 moments with one shared illustration style.; Extracting one scene as a richer empty state for a key screen.
- Avoid when: Use empty-state for a simple empty state with an icon, text, and action.

### `faq-section` — FAQ section
FAQs as an accordion, a topic rail, or a searchable list that highlights matches.
- Files: uiarc-free-code/blocks/faq-section/faq-section.tsx; uiarc-free-code/blocks/faq-section/faq-section.module.css
- Exports: FaqSection, FaqSectionBlock
- npm: lucide-react, motion · also copy: arc-motion-tokens, search-field, segmented-control
- Use when: FAQ sections on pricing, product, and support pages.; Long FAQs that benefit from categories or live search.
- Avoid when: Use accordion for generic collapsible content that is not a question list.

### `file-upload` — File upload
A complete file selection flow with constraints, progress, and error feedback.
- Files: uiarc-free-code/blocks/file-upload/file-upload.tsx; uiarc-free-code/blocks/file-upload/file-upload.module.css
- Exports: FileUpload, FileUploadItem
- npm: lucide-react, motion · also copy: arc-motion-tokens
- Use when: Uploading files with per-file progress, retry, and remove.; Attachments that must be validated by type and size before upload.; Uploads that should abort when a file is removed, via the AbortSignal.
- Avoid when: Use file-dropzone when you only need to pick files without upload state.

### `hero-section` — Hero section
Three full screen SaaS heroes: a live dashboard rising from the bottom edge over a drifting mesh, a workflow graph that routes sample events node by node, and editorial type over a mesh gradient.
- Files: uiarc-free-code/blocks/hero-section/hero-section.tsx; uiarc-free-code/blocks/hero-section/hero-section.module.css; uiarc-free-code/blocks/hero-section/hero-content.tsx; uiarc-free-code/blocks/hero-section/hero-content.module.css; uiarc-free-code/blocks/hero-section/hero-motion.ts; uiarc-free-code/blocks/hero-section/hero-mesh.tsx; uiarc-free-code/blocks/hero-section/hero-mesh.module.css; uiarc-free-code/blocks/hero-section/hero-cadence.tsx; uiarc-free-code/blocks/hero-section/hero-cadence.module.css; uiarc-free-code/blocks/hero-section/hero-relay.tsx; uiarc-free-code/blocks/hero-section/hero-relay.module.css; uiarc-free-code/blocks/hero-section/hero-lumen.tsx; uiarc-free-code/blocks/hero-section/hero-lumen.module.css; uiarc-free-code/blocks/hero-section/hero-lumen-data.ts; uiarc-free-code/blocks/hero-section/lib/media.ts
- Exports: HeroSection, HeroLumen, HeroRelay, HeroCadence, HeroMesh, HeroSectionBlock
- npm: lucide-react, motion · also copy: arc-motion-tokens, avatar, button, copy-button, line-chart, segmented-control, sparkline
- Use when: The first section of a SaaS landing page, when the product screen is the pitch (Screenshot).; Developer tools, automation, and infrastructure products, where showing the product working is the pitch (Workflow).; A launch or download page that wants one confid…
- Avoid when: Use page-header for titles inside app screens.

### `login-centered` — Centered login
A passkey-first login card on a quiet ring backdrop that morphs through email and code.
- Files: uiarc-free-code/blocks/login-centered/login-centered.tsx; uiarc-free-code/blocks/login-centered/login-centered.module.css
- Exports: LoginCentered
- npm: lucide-react, motion · also copy: arc-motion-tokens, button, input, otp-input
- Use when: A full screen sign in or sign up page where passkeys are the main method.; Auth flows that fall back to a six digit email code.; Products that want one card for both sign in and sign up.
- Avoid when: Use login-split for password sign in beside a brand photo.

### `logo-marquee` — Logo marquee
A quiet, continuously moving row of brand marks with a pause control.
- Files: uiarc-free-code/blocks/logo-marquee/logo-marquee.tsx; uiarc-free-code/blocks/logo-marquee/logo-marquee.module.css
- Exports: LogoMarquee, LogoMarqueeBrand
- npm: lucide-react · also copy: button
- Use when: A customer or integration logo strip on a landing page.; Social proof sections with a heading and a short supporting line.
- Avoid when: Use integrations when each logo needs a description or a connect action.

### `newsletter-signup` — Newsletter signup
An email signup framed by a stack of past issues; subscribing drops the next issue, addressed to you, onto the front.
- Files: uiarc-free-code/blocks/newsletter-signup/newsletter-signup.tsx; uiarc-free-code/blocks/newsletter-signup/newsletter-signup-data.ts; uiarc-free-code/blocks/newsletter-signup/lib/media.ts; uiarc-free-code/blocks/newsletter-signup/newsletter-signup.module.css
- Exports: NewsletterSignup
- npm: lucide-react, motion · also copy: arc-motion-tokens, animated-counter, segmented-control, switch
- Use when: Collecting emails for a newsletter, digest, or changelog that has real issues to show.; The end of a blog post or docs page.
- Avoid when: Account creation with a password. Use Signup form.

### `notification-center` — Notification center
A home for updates with read state, grouped information, and animated disclosure.
- Files: uiarc-free-code/blocks/notification-center/notification-center.tsx; uiarc-free-code/blocks/notification-center/notification-center.module.css
- Exports: NotificationCenter, NotificationItem
- npm: @radix-ui/react-popover, lucide-react, motion · also copy: arc-motion-tokens, avatar
- Use when: A bell in the app header with an unread badge and an inbox of recent updates.; Notifications people can mark read, expand, and dismiss in bulk.
- Avoid when: Use toast-stack for transient messages that should disappear.

### `otp-input` — OTP input
A six digit verification flow with paste support and keyboard navigation.
- Files: uiarc-free-code/blocks/otp-input/otp-input.tsx; uiarc-free-code/blocks/otp-input/otp-input.module.css
- Exports: OtpInput
- npm: motion · also copy: arc-motion-tokens
- Use when: Verification codes from email or SMS.; Two-factor authentication code entry.
- Avoid when: Use password-field for secrets people type from memory.

### `page-header` — Page header
A project page header that folds into a compact bar as you scroll, with tabs whose counts roll.
- Files: uiarc-free-code/blocks/page-header/page-header.tsx; uiarc-free-code/blocks/page-header/lib/use-copy-feedback.ts; uiarc-free-code/blocks/page-header/page-header.module.css
- Exports: PageHeader
- npm: @radix-ui/react-dropdown-menu, @radix-ui/react-tabs, lucide-react, motion · also copy: arc-motion-tokens, animated-counter, avatar-group, avatar, badge, button, progress
- Use when: The top of a project, repository, or record page with breadcrumbs, status, people, and tabs.; Detail pages with long content where the header should fold into a compact bar as people scroll.; Headers that need a few primary actions plus an overflow menu for t…
- Avoid when: Use tabs and breadcrumb on their own when the page only needs navigation, not status and people.

### `plan-comparison` — Plan comparison
Compare meaningful differences between plans and billing periods.
- Files: uiarc-free-code/blocks/plan-comparison/plan-comparison.tsx; uiarc-free-code/blocks/plan-comparison/plan-comparison.module.css
- Exports: PlanComparison
- npm: lucide-react, motion · also copy: arc-motion-tokens, button, segmented-control, switch
- Use when: Comparing two tiers side by side with a feature matrix.; Pricing pages that switch between monthly and yearly prices.; Long feature lists where people want to see only the differences.
- Avoid when: Use usage-pricing when price depends on seats or volume.

### `sign-in` — Sign in
A sign in card that morphs from email to a six digit code to your account.
- Files: uiarc-free-code/blocks/sign-in/sign-in.tsx; uiarc-free-code/blocks/sign-in/sign-in.module.css; uiarc-free-code/blocks/sign-in/lib/media.ts
- Exports: SignIn
- npm: lucide-react, motion · also copy: arc-motion-tokens, avatar, button, input, otp-input
- Use when: The entry screen of an app with email code sign in.; Sign in cards that also offer passkeys and single sign-on.; Passwordless flows that should confirm the account before continuing.
- Avoid when: Use login-centered, login-split, or login-immersive for password based layouts.

### `signup-form` — Sign up form
An account creation flow with field validation, password strength, and a clear completion state.
- Files: uiarc-free-code/blocks/signup-form/signup-form.tsx; uiarc-free-code/blocks/signup-form/signup-form.module.css
- Exports: SignupForm, SignupDetails
- npm: motion · also copy: arc-motion-tokens, button, checkbox, input, password-field
- Use when: The client side of an email and password sign-up.; Sign-up pages that should show password strength and a product updates opt-in.; Flows that want an in-place success panel after the account is created.
- Avoid when: Use sign-in or login-split for returning users.

### `site-footer` — Site footer
A website footer with link columns and newsletter, a minimal layout, and a large fading Arc mark.
- Files: uiarc-free-code/blocks/site-footer/site-footer.tsx; uiarc-free-code/blocks/site-footer/site-footer.module.css
- Exports: SiteFooter, SiteFooterLink, SiteFooterBlock
- npm: lucide-react, motion · also copy: arc-motion-tokens, button, segmented-control
- Use when: The closing section of a marketing, docs, or product site.; Footers that need a newsletter signup and a status link.; Minimal one-row footers for app shells and docs.
- Avoid when: Use a plain row with breadcrumb or links inside signed-in app screens.

### `site-header` — Site header
A sticky website header that turns solid on scroll, with a gliding active link, mega menu panels, and a mobile sheet.
- Files: uiarc-free-code/blocks/site-header/site-header.tsx; uiarc-free-code/blocks/site-header/site-header.module.css; uiarc-free-code/blocks/site-header/lib/media.ts
- Exports: SiteHeader, SiteHeaderBlock
- npm: lucide-react, motion · also copy: arc-motion-tokens, segmented-control
- Use when: The top bar of a marketing site, landing page, or docs site.; Product sites with grouped destinations that deserve a mega menu with a feature card.; Pages that need one clear sign-up action in the header.
- Avoid when: Use workspace-sidebar or sidebar-rail inside a signed-in app.

### `stats-band` — Stats band
Headline numbers that count up in view, each with a tiny visual that proves it and a context line on hover, plain or in a hairline grid.
- Files: uiarc-free-code/blocks/stats-band/stats-band.tsx; uiarc-free-code/blocks/stats-band/stats-band-data.ts; uiarc-free-code/blocks/stats-band/stats-band.module.css; uiarc-free-code/blocks/stats-band/stats-band-world.ts
- Exports: StatsBand
- npm: motion · also copy: arc-motion-tokens, segmented-control
- Use when: Marketing pages that back a claim with a few numbers.; About and investor pages with headline metrics.
- Avoid when: Live product metrics with trends. Use Metric card or Metrics dashboard.

### `arc-foundation` — Arc foundation

- Files: uiarc-free-code/shared/arc-foundation/foundation.css
- also copy: arc-motion-tokens

### `arc-motion-tokens` — Arc motion tokens

- Files: uiarc-free-code/shared/arc-motion-tokens/motion-tokens.ts; uiarc-free-code/shared/arc-motion-tokens/lib/motion-tokens.ts

### `arc-skill` — Arc agent skill

- Files: uiarc-free-code/shared/arc-skill/SKILL.md; uiarc-free-code/shared/arc-skill/INSTRUCTIONS.md; uiarc-free-code/shared/arc-skill/accessibility.md; uiarc-free-code/shared/arc-skill/checklist.md; uiarc-free-code/shared/arc-skill/components.md; uiarc-free-code/shared/arc-skill/composition.md; uiarc-free-code/shared/arc-skill/copy.md; uiarc-free-code/shared/arc-skill/design.md; uiarc-free-code/shared/arc-skill/example-dashboard.md; uiarc-free-code/shared/arc-skill/example-pricing.md; uiarc-free-code/shared/arc-skill/example-settings.md; uiarc-free-code/shared/arc-skill/motion.md; uiarc-free-code/shared/arc-skill/responsive.md


---

<!-- references/pro-components.md -->

# Pro components — markdown specs (119)

## Contents

- `action-morph` — Action morph
- `activity-rings` — Activity rings
- `agent-cursor` — Agent cursor
- `agent-handoff` — Agent handoff
- `agent-loop` — Agent loop
- `agent-plan` — Agent plan
- `agent-status` — Agent status
- `agent-timeline` — Agent timeline
- `ai-command` — AI command
- `ai-mascot` — AI mascot
- `ai-spark` — AI spark
- `ai-translate` — AI translate
- `ai-workflow` — AI workflow
- `ask-your-data` — Ask your data
- `avatar-upload` — Avatar upload
- `black-hole` — Black hole
- `booking-pill` — Booking pill
- `branch-graph` — Branch graph
- `card-to-article` — Card to article
- `code-suggestion` — Code suggestion
- `confirm-popover` — Confirm popover
- `connector-setup` — Connector setup
- `context-window` — Context window
- `control-center` — Control center
- `cover-flow` — Cover flow
- `cube-mascot` — Cube mascot
- `data-flow` — Data flow
- `data-grid` — Data grid
- `date-reel` — Date reel
- `dictation-button` — Dictation button
- `dns-resolution` — DNS resolution
- `dock` — Dock
- `dot-grid` — Dot grid
- `emoji-picker` — Emoji picker
- `enrich-column` — Enrich column
- `funnel-chart` — Funnel chart
- `generation-stats` — Generation stats
- `ghost-mascot` — Ghost mascot
- `ghost-text` — Ghost text
- `glass-card` — Glass card
- `glass-menu` — Glass menu
- `glass-segmented` — Glass segmented
- `glass-tabbar` — Glass tab bar
- `gravity-well` — Gravity well
- `holo-card` — Holo card
- `image-generation` — Image generation
- `image-reveal` — Image reveal
- `image-trail` — Image trail
- `ink-fluid` — Ink fluid
- `install-snippet` — Install snippet
- `keycap-keyboard` — Keycap keyboard
- `lightbox-gallery` — Lightbox gallery
- `link-unfurl` — Link unfurl
- `liquid-tab-bar` — Liquid tab bar
- `live-visitors` — Live visitors
- `llm-cost-calculator` — LLM cost calculator
- `meeting-summary` — Meeting summary
- `mega-menu-morph` — Mega menu morph
- `metric-ticker` — Metric ticker
- `mixture-of-experts` — Mixture of experts
- `model-card` — Model card
- `model-training` — Model training
- `morph-loader` — Morph loader
- `morph-nav` — Morph nav
- `multi-region-failover` — Multi-region failover
- `now-playing` — Now playing
- `orbit-logos` — Orbit logos
- `orbit-menu` — Orbit menu
- `page-curl` — Page curl
- `payment-flow` — Payment flow
- `photo-grid` — Photo grid
- `pii-redaction` — PII redaction
- `pixel-mascot` — Pixel mascot
- `presence-stack` — Presence stack
- `prize-wheel` — Prize wheel
- `product-gallery` — Product gallery
- `prompt-cache` — Prompt cache
- `provider-keys` — Provider keys
- `provider-status` — Provider status
- `race-bar-chart` — Race bar chart
- `radar-chart` — Radar chart
- `realtime-stream` — Realtime stream
- `reasoning-block` — Reasoning block
- `reasoning-tree` — Reasoning tree
- `referral-card` — Referral card
- `reply-draft` — Reply draft
- `response-feedback` — Response feedback
- `sand-text` — Sand text
- `sankey-flow` — Sankey flow
- `share-access` — Share access
- `share-sheet` — Share sheet
- `sheet-stack` — Sheet stack
- `skeleton-morph` — Skeleton morph
- `smart-form-fill` — Smart form fill
- `social-proof-toast` — Social proof toast
- `source-cards` — Source cards
- `speculative-decoding` — Speculative decoding
- `speech-player` — Speech player
- `split-bar` — Split bar
- `starter-prompts` — Starter prompts
- `sticker-peel` — Sticker peel
- `stretch-refresh` — Stretch refresh
- `sunburst` — Sunburst
- `team-switcher` — Team switcher
- `ticket-router` — Ticket router
- `time-dial` — Time dial
- `tldr-toggle` — TL;DR toggle
- `toc-progress` — Table of contents progress
- `tone-tuner` — Tone tuner
- `tool-call` — Tool call
- `training-run` — Training run
- `trial-banner` — Trial banner
- `typewriter-terminal` — Typewriter terminal
- `undo-toast` — Undo toast
- `upgrade-prompt` — Upgrade prompt
- `vector-search` — Vector search
- `voice-orb` — Voice orb
- `voice-recorder` — Voice recorder
- `wallet-stack` — Wallet stack
Pro source code is NOT in the pack (it is token-gated by Arc). What the pack has
is the official markdown spec for each item: documented props, usage, keyboard,
accessibility, motion, responsive and performance behavior. Rebuild the item from
its spec (SKILL.md workflow C). Never claim the rebuild is the original source.

### `action-morph` — Action morph [Special]
A floating button that morphs into a quick-action menu, then an inline form, then back with a check.
- Spec (read fully before building): uiarc-pro-markdowns/components/action-morph.md
- Main export in the spec's usage: ActionMorph
- Use when: Quick capture of tasks, notes, or comments without leaving the page.; Apps with a few frequent create actions that deserve a persistent button.; Mobile layouts where a corner button should expand into a small form.
- Avoid when: Use dialog or drawer for longer forms with several fields.
- Related: `action-button`, `orbit-menu`, `dropdown-menu`, `dialog`, `toast`

### `activity-rings` — Activity rings [Special]
Daily goals as tick rings that sweep, count up, and trace a second lap past 100%.
- Spec (read fully before building): uiarc-pro-markdowns/components/activity-rings.md
- Main export in the spec's usage: ActivityRings
- Use when: Daily goals that fill up and can be exceeded, like move, exercise, and stand.; Fitness or habit dashboards with a week picker to compare days.
- Avoid when: Use progress or gauge for a single value.
- Related: `progress`, `gauge`, `usage-meter`, `activity-heatmap`, `animated-counter`

### `agent-cursor` — Agent cursor [Special]
A live document where Claude edits like a collaborator. Its labeled cursor comes out of its avatar, selects a paragraph and streams in a rewrite, adds a heading and fixes a typo, while a teammate's cursor reads along. Changes stay tinted until someone accepts or undoes them from a floating review bar.
- Spec (read fully before building): uiarc-pro-markdowns/components/agent-cursor.md
- Main export in the spec's usage: AgentCursor
- Use when: Showing an AI writing assistant that edits a doc alongside people, with accept and undo.; Landing or onboarding sections that demo a collaborative AI editor in motion.; A product surface that streams structured edits from an agent and needs a human review ste…
- Avoid when: Free form chat or Q&A: use a chat transcript component.
- Related: `agent-status`, `tool-call`, `text-shimmer`, `avatar`, `button`

### `agent-handoff` — Agent handoff [Special]
A support conversation where an AI assistant hands off to a person. When it transfers, a card shows the summary it passes to the team and the typical wait. The person then joins and takes over, and a thin timeline on the left marks each step.
- Spec (read fully before building): uiarc-pro-markdowns/components/agent-handoff.md
- Main export in the spec's usage: AgentHandoff, useHandoffSimulation
- Use when: A support widget where the AI answers first and escalates to a human agent.; Showing customers what the assistant shared with the team, so they do not repeat themselves.; Marketing or docs pages that explain an AI to human handoff flow.
- Avoid when: A general chat with one assistant and no handoff: use chat-thread.
- Related: `chat-thread`, `agent-status`, `agent-timeline`, `tool-call`, `avatar`

### `agent-loop` — Agent loop [Special]
An illustration of the agent loop: gather context, take action, verify, repeat, with a bright head circling three stations around the model.
- Spec (read fully before building): uiarc-pro-markdowns/components/agent-loop.md
- Main export in the spec's usage: AgentLoop
- Use when: Docs, explainers and landing pages that teach how an AI agent works: it gathers context, calls tools, checks the result and repeats until the task is done.; Showing why agents take several passes, with a failed check or a failed tool call that sends the loop…
- Avoid when: Use agent-run or research-run to show a real agent's live steps and streamed output.
- Related: `reasoning-tree`, `agent-run`, `tool-call`, `agent-plan`, `context-window`, `text-shimmer`

### `agent-plan` — Agent plan [Special]
The plan an agent writes before it acts: edit, reorder or add steps while it is a draft, then watch it work through them as a live checklist.
- Spec (read fully before building): uiarc-pro-markdowns/components/agent-plan.md
- Main export in the spec's usage: AgentPlan
- Use when: An agent should show and get approval for its plan before it edits code, runs commands or touches production.; A person needs to adjust the agent's plan (rename, reorder, remove or add steps) and then watch the same plan execute.; A side panel or chat message…
- Avoid when: Use agent-run for a streaming transcript of everything the agent did, with tool calls and output, rather than a checklist of steps.
- Related: `agent-run`, `agent-tasks`, `agent-approvals`, `agent-loop`, `ai-chat`, `text-shimmer`

### `agent-status` — Agent status [Special]
A compact live status pill for a running AI agent: the agent's mark in a live ring, the current activity and an elapsed timer, opening into the steps so far.
- Spec (read fully before building): uiarc-pro-markdowns/components/agent-status.md
- Main export in the spec's usage: AgentStatus, useAgentRunSimulation
- Use when: An app header, title bar or composer that needs to show at a glance that an agent is running, what it is doing and for how long.; Coding, research or browser agents that pause for approval, so the person can approve or deny without opening a full run view.; B…
- Avoid when: Use agent-run or research-run when the run itself is the page and every step, tool call and output needs room.
- Related: `agent-run`, `agent-approvals`, `ai-composer`, `research-run`, `tool-call`, `agent-plan`, `text-shimmer`

### `agent-timeline` — Agent timeline [Special]
A compact timeline of one orchestrated agent run: the orchestrator and its subagents share a time axis, handoffs draw in between rows, and a playhead replays thinking, tool calls and waiting while the header counts time, tokens and cost. Hover a span for what it did, or click it to trace its handoff path.
- Spec (read fully before building): uiarc-pro-markdowns/components/agent-timeline.md
- Main export in the spec's usage: AgentTimeline
- Use when: Showing how an orchestrator split work across subagents and how long each part took, in a run history, a trace viewer or a debugging panel.; Replaying a finished agent run in a product demo or changelog, with real numbers for time, tokens and cost.; Following…
- Avoid when: Use agent-orchestrator for a full screen of agent lanes with streaming text and messages; this timeline is the compact, reusable view of timing.
- Related: `agent-orchestrator`, `agent-run`, `research-run`, `tool-call`, `agent-status`, `agent-plan`, `context-window`

### `ai-command` — AI command [Special]
A Cmd+K command palette with an AI mode. Search pages and actions, or press Tab to ask a question: the answer streams inside the palette with numbered sources, and the next steps it suggests, like filing a Linear issue or opening a Notion doc, run straight from the list.
- Spec (read fully before building): uiarc-pro-markdowns/components/ai-command.md
- Main export in the spec's usage: AiCommand, AiCommandAction, AiCommandSource
- Use when: A global Cmd+K in a SaaS app where people both jump to pages and ask questions about their workspace.; Search that should fall back to an AI answer when nothing matches.; Answers that lead straight to an action in another tool, like filing a Linear issue or p…
- Avoid when: A long, multi-turn conversation: use a chat thread.
- Related: `command-palette`, `source-cards`, `tool-call`, `starter-prompts`

### `ai-mascot` — AI mascot [Special]
A small assistant character, a soft pebble with pill eyes and a companion dot, that shows what the AI is doing. It breathes and glances when idle, leans in to listen, looks up while the dot orbits its head, reads along the line it writes, squints with a sparkle when done and shakes once with worried brows on an error.
- Spec (read fully before building): uiarc-pro-markdowns/components/ai-mascot.md
- Main export in the spec's usage: AiMascot
- Use when: Give an assistant a face that shows what it is doing: in a reply header, beside a composer, on an image canvas while it generates, or in an empty state.; Products that want generation to feel alive and friendly without a spinner, with states that read at 24px.
- Avoid when: Use agent-status when people need the steps, tools and elapsed time of a run, not just a mood.
- Related: `agent-status`, `text-shimmer`, `ai-spark`, `image-reveal`, `starter-prompts`, `dictation-button`, `ai-chat`, `reasoning-block`

### `ai-spark` — AI spark [Special]
A brand-quality animated spark mark. Four tapered rays and four lighter diagonals breathe at rest, ripple while thinking, pulse like a heartbeat while writing, then gather and settle when done. Every status change blends from the pose the mark is already in.
- Spec (read fully before building): uiarc-pro-markdowns/components/ai-spark.md
- Main export in the spec's usage: AiSpark
- Use when: Showing that an assistant is thinking or writing, inline above a streaming reply.; A send or generate button that turns into a working indicator inside a composer.; An image or canvas tool that needs a calm, branded working mark over the canvas while a render…
- Avoid when: Determinate progress with a known percentage; use a progress bar or the generation stats component instead.
- Related: `text-shimmer`, `agent-status`, `reasoning-block`, `ai-mascot`, `ai-chat`, `ai-composer`

### `ai-translate` — AI translate [Special]
A message card where picking a language streams the AI translation in place, sentence by sentence over the dimmed original, with a detected-language chip, a Show original toggle and a status line credited to the model's mark.
- Spec (read fully before building): uiarc-pro-markdowns/components/ai-translate.md
- Main export in the spec's usage: AiTranslate
- Use when: Messages, comments, reviews or support tickets written in another language, translated on demand inside the product.; Release notes or announcements that readers in several regions open in their own language.; Any place you want an AI translation to feel inli…
- Avoid when: Translating a whole page or app interface; use your i18n framework.
- Related: `chat-thread`, `text-shimmer`, `dropdown-menu`, `response-feedback`, `meeting-summary`

### `ai-workflow` — AI workflow [Special]
A Linear-style AI workflow card where a Gmail trigger, a Claude step, a branch and Slack and Linear actions sit on one hairline rail, and a test run glides down it, opening each step's output inline. Steps are added from a compact command menu with real app marks.
- Spec (read fully before building): uiarc-pro-markdowns/components/ai-workflow.md
- Main export in the spec's usage: AiWorkflow, WorkflowOutput
- Use when: An automation or integrations page where people assemble a short trigger, AI step and action flow and want to test it in place.; Onboarding or marketing surfaces that show how an AI step slots between real apps, with a working test run.; Reviewing what an exi…
- Avoid when: Large free-form graphs with many branches, loops or merges: use a canvas editor instead.
- Related: `agent-run`, `agent-plan`, `tool-call`, `agent-routines`, `connector-setup`, `agent-orchestrator`

### `ask-your-data` — Ask your data [Special]
A natural language to chart card: you ask a question, PostgreSQL streams into a collapsible, syntax highlighted panel, the query runs with a rolling row count, and the answer builds as stacked bars, lines or a table, with a one line insight streamed in underneath.
- Spec (read fully before building): uiarc-pro-markdowns/components/ask-your-data.md
- Main export in the spec's usage: AskYourData, AskYourDataResult
- Use when: Letting people ask product or business questions in plain words and see a chart, with the SQL one click away to verify or copy.; Embedding an analytics answer in a dashboard card, an admin page or an AI assistant's result view.; Teaching or auditing text to S…
- Avoid when: Use bar-chart or line-chart when the query is fixed and there is no question to ask.
- Related: `tool-call`, `ai-chat`, `agent-run`, `bar-chart`, `line-chart`, `text-shimmer`

### `avatar-upload` — Avatar upload [Inputs]
Click or drop a photo onto the avatar to crop it in place with drag, pinch and zoom. It uploads through a progress ring and settles, with clear errors and retry.
- Spec (read fully before building): uiarc-pro-markdowns/components/avatar-upload.md
- Main export in the spec's usage: AvatarUpload
- Use when: Profile, account and team member settings where a person sets their own photo.; Workspace or organization logos that display in a circle.; Onboarding steps that ask for a photo and should show upload progress in place.
- Avoid when: Several files or documents at once: use file-dropzone.
- Related: `avatar`, `file-dropzone`, `avatar-group`

### `black-hole` — Black hole [Special]
A delete transition that pulls the chosen items into a tiny singularity while the rest of the list bends around it; undo spins them back out.
- Spec (read fully before building): uiarc-pro-markdowns/components/black-hole.md
- Main export in the spec's usage: BlackHole, BlackHoleHandle, BlackHoleOptions
- Use when: Deleting or archiving a handful of selected rows, cards, or files, with an Undo right after.; Emptying a trash, clearing notifications, or dismissing a batch where the removal should feel final.
- Avoid when: High frequency deletes such as clearing a single chip or tag. Use a quick height collapse instead.
- Related: `swipe-actions`, `toast-stack`

### `booking-pill` — Booking pill [Special]
One pill that reshapes through party size, date, time, and a ticket.
- Spec (read fully before building): uiarc-pro-markdowns/components/booking-pill.md
- Main export in the spec's usage: BookingPill
- Use when: Venue or service pages where booking a table or slot is the one action people came for.; Mobile-first flows that walk through party size, date, time, and confirm in one surface.
- Avoid when: Use date-picker and time-picker inside a regular form for multi-field checkouts.
- Related: `date-picker`, `time-picker`, `calendar`, `number-field`, `stepper`

### `branch-graph` — Branch graph [Special]
A git commit graph where branches draw in as colored lanes, merge commits join lines, a rebase lifts commits and replays them onto main, a squash folds them into one, and hovering a commit shows its message, author and diff stats.
- Spec (read fully before building): uiarc-pro-markdowns/components/branch-graph.md
- Main export in the spec's usage: BranchGraph
- Use when: A merge strategy picker in a code review or pull request screen, showing exactly what main will look like afterwards.; A commit history panel in a developer tool, with hover details and keyboard browsing.; Docs and landing pages for version control or CI prod…
- Avoid when: Use git-branches for a looping, non-interactive illustration of a branch, pull request, and release.
- Related: `timeline`

### `card-to-article` — Card to article [Special]
Story cards that open into full articles with one seamless morph and shrink back into their exact slot when dragged down.
- Spec (read fully before building): uiarc-pro-markdowns/components/card-to-article.md
- Main export in the spec's usage: CardToArticle
- Use when: Blogs, journals, and changelogs where each entry has a strong image.; Case study and portfolio grids.; Editorial landing sections that preview stories without leaving the page.
- Avoid when: Use a normal link to a page when articles are long or need their own URL and SEO.
- Related: `expandable-card`, `lightbox-gallery`, `photo-grid`, `dialog`

### `code-suggestion` — Code suggestion [Special]
An AI code edit suggestion where the model's proposed changes stream into a small editor panel as inline diff hunks, and you accept or reject each one, or all at once with Cmd+Enter. Accepted hunks fold into the file with a smooth height change.
- Spec (read fully before building): uiarc-pro-markdowns/components/code-suggestion.md
- Main export in the spec's usage: CodeSuggestion
- Use when: Showing an AI's proposed edit to a file as an inline diff the person accepts or rejects hunk by hunk.; Approving an agent's file change before it is written, with a clear record of what was kept.; Landing pages and docs that demonstrate an AI coding feature w…
- Avoid when: Use a dedicated diff tool for large multi file diffs or side by side comparisons; this card is for one file and a handful of hunks.
- Related: `tool-call`, `agent-approvals`, `code-block`, `text-shimmer`, `button`

### `confirm-popover` — Confirm popover [Disclosure]
A destructive button that grows into a small confirmation card, with the consequence, optional type-to-confirm, progress on the Confirm button, and a check or error before folding back.
- Spec (read fully before building): uiarc-pro-markdowns/components/confirm-popover.md
- Main export in the spec's usage: ConfirmPopover
- Use when: A danger zone in settings: delete project, transfer ownership, revoke a member.; A row action in a table where a modal would lose the row's context.; Any destructive action that needs a sentence of consequence and a visible result without leaving the page.
- Avoid when: Reversible removals such as archiving; use undo-toast so the action is instant and recoverable.
- Related: `confirm-morph`, `hold-to-confirm`, `dialog`, `undo-toast`

### `connector-setup` — Connector setup [Special]
A "Connect your tools" card for an AI assistant. Each app connects inline: it redirects, authorizes and runs a first sync with a progress hairline, then lists the scopes it was granted and offers Disconnect with an inline confirm.
- Spec (read fully before building): uiarc-pro-markdowns/components/connector-setup.md
- Main export in the spec's usage: ConnectorSetup, ConnectorMark
- Use when: An assistant's settings or onboarding step where people connect workspace apps.; A first-run checklist that needs to show the OAuth handshake and first sync inline, without leaving the page.; Reviewing which scopes an assistant holds per app and revoking them.
- Avoid when: Browsing dozens of integrations by category: use the integrations-grid block.
- Related: `tool-call`, `agent-status`, `agent-approvals`

### `context-window` — Context window [Special]
An AI context window as a grid of 200 cells: the system prompt, tools, files, summary and messages fill it in order, a threshold row marks where compaction starts, and sending a message, attaching a file or compacting shows exactly how much still fits.
- Spec (read fully before building): uiarc-pro-markdowns/components/context-window.md
- Main export in the spec's usage: ContextWindow
- Use when: Showing developers or power users what fills a model's context and when it will compact.; Agent and coding tools that compact long sessions and want the effect to be understandable.; Docs and onboarding that explain context windows, compaction and output rese…
- Avoid when: A simple quota or plan usage bar; use usage-meter.
- Related: `model-picker`, `ai-composer`, `agent-run`, `usage-meter`, `ai-chat`

### `control-center` — Control center [Special]
Workspace quick settings: tiles that morph into detail, a duration dial, and rubber-banded meters.
- Spec (read fully before building): uiarc-pro-markdowns/components/control-center.md
- Main export in the spec's usage: ControlCenter
- Use when: A quick settings panel with a handful of toggles and levels for a web workspace.; Focus session controls with a duration dial and allowed people.; Notification channel toggles grouped behind one tile.
- Avoid when: Use switch, slider, and radio-group directly in a regular settings form.
- Related: `switch`, `slider`, `radio-group`, `time-dial`, `dialog`

### `cover-flow` — Cover flow [Special]
A depth rail of images you can throw, with soft grounded shadows and a quiet reflection.
- Spec (read fully before building): uiarc-pro-markdowns/components/cover-flow.md
- Main export in the spec's usage: CoverFlow
- Use when: Six to twelve visual items where looking at one at a time is the point, such as albums, places, or collections.; Showcase rails that should respond to drag, throw, and sideways trackpad scroll.
- Avoid when: Use carousel for general slides or content cards.
- Related: `carousel`, `card-stack`, `photo-grid`

### `cube-mascot` — Cube mascot [Special]
An isometric cube mascot where three shaded faces and a painted-on face show what the assistant is doing. It turns a quarter turn in eased steps while thinking, prints lines onto the floor while writing, settles with a sparkle when done, and shakes once on error.
- Spec (read fully before building): uiarc-pro-markdowns/components/cube-mascot.md
- Main export in the spec's usage: CubeMascot
- Use when: Give an assistant a recognisable, product-like character that shows it is generating: in a reply header, in a composer, on an image canvas or in an empty state.; Brands with a geometric, technical feel where a soft blob would feel off.
- Avoid when: Use ai-mascot for a softer, rounder character, or when you need a listening state.
- Related: `ai-mascot`, `agent-status`, `text-shimmer`, `ai-spark`, `image-reveal`, `ai-chat`, `reasoning-block`

### `data-flow` — Data flow [Special]
Data flow illustration. Sources (app, database, events) are on the left, a processing core with a live count sits in the middle, and destinations (warehouse, dashboard, alerts) are on the right. Records leave as hollow dots and travel curved paths. In the core they turn into solid accent squares, then fan out to each destination; alerts receives about every third record.
- Spec (read fully before building): uiarc-pro-markdowns/components/data-flow.md
- Main export in the spec's usage: DataFlow
- Use when: A hero or feature section explaining how data moves through a product.; Docs pages introducing an ingestion, transform, or routing concept.; Integration pages that show which sources feed which destinations.
- Avoid when: Use sankey-flow to show real volumes between stages.
- Related: `sankey-flow`, `orbit-logos`, `realtime-stream`

### `data-grid` — Data grid [Data]
A spreadsheet grid with range selection, inline editing, a fill handle, and animated sorting.
- Spec (read fully before building): uiarc-pro-markdowns/components/data-grid.md
- Main export in the spec's usage: DataGrid, DataGridColumn, DataGridBulkAction, DataGridDataSource, Types, data-grid-model helpers
- Use when: Editing many values in place like a spreadsheet, such as budgets, price lists, or inventory.; Data people move to and from Excel or Google Sheets with copy and paste.; Work that needs range selection, a fill handle, fill down, and undo.; Large tables, up to t…
- Avoid when: Use sortable-data-table for read-only records with sorting and row selection.
- Related: `sortable-data-table`, `filter-toolbar`, `date-picker`, `animated-counter`, `pagination`

### `date-reel` — Date reel [Special]
A 3D wheel date and time picker (like iOS reels) with momentum scrolling, snapping, curved perspective, and full keyboard support.
- Spec (read fully before building): uiarc-pro-markdowns/components/date-reel.md
- Main export in the spec's usage: DateReel
- Use when: Scheduling a send, reminder or post where a phone-style wheel is familiar and faster than a calendar grid.; Touch-first flows and mobile web, where flicking a reel beats typing a date.; Birthdays and other dates far from today, using date mode with its month,…
- Avoid when: Use date-picker or date-range-picker when people need to see a whole month or pick a range.
- Related: `time-picker`, `date-picker`, `time-dial`

### `dictation-button` — Dictation button [Special]
A chat composer with voice input, where the mic springs into a recording pill with a smooth live waveform, a timer, and cancel and insert buttons. Words stream into the field as you speak, muted until the recognizer settles them.
- Spec (read fully before building): uiarc-pro-markdowns/components/dictation-button.md
- Main export in the spec's usage: DictationButton, DictationControl, useDictation, DictationRecognizer
- Use when: Chat and agent composers where people would rather talk than type: mobile, long prompts, accessibility.; Notes, comments and support replies where dictation saves time and the person still edits before sending.; Any field that already has a send action and ne…
- Avoid when: Full duplex voice conversations with spoken replies; use a voice agent pattern with call controls instead.
- Related: `chat-thread`, `text-shimmer`, `tooltip`, `tool-call`, `agent-status`

### `dns-resolution` — DNS resolution [Special]
A browser asks for a domain and the query hops from the resolver to a root server, the TLD server and the authoritative nameserver, each pointing to the next, until an IP address comes back and the page connects. The resolver keeps the answer with a TTL ring that drains, and a second lookup is answered straight from that cache in one short hop.
- Spec (read fully before building): uiarc-pro-markdowns/components/dns-resolution.md
- Main export in the spec's usage: DnsResolution
- Use when: A docs or marketing section that explains how a domain name turns into an address and why the second visit is faster.; Custom domain setup, DNS hosting, resolver or CDN pages that need the chain of servers and the role of TTL to click.; Teaching material wher…
- Avoid when: Use webhook-fanout to show one event delivered to many endpoints with retries.
- Related: `data-flow`

### `dock` — Dock [Special]
A floating tool dock with a gliding label, a springy selection, and trays that grow out of it.
- Spec (read fully before building): uiarc-pro-markdowns/components/dock.md
- Main export in the spec's usage: Dock
- Use when: A floating tool or mode switcher, such as the tools of a canvas or whiteboard editor.; Toolbars where related tools share one slot and open a tray, like shape variants.; Tool sets people may reorder by drag or Alt with the arrow keys.
- Avoid when: Use segmented-control for two to four inline options.
- Related: `segmented-control`, `action-button`, `liquid-tab-bar`, `reorderable-list`, `orbit-menu`

### `dot-grid` — Dot grid [Special]
A dot field that bulges around the cursor like a lens and ripples from every click.
- Spec (read fully before building): uiarc-pro-markdowns/components/dot-grid.md
- Main export in the spec's usage: DotGrid
- Use when: A landing page hero that should feel alive without video.; A background for an empty state, a sign in panel, or a launch countdown.; A playful section divider people can poke at.
- Avoid when: Behind dense text or data; the moving dots compete with reading.
- Related: `stretch-refresh`

### `emoji-picker` — Emoji picker [Inputs]
A full emoji picker with instant search, scroll-synced categories, skin tones, recently used emoji, and a virtualized, keyboard-navigable grid.
- Spec (read fully before building): uiarc-pro-markdowns/components/emoji-picker.md
- Main export in the spec's usage: EmojiPicker
- Use when: Message composers, comment boxes, and chat inputs.; Choosing an emoji for a status, a project, a page icon, or a label.; Any text field where people expect the full emoji set with search.
- Avoid when: Use reactions for a small, fixed set of quick responses on a post or comment.
- Related: `reactions`, `popover`, `combobox`, `textarea`, `mention-input`, `rich-text-editor`

### `enrich-column` — Enrich column [Special]
An AI enrichment column for a data table, where one prompt runs down every row and each cell shimmers while it works, then settles into a value with its source or a failure you can retry.
- Spec (read fully before building): uiarc-pro-markdowns/components/enrich-column.md
- Main export in the spec's usage: EnrichColumn
- Use when: Enriching a list of companies or leads with facts an agent can look up (headcount, funding, tech stack).; Classifying or summarizing rows with one prompt, with a visible source per answer.; Showing per-row AI progress with stop, re-run and retry in a CRM, sal…
- Avoid when: Large spreadsheets with many columns and editing; use Data grid and add an AI column there.
- Related: `tool-call`, `agent-status`, `text-shimmer`, `sortable-data-table`, `data-grid`, `ask-your-data`

### `funnel-chart` — Funnel chart [Data]
A tapered conversion funnel with drop-off at every step, a device split that morphs the band, and dots that stream through it.
- Spec (read fully before building): uiarc-pro-markdowns/components/funnel-chart.md
- Main export in the spec's usage: FunnelChart
- Use when: Conversion through a fixed sequence of steps.; Comparing how two segments convert through the same steps.; A hero chart on a growth or analytics page where the drop-off is the story.
- Avoid when: Use sankey-flow when people can branch, skip, or loop between steps.
- Related: `sankey-flow`, `bar-chart`, `waffle-chart`, `stepper`

### `generation-stats` — Generation stats [Special]
A live stats strip for a streaming LLM response where time to first token, speed with a sparkline, output tokens and cost count up in tabular numerals beside the model's real mark, then settle and open into a latency and token cost breakdown.
- Spec (read fully before building): uiarc-pro-markdowns/components/generation-stats.md
- Main export in the spec's usage: GenerationStats, useGenerationSimulation
- Use when: Under assistant messages in a chat product that shows people what a response cost or how fast it was.; Playgrounds, eval runners and internal dev panels comparing models on latency, throughput and cost.; Admin or debugging views that inspect a single request'…
- Avoid when: Use context-window to show how much of a model's context a conversation has used.
- Related: `context-window`, `tool-call`, `agent-status`, `ai-chat`, `model-picker`, `text-shimmer`, `copy-button`

### `ghost-mascot` — Ghost mascot [Special]
A floating ghost mascot whose soft sheet ripples at the hem while it hovers. It blinks when idle, turns toward you to listen, fades a little translucent while thinking, draws a tiny pen line while writing, smiles with a sparkle when done and wobbles once on an error.
- Spec (read fully before building): uiarc-pro-markdowns/components/ghost-mascot.md
- Main export in the spec's usage: GhostMascot
- Use when: Give an assistant a light, friendly face that shows what it is doing: in a reply header, in a composer, over an image canvas while it generates, or in an empty state.; Products that want generation to feel alive without a spinner, with states that still read…
- Avoid when: Use agent-status when people need the steps, tools and elapsed time of a run, not just a mood.
- Related: `ai-mascot`, `agent-status`, `text-shimmer`, `ai-spark`, `image-generation`, `ai-chat`, `ai-composer`, `dictation-button`

### `ghost-text` — Ghost text [Special]
An inline AI autocomplete where muted ghost text continues your sentence exactly at the caret and Tab turns it solid in place. Cmd+Right takes it one word at a time, Escape fades it away, and a calm chip shows the model behind it.
- Spec (read fully before building): uiarc-pro-markdowns/components/ghost-text.md
- Main export in the spec's usage: GhostText, createDemoSuggest
- Use when: Long-form fields people write in product: pull request descriptions, emails, support replies, issue bodies, release notes, CRM notes.; Short single-line fields where a likely completion saves typing, such as an email subject or a commit message.; Anywhere you…
- Avoid when: Use ai-composer for a chat-style prompt box that sends a message to an assistant.
- Related: `textarea`, `input`, `ai-composer`, `code-suggestion`, `text-shimmer`, `ai-chat`

### `glass-card` — Glass card [Special]
A glass info panel over a photo whose rim catches a pointer-following highlight while the card tilts; tap to morph it into a detail sheet.
- Spec (read fully before building): uiarc-pro-markdowns/components/glass-card.md
- Main export in the spec's usage: GlassCard
- Use when: Profile, host, or creator cards on a landing page or in a discovery grid.; A featured product or stay where the photo sells and the details can wait for a tap.
- Avoid when: Dense grids of many cards; tilt and glass on every tile gets busy. Use card.
- Related: `holo-card`, `expandable-card`, `card-to-article`

### `glass-menu` — Glass menu [Special]
A glass action menu whose trigger morphs into the panel, with a highlight pill that glides between rows, one in-place submenu, and full keyboard support.
- Spec (read fully before building): uiarc-pro-markdowns/components/glass-menu.md
- Main export in the spec's usage: GlassMenu, GlassMenuItem
- Use when: Actions for a photo, file, or card shown over an image or a colorful canvas.; A title menu in an editor or viewer, where the title itself opens the actions.
- Avoid when: Plain settings pages with no imagery behind the menu. Use dropdown-menu on a neutral surface.
- Related: `dropdown-menu`, `orbit-menu`, `morph-nav`

### `glass-segmented` — Glass segmented [Special]
A glass segmented control whose liquid indicator stretches between segments and can be dragged and flung.
- Spec (read fully before building): uiarc-pro-markdowns/components/glass-segmented.md
- Main export in the spec's usage: GlassSegmented
- Use when: Switching the view of a photo, map, or media surface.; A compact filter over imagery, such as day, week, month on a hero chart.
- Avoid when: Plain forms on neutral surfaces. Use segmented-control.
- Related: `segmented-control`, `liquid-tab-bar`, `billing-toggle`

### `glass-tabbar` — Glass tab bar [Special]
A floating Liquid Glass tab bar that refracts what scrolls beneath it, with a glass lens that glides, magnifies and can be dragged between tabs, and an optional search bubble; it compacts on scroll down.
- Spec (read fully before building): uiarc-pro-markdowns/components/glass-tabbar.md
- Main export in the spec's usage: GlassTabBar, GlassTabBarItem
- Use when: Mobile web apps and PWAs with three to five top level sections and one global action such as search.; Content feeds where the bar should step aside while reading and come back on scroll up.
- Avoid when: Desktop layouts with many sections; use a sidebar or morph-nav.
- Related: `liquid-tab-bar`, `morph-nav`, `dock`, `tabs`

### `gravity-well` — Gravity well [Special]
A grid of tiles that bends toward the cursor like spacetime, with a click that sends a shockwave through it.
- Spec (read fully before building): uiarc-pro-markdowns/components/gravity-well.md
- Main export in the spec's usage: GravityWell
- Use when: A team, customer, or moodboard wall where playfulness is the point.; Landing page sections that show breadth: many logos, avatars, or photos at once.
- Avoid when: Grids people must scan or click precisely, like file pickers; use a plain grid.
- Related: `dot-grid`, `photo-grid`

### `holo-card` — Holo card [Special]
A member card that tilts toward you with a holographic foil and flips to its back.
- Spec (read fully before building): uiarc-pro-markdowns/components/holo-card.md
- Main export in the spec's usage: HoloCard
- Use when: A membership or subscription card on an account or welcome page.; A shareable profile, badge, or achievement that people will screenshot.; A collectible or reward reveal.
- Avoid when: Use card for ordinary content; the effect is too loud for lists.
- Related: `sticker-peel`, `wallet-stack`, `cover-flow`

### `image-generation` — Image generation [Special]
An image studio where each image forms on a dot matrix: a soft halftone wave breathes across the grid, the dots take the colours of the coming photo and grow into a coloured halftone, then blur away into the sharp photo. One large canvas with a mono size label, a filmstrip of four variations, a prompt bar with model and ratio, and upscale with a sweeping dot band, vary or download, with real provider marks and a built-in simulation.
- Spec (read fully before building): uiarc-pro-markdowns/components/image-generation.md
- Main export in the spec's usage: ImageGeneration, simulateImageGeneration
- Use when: A text to image feature inside a product: marketing asset tools, listing photo helpers, slide or doc illustration.; Any flow where people compare a few candidates and continue with one (upscale, vary, download).; Prototyping an image model integration before…
- Avoid when: A full canvas editor with layers, masks and inpainting; build on a canvas library instead.
- Related: `model-picker`, `ai-composer`, `text-shimmer`

### `image-reveal` — Image reveal [Special]
An image generation canvas where a soft, blurred preview made from the image's own colors sharpens top to bottom behind a soft-edged band. It works the way ChatGPT, Midjourney and Gemini show images forming, with fine film grain, a translucent progress pill and calm queued and error states.
- Spec (read fully before building): uiarc-pro-markdowns/components/image-reveal.md
- Main export in the spec's usage: ImageReveal
- Use when: Showing an image model's progress on a canvas or in a chat reply.; A batch of image variations sampling side by side.; A queued image job that should feel alive before it starts.
- Avoid when: Plain image loading from a CDN; use a blur-up placeholder or a skeleton.
- Related: `text-shimmer`, `agent-status`, `tool-call`, `progress`

### `image-trail` — Image trail [Special]
Moving the pointer leaves a curated trail of photos that pop in, lean, and fade away.
- Spec (read fully before building): uiarc-pro-markdowns/components/image-trail.md
- Main export in the spec's usage: ImageTrail
- Use when: A portfolio or agency hero that should feel alive on first move.; Travel, food, or product stories told through a sequence of photos.; Launch pages that want an instantly playful surface.
- Avoid when: Use photo-grid or lightbox-gallery when people need to look at each photo.
- Related: `photo-grid`, `lightbox-gallery`

### `ink-fluid` — Ink fluid [Special]
A real time fluid simulation behind your hero: the cursor stirs soft ink that swirls, settles and fades; calm when left alone.
- Spec (read fully before building): uiarc-pro-markdowns/components/ink-fluid.md
- Main export in the spec's usage: InkFluid
- Use when: A landing hero or sign in screen that should feel alive without a video.; Empty states and waiting screens where a gentle, interactive background rewards curiosity.
- Avoid when: Dense product surfaces such as tables and forms. Movement behind data distracts.
- Related: `dot-grid`, `image-trail`

### `install-snippet` — Install snippet [Special]
A "get started in 30 seconds" card where framework tabs, three numbered steps and highlighted snippets take a developer from install to first event. Generate key wipes a fresh API key into the placeholder in place.
- Spec (read fully before building): uiarc-pro-markdowns/components/install-snippet.md
- Main export in the spec's usage: InstallSnippet
- Use when: A quickstart that has to work for several frameworks without three pages of docs.; Onboarding where creating an API key is part of getting started.; Marketing pages for developer tools that want to show how little setup it takes.
- Avoid when: A single code sample with no steps: use code-block.
- Related: `code-block`, `copy-button`, `connector-setup`, `onboarding-checklist`, `tabs`

### `keycap-keyboard` — Keycap keyboard [Special]
Mechanical keycaps that sink and light up as you type, with the text above the board.
- Spec (read fully before building): uiarc-pro-markdowns/components/keycap-keyboard.md
- Main export in the spec's usage: KeycapKeyboard
- Use when: Landing pages for keyboard-first products and developer tools.; Onboarding that teaches shortcuts by lighting the keys they use.; Playful empty states and easter eggs.
- Avoid when: Form input; use a real text field.
- Related: `shortcut-recorder`, `command-palette`, `hold-to-confirm`

### `lightbox-gallery` — Lightbox gallery [Special]
A masonry grid where photos zoom from their slot into a viewer you can swipe, pinch, and drag away.
- Spec (read fully before building): uiarc-pro-markdowns/components/lightbox-gallery.md
- Main export in the spec's usage: LightboxGallery
- Use when: Photo collections people browse and inspect up close, such as trips, portfolios, or listings.; Mixed portrait and landscape sets that should keep their aspect ratios in a masonry grid.
- Avoid when: Use photo-grid for a square grid with pinch zoom between densities.
- Related: `photo-grid`, `carousel`, `dialog`, `cover-flow`

### `link-unfurl` — Link unfurl [Special]
A composer where pasting a URL shows a loading shimmer on the link, then unfurls it into a rich preview card with title, image and favicon in one morph, which can be collapsed back to the inline link or removed.
- Spec (read fully before building): uiarc-pro-markdowns/components/link-unfurl.md
- Main export in the spec's usage: LinkUnfurl
- Use when: A message or comment composer where pasted links should show what they point to before sending.; Product marketing that shows how a chat or notes app handles links.
- Avoid when: Use hover-card to preview a link someone reads, not writes.
- Related: `mention-input`, `rich-text-editor`, `hover-card`, `chat-thread`

### `liquid-tab-bar` — Liquid tab bar [Special]
Tabs with a lens selection that slides between them, swaps labels cleanly, and fills in icons as it passes.
- Spec (read fully before building): uiarc-pro-markdowns/components/liquid-tab-bar.md
- Main export in the spec's usage: LiquidTabBar, liquidTabId / liquidPanelId
- Use when: Switching between a handful of peer sections with icons, such as an app's main areas.; Bottom or top bars on mobile-style layouts where the selection should feel physical.; Tabs that carry badge counts for new items.
- Avoid when: Use tabs for text-only panels inside a page.
- Related: `tabs`, `segmented-control`, `morph-nav`, `dock`

### `live-visitors` — Live visitors [Special]
A realtime visitors card where the live count rolls digit by digit, new arrivals ping in on a dotted world map, the top pages reorder with bars, and signups and upgrades tick in with country flags.
- Spec (read fully before building): uiarc-pro-markdowns/components/live-visitors.md
- Main export in the spec's usage: LiveVisitors, useLiveVisitorsSimulation
- Use when: Realtime visitors on a marketing site or app, next to signups and upgrades as they happen.; Launch days and campaigns where a team watches traffic and conversions live.; Admin and growth dashboards that need one glanceable tile for right now.
- Avoid when: Historical trends over days or weeks; use a chart with axes.
- Related: `account-health`, `generation-stats`, `goal-tracker`, `agent-status`, `credit-topup`

### `llm-cost-calculator` — LLM cost calculator [Special]
A pricing calculator for LLM workloads. Set tokens per request, requests per day and prompt caching, and eight current models re-rank by monthly cost. Bars glide and prices roll as you drag.
- Spec (read fully before building): uiarc-pro-markdowns/components/llm-cost-calculator.md
- Main export in the spec's usage: LlmCostCalculator, computeLlmCost
- Use when: A pricing or settings page needs an honest monthly estimate for an LLM workload across several models.; People pick a model for a feature and should see how cost moves with prompt size, output length, traffic and caching.; An internal tool compares provider p…
- Avoid when: Use model-picker to choose a model in a chat or composer without a cost comparison.
- Related: `model-picker`, `model-card`, `context-window`, `usage-meter`, `usage-pricing`, `slider`

### `meeting-summary` — Meeting summary [Special]
An AI meeting notes card: the header shows the Google Meet or Zoom mark, the attendees and the duration. Summary, Decisions and Action items stream in after a short summarizing pass. Hover any line to see the transcript quote it came from, then check off action items or send them to Linear or Notion.
- Spec (read fully before building): uiarc-pro-markdowns/components/meeting-summary.md
- Main export in the spec's usage: MeetingSummary
- Use when: Showing AI notes after a call in a CRM, a recruiting tool, a meeting recorder or a team workspace.; Turning a transcript into decisions and owned tasks that people can push to their tracker.; Any summary where readers should be able to check a point against w…
- Avoid when: Live captions or a running transcript during the call; use text-stream or a transcript view.
- Related: `tool-call`, `agent-status`, `checkbox`, `avatar`, `copy-button`

### `mega-menu-morph` — Mega menu morph [Disclosure]
A site header whose menus share one floating panel. Moving between sections morphs its size, slides the next menu in from that side and glides the caret under the new trigger, with hover intent, a safe triangle and an accordion sheet on narrow screens.
- Spec (read fully before building): uiarc-pro-markdowns/components/mega-menu-morph.md
- Main export in the spec's usage: MegaMenuMorph
- Use when: A marketing site header with product, solution, developer and company sections that each need a rich menu.; A documentation or platform site whose top sections deserve descriptions, a featured story or a status line.; Anywhere visitors browse several menus in…
- Avoid when: Use morph-nav for a compact floating pill navigation with search built in.
- Related: `morph-nav`, `dropdown-menu`, `site-header`, `tabs`

### `metric-ticker` — Metric ticker [Data]
A strip of live KPIs that roll to new values digit by digit and flash their change; rest on one to pause the strip and open its recent trend as a sparkline.
- Spec (read fully before building): uiarc-pro-markdowns/components/metric-ticker.md
- Main export in the spec's usage: MetricTicker
- Use when: A compact live readout of several KPIs above a dashboard, a status page or a trading view.; Wall screens and operations views where values change on their own and people glance at them.; A header strip that must fit anywhere from a phone to a wide monitor wit…
- Avoid when: Use metric-card or stat-card for one or two headline numbers with room for context.
- Related: `metric-card`, `sparkline`, `animated-counter`, `line-chart`

### `mixture-of-experts` — Mixture of experts [Special]
An illustration of mixture of experts routing: each token is scored by a router, travels to its top experts, and their outputs merge into the token's result.
- Spec (read fully before building): uiarc-pro-markdowns/components/mixture-of-experts.md
- Main export in the spec's usage: MixtureOfExperts
- Use when: Explaining why a mixture of experts model is cheap per token: only the chosen experts run, which the active parameter readout makes concrete.; Showing how a gate scores experts, picks the top k and blends their outputs, with real or sample scores.; Teaching l…
- Avoid when: Use model-router to pick which model handles a request in a product; this card explains routing inside one model.
- Related: `speculative-decoding`, `agent-loop`, `vector-search`, `context-window`

### `model-card` — Model card [Special]
A model details card where switching models rolls every price, limit and score in place, a token slider estimates monthly cost live, and benchmark bars show each model's rank on hover. Compare crossfades to a side-by-side table against any rival with the better values marked, and the card never changes size.
- Spec (read fully before building): uiarc-pro-markdowns/components/model-card.md
- Main export in the spec's usage: ModelCard
- Use when: The detail pane of a model picker, showing what the highlighted model can do and what it costs before someone selects it.; Model pages in docs or a marketplace, with limits, prices and a quick benchmark read against close rivals.; Settings where a team picks…
- Avoid when: Use model-picker to choose between many models; pair it with this card for the details.
- Related: `model-picker`, `context-window`, `copy-button`, `segmented-control`, `switch`, `dropdown-menu`, `slider`

### `model-training` — Model training [Special]
Training data batches feed a small neural net diagram whose connections strengthen, a loss curve descends beside it, and an evaluation check turns green at the end.
- Spec (read fully before building): uiarc-pro-markdowns/components/model-training.md
- Main export in the spec's usage: ModelTraining
- Use when: An AI or ML product section that explains training, fine-tuning or evaluation in one glance.; Docs pages introducing batches, epochs, loss curves or held-out evaluation.
- Avoid when: Use line-chart or metric-card for real, live training metrics.
- Related: `data-flow`

### `morph-loader` — Morph loader [Special]
Tiny loaders that morph between shapes and fold into a check or a cross when done.
- Spec (read fully before building): uiarc-pro-markdowns/components/morph-loader.md
- Main export in the spec's usage: MorphLoader
- Use when: Inline progress inside a button, row, or field where the result should appear in the same spot.; Short operations that end in a clear success or failure, such as save, publish, or upload.; Any spinner where a tiny, crisp, brand-consistent mark matters.
- Avoid when: Use progress when the percentage is known.
- Related: `progress`, `skeleton`, `action-button`, `icon-morph`

### `morph-nav` — Morph nav [Special]
A navigation bar that morphs into rich menus, search, and a compact state as one surface.
- Spec (read fully before building): uiarc-pro-markdowns/components/morph-nav.md
- Main export in the spec's usage: MorphNav
- Use when: The top navigation of a marketing or product site with a few sections that each hold several destinations.; Headers where search should grow out of the bar instead of opening a separate modal.; Sites that want one primary action, such as Sign up, pinned to th…
- Avoid when: Use liquid-tab-bar for an app-style switcher between a handful of peer sections.
- Related: `tabs`, `liquid-tab-bar`, `dropdown-menu`, `search-field`, `popover`

### `multi-region-failover` — Multi-region failover [Special]
Animated multi-region failover on a 2.5D stage: users stream requests through a global load balancer to two regions; the primary degrades, fails three health checks, traffic shifts smoothly to the healthy region, then it recovers, passes three checks and traffic ramps back to an even split.
- Spec (read fully before building): uiarc-pro-markdowns/components/multi-region-failover.md
- Main export in the spec's usage: MultiRegionFailover
- Use when: A reliability, infrastructure or pricing page that needs to show why running in two regions keeps a service up during an outage.; Docs for health checks, failover policies, traffic weights or slow start, where viewers should step through detection, failover,…
- Avoid when: Use database-replication to show a primary database failing over to a replica.
- Related: `dns-resolution`

### `now-playing` — Now playing [Special]
Grow a mini player into the full player in one continuous morph.
- Spec (read fully before building): uiarc-pro-markdowns/components/now-playing.md
- Main export in the spec's usage: NowPlaying, NowPlayingLevels
- Use when: Media that keeps playing while people browse, such as music, podcasts, or audio lessons.; A mini player bar that expands into a full player with artwork and a scrubber.
- Avoid when: Use bottom-sheet or dialog for a one-off overlay that is not a player.
- Related: `bottom-sheet`, `cover-flow`, `slider`, `voice-recorder`

### `orbit-logos` — Orbit logos [Special]
An integrations showcase with brand logos orbiting your product mark on tilted rings. Hover or focus one to rest the orbit, draw a connection, and see what it does.
- Spec (read fully before building): uiarc-pro-markdowns/components/orbit-logos.md
- Main export in the spec's usage: OrbitLogos
- Use when: An integrations or ecosystem hero on a marketing site.; An integrations settings screen where people browse, read about, and connect tools.; A launch page showing everything a product plugs into.
- Avoid when: Use a logo marquee for a long list of customer logos.
- Related: `logo-marquee`, `hover-card`, `orbit-menu`, `chip-group`

### `orbit-menu` — Orbit menu [Special]
Hold a button and its actions orbit out, ready to pick with a drag.
- Spec (read fully before building): uiarc-pro-markdowns/components/orbit-menu.md
- Main export in the spec's usage: OrbitMenu
- Use when: Three to six quick actions on one object, such as a note or photo.; Touch-first surfaces where press, drag, and release should fire an action in one gesture.
- Avoid when: Use dropdown-menu or context-menu for longer or text-heavy lists.
- Related: `dropdown-menu`, `context-menu`, `action-button`, `dock`

### `page-curl` — Page curl [Special]
A small magazine you read by dragging page corners, with a real fold, lit curl, and flick to turn.
- Spec (read fully before building): uiarc-pro-markdowns/components/page-curl.md
- Main export in the spec's usage: PageCurl
- Use when: Editorial and brand showcases where paper is part of the story.; Menus, catalogs, and yearbooks with a handful of spreads.
- Avoid when: Use carousel or a scrolling page for long content or content people search.
- Related: `cover-flow`, `carousel`, `lightbox-gallery`

### `payment-flow` — Payment flow [Special]
A card tap goes to a processor, then the network, then the bank and back with authorization, then settlement; each hop lights up with a status label and the amount travels as a chip.
- Spec (read fully before building): uiarc-pro-markdowns/components/payment-flow.md
- Main export in the spec's usage: PaymentFlow
- Use when: A payments or checkout landing section that explains authorization and settlement.; Docs pages introducing processors, card networks, issuers, fees, and payout timing.
- Avoid when: Use checkout-flow or checkout-live for a real checkout form.
- Related: `data-flow`

### `photo-grid` — Photo grid [Special]
Pinch through zoom levels and open any photo straight from its cell.
- Spec (read fully before building): uiarc-pro-markdowns/components/photo-grid.md
- Main export in the spec's usage: PhotoGrid
- Use when: A browsable photo library or album where people zoom between column counts.; Galleries that need favorites and a full-screen viewer with a filmstrip.; Touch and trackpad users who expect pinch to change density.
- Avoid when: Use lightbox-gallery for a masonry layout that keeps each photo's aspect ratio.
- Related: `carousel`, `image-compare`, `cover-flow`, `dialog`

### `pii-redaction` — PII redaction [Special]
A guardrail card where personal data is redacted before the prompt reaches the model. Scan marks each name, email, phone number and card with its type and swaps it for a placeholder like [EMAIL_1]. The safe prompt travels to Claude, and the reply comes back with the original values put back for the person.
- Spec (read fully before building): uiarc-pro-markdowns/components/pii-redaction.md
- Main export in the spec's usage: PiiRedaction, detectPii, redactPii, restorePii
- Use when: Explaining or proving a privacy guardrail in an AI product: support assistants, health or finance copilots, enterprise chat.; A settings or onboarding screen where admins see what the PII filter does before they turn it on.; A playground where people paste te…
- Avoid when: Use ai-chat or ai-composer for the conversation itself; redact behind the scenes and show this card only where the guardrail needs explaining.
- Related: `ai-chat`, `ai-composer`, `tool-call`, `agent-approvals`, `prompt-studio`, `text-shimmer`, `switch`

### `pixel-mascot` — Pixel mascot [Special]
A pixel-art robot that shows what an AI assistant is doing. It idles, thinks, types, celebrates and errors in frame-stepped sprite animations, and stays crisp at every integer size from 24px to 192px.
- Spec (read fully before building): uiarc-pro-markdowns/components/pixel-mascot.md
- Main export in the spec's usage: PixelMascot, usePixelMascotLoop
- Use when: A friendly generating indicator next to an assistant reply or in a chat composer.; An empty state or onboarding panel where a small character makes an AI feature feel approachable.; Image or canvas generation, where a mascot in the corner shows thinking, draw…
- Avoid when: Detailed agent progress with steps and timings; use agent-status or agent-timeline.
- Related: `ai-mascot`, `cube-mascot`, `ghost-mascot`, `agent-status`, `text-shimmer`, `reasoning-block`, `chat-thread`, `empty-state`

### `presence-stack` — Presence stack [Data]
Avatars of the people here now: joins pop in as the stack reflows, a counter rolls past the limit, dots show typing and idle, and hover fans it out with a gliding name label.
- Spec (read fully before building): uiarc-pro-markdowns/components/presence-stack.md
- Main export in the spec's usage: PresenceStack
- Use when: A document, board or design file header that shows who is here right now.; A call or meeting roster where people come and go and some are talking or idle.; Any realtime surface where joins, leaves and typing should be felt, not just counted.
- Avoid when: Use avatar-group for a static list of owners, assignees or members that does not change while you look at it.
- Related: `avatar-group`, `avatar`, `popover`

### `prize-wheel` — Prize wheel [Special]
A referral or promo prize wheel you flick to spin, with real angular momentum, a flexible pointer that ticks against each peg, weighted segments set by the host, a slow suspenseful settle, and the won segment lifting into a reward card with a copyable code.
- Spec (read fully before building): uiarc-pro-markdowns/components/prize-wheel.md
- Main export in the spec's usage: PrizeWheel
- Use when: A referral or launch page that rewards a signup with a discount code.; An in-product moment that grants one of several perks, such as a milestone reward.
- Avoid when: Use a plain coupon card or copy button when everyone gets the same reward.
- Related: `slot-text`, `wallet-stack`, `copy-button`

### `product-gallery` — Product gallery [Special]
A product gallery with a hover magnifier, gliding thumbnails, and color and size variants that crossfade photos.
- Spec (read fully before building): uiarc-pro-markdowns/components/product-gallery.md
- Main export in the spec's usage: ProductGallery, isSoldOut
- Use when: Product detail pages with several photos per color and a size picker.; Stores where shoppers need to zoom into fabric, texture, or small print.; Variants that sell out per color and should be struck through, not hidden.
- Avoid when: Use lightbox-gallery for a photo grid that opens into a viewer, with no variants.
- Related: `lightbox-gallery`, `carousel`, `photo-grid`, `segmented-control`, `radio-group`

### `prompt-cache` — Prompt cache [Special]
An animated explainer for prompt caching: the shared prefix of each request is cached once, later requests read it back, and the cost and time saved add up.
- Spec (read fully before building): uiarc-pro-markdowns/components/prompt-cache.md
- Main export in the spec's usage: PromptCache
- Use when: A docs page or blog post that explains why a stable prefix makes repeat requests cheaper and faster.; A pricing or usage page that shows how cache reads, writes and the time to live affect cost.; Developer onboarding for an AI product where prompt order and c…
- Avoid when: Use context-window to show how much of a model's window a conversation fills and when it compacts.
- Related: `context-window`, `model-picker`, `speculative-decoding`, `agent-loop`, `text-shimmer`

### `provider-keys` — Provider keys [Special]
A settings card for bring-your-own-key AI products. Each provider row shows its real mark, the masked key, a status and when the key was last used. You can reveal a key for five seconds, copy, rotate or remove it with undo. Adding or rotating a key opens an inline form that checks the format as you type, then tests the connection before saving.
- Spec (read fully before building): uiarc-pro-markdowns/components/provider-keys.md
- Main export in the spec's usage: ProviderKeys
- Use when: A settings page where users add their own Anthropic, OpenAI, Google AI, Mistral or xAI keys.; Showing which providers are connected, which keys were rejected, and when each key was last used.; Letting users rotate a leaked key or remove one with a short undo…
- Avoid when: Choosing a model for a request; use model-picker.
- Related: `usage-meter`, `copy-button`, `input`, `model-picker`

### `provider-status` — Provider status [Special]
A status card for the AI providers your product depends on. Each row shows the provider's real mark, its health as an icon and label, p50 latency and a 30-day uptime bar with a tooltip for each day. An incident row expands into its timeline of updates, and the card checks again on a visible countdown.
- Spec (read fully before building): uiarc-pro-markdowns/components/provider-status.md
- Main export in the spec's usage: ProviderStatus, sampleProviders, AnthropicMark, OpenaiMark, GeminiColorMark, MistralColorMark, XaiMark, AwsMark
- Use when: Showing the live health, latency and recent uptime of the model providers your product routes to.; Explaining degraded AI features to users or admins with the provider's incident updates in place.; A routing or fallback settings page where people need to see…
- Avoid when: A full public status page with components, subscriptions and history: build a page, not a card.
- Related: `agent-status`, `tool-call`, `tooltip`, `text-shimmer`, `button`

### `race-bar-chart` — Race bar chart [Data]
A ranking over time: bars overtake each other on springs, values count up, and a timeline you can play or scrub.
- Spec (read fully before building): uiarc-pro-markdowns/components/race-bar-chart.md
- Main export in the spec's usage: RaceBarChart
- Use when: Showing how the leaders of a ranking change across many periods.; A launch or recap moment where the motion itself is the point.; Letting people scrub to any period and read exact values.
- Avoid when: Use line-chart when exact trends over time matter more than rank.
- Related: `bar-chart`, `line-chart`, `streamgraph`, `slope-chart`

### `radar-chart` — Radar chart [Data]
Two or three profiles on one web: shapes morph when you swap a profile, and a sweep across the axes compares values in place.
- Spec (read fully before building): uiarc-pro-markdowns/components/radar-chart.md
- Main export in the spec's usage: RadarChart
- Use when: Comparing the profile of a few options across shared measures.; Showing strengths and gaps at a glance, such as scores or ratings.
- Avoid when: Use bar-chart when the precise difference on one measure matters.
- Related: `bar-chart`, `slope-chart`, `donut-chart`

### `realtime-stream` — Realtime stream [Data]
A live line that scrolls at 60fps as readings arrive, holds still on hover to read, and pops a marker on every anomaly.
- Spec (read fully before building): uiarc-pro-markdowns/components/realtime-stream.md
- Main export in the spec's usage: RealtimeStream
- Use when: Live monitoring panels and status pages.; A hero on an infrastructure or observability page where motion shows the system is alive.
- Avoid when: Use line-chart for static time series.
- Related: `line-chart`, `brush-chart`, `sparkline`, `animated-counter`

### `reasoning-block` — Reasoning block [Special]
The collapsible thinking block of an AI reply. While the model thinks, a shimmering label counts the seconds and the latest reasoning streams underneath. When it finishes, it folds to "Thought for 7s" and opens to show the full reasoning as calm steps with headings.
- Spec (read fully before building): uiarc-pro-markdowns/components/reasoning-block.md
- Main export in the spec's usage: ReasoningBlock, parseReasoning, ClaudeMark
- Use when: Showing a reasoning model's thinking above its answer in a chat or agent transcript.; Letting people audit why an assistant reached a recommendation without crowding the reply.; Restoring past messages where the reasoning should stay folded with its original…
- Avoid when: Tool or function calls with inputs and outputs: use ToolCall.
- Related: `tool-call`, `agent-status`, `text-shimmer`, `agent-plan`

### `reasoning-tree` — Reasoning tree [Special]
An illustration of tree search over thoughts: candidates are scored, weak branches fade, the best expand, and the winning path from question to answer draws in.
- Spec (read fully before building): uiarc-pro-markdowns/components/reasoning-tree.md
- Main export in the spec's usage: ReasoningTree
- Use when: Explainers, docs and landing pages that teach tree of thoughts, beam search or test time search over reasoning steps.; Showing why a wider search can beat a greedy one, with a control the reader can change and replay.; A visual summary of how an agent weighed…
- Avoid when: Use agent-run or research-run to show a real agent's steps and output as they stream.
- Related: `agent-loop`, `mixture-of-experts`, `speculative-decoding`, `vector-search`, `research-run`

### `referral-card` — Referral card [Special]
A give-and-get referral card where people copy or share their invite link, invite friends by email as chips, and watch invites move from invited to signed up to earned, with the credit total counting up and a milestone reward unlocking.
- Spec (read fully before building): uiarc-pro-markdowns/components/referral-card.md
- Main export in the spec's usage: ReferralCard, referralShareUrl
- Use when: A referral or invite program in account settings, billing or an onboarding checklist.; Showing a person what their invites have earned and how close they are to a bonus reward.
- Avoid when: Team member invites with roles and permissions; use a members table.
- Related: `copy-button`, `avatar`, `button`, `tooltip`, `agent-status`

### `reply-draft` — Reply draft [Special]
An AI email reply drafter where Claude streams a reply under a received Gmail message. Quick replies steer a fresh draft, tone and length rewrite it with a single crossfade, and you can edit the finished draft before you insert it.
- Spec (read fully before building): uiarc-pro-markdowns/components/reply-draft.md
- Main export in the spec's usage: ReplyDraft
- Use when: Drafting a reply to an email, ticket or message with an AI model, where the reader reviews and edits before sending.; Offering quick reply intents plus tone and length controls for generated text.; Showing an AI writing feature on a landing page with a realis…
- Avoid when: Free-form chat with a model: use a chat or composer component instead.
- Related: `ai-composer`, `ghost-text`, `tool-call`, `agent-status`, `text-shimmer`, `segmented-control`

### `response-feedback` — Response feedback [Special]
A feedback control for AI replies where thumbs down opens an inline panel with reason chips and an optional note, thumbs up fills and asks what was good, and a submit shows a short thank-you before folding back into the row.
- Spec (read fully before building): uiarc-pro-markdowns/components/response-feedback.md
- Main export in the spec's usage: ResponseFeedback, FeedbackActions
- Use when: Collecting thumbs up and down on AI replies in a chat, copilot or search answer.; Gathering structured reasons (inaccurate, unsafe) for model evaluation or support triage.; Adding a message action row with copy and regenerate next to feedback.
- Avoid when: Star or numeric ratings of a product or session: use rating.
- Related: `chat-thread`, `copy-button`, `tool-call`, `agent-status`, `rating`

### `sand-text` — Sand text [Special]
A headline made of sand that pours into the letters, crumbles where the cursor digs, and heals itself.
- Spec (read fully before building): uiarc-pro-markdowns/components/sand-text.md
- Main export in the spec's usage: SandText
- Use when: A hero headline or section title that should be fun to touch.; Short words that change on a selection, like a product name or theme.
- Avoid when: Body copy or long headings; use in-view-title or text-reveal.

### `sankey-flow` — Sankey flow [Data]
Flows between stages as ribbons with drifting particles; hover any node or ribbon to pour its share through the whole journey.
- Spec (read fully before building): uiarc-pro-markdowns/components/sankey-flow.md
- Main export in the spec's usage: SankeyFlow
- Use when: Showing how a total splits and recombines across three to five stages.; Explaining where a funnel leaks, with the share at each step one hover away.; Comparing two periods of the same flow by switching data.
- Avoid when: Use bar-chart for a simple linear funnel with no branches.
- Related: `sunburst`, `streamgraph`, `bar-chart`, `donut-chart`

### `share-access` — Share access [Disclosure]
A share panel: invite people as validated email chips with suggestions, change roles from a compact menu, remove with undo, switch link access and copy the link, with every change landing in place.
- Spec (read fully before building): uiarc-pro-markdowns/components/share-access.md
- Main export in the spec's usage: ShareAccess
- Use when: A Share button on a document, board or project that controls who can open it and what they can do.; Inviting teammates by email with suggestions from a workspace directory.; Managing link sharing next to per person access in one place.
- Avoid when: Use the invite-people block for inviting people to a whole workspace with seats and plans.
- Related: `popover`, `tag-input`, `dropdown-menu`, `copy-button`, `presence-stack`, `combobox`

### `share-sheet` — Share sheet [Special]
A Share button that opens into a panel with copy link, access level, channels, and people to send to.
- Spec (read fully before building): uiarc-pro-markdowns/components/share-sheet.md
- Main export in the spec's usage: ShareSheet
- Use when: A Share button on a document, design, or board header where people share often.; Sharing flows that combine copy link, access level, and sending to a few recent people.; Posting to a small set of channels, such as Slack or email, with in-place pending and don…
- Avoid when: Use copy-button when all you need is to copy a URL.
- Related: `popover`, `copy-button`, `avatar-group`, `dialog`, `toast`

### `sheet-stack` — Sheet stack [Special]
Nested sheets that stack with depth, drag to dismiss, and become stacked dialogs on wide screens.
- Spec (read fully before building): uiarc-pro-markdowns/components/sheet-stack.md
- Main export in the spec's usage: SheetStack, Sheet, SheetTrigger, useSheetStack
- Use when: Mobile settings where each row opens a deeper page and back should feel spatial.; Nested pickers, such as choosing a workspace and then a project inside it.; Flows that should be a bottom sheet on phones and a centered dialog on desktop from one declaration.
- Avoid when: Use dialog for a single confirmation or form with no nested steps.
- Related: `bottom-sheet`, `drawer`, `dialog`, `settings-page`, `multi-step-form`

### `skeleton-morph` — Skeleton morph [Special]
Loading skeletons that grow into the real content, block by block, instead of swapping.
- Spec (read fully before building): uiarc-pro-markdowns/components/skeleton-morph.md
- Main export in the spec's usage: SkeletonMorph, MorphBlock
- Use when: Profile cards, feeds, and lists that load in under a few seconds.; Dashboards where the layout is known before the data arrives.; Places where a hard swap from gray boxes to content would feel jarring.
- Avoid when: Use skeleton for long lists of hundreds of rows; layout animation there is costly.
- Related: `skeleton`, `morph-loader`, `empty-state`

### `smart-form-fill` — Smart form fill [Special]
A paste-to-fill form card where AI reads an email signature or messy notes and fills a contact field by field. Each value flashes in with a confidence dot, its source lights up in the pasted text, low-confidence guesses ask for review, and Undo puts the old values back.
- Spec (read fully before building): uiarc-pro-markdowns/components/smart-form-fill.md
- Main export in the spec's usage: SmartFormFill
- Use when: People paste an email signature, a forwarded message or notes and expect the record to fill itself.; You need visible confidence and an easy review path before AI-filled data is saved.; Onboarding or CRM flows where typing six fields by hand is the main frict…
- Avoid when: Plain data entry with no unstructured source; use form-field and input.
- Related: `input`, `textarea`, `multi-step-form`, `ai-command`

### `social-proof-toast` — Social proof toast [Special]
A stack of social proof notifications for landing and pricing pages, where recent trials, upgrades and verified purchases from people and companies arrive every few seconds. The stack pauses and fans out on hover, and visitors can dismiss any toast.
- Spec (read fully before building): uiarc-pro-markdowns/components/social-proof-toast.md
- Main export in the spec's usage: SocialProofToast, SocialProofEvent
- Use when: Showing recent trials, purchases or upgrades on a landing or pricing page.; A live activity feed for a launch or waitlist page (people joining, teams upgrading).; Highlighting verified purchases from known companies near a checkout CTA.
- Avoid when: System feedback after a user action (saved, copied, failed): use toast or undo-toast.
- Related: `toast`, `toast-stack`, `undo-toast`, `avatar`, `avatar-group`

### `source-cards` — Source cards [Special]
A row of cited sources under an AI answer where cards stream in with real site marks while the model searches, the overflow collapses into a stack of favicons, hovering lifts a preview with the passage, and an inline [n] citation highlights its card.
- Spec (read fully before building): uiarc-pro-markdowns/components/source-cards.md
- Main export in the spec's usage: SourceCards, SourceCitation, SourceCardsSource, SourceCardsSimulation
- Use when: Citations under an AI search or docs assistant answer.; Showing live search progress ("Searching 3 of 8") while an agent browses.; Linking inline [n] references in generated text to the pages they came from.
- Avoid when: A full search results page with many results and filters; use a list layout instead.
- Related: `tool-call`, `agent-status`, `text-shimmer`, `tooltip`, `copy-button`

### `speculative-decoding` — Speculative decoding [Special]
An illustration of speculative decoding: a fast draft model guesses a few tokens, the target model checks them in one pass, and accepted guesses join the answer.
- Spec (read fully before building): uiarc-pro-markdowns/components/speculative-decoding.md
- Main export in the spec's usage: SpeculativeDecoding
- Use when: Explaining why a product answers faster: docs, model pages, inference dashboards and blog posts about latency.; Showing a recorded speculative run from your own server, with acceptance and tokens per pass for a chosen draft length.; Teaching the trade off bet…
- Avoid when: Use text-stream to show an answer streaming to a user; this card explains the mechanism behind the speed.
- Related: `mixture-of-experts`, `context-window`

### `speech-player` — Speech player [Special]
A read-aloud player for AI replies. The Read aloud button in the message's action row turns into a compact player with play, a scrubbable progress bar, speed and a voice picker, and a highlight follows the spoken word through the reply, karaoke style.
- Spec (read fully before building): uiarc-pro-markdowns/components/speech-player.md
- Main export in the spec's usage: SpeechPlayer, simulateSpeech
- Use when: A chat or answer surface where people want a reply read out, with the spoken word followed in the text.; Accessibility and hands free reading for long AI answers, summaries or briefings.; Previewing TTS voices and speeds against real product copy.
- Avoid when: Use dictation-button to turn speech into text in a composer.
- Related: `ai-chat`, `ai-answer`, `dictation-button`, `copy-button`, `text-shimmer`, `meeting-summary`

### `split-bar` — Split bar [Data]
A single 100% bar split into shares: rest on a segment to widen it and read its exact figures, toggle segments from the legend and the rest reflow, with labels inside when they fit and on leader lines when they don't.
- Spec (read fully before building): uiarc-pro-markdowns/components/split-bar.md
- Main export in the spec's usage: SplitBar
- Use when: A compact part to whole view that fits in a card row or a dashboard header.; Comparing shares where people also want exact figures on demand and the option to leave a category out.; Showing how a mix changes between periods or filters with one continuous refl…
- Avoid when: Use bar-chart to compare absolute values across many categories.
- Related: `donut-chart`, `waffle-chart`, `treemap`, `bar-chart`, `usage-meter`

### `starter-prompts` — Starter prompts [Special]
A greeting and a grid of starter cards for the empty state of an AI app. The cards are grouped into Write, Code, Analyze and Plan tabs, and a shuffle swaps them with a short staggered crossfade. Picking a card fills the composer, and cards that use a connected app show its mark (Gmail, GitHub, Notion, Linear, Google Calendar).
- Spec (read fully before building): uiarc-pro-markdowns/components/starter-prompts.md
- Main export in the spec's usage: StarterPrompts
- Use when: The empty state of a chat, copilot or agent, before the first message.; Teaching what an assistant can do with connected tools, such as Gmail, GitHub or Notion.; Onboarding a new workspace with a few tailored, ready to send prompts.
- Avoid when: Inside a running conversation; use follow-up suggestion chips in the chat thread instead.
- Related: `chat-thread`, `tool-call`, `ghost-text`, `empty-state`, `ai-command`, `segmented-control`

### `sticker-peel` — Sticker peel [Special]
Peel stickers off a surface with a real curl, move them around, and stick them back down.
- Spec (read fully before building): uiarc-pro-markdowns/components/sticker-peel.md
- Main export in the spec's usage: StickerPeel, StickerPeelItem
- Use when: A personal or team page where people arrange badges, achievements, or brand stickers.; A launch or marketing moment that invites people to play with the product's marks.; A reward screen where earned stickers are placed on a surface.
- Avoid when: Use reorderable-list or a sortable grid when the order of items carries meaning.
- Related: `holo-card`

### `stretch-refresh` — Stretch refresh [Special]
Pull a feed down and a line stretches to tell you when to let go.
- Spec (read fully before building): uiarc-pro-markdowns/components/stretch-refresh.md
- Main export in the spec's usage: StretchRefresh
- Use when: Timelines, inboxes, and activity feeds where new entries arrive at the top.; Panels that should support pull to refresh by touch, mouse drag, and trackpad scroll.
- Avoid when: Use a plain list for static content that never refreshes.
- Related: `timeline`, `skeleton`, `toast`, `reorderable-list`

### `sunburst` — Sunburst [Data]
A hierarchy in rings: click a segment and every arc swings around it as the new centre, with a breadcrumb back and a rolling total.
- Spec (read fully before building): uiarc-pro-markdowns/components/sunburst.md
- Main export in the spec's usage: Sunburst
- Use when: Drilling into where a total comes from, one level at a time.; Showing the share of each part within its parent and within the whole.; Dashboards where a compact, explorable overview beats a long table.
- Avoid when: Use donut-chart for a single level of parts.
- Related: `donut-chart`, `sankey-flow`, `tree-table`, `tree-view`

### `team-switcher` — Team switcher [Special]
A workspace switcher like Linear, Vercel or Slack. The trigger shows the current workspace's logo and plan. The menu has search, your role in each workspace and a Cmd+1 to 9 shortcut for each, and lets you create or join a workspace inline. A highlight glides between rows, and switching crossfades the trigger through a short loading state.
- Spec (read fully before building): uiarc-pro-markdowns/components/team-switcher.md
- Main export in the spec's usage: TeamSwitcher, WorkspaceTile
- Use when: Switching between organizations, teams or workspaces in a multi-tenant SaaS app.; An account or project picker that needs search, roles and keyboard shortcuts.; Letting people create a new workspace or accept an invite without leaving the current page.
- Avoid when: Picking from a short static list of options in a form: use a select or segmented control.
- Related: `dropdown-menu`, `popover`, `combobox`, `avatar`

### `ticket-router` — Ticket router [Special]
A support ticket router where messages from Gmail, Intercom, Slack and Zendesk come in one at a time. An AI classifier labels each one with intent, sentiment and confidence, and the ticket moves into a team lane with an assignee. Low confidence tickets wait in a review lane, and one click there routes them to the suggested team.
- Spec (read fully before building): uiarc-pro-markdowns/components/ticket-router.md
- Main export in the spec's usage: TicketRouter
- Use when: Showing how an AI classifier triages inbound support messages into team queues.; A live triage widget in a helpdesk or ops dashboard, with a human review lane for low confidence.; Landing page or onboarding demos of AI routing for support products.
- Avoid when: A full ticket inbox with search and bulk actions; use a table or list layout.
- Related: `agent-status`, `tool-call`, `agent-approvals`, `agent-handoff`, `ai-workflow`

### `time-dial` — Time dial [Special]
Spin a dial to pick an hour and see which team cities are at work.
- Spec (read fully before building): uiarc-pro-markdowns/components/time-dial.md
- Main export in the spec's usage: TimeDial
- Use when: Planning a moment across two to five cities, such as calls, releases, or handovers.; Distributed teams that need to see at a glance who is inside working hours.
- Avoid when: Use time-picker for a single local time.
- Related: `time-picker`, `date-picker`, `calendar`, `slider`

### `tldr-toggle` — TL;DR toggle [Special]
An article card with a Full, Summary and Key points switch and a length slider. Switching streams an AI summary in place of the article as the card's height springs to fit, and each key point links back to the paragraph it came from, which gets scrolled to and highlighted.
- Spec (read fully before building): uiarc-pro-markdowns/components/tldr-toggle.md
- Main export in the spec's usage: TldrToggle, simulateTldr, streamResult
- Use when: Offering a quick summary or key points above or in place of a long article, doc or report.; Letting readers verify AI claims against the source, through key points that link back to paragraphs.; Reading surfaces where people choose how much detail they want w…
- Avoid when: Open-ended questions about content: use an answer or chat component such as ai-answer.
- Related: `ai-answer`, `text-shimmer`, `segmented-control`, `slider`, `copy-button`, `tool-call`

### `toc-progress` — Table of contents progress [Disclosure]
A table of contents that reads along with you: a line bends through the nested headings, fills as you scroll, and carries a marker to the current section, with smooth jumps and a time-left countdown.
- Spec (read fully before building): uiarc-pro-markdowns/components/toc-progress.md
- Main export in the spec's usage: TocProgress
- Use when: A documentation page, guide or blog post long enough that readers jump between sections.; An engineering write up or policy where knowing how much is left helps readers commit to it.; Any long article in its own scroll container, such as a help panel or a rea…
- Avoid when: Use tabs when sections are alternatives rather than parts of one document.
- Related: `docs-sidebar`, `tabs`

### `tone-tuner` — Tone tuner [Special]
A brand voice card where two sliders (formality and detail) and Friendly, Confident and Empathetic chips rewrite a customer reply. Each changed sentence crossfades in place, new words can be highlighted against the original, and Copy takes the current version.
- Spec (read fully before building): uiarc-pro-markdowns/components/tone-tuner.md
- Main export in the spec's usage: ToneTuner
- Use when: A composer or help desk reply that offers AI tone controls before sending.; Brand voice tooling where marketers compare versions of the same copy.; Any rewrite where people want to steer with a few dials rather than write a prompt.
- Avoid when: Free form AI editing with a prompt box: use a chat or composer instead.
- Related: `slider`, `switch`, `copy-button`, `text-shimmer`, `segmented-control`, `agent-status`

### `tool-call` — Tool call [Special]
A tool call row for agent transcripts: the tool's mark and the call in plain words, a live state while it runs, and the input and output a click away, with approval and retry when needed.
- Spec (read fully before building): uiarc-pro-markdowns/components/tool-call.md
- Main export in the spec's usage: ToolCall, ToolCallGroup, ToolCallData
- Use when: Showing what tools an AI agent used inside a chat or agent transcript, with the arguments and results one click away.; Human in the loop actions where a call must be allowed or denied inline before it runs, such as posting a message or writing to a database.;…
- Avoid when: Use agent-run for a full multi step run with a plan, a timeline and live logs rather than inline rows in a message.
- Related: `ai-chat`, `agent-run`, `agent-approvals`, `agent-loop`, `research-run`, `mcp-servers`, `text-shimmer`

### `training-run` — Training run [Special]
A fine-tuning job card where a live train and validation loss curve draws across a fixed step axis that doubles as the epoch progress bar. It shows the learning rate, elapsed time, ETA and the latest evals and checkpoints, has Pause and Cancel while it runs, and ends in results with a Deploy button.
- Spec (read fully before building): uiarc-pro-markdowns/components/training-run.md
- Main export in the spec's usage: TrainingRun, useTrainingRunSimulation
- Use when: A fine-tuning or training job page in an AI platform, where people watch loss, pause, cancel and deploy.; An eval or distillation run that reports a loss curve, checkpoints and a final score.; A product onboarding step that trains a custom model on the custom…
- Avoid when: A generic multi-series chart with no job lifecycle: use line-chart.
- Related: `agent-status`, `tool-call`, `model-training`, `line-chart`, `progress`, `copy-button`

### `trial-banner` — Trial banner [Special]
A trial status banner where a ring counts down the days left, the copy names what the workspace loses, and the upgrade path is one click away. It comes as a slim banner, a sidebar card or a header pill. It shifts to a warning tone in the last days, has expired and upgraded states, and folds into the pill when dismissed or snoozed.
- Spec (read fully before building): uiarc-pro-markdowns/components/trial-banner.md
- Main export in the spec's usage: TrialBanner
- Use when: A SaaS app with a free trial that needs a quiet, always visible upgrade path.; Telling a workspace what it loses when the trial ends and nudging harder in the last days.; Showing an expired trial without blocking the app.
- Avoid when: A hard paywall that blocks a feature; use a modal or an upgrade screen instead.
- Related: `agent-status`, `button`, `dropdown-menu`, `popover`, `segmented-control`

### `typewriter-terminal` — Typewriter terminal [Special]
A terminal that types a scripted CLI session with a seeded human cadence, colors the shell syntax, and streams output lines, progress bars and spinners, with a scrubber, play/pause and replay controls.
- Spec (read fully before building): uiarc-pro-markdowns/components/typewriter-terminal.md
- Main export in the spec's usage: TypewriterTerminal
- Use when: A landing page hero or install section for a developer tool, SDK, or CLI.; Docs quick starts that show what each command prints before people run it.; Changelog or launch posts that show a new command in action.
- Avoid when: Use code-block for commands and source that people need to read and copy without waiting.
- Related: `code-block`, `hero-section`

### `undo-toast` — Undo toast [Feedback]
Archive or delete rows with a second chance: the gap closes, a countdown toast merges repeat actions, and Undo or \u2318Z puts every row back exactly where it was.
- Spec (read fully before building): uiarc-pro-markdowns/components/undo-toast.md
- Main export in the spec's usage: UndoToast, UndoToastRow, UndoToastRowAction
- Use when: An inbox, notification list, task list or file list where archiving or deleting should be one click with a way back.; Bulk triage, where people remove several items quickly and one toast should summarise them all.; Anywhere a confirmation dialog would slow do…
- Avoid when: Irreversible destruction such as deleting a project or revoking keys; use confirm-popover so the consequence is stated first.
- Related: `toast-stack`, `toast`, `swipe-actions`, `confirm-morph`, `hold-to-confirm`

### `upgrade-prompt` — Upgrade prompt [Special]
An upgrade nudge for the moment someone hits a limit. It shows a usage meter at 50 of 50 AI credits, a rolling price with a monthly and yearly toggle, three concrete unlocks with real model marks, and Upgrade or Maybe later. Upgrading leads into a success state with the new limits, and the card never changes size between states.
- Spec (read fully before building): uiarc-pro-markdowns/components/upgrade-prompt.md
- Main export in the spec's usage: UpgradePrompt
- Use when: An AI product that hits a usage limit (credits, generations, seats) and needs a tasteful, conversion focused nudge.; A paywall moment inside an app, in a dialog, popover or inline in place of the blocked result.; Offering one next plan with a monthly and year…
- Avoid when: Comparing several plans side by side: use a pricing table or plan picker.
- Related: `credit-topup`, `plan-picker`, `usage-meter`, `checkout-live`, `segmented-control`, `button`

### `vector-search` — Vector search [Special]
Documents drop onto a tilted embedding plane and fold into points that cluster by topic; the index links neighbours, a query is typed, embedded and lowered onto the plane, a signal hops along the graph toward it, and a widening ring lights the nearest documents with connecting lines, similarity scores and a ranked list.
- Spec (read fully before building): uiarc-pro-markdowns/components/vector-search.md
- Main export in the spec's usage: VectorSearch
- Use when: A feature section on semantic search, AI answers, or retrieval over a team's docs.; Docs pages introducing embeddings, nearest neighbour search, or approximate indexes.
- Avoid when: Use search-index to explain keyword search with an inverted index.
- Related: `model-training`, `data-flow`

### `voice-orb` — Voice orb [Special]
A voice mode orb that listens, thinks, and speaks, with a live transcript and call controls.
- Spec (read fully before building): uiarc-pro-markdowns/components/voice-orb.md
- Main export in the spec's usage: VoiceOrb, useMicLevel, VoiceTranscript, VoiceControls
- Use when: A voice mode for an assistant where the user needs to see whether it is listening, thinking, or speaking.; Hands-free or call-like flows that need start, mute, a running clock, and end in one compact control.; Live captions under a speaking agent, via VoiceTr…
- Avoid when: Use voice-recorder when the user records a clip to send or save.
- Related: `voice-recorder`, `chat-thread`

### `voice-recorder` — Voice recorder [Special]
Record with a live waveform, review and scrub, then send the take into the thread.
- Spec (read fully before building): uiarc-pro-markdowns/components/voice-recorder.md
- Main export in the spec's usage: VoiceRecorder
- Use when: Voice notes in chats, comments, or field notes where speaking beats typing.; A thread of voice bubbles with playback and scrubbing.
- Avoid when: Use now-playing for music or long-form audio.
- Related: `now-playing`, `slider`, `hold-to-confirm`

### `wallet-stack` — Wallet stack [Special]
Fan a stack of cards and lift one out to see its activity.
- Spec (read fully before building): uiarc-pro-markdowns/components/wallet-stack.md
- Main export in the spec's usage: WalletStack
- Use when: A few payment cards, passes, or memberships where people open one to see its balance and activity.; Fintech or wallet screens that want a physical card metaphor with realistic materials.
- Avoid when: Use card-stack for generic swipeable content that is not a card wallet.
- Related: `card-stack`, `expandable-card`


---

<!-- references/pro-blocks.md -->

# Pro blocks — markdown specs (114 pages)

## Contents

- `account-health` — Account health
- `activity-feed` — Activity feed
- `activity-terrain` — Activity terrain
- `agent-approvals` — Agent approvals
- `agent-builder` — Agent builder
- `agent-gallery` — Agent gallery
- `agent-memory` — Agent memory
- `agent-orchestrator` — Agent orchestrator
- `agent-routines` — Agent routines
- `agent-run` — Agent run
- `agent-tasks` — Agent tasks
- `ai-answer` — AI answer
- `ai-chat` — AI chat
- `ai-composer` — AI composer
- `ai-feature-launch` — AI feature launch
- `ai-inline-edit` — AI inline edit
- `ai-insight-card` — AI insight card
- `ai-search-bar` — AI search bar
- `ai-setup-wizard` — AI setup wizard
- `ai-side-panel` — AI side panel
- `api-keys` — API keys
- `availability-picker` — Availability picker
- `billing-overview` — Billing overview
- `budget-variance` — Budget variance
- `call-insights` — Call insights
- `cancel-flow` — Cancel flow
- `cart-drawer` — Cart drawer
- `catch-up` — Catch up
- `checkout-live` — Live checkout
- `checkout-summary` — Checkout summary
- `choropleth-explorer` — Choropleth explorer
- `cohort-retention` — Cohort retention
- `connected-scatter` — Connected scatter
- `credit-topup` — Credit top-up
- `customer-galaxy` — Customer galaxy
- `delivery-tracker` — Delivery tracker
- `document-extract` — Document extraction
- `domain-verify` — Domain verify
- `env-variables` — Environment variables
- `eval-suite` — Eval suite
- `exploded-view` — Exploded view
- `feature-bento` — Feature bento
- `feature-voting` — Feature voting
- `feedback-board` — Feedback board
- `gantt-timeline` — Gantt timeline
- `goal-tracker` — Goal tracker
- `help-center` — Help center
- `hero-signup` — Hero signup
- `horizon-chart` — Horizon chart
- `inbox-triage` — Inbox triage
- `integrations` — Integrations
- `invite-people` — Invite people
- `invoice-studio` — Invoice studio
- `journey-flow` — Journey flow
- `kanban-board` — Kanban board
- `knowledge-base` — Knowledge base
- `kpi-drilldown` — KPI drilldown
- `layout-morph` — Layout morph
- `lead-scoring` — Lead scoring
- `line-replay` — Line replay
- `login` — Login and sign up
- `magic-link` — Magic link
- `market-terminal` — Market terminal
- `mcp-servers` — MCP servers
- `media-player` — Media player
- `metric-explorer` — Metric explorer
- `metrics-dashboard` — Metrics dashboard
- `model-arena` — Model arena
- `model-picker` — Model picker
- `mrr-waterfall` — MRR waterfall
- `multi-step-form` — Multi-step form
- `onboarding-illustration` — Onboarding illustration
- `onboarding-survey` — Onboarding survey
- `pricing-calculator` — Pricing calculator
- `product-detail` — Product detail
- `product-listing` — Product listing
- `profile-page` — Profile page
- `project-board` — Project board
- `prompt-studio` — Prompt studio
- `release-readiness` — Release readiness
- `research-run` — Research run
- `revenue-explorer` — Revenue explorer
- `revenue-globe` — Revenue globe
- `roles-permissions` — Roles and permissions
- `scroll-story` — Scroll story
- `search-results` — Search results
- `seat-manager` — Seat manager
- `seat-map` — Seat map
- `security-settings` — Security settings
- `selection-toolbar` — Selection toolbar
- `semantic-zoom` — Semantic zoom
- `settings-command` — Settings command
- `settings-page` — Settings page
- `sidebar` — Sidebar
- `small-multiples` — Small multiples
- `smart-scheduler` — Smart scheduler
- `spend-alert` — Spend alert
- `spotlight-grid` — Spotlight grid
- `support-conversation` — Support conversation
- `support-widget` — Support widget
- `task-breakdown` — Task breakdown
- `team-directory` — Team directory
- `team-members` — Team members
- `team-showcase` — Team showcase
- `testimonial-stage` — Studio perspectives
- `two-factor-setup` — Two-factor setup
- `uptime-status` — Uptime status
- `usage-billing` — Usage billing
- `usage-forecast` — Usage forecast
- `usage-pricing` — Usage pricing
- `wallet-card` — Wallet card
- `webhook-tester` — Webhook tester
- `webhooks` — Webhooks
- `week-calendar` — Week calendar
Pro blocks are complete product screens/sections specified as markdown (see the
note in pro-components.md: spec-driven rebuild, not original source). Two pages
are grouped: `sidebar` covers 4 Pro variants and `login` covers 5 variants of
which 2 are Pro (login-split, login-immersive) and 3 are free with real source
in the free bundle (sign-in, login-centered, signup-form).

### `account-health` — Account health
A customer success card where a health score gauge, a renewal countdown and five sourced signals with sparklines lead into an AI risk summary and one recommended next step, like scheduling a QBR before usage slips further.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/account-health.md
- Main export in the spec's usage: AccountHealth, AccountHealthSignal, AccountHealthAction
- Use when: A customer success or account page that needs a score, the signals behind it and a next step.; Renewal prep views where the countdown and risk drivers matter more than raw metrics.; Showing an AI written risk summary next to the evidence it was written from.
- Avoid when: Portfolio views across many accounts; use a table with a score column instead.
- Related: `agent-status`, `ai-insight-card`, `call-insights`, `goal-tracker`, `generation-stats`

### `activity-feed` — Activity feed
A team activity feed grouped by day on a quiet avatar timeline, with a type filter, a live new updates button, expandable details, and a mark all read sweep.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/activity-feed.md
- Main export in the spec's usage: ActivityFeed
- Use when: A workspace or project activity page for a team product.; A dashboard panel that shows what changed since someone last looked.
- Avoid when: Use audit-log for compliance history that needs search, export, and exact timestamps.
- Related: `notification-center`, `changelog-feed`, `timeline`, `inbox-triage`

### `activity-terrain` — Activity terrain
A 3D terrain of hourly activity you can orbit, zoom, fly into and flatten into a heatmap.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/activity-terrain.md
- Main export in the spec's usage: ActivityTerrain
- Use when: Analytics or operations pages showing when a product is busiest across a week.; Showcase dashboards where a 3D view of a 7 by 24 grid adds impact, with a flat heatmap fallback.
- Avoid when: Use activity-heatmap for a plain 2D grid that is easier to read.
- Related: `activity-heatmap`, `revenue-globe`, `customer-galaxy`, `segmented-control`

### `agent-approvals` — Agent approvals
One approval card for agents: the waiting tool call reads like a permission prompt with the tool's mark, the agent's reason and its arguments, and you approve, deny or allow it from now on.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/agent-approvals.md
- Main export in the spec's usage: AgentApprovals, ApprovalRequest
- Use when: Human in the loop control for agents that call tools with side effects: deploys, emails, database writes, payments and ticket changes.; An approvals card in an agent console or side panel where one person reviews, edits and decides tool calls quickly, from th…
- Avoid when: Use agent-run to follow one agent's steps and tool calls live, with an inline confirm inside the run.
- Related: `agent-run`, `agent-tasks`, `agent-orchestrator`, `agent-routines`, `mcp-servers`

### `agent-builder` — Agent builder
A card for setting up an AI agent: an inline editable name, a model picker, instructions, tool toggles with real app marks, and knowledge files with upload progress. A Configure / Test switch opens a compact chat that answers with the tools you turned on, and Publish ships the setup with a saved or unsaved state.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/agent-builder.md
- Main export in the spec's usage: AgentBuilder, simulateReply
- Use when: Letting customers configure their own AI agent inside your product, like Intercom Fin, Zapier agents or an OpenAI GPT builder.; Internal admin screens where ops teams tune instructions, tools and knowledge for a support or billing agent.; A product tour or la…
- Avoid when: Running or monitoring an agent in production: use agent-status or agent-routines.
- Related: `model-picker`, `agent-routines`, `agent-approvals`, `ai-chat`, `tool-call`, `agent-status`

### `agent-gallery` — Agent gallery
A marketplace card of AI agent templates where you filter by team, search by agent or app, preview a sample run and install an agent inline: choose a workspace, grant access app by app, and the card confirms with a check.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/agent-gallery.md
- Main export in the spec's usage: AgentGallery
- Use when: An agents or integrations page where people browse and install ready made AI agents.; Onboarding that suggests agent templates by team and installs one without leaving the page.; A marketplace teaser on a dashboard or settings page.
- Avoid when: Configuring a single agent's prompt, tools or schedule: use a settings form or agent routines.
- Related: `agent-status`, `tool-call`, `model-picker`, `agent-routines`, `agent-approvals`

### `agent-memory` — Agent memory
One card for what an assistant remembers about you: filter and search memories, edit or forget one in place, and turn saved memories and chat history on or off.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/agent-memory.md
- Main export in the spec's usage: AgentMemory
- Use when: Settings for an assistant that remembers people across chats, where people need to see, filter, search, correct and delete what it knows.; Showing the moment an assistant saves something from a chat, with a way to see where it was filed.; Any small personal k…
- Avoid when: Use knowledge-base for documents and files an agent retrieves from, rather than short facts about the user.
- Related: `ai-chat`, `ai-side-panel`, `knowledge-base`, `context-window`, `agent-tasks`, `agent-routines`, `mcp-servers`

### `agent-orchestrator` — Agent orchestrator
A lead agent splits a goal into a plan, fans the subtasks out to parallel worker lanes and merges what comes back, with each lane's model, progress and result in view.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/agent-orchestrator.md
- Main export in the spec's usage: AgentOrchestrator, simulateOrchestration
- Use when: Showing a multi agent run where a lead model splits a task across subagents, such as research, audits, migrations or comparisons.; Debug or observability panels that need per worker progress, tool calls, errors, retries, tokens and cost in one view.; Explaini…
- Avoid when: Use agent-run for a single agent working through steps in one thread.
- Related: `agent-run`, `agent-plan`, `agent-tasks`, `research-run`, `agent-loop`, `mixture-of-experts`, `agent-status`

### `agent-routines` — Agent routines
Scheduled agents in one card: each routine reads as a sentence with its schedule, next run countdown, connectors and destination, and opens smoothly to edit or run it now.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/agent-routines.md
- Main export in the spec's usage: AgentRoutines
- Use when: Settings or automation screens where people schedule agents to run on their own and post results to Slack.; A card on a dashboard that shows at a glance which scheduled agents are healthy, which failed and when each runs next.; Products that let people create…
- Avoid when: Use agent-run to watch a single agent work through a task in real time with its tool calls.
- Related: `agent-run`, `agent-tasks`, `agent-approvals`, `agent-orchestrator`, `mcp-servers`, `model-picker`, `research-run`, `text-shimmer`

### `agent-run` — Agent run
A single card that follows one AI coding agent through a task: steps stream in with the live one shimmering, tool calls open in place, and the agent stops on a two-file diff for you to approve or send back before it writes. When the run ends, the steps fold into one line and a result shows the files changed, the checks that passed and a pull request button.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/agent-run.md
- Main export in the spec's usage: AgentRun, useSimulatedRun
- Use when: Coding agents and background jobs that read, search, edit and test, where people watch progress and approve the change before it is written.; Product surfaces that hand an agent a ticket and return a pull request, such as an issue tracker, a review tool or an…
- Avoid when: Use research-run for a research agent that reads sources and writes a cited report.
- Related: `research-run`, `agent-approvals`, `agent-orchestrator`, `agent-tasks`, `text-shimmer`

### `agent-tasks` — Agent tasks
A home for background coding agents: start a task on a repository and branch, watch each card move from queued to running to ready for review, and open a pull request from the result.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/agent-tasks.md
- Main export in the spec's usage: AgentTasks
- Use when: A product surface where people hand coding tasks to background agents and come back later to review, open a pull request, retry or archive.; Dashboards for automated maintenance runs, such as dependency upgrades, flaky test fixes or codemods, where each run e…
- Avoid when: Use agent-run to follow one live agent run in detail, with its plan, tool calls and output.
- Related: `agent-run`, `agent-approvals`, `agent-routines`, `agent-orchestrator`, `model-picker`, `ai-composer`

### `ai-answer` — AI answer
One AI answer set like a clean article: it thinks, shows its sources as small cards with colored marks, and streams a formatted answer where every citation lights the sentence it supports. Copy, regenerate with options, rate, share, page through versions and ask a related question in place.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/ai-answer.md
- Main export in the spec's usage: AiAnswer
- Use when: An answer page where one question gets one well formatted, cited answer that people read, copy and share.; Docs and help center assistants that must show where each claim comes from.; Internal knowledge search where the answer mixes prose, steps, a comparison…
- Avoid when: Use ai-chat for a back and forth conversation with many turns kept on screen.
- Related: `ai-chat`, `research-run`, `ai-composer`, `ai-side-panel`, `model-picker`, `text-shimmer`

### `ai-chat` — AI chat
A full-screen AI chat where answers stream in as markdown with folding reasoning, tool chips and cited sources. People can switch chats and models, edit or retry a message into versions, rate replies and stop a reply mid-stream.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/ai-chat.md
- Main export in the spec's usage: AiChat
- Use when: A multi turn assistant inside a product page, drawer or dashboard card, with streaming answers, reasoning, tools and citations.; Any place users need to retry, edit, rate or copy answers and switch models mid conversation.; Prototyping an LLM feature: with no…
- Avoid when: Use ai-composer when you only need the prompt box with attachments, mentions and commands.
- Related: `ai-composer`, `ai-answer`, `model-picker`, `research-run`, `agent-run`, `text-shimmer`, `context-window`

### `ai-composer` — AI composer
The prompt box at the bottom of an AI app: files upload in place, / opens commands, @ inserts mentions, a model and effort menu sits in the toolbar, and the send button turns into a stop control ringed by the reply's progress.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/ai-composer.md
- Main export in the spec's usage: AiComposer
- Use when: The prompt box of an assistant, a coding agent or an in-product AI feature where people attach files, mention docs and pick a model.; A new chat screen that should open on a greeting and suggestions, then show the first exchange.; Any place that needs a strea…
- Avoid when: Use ai-chat for a full conversation with history, message actions and a sidebar of chats.
- Related: `ai-chat`, `ai-answer`, `ai-side-panel`, `model-picker`, `context-window`, `text-shimmer`

### `ai-feature-launch` — AI feature launch
An in-product launch card for an AI feature. A looping mini demo plays above a three-step tour (inline rewrite, thread summary, ask your workspace), with benefit rows, an admin-gated "Enable for my workspace" switch, and Try it now and Learn more actions.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/ai-feature-launch.md
- Main export in the spec's usage: AiFeatureLaunch, LaunchStep
- Use when: Announcing a new AI feature inside the product, with a tour of what it does and a switch to turn it on for the workspace.; Admin-gated rollouts where an admin enables AI for everyone and members can still try it.; A what's new modal or popover that needs to l…
- Avoid when: Multi-step configuration with real inputs (models, data sources): use ai-setup-wizard.
- Related: `ai-setup-wizard`, `onboarding-checklist`, `catch-up`, `ghost-text`, `ai-answer`, `switch`, `text-shimmer`

### `ai-inline-edit` — AI inline edit
A document you edit with AI in place: \u2318K on a selection, watch the rewrite stream in as a diff, accept each change, and Tab through ghost text.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/ai-inline-edit.md
- Main export in the spec's usage: AiInlineEdit
- Use when: Rewriting a selection: shorten, clarify, change tone or fix grammar in place.; Inline autocomplete while writing documents or messages.; Any AI suggestion that should be reviewed as a diff before it lands.
- Avoid when: Rich formatting such as headings, lists or links; the block edits plain paragraphs.
- Related: `ai-side-panel`, `ai-composer`, `ai-chat`, `rich-text-editor`

### `ai-insight-card` — AI insight card
A KPI card that explains itself. Explain streams a short reason for the change and ranks three drivers with contribution bars. A numbered annotation lights up on the sparkline as each driver is read, and follow-up chips ask the next question in place.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/ai-insight-card.md
- Main export in the spec's usage: AiInsightCard
- Use when: A dashboard KPI where readers ask why it moved, such as net revenue, MRR, signups or churn.; Weekly business reviews and finance dashboards that want an explanation next to the number.; Products adding AI analysis to existing analytics without a separate chat.
- Avoid when: Open ended questions across many tables: use ask-your-data.
- Related: `ask-your-data`, `metric-card`, `sparkline`, `account-health`, `text-shimmer`

### `ai-search-bar` — AI search bar
A search card for an app or docs, where typing lists grouped results right away (Docs, Customers, Issues) and pressing Tab streams a short AI answer on top. The answer's numbered citations point to the results below it.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/ai-search-bar.md
- Main export in the spec's usage: AiSearchBar
- Use when: A product or docs search where people mix finding a page or record with asking a question.; Support and success tools that search docs, customers and tickets in one place.; A command bar or search dialog that should offer an AI answer without leaving the resu…
- Avoid when: Use ai-answer for a full answer page with long formatted answers, follow ups and feedback.
- Related: `ai-answer`, `ai-command`, `ai-chat`, `ai-side-panel`, `text-shimmer`

### `ai-setup-wizard` — AI setup wizard
A three-step setup card for turning on an AI feature. You connect Notion, Google Drive, Confluence or Zendesk and watch each one sync. Then you pick the model, tone and guardrails, and ask a test question whose answer streams with numbered citations before you go live.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/ai-setup-wizard.md
- Main export in the spec's usage: AiSetupWizard
- Use when: Turning on an AI answers feature for a support, sales or internal knowledge team, like Intercom Fin, Zendesk AI or Notion Q&A.; Onboarding admins to a copilot that needs data sources, a model choice and guardrails before it is enabled.; A landing page or prod…
- Avoid when: Configuring an agent's instructions, tools and files in depth: use agent-builder.
- Related: `agent-builder`, `model-picker`, `ai-chat`, `agent-status`, `tool-call`

### `ai-side-panel` — AI side panel
An assistant docked beside a page that reads it and edits it: ask about the page or a selected passage, review each edit as a word diff, and apply it with a tint sweep on the page and one-click undo.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/ai-side-panel.md
- Main export in the spec's usage: AiSidePanel
- Use when: An assistant next to a document or record that can summarize it and propose edits.; Copilot style help where edits must be approved, applied visibly and undone.; Asking about a selected passage or table without leaving the page.
- Avoid when: A standalone conversation; use ai-chat.
- Related: `ai-chat`, `ai-composer`, `ai-inline-edit`, `ai-answer`, `context-window`

### `api-keys` — API keys
API key management where Create key unfolds into its form and each secret is shown once.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/api-keys.md
- Main export in the spec's usage: ApiKeys
- Use when: The developer settings page of an API product.; Key management with scopes, environments, and a one-time secret reveal.; Revoking keys where a stray click must not fire.
- Avoid when: Use webhooks for event endpoints and signing secrets.
- Related: `webhooks`, `integrations`, `hold-to-confirm`, `copy-button`, `roles-permissions`

### `availability-picker` — Availability picker
Find a meeting time across people and see the choice come together.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/availability-picker.md
- Main export in the spec's usage: AvailabilityPicker
- Use when: Picking a meeting time that works for several attendees.; Booking flows that show a few days and open slots with a confirmation step.
- Avoid when: Use calendar or date-picker to pick a single date.
- Related: `calendar`, `time-picker`, `date-picker`, `booking-pill`

### `billing-overview` — Billing overview
A billing page where the plan card morphs into a picker and usage, invoices, and card follow.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/billing-overview.md
- Main export in the spec's usage: BillingOverview
- Use when: The billing settings page of a SaaS app.; Pages that show plan, usage, payment method, and invoices together.; Plan changes that should happen in place without leaving billing.
- Avoid when: Use plan-comparison or usage-pricing on a public pricing page.
- Related: `usage-meter`, `plan-comparison`, `cancel-flow`, `invoice-studio`, `settings-page`

### `budget-variance` — Budget variance
Budget against actual operating spend by department as aligned bullet charts, with favorable and unfavorable variance, a month, quarter and year to date switch that springs every bar, in-place drill-down into budget lines, and a total row.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/budget-variance.md
- Main export in the spec's usage: BudgetVariance
- Use when: Monthly close and budget review screens that compare planned and actual operating spend by department or cost center.; Finance dashboards where a controller needs to see at a glance which teams are over, which are under, and by how much.; Any plan against act…
- Avoid when: Use mrr-waterfall to explain how a single total moved from one value to another.
- Related: `mrr-waterfall`, `usage-forecast`, `revenue-explorer`, `metrics-dashboard`

### `call-insights` — Call insights
A sales call insights card where talk time, flagged pricing, competitor and objection moments, an AI summary and owned next steps sit in one view. Selecting a moment plays its quote, and checking off next steps lowers the deal risk.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/call-insights.md
- Main export in the spec's usage: CallInsights, deriveRisk
- Use when: A deal page that shows the latest sales call with talk ratio, flagged moments, summary and next steps.; A call review queue for sales managers who coach on talk time and objection handling.; A research or support tool that recaps a recorded customer call with…
- Avoid when: Full transcript reading or editing: use transcript-studio.
- Related: `meeting-summary`, `lead-scoring`, `account-health`

### `cancel-flow` — Cancel flow
A cancellation flow that answers each reason with a tailored offer and a calm hold-to-cancel.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/cancel-flow.md
- Main export in the spec's usage: CancelFlow
- Use when: Subscription cancellation in billing settings with a reason step and a retention offer.; Flows that offer a discount, pause, or downgrade before confirming the cancel.
- Avoid when: Use dialog with hold-to-confirm for a one step destructive action without offers.
- Related: `billing-overview`, `plan-comparison`, `hold-to-confirm`, `stepper`

### `cart-drawer` — Cart drawer
Products fly into the cart, counts roll, and a drawer handles quantities, shipping progress, and checkout.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/cart-drawer.md
- Main export in the spec's usage: CartDrawer
- Use when: Product listings where people add several items and review them in a side cart.; Stores that show a free shipping threshold and promo codes before checkout.; Demos of an add to cart interaction with clear feedback on where the item went.
- Avoid when: Use checkout-flow for a full multi-step checkout with address and payment.
- Related: `checkout-summary`, `drawer`, `swipe-actions`, `number-field`

### `catch-up` — Catch up
A catch me up digest for when you return, where one button reads Slack, Linear, GitHub and Gmail for the range you pick and streams back a short ranked summary: Needs you, Decisions made, Shipped and FYI. Each item is one sentence with its source mark, people and a jump link, and marking items as read clears them with a smooth collapse.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/catch-up.md
- Main export in the spec's usage: CatchUp, CatchUpItem
- Use when: A home or inbox screen that summarizes what happened across connected tools while the user was away.; An AI assistant feature that turns hundreds of notifications into a short ranked list with jump links.; A weekly or daily digest preview inside a product's n…
- Avoid when: A live notification feed where every event matters; use a plain activity list instead.
- Related: `agent-status`, `tool-call`, `agent-approvals`, `ai-chat`

### `checkout-live` — Live checkout
A subscription checkout whose summary recomputes as you edit, then glides to the centre and unfolds into a receipt.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/checkout-live.md
- Main export in the spec's usage: CheckoutLive
- Use when: Upgrade from a free plan to a paid team plan.; Paid signup where seats and add-ons change the price.; A self serve checkout that needs coupons and tax by country.
- Avoid when: A physical goods cart with shipping; use checkout-flow.
- Related: `checkout-summary`, `pricing-calculator`, `plan-comparison`

### `checkout-summary` — Checkout summary
An order summary with a promo code that becomes a chip, discount and tax lines, and pay button states.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/checkout-summary.md
- Main export in the spec's usage: CheckoutSummary, CheckoutSummaryItem, CheckoutSummaryLine
- Use when: The last step before a hosted checkout such as a Stripe session redirect.; A single product purchase with launch discounts or promo codes.; A pricing page side panel that confirms the final total.
- Avoid when: Use checkout-flow when you collect shipping and card details in the page.
- Related: `cart-drawer`, `billing-toggle`, `action-button`, `money-input`

### `choropleth-explorer` — Choropleth explorer
A filled-region map that shades every state or region by revenue, growth or penetration on a stepped scale, with a country switch (United States, Canada, Brazil, United Kingdom, France, Germany, Italy, Australia), a hoverable legend, a synced ranked list and a camera zoom into local detail.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/choropleth-explorer.md
- Main export in the spec's usage: ChoroplethExplorer
- Use when: Sales, revenue or usage dashboards that break a metric down by state, country or territory.; Market coverage and penetration reviews where a region's own subareas explain its number.; Any analytics view where readers compare neighbouring areas and need the ra…
- Avoid when: Use offices-map to place pins at specific locations such as offices or stores.
- Related: `revenue-globe`, `revenue-explorer`, `kpi-drilldown`, `metric-explorer`

### `cohort-retention` — Cohort retention
A cohort retention triangle that morphs into retention curves and rewashes by segment.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/cohort-retention.md
- Main export in the spec's usage: CohortRetention
- Use when: Growth or customer success dashboards comparing how signup cohorts retain month over month.; Views that need both the cohort triangle and retention curves from the same data.
- Avoid when: Use journey-flow for paths between funnel steps.
- Related: `revenue-explorer`, `journey-flow`, `metrics-dashboard`, `activity-heatmap`, `segmented-control`

### `connected-scatter` — Connected scatter
A connected scatterplot of monthly CAC against LTV where the path draws itself in, a scrubber moves a head along the curve, and a channel switch morphs the path against a shaded 3x target line.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/connected-scatter.md
- Main export in the spec's usage: ConnectedScatter
- Use when: A growth or finance screen that shows whether unit economics are moving toward or away from a target ratio.; Comparing how a few segments or channels travelled through the same two metrics over the same months.; A report where specific months (a pricing chang…
- Avoid when: Use line-chart or metric-explorer when time itself is the axis and one metric is enough.
- Related: `metric-explorer`, `segmented-control`, `line-chart`

### `credit-topup` — Credit top-up
A card for buying AI credits. It shows the balance with a 14 day usage chart and how many days are left, three preset packs with bonus badges, a custom amount slider with a live price, auto top-up with a threshold and the saved Visa or Mastercard. When you buy, the new balance rolls in like an odometer.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/credit-topup.md
- Main export in the spec's usage: CreditTopup, quoteCredits
- Use when: Selling prepaid AI credits or tokens with volume bonuses.; A billing settings section where people also manage auto top-up and their card.; An out of credits moment where the balance, burn rate and a one click refill belong together.
- Avoid when: Subscription plan changes with seats and billing cycles: use a plan picker or checkout-live.
- Related: `checkout-live`, `payment-flow`, `usage-meter`, `slider`, `switch`, `button`

### `customer-galaxy` — Customer galaxy
2,400 accounts as a drifting galaxy that spirals into clusters by plan, region or health.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/customer-galaxy.md
- Main export in the spec's usage: CustomerGalaxy
- Use when: Customer success or revenue pages to explore where MRR and risk concentrate.; Showcase views that cluster thousands of accounts by plan, region, or health.
- Avoid when: Use customers-table when people need to find and act on specific accounts.
- Related: `revenue-globe`, `semantic-zoom`, `cohort-retention`

### `delivery-tracker` — Delivery tracker
A live order tracker whose marker glides between stops while the arrival time rolls.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/delivery-tracker.md
- Main export in the spec's usage: DeliveryTracker
- Use when: Order status pages that follow a delivery from dispatch to door.; Tracking screens with a live arrival time and an event history.; Deliveries where people can message or call the courier.
- Avoid when: Use timeline for a static list of past events.
- Related: `timeline`, `avatar`, `support-conversation`

### `document-extract` — Document extraction
Turns a document into typed data with a model and shows where every value came from: fields fill in as the page is read, and hovering a value lights its source on the PDF.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/document-extract.md
- Main export in the spec's usage: DocumentExtract
- Use when: Accounts payable, logistics or back office tools that turn invoices, receipts, emails or forms into records a person accepts before saving.; Any extraction flow where a reviewer needs to see exactly where each value came from and fix the few the model was uns…
- Avoid when: Use ai-answer for a written answer with citations rather than typed fields.
- Related: `knowledge-base`, `ai-answer`, `agent-approvals`, `model-picker`, `text-shimmer`

### `domain-verify` — Domain verify
A custom domain setup card where customers add a domain and copy the DNS records. A live checker then polls resolvers, marks each record valid, not found or misconfigured with a one-line fix, and finishes with the domain verified and the SSL certificate issued.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/domain-verify.md
- Main export in the spec's usage: DomainVerify
- Use when: Letting customers serve an app, docs site, status page or storefront from their own domain.; Verifying a sending domain for email (SPF, DKIM, DMARC) before turning on delivery.; Any setup step where a person must copy values into a third party and wait for pr…
- Avoid when: Buying or searching domains: use a search field with results instead.
- Related: `copy-button`, `button`, `text-shimmer`, `agent-status`, `tool-call`

### `env-variables` — Environment variables
An environment variables and secrets manager with masked values, per-environment scope toggles, .env paste import with duplicate and invalid key warnings, write-only sensitive values, an environment diff by fingerprint, and a redeploy banner.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/env-variables.md
- Main export in the spec's usage: EnvVariables
- Use when: A settings screen where developers manage configuration and secrets across development, preview, and production.; Onboarding a project by pasting an existing .env file and scoping it to environments in one step.; Auditing drift between environments before a r…
- Avoid when: Use api-keys for creating, scoping, and revoking access tokens that your product issues to its users.
- Related: `api-keys`, `security-settings`

### `eval-suite` — Eval suite
Run an evaluation suite on a new version of an LLM feature against its baseline: results stream in case by case, and regressions and fixes are called out with the cases behind them.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/eval-suite.md
- Main export in the spec's usage: EvalSuite
- Use when: Regression testing an LLM feature before shipping a new prompt, model or agent version.; CI style eval dashboards where people need the overall score, the per category picture and the exact cases that broke in one place.; Triage of failing cases with an LLM j…
- Avoid when: Use prompt-studio to edit a prompt and try it on one test case at a time.
- Related: `prompt-studio`, `model-arena`, `agent-run`

### `exploded-view` — Exploded view
A scroll driven exploded view where a live phone screen built from five CSS 3D layers lies back, separates in depth with labels that follow each layer, takes each layer into focus, and then reassembles.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/exploded-view.md
- Main export in the spec's usage: ExplodedView
- Use when: A showpiece section that shows a product is built with care, by literally taking its screen apart.; Explaining the layers of a design system or UI kit: tokens, grid, content, controls and overlays.; A launch page moment between the hero and the feature list,…
- Avoid when: Use zoom-into-ui to fly into parts of a flat product screen and explain features in place.
- Related: `scroll-story`

### `feature-bento` — Feature bento
A six cell feature bento where small, real product UI acts each feature out on hover.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/feature-bento.md
- Main export in the spec's usage: FeatureBento
- Use when: A landing page features section that should show the product rather than list it.; Launch pages where each capability has one clear, demonstrable behavior.
- Avoid when: Long feature lists or comparison tables. Use Plan comparison.
- Related: `spotlight-grid`, `scroll-story`, `hero-section`

### `feature-voting` — Feature voting
A public feature request board where votes roll digit by digit and the button fills with the accent. Top, New and Trending reorder the rows with one smooth move. A built-in composer suggests similar requests as you type, so people vote instead of posting duplicates.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/feature-voting.md
- Main export in the spec's usage: FeatureVoting, findSimilarRequests, sortRequests
- Use when: A public feature request page where customers vote and suggest ideas.; An in-app Give feedback panel that shows what is planned and shipped.; A customer portal that needs to deflect duplicate requests before they are posted.
- Avoid when: A full roadmap with columns per stage: use a kanban style board.
- Related: `feedback-board`, `changelog-feed`, `ai-feature-launch`, `segmented-control`, `avatar`

### `feedback-board` — Feedback board
A feature request board with a submit form that finds similar requests, upvotes, top and new sorting, status filters, and comments.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/feedback-board.md
- Main export in the spec's usage: FeedbackBoard, FeedbackRequest
- Use when: A public or in app board where customers suggest and vote on features.; Beta programs that need a lightweight place for requests and team replies.
- Avoid when: One to one support conversations; use support-conversation or support-widget.
- Related: `changelog-feed`, `support-widget`, `activity-feed`

### `gantt-timeline` — Gantt timeline
A project timeline with draggable, resizable bars, dependency arrows that follow them, and animated zoom.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/gantt-timeline.md
- Main export in the spec's usage: GanttTimeline, GanttTask, GanttGroup, GanttChange
- Use when: Planning work across weeks or months where tasks depend on each other.; Roadmaps that people reschedule by dragging, with undo and conflict warnings.; Phase based plans where finished phases can be folded into a summary bar.
- Avoid when: Use project-board for status columns without dates.
- Related: `project-board`, `week-calendar`, `timeline`, `workflow-canvas`, `tree-table`

### `goal-tracker` — Goal tracker
A team goals card where objectives open into key results with owners, confidence and progress bars. A weekly check-in updates a value, confidence and note in place, fills the bar and recalculates the objective, and a quarter selector steps from last quarter's final scores to next quarter's planning.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/goal-tracker.md
- Main export in the spec's usage: GoalTracker, GoalKeyResult, GoalObjective
- Use when: Showing a team's quarterly objectives and key results with owners and confidence.; Collecting a lightweight weekly check-in (value, confidence, note) without leaving the page.; Comparing the active quarter against last quarter's final scores.
- Avoid when: A single KPI with a trend line; use a metric or stat card.
- Related: `agent-tasks`, `activity-feed`, `account-health`

### `help-center` — Help center
A help center with instant search, topic cards, and popular articles that open into a readable article with an outline and feedback.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/help-center.md
- Main export in the spec's usage: HelpCenter
- Use when: A public help center or knowledge base; In-app help with searchable articles; Support portals that deflect tickets with good answers
- Avoid when: Developer API reference with a nav tree, use docs-sidebar
- Related: `docs-sidebar`, `faq-section`, `support-widget`, `support-conversation`

### `hero-signup` — Hero signup
A full screen waitlist hero on a soft, drifting mesh gradient: the email field validates as you type and its button grows into the confirmation with your place in line.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/hero-signup.md
- Main export in the spec's usage: HeroSignup
- Use when: Waitlists, early access, and launch pages where the email is the only ask.; Pages that want a calm but alive first impression without product screenshots.
- Avoid when: Signup that needs a password, SSO choice, or consent up front; use Sign up form.
- Related: `hero-section`, `newsletter-signup`, `cta-section`

### `horizon-chart` — Horizon chart
A horizon chart that stacks fourteen daily series as compact folded rows, with a synced crosshair, a sort by name, peak or latest, a band count setting that folds every row on one spring, and a legend that explains how to read the bands.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/horizon-chart.md
- Main export in the spec's usage: HorizonChart
- Use when: Operations or growth dashboards comparing many markets, services or products against their own baseline over weeks or months.; Monitoring views where the reader scans for which rows broke from normal and when, then reads exact values on one day.; Any time ser…
- Avoid when: Use small-multiples when there are only a few series and the reader needs axes and exact levels in each panel.
- Related: `small-multiples`, `ridgeline`, `streamgraph`, `activity-heatmap`

### `inbox-triage` — Inbox triage
Process a focused inbox with archive, snooze, and restore actions.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/inbox-triage.md
- Main export in the spec's usage: InboxTriage
- Use when: A queue of messages or requests that need archive, snooze, or restore decisions.; Inboxes where rows expand in place to show details and actions.
- Avoid when: Use inbox-sidebar for mail navigation with folders and counts.
- Related: `inbox-sidebar`, `notification-center`, `swipe-actions`, `support-conversation`

### `integrations` — Integrations
An integrations directory where Connect morphs to Connected and the filters recount as you go.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/integrations.md
- Main export in the spec's usage: Integrations
- Use when: Settings or marketplace pages for third party connections.; Directories with search, category filters, and Connect buttons.; Connections that need sync settings and a safe disconnect.
- Avoid when: Use webhooks for outgoing event endpoints.
- Related: `webhooks`, `api-keys`, `drawer`, `hold-to-confirm`, `search-field`

### `invite-people` — Invite people
Invite teammates with roles, bulk paste validation, a seat meter, and avatars that fly into a pending list.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/invite-people.md
- Main export in the spec's usage: InvitePeople
- Use when: Inviting several people at once by name or email, with a role for each.; Plans with a seat limit where people should see the effect of an invite before sending.; Flows where users paste a messy list from a spreadsheet and need clear per-entry errors.
- Avoid when: Use team-members to manage people who already joined.
- Related: `team-members`, `roles-permissions`, `tag-input`, `multi-select`, `avatar-group`

### `invoice-studio` — Invoice studio
An editable invoice with live totals and a clear save flow.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/invoice-studio.md
- Main export in the spec's usage: InvoiceStudio, InvoiceLine
- Use when: Creating or editing an invoice or quote with line items.; Forms that need a live subtotal and total as quantities and rates change.
- Avoid when: Use billing-overview to show past invoices and plan status.
- Related: `billing-overview`, `number-field`, `sortable-data-table`

### `journey-flow` — Journey flow
A Sankey of user journeys whose flows morph by channel and trace a cohort on hover.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/journey-flow.md
- Main export in the spec's usage: JourneyFlow
- Use when: Showing where users go between funnel stages, such as visit to signup to activation.; Comparing flows across acquisition channels with a segment switch.; Tracing one step to see which paths lead into and out of it.
- Avoid when: Use cohort-retention to show how groups retain over time.
- Related: `metrics-dashboard`, `cohort-retention`, `revenue-explorer`, `segmented-control`

### `kanban-board` — Kanban board
A kanban board where cards lift, tilt and spring into the slot that opens for them, with swimlanes and live WIP limits.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/kanban-board.md
- Main export in the spec's usage: KanbanBoard
- Use when: A team board where cards move between statuses.; Pipelines where ordering within a stage matters.; Boards that need a per person view.
- Avoid when: Scheduling on dates; use gantt-timeline or week-calendar.
- Related: `project-board`, `gantt-timeline`, `week-calendar`, `reorderable-list`

### `knowledge-base` — Knowledge base
A retrieval knowledge base in one card: add sources and watch them parse, chunk, embed and index, then test a question and see which chunks come back and why.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/knowledge-base.md
- Main export in the spec's usage: KnowledgeBase
- Use when: Admin screens for a RAG or support assistant where people add documents, watch them index, and check what a question retrieves.; Explaining or tuning chunking, hybrid search and reranking with a working test bench instead of a diagram.; Debugging why an assis…
- Avoid when: Use vector-search to illustrate how embeddings and nearest neighbours work; this block is the working product surface.
- Related: `vector-search`, `document-extract`, `agent-memory`, `ai-answer`, `research-run`, `mcp-servers`

### `kpi-drilldown` — KPI drilldown
KPI cards that expand into a full detail chart with period comparison and a breakdown table, then fold back.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/kpi-drilldown.md
- Main export in the spec's usage: KpiDrilldown
- Use when: An analytics or finance overview where each number deserves a closer look.; Executive dashboards that compare the current period with the previous one.
- Avoid when: Use metric-explorer to compare many metrics on one chart.
- Related: `metrics-dashboard`, `metric-explorer`, `revenue-explorer`, `mrr-waterfall`, `bar-chart`

### `layout-morph` — Layout morph
A 24 card gallery that flies between grid, masonry, list, fan, carousel and a 3D helix.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/layout-morph.md
- Main export in the spec's usage: LayoutMorph
- Use when: Catalogue, portfolio, or team pages where people browse the same set in different layouts.; Showcase galleries that fly between grid, masonry, list, fan, carousel, and a 3D helix.
- Avoid when: Use photo-grid for a simple gallery.
- Related: `photo-grid`, `carousel`, `cover-flow`, `card-stack`, `segmented-control`

### `lead-scoring` — Lead scoring
A lead scoring card where inbound B2B leads are ranked by an AI fit score, each with a score ring and a one-line reason. Open a lead to see its signals and score breakdown, then push it to HubSpot or Salesforce.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/lead-scoring.md
- Main export in the spec's usage: LeadScoring, Lead
- Use when: A sales inbox or SDR queue that ranks new inbound leads by fit.; Showing why a model scored a lead, with signals and a weighted breakdown.; Handing a qualified lead to HubSpot or Salesforce from the same view.
- Avoid when: Large tables of hundreds of leads with filters and bulk edits; use a data table.
- Related: `account-health`, `enrich-column`, `call-insights`, `agent-approvals`, `connector-setup`

### `line-replay` — Line replay
A time replay line chart that draws a day of traffic with a moving playhead, a value label on the tip, a scrubber, speed control and key moments annotated as the playhead passes them.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/line-replay.md
- Main export in the spec's usage: LineReplay
- Use when: Post-launch or campaign reviews where the team wants to watch traffic respond to each announcement.; Incident retrospectives that step through a metric with the alert, the deploy and the recovery marked.; Storytelling pages and reports where a single series o…
- Avoid when: Use annotated-trend when people need to add and edit their own notes on a static trend.
- Related: `connected-scatter`, `metric-explorer`

### `login` — Login and sign up
A glass magic link card over dusk photography that folds its envelope shut once sent.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/login.md
- Covers variants: `login-immersive` (pro), `login-split` (pro)
- Main export in the spec's usage: LoginImmersive
- Use when: A magic link sign in page with a strong brand photo behind a glass card.; Consumer or creative products where the sign in screen carries the brand mood.
- Avoid when: Use login-centered for passkey-first auth with an email code.
- Related: `login-centered`, `login-split`, `sign-in`, `signup-form`

### `magic-link` — Magic link
A passwordless sign in card where an email with inline validation and typo fixes sends a magic link, and the card crossfades in place to a check your inbox step with a sealing envelope, Gmail and Outlook shortcuts and a resend countdown. Google and GitHub sign in sit above, with their real marks.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/magic-link.md
- Main export in the spec's usage: MagicLink
- Use when: Passwordless sign in or sign up by email link, with optional Google and GitHub sign in.; B2B products that want a work email gate with a clear what happens next screen.; Replacing a password form to cut sign in friction and reset requests.
- Avoid when: Password plus email sign in or MFA codes; use sign-in or a login block instead.
- Related: `sign-in`, `login-centered`, `login-split`, `input`, `button`

### `market-terminal` — Market terminal
A trading terminal with a canvas candlestick chart, volume, moving averages, crosshair OHLC readout, wheel, drag and pinch zoom, a live watchlist with sparklines and flashing prices, and a market and limit order ticket.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/market-terminal.md
- Main export in the spec's usage: MarketTerminal
- Use when: A trading or investing product that needs a full chart, a watchlist and an order ticket on one screen.; A paper trading or education app where people practice placing market and limit orders against moving prices.; A markets dashboard where candles, volume an…
- Avoid when: Use order-book-depth to show bids and asks at each price level.
- Related: `metric-explorer`, `wallet-card`

### `mcp-servers` — MCP servers
Manage the MCP servers that give an agent its tools: see what the enabled tools cost in context, connect or pause a server, and switch single tools on or off.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/mcp-servers.md
- Main export in the spec's usage: McpServers, McpTool
- Use when: Settings for an agent or AI assistant that connects to MCP servers: which servers it has, which tools are on and what they cost in context.; Onboarding a new integration with a directory, sign in and tool discovery in one place.; Keeping tool definitions insi…
- Avoid when: Use agent-approvals to approve or deny individual tool calls while the agent runs.
- Related: `agent-approvals`, `context-window`, `agent-run`, `ai-composer`, `agent-routines`, `agent-orchestrator`, `knowledge-base`

### `media-player` — Media player
An audio player with a living playlist and complete playback controls.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/media-player.md
- Main export in the spec's usage: MediaPlayerBlock
- Use when: A small audio collection such as a podcast, sample pack, or playlist.; Pages that need a full player with seek, skip, volume, and a track list.
- Avoid when: Use now-playing for a compact now playing widget.
- Related: `now-playing`, `slider`, `voice-recorder`

### `metric-explorer` — Metric explorer
KPI cards that open into a scrubbable chart and morph between metrics and ranges.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/metric-explorer.md
- Main export in the spec's usage: MetricExplorer
- Use when: The top of a SaaS analytics or finance page with KPI cards that open into a chart.; Dashboards where people move between a few metrics and date ranges.
- Avoid when: Use stat-card or metric-card for static KPI tiles.
- Related: `metric-card`, `sparkline`, `revenue-explorer`, `segmented-control`

### `metrics-dashboard` — Metrics dashboard
A dense analytics view with KPI tabs, one inspectable chart, and top pages and sources.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/metrics-dashboard.md
- Main export in the spec's usage: MetricsDashboard
- Use when: A small, explorable KPI overview with a range toggle and one chart.; Product or marketing dashboards with four headline metrics, a 7, 30, or 90 day range, and top pages and sources.
- Avoid when: Use metric-explorer or revenue-explorer for larger or drill-down data.
- Related: `metric-explorer`, `revenue-explorer`, `sparkline`, `bar-chart`

### `model-arena` — Model arena
A blind side by side model comparison in one card: send one prompt to two models, watch both answers stream at the same pace, vote for the better one, then reveal which model wrote each.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/model-arena.md
- Main export in the spec's usage: ModelArena
- Use when: Blind human preference tests between two models on the same prompt, such as an internal bake-off before switching providers.; Prompt or model evaluation tools where people should judge answers without knowing which model wrote them.; Showing latency, speed an…
- Avoid when: Use model-picker to let someone choose one model for their own chat; this block compares answers, it does not set a default.
- Related: `model-picker`, `eval-suite`, `prompt-studio`, `ai-chat`

### `model-picker` — Model picker
A model picker in one quiet pill: open it to choose from featured models with a one line note each, set the reasoning effort, or browse every other model by provider, and the pill swaps to your choice in place.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/model-picker.md
- Main export in the spec's usage: ModelPicker
- Use when: Choosing the model and effort for a chat, an agent or a playground.; A default model setting with a short review of what the chosen model costs and how much context it takes.
- Avoid when: Comparing two models' answers side by side; use model-arena.
- Related: `ai-composer`, `model-arena`, `ai-chat`, `context-window`, `dropdown-menu`

### `mrr-waterfall` — MRR waterfall
An MRR bridge whose floating bars morph by period and open the accounts behind each move.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/mrr-waterfall.md
- Main export in the spec's usage: MrrWaterfall
- Use when: Revenue or board reporting that explains how MRR moved from start to end of a period.; Finance views where each movement should list the accounts behind it.
- Avoid when: Use revenue-explorer for MRR over many months.
- Related: `revenue-explorer`, `cohort-retention`, `bar-chart`, `segmented-control`, `metric-explorer`

### `multi-step-form` — Multi-step form
A guided form that presents one decision at a time and preserves progress.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/multi-step-form.md
- Main export in the spec's usage: MultiStepForm, FormStep
- Use when: Onboarding or intake flows split into a few short steps.; Wizards that need Back and Continue, progress, and a success state out of the box.
- Avoid when: Use stepper when you only need the progress indicator.
- Related: `stepper`, `signup-form`

### `onboarding-illustration` — Onboarding illustration
A compact onboarding card whose line illustration morphs from folder to files, team, and badge.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/onboarding-illustration.md
- Main export in the spec's usage: OnboardingIllustration
- Use when: A short first-run dialog in a document or workspace product.; Onboarding with three or four steps that each need a simple picture.
- Avoid when: Use onboarding-checklist for tasks people complete over time.
- Related: `onboarding-checklist`, `stepper`, `empty-states`

### `onboarding-survey` — Onboarding survey
A post-signup onboarding survey where each question gets its own step of large option cards, picked with keys 1 to 4 and Enter. A short personalization checklist then ticks off and lands on an editable "You're all set" summary.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/onboarding-survey.md
- Main export in the spec's usage: OnboardingSurvey
- Use when: Post-signup personalization: role, team size and first action before the first screen.; Short in-product surveys where every answer changes what someone sees next.; Re-onboarding when a workspace changes plan or adds a team.
- Avoid when: Long forms with free text or many fields; use a regular form or import-wizard.
- Related: `ai-setup-wizard`, `invite-people`, `signup-form`, `radio-cards`, `stepper`

### `pricing-calculator` — Pricing calculator
A seat slider and billing toggle drive plan cards with rolling prices and a moving recommended badge.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/pricing-calculator.md
- Main export in the spec's usage: PricingCalculator
- Use when: Per-seat pricing where showing the exact total for a team size helps people choose.; Pricing pages with a monthly and yearly toggle and a visible yearly saving.; Plans with seat caps or volume discounts that are hard to explain in a static table.
- Avoid when: Use usage-pricing when price depends on metered usage rather than seats.
- Related: `usage-pricing`, `plan-comparison`, `billing-toggle`, `slider`

### `product-detail` — Product detail
A product page with a swipeable gallery, finish and size variants, add to bag that confirms in place, shipping, a reviews summary, and details.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/product-detail.md
- Main export in the spec's usage: ProductDetail, DetailProduct
- Use when: Product pages with a few variants, a gallery, and reviews.; Stores that want stock aware variants with a restock alert instead of a dead button.
- Avoid when: Products built from many options with live pricing; use product-configurator.
- Related: `product-listing`, `cart-drawer`

### `product-listing` — Product listing
A storefront grid with price, color and size filters, a sort menu, hover photo swaps, and quick add with a size row.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/product-listing.md
- Main export in the spec's usage: ProductListing, ListingProduct
- Use when: A shop's collection or category page with a few dozen to a few hundred products.; Catalogs where color and size are the main filters and a quick add saves a trip to the product page.
- Avoid when: One product with many options; use product-detail or product-configurator.
- Related: `product-detail`, `cart-drawer`

### `profile-page` — Profile page
A user profile with cover, bio, stats, activity and project tabs, and an edit sheet that writes back into the page.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/profile-page.md
- Main export in the spec's usage: ProfilePage
- Use when: A person's own profile with an edit flow; Public creator or member pages inside an app; Team member pages that show recent work
- Avoid when: Account security or billing settings, use settings-page
- Related: `settings-page`, `team-directory`, `activity-feed`, `team-members`

### `project-board` — Project board
A living workflow board for moving work between stages.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/project-board.md
- Main export in the spec's usage: ProjectBoard
- Use when: A compact kanban with a handful of tasks across fixed stages.; Boards where moving tasks should be accessible through explicit buttons, not drag only.
- Avoid when: Use reorderable-list when order within one list matters more than stages.
- Related: `reorderable-list`, `workspace-sidebar`, `avatar-group`, `filter-toolbar`

### `prompt-studio` — Prompt studio
One card for editing, testing and shipping a prompt template: variables as chips with sample values, a test run against the chosen model, and versions you can compare and promote to production.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/prompt-studio.md
- Main export in the spec's usage: PromptStudio, PromptEditor
- Use when: A settings or admin page where a support lead or engineer tunes the prompt behind one AI feature and tests it on real cases.; Prompt management that needs a compact version history with authors, a diff against an earlier version and a visible production point…
- Avoid when: Use ai-chat for an end user conversation; this card edits templates, not messages.
- Related: `model-picker`, `model-arena`, `eval-suite`, `ai-inline-edit`, `ai-chat`

### `release-readiness` — Release readiness
A launch checklist that keeps prerequisites, progress, and the final action together.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/release-readiness.md
- Main export in the spec's usage: ReleaseReadiness
- Use when: A pre-launch or handoff gate where several checks must be done before one action unlocks.; Release or launch checklists with a readiness bar and owners.; Handoffs that should optionally notify people when the action runs.
- Avoid when: Use onboarding-checklist for a user's own getting-started tasks.
- Related: `onboarding-checklist`, `progress`

### `research-run` — Research run
Deep research that plans searches, reads sources with their marks, and streams a cited answer where every chip lights up the sentence it supports.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/research-run.md
- Main export in the spec's usage: ResearchRun, ResearchSource
- Use when: An answer engine or deep research feature that searches, reads and cites.; Internal knowledge search where people must verify each claim.; Any long streamed answer that benefits from visible sources and follow ups.
- Avoid when: Open ended conversation without sources; use ai-chat.
- Related: `ai-chat`, `agent-run`, `ai-side-panel`, `ai-answer`

### `revenue-explorer` — Revenue explorer
A SaaS revenue chart you zoom with a brush while paths, axes and figures glide to the range.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/revenue-explorer.md
- Main export in the spec's usage: RevenueExplorer
- Use when: Monthly MRR or revenue broken into new, expansion, and churn on an analytics page.; Charts where people need to zoom a date range with an overview brush and compare against a prior period.
- Avoid when: Use mrr-waterfall to explain how MRR moved between two points in time.
- Related: `metric-explorer`, `mrr-waterfall`, `usage-forecast`, `cohort-retention`, `animated-counter`

### `revenue-globe` — Revenue globe
A dotted globe where live payments arc home to headquarters, with a replayable day.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/revenue-globe.md
- Main export in the spec's usage: RevenueGlobe
- Use when: Revenue or operations overviews showing where payments come from right now.; Showcase pages where a live globe with arcs and a day timeline adds impact.
- Avoid when: Use a table or bar-chart when exact regional numbers matter more than the view.
- Related: `customer-galaxy`, `activity-terrain`, `animated-counter`, `revenue-explorer`

### `roles-permissions` — Roles and permissions
A permissions matrix with group toggles that ripple, role duplication and a review bar.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/roles-permissions.md
- Main export in the spec's usage: RolesPermissions
- Use when: Workspace settings where admins edit what each role can do.; Permission matrices with grouped permissions and a review step before saving.
- Avoid when: Use team-members to assign roles to people.
- Related: `team-members`, `security-settings`, `settings-page`, `switch`, `avatar-group`

### `scroll-story` — Scroll story
A feature section where scrolling the copy drives a pinned product view through each step.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/scroll-story.md
- Main export in the spec's usage: ScrollStory
- Use when: Marketing pages that walk through a product in a few steps as people scroll.; Feature sections where a pinned product view should change with the copy.
- Avoid when: Use scroll-highlight for a single paragraph that reveals with scroll.
- Related: `text-reveal`, `in-view-title`

### `search-results` — Search results
A faceted workspace search page with suggestions, facet counts that follow the query, filter chips, mixed doc, person and file results with highlighted matches, a gliding keyboard cursor and a preview pane.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/search-results.md
- Main export in the spec's usage: SearchResults
- Use when: A full search page for a workspace or knowledge base that returns several kinds of things at once.; Search where people narrow by type, team, and date, and want to read a match before opening it.
- Avoid when: Use command-palette for quick jump to navigation from any screen.
- Related: `command-palette`, `filter-toolbar`, `help-center`, `product-listing`

### `seat-manager` — Seat manager
A team seats and billing card where avatars and a seat meter show members, invites and open seats against what you pay for, a stepper rolls the prorated charge for today and the new monthly total live, and changes go through a confirm step before anyone is charged. Pending invites can be resent or revoked with undo, and when every seat is taken the card says so and offers to add one.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/seat-manager.md
- Main export in the spec's usage: SeatManager, buildQuote
- Use when: Letting a team admin add or remove paid seats with the price impact visible before paying.; Showing seat usage against purchased seats, including invites that reserve a seat.; Handling the seat limit at the moment an admin hits it, with a one tap way to add a…
- Avoid when: Managing roles and permissions for many members: use a member table and link to this card for seats.
- Related: `billing-overview`, `credit-topup`, `button`, `avatar`, `text-shimmer`, `checkout-summary`

### `seat-map` — Seat map
An event seat picker with a curved concert hall map, price tiers, zoom and pan, sold, held and wheelchair seats, and a live summary with fees and a hold countdown.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/seat-map.md
- Main export in the spec's usage: SeatMap
- Use when: Reserved seating for concerts, theatre, sports and conferences where the buyer picks exact seats.; Any spatial picker with priced places: tables in a restaurant plan, desks in an office, cabins on a deck.; Checkout flows that need a live total and a short hol…
- Avoid when: Use a quantity stepper with best available when seats are general admission or assigned by the box office.
- Related: `availability-picker`, `choropleth-explorer`

### `security-settings` — Security settings
An account security page with guided two-factor setup, password change and active sessions.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/security-settings.md
- Main export in the spec's usage: SecuritySettings
- Use when: The security tab of account settings with two-factor setup, password change, and sessions.; Guided TOTP setup that walks through scan, verify, and backup codes.
- Avoid when: Use settings-page for general account and workspace settings.
- Related: `settings-page`, `api-keys`, `password-strength`, `otp-input`

### `selection-toolbar` — Selection toolbar
A contextual batch action surface that appears when items are selected.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/selection-toolbar.md
- Main export in the spec's usage: SelectionToolbar, SelectionAction
- Use when: Bulk actions for checkbox-selectable tables or grids.; Floating bars that appear only while items are selected.
- Avoid when: Use dropdown-menu for per-row actions.
- Related: `sortable-data-table`, `checkbox`

### `semantic-zoom` — Semantic zoom
An infinite-zoom map of a company that reveals teams, projects, tasks and people as you fly in.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/semantic-zoom.md
- Main export in the spec's usage: SemanticZoom
- Use when: Workspace or portfolio overviews where people zoom from the whole company to one task.; Hierarchical data where each zoom level should show different detail.
- Avoid when: Use tree-view for a plain hierarchy people scan and expand.
- Related: `customer-galaxy`, `tree-view`, `breadcrumb`, `layout-morph`

### `settings-command` — Settings command
Workspace settings where a search field grows into a palette that flies you to any setting.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/settings-command.md
- Main export in the spec's usage: SettingsCommand
- Use when: Workspace or account settings with several sections and many options.; Admin consoles where support links people to a specific setting.; Any settings page where people ask where something lives.
- Avoid when: Use settings-page for a short, paged profile form with a few fields per section.
- Related: `settings-page`, `command-palette`, `security-settings`, `switch`, `segmented-control`

### `settings-page` — Settings page
Account settings with a gliding section nav and a save bar that morphs in as you edit.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/settings-page.md
- Main export in the spec's usage: SettingsPage
- Use when: Account or workspace settings with several sections.; Forms that should show a save bar only when something changed.; Settings where Cmd or Ctrl+S should save.
- Avoid when: Use security-settings for sessions, two factor, and passwords.
- Related: `security-settings`, `billing-overview`, `team-members`, `api-keys`, `switch`

### `sidebar` — Sidebar
A product sidebar with a workspace switcher, live search, draggable favorites, and inline projects.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/sidebar.md
- Covers variants: `workspace-sidebar` (pro), `sidebar-rail` (pro), `docs-sidebar` (pro), `inbox-sidebar` (pro)
- Main export in the spec's usage: WorkspaceSidebar
- Use when: The main navigation of a multi-workspace app.; Sidebars with draggable favorites and inline project creation.; Navigation that should collapse to an icon rail with the [ shortcut.
- Avoid when: Use sidebar-rail when you need the whole app shell with a mobile sheet.
- Related: `sidebar-rail`, `inbox-sidebar`, `docs-sidebar`, `search-field`, `reorderable-list`

### `small-multiples` — Small multiples
A trellis of small line charts that reads as one chart, with a synced crosshair, a shared or independent y scale that springs the axes, sorting with a FLIP reorder, a ghost of the overall total behind every panel and dimming for flat trends.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/small-multiples.md
- Main export in the spec's usage: SmallMultiples
- Use when: Comparing revenue, signups or usage across regions, products, plans or channels over the same months.; Showing which segments grow, shrink or stall at a glance, with one shared crosshair to read every value for the same period.; Dashboards where one multi-lin…
- Avoid when: Use line-chart when two or three series need to be read against each other on one plot.
- Related: `metric-explorer`, `kpi-drilldown`, `revenue-explorer`, `line-chart`, `sparkline`

### `smart-scheduler` — Smart scheduler
A scheduling card where one sentence like "Find 30 min with Maya and Leo next week, mornings" is read into chips. The three best slots are then ranked across everyone's Google Calendar and Outlook calendars, with an availability strip per person and conflicts called out. Picking a slot opens a draft invite with a Google Meet link, ready to send.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/smart-scheduler.md
- Main export in the spec's usage: SmartScheduler, BusyBlock
- Use when: A scheduling assistant inside a CRM, recruiting tool, or team app that books internal meetings from one sentence.; Showing why a time was suggested: who is free, what conflicts, and what is tentative.; An AI feature demo where the result has to be checkable a…
- Avoid when: Public booking pages where guests pick from your open times; use availability-picker or booking-pill.
- Related: `availability-picker`, `week-calendar`, `booking-pill`, `meeting-summary`, `smart-form-fill`, `date-range-picker`

### `spend-alert` — Spend alert
A budget and spend alert card where the threshold is set right on the live spend bar, with forecast, Email, Slack and PagerDuty toggles, a hard stop and a live preview of the Slack message the alert will post.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/spend-alert.md
- Main export in the spec's usage: SpendAlert
- Use when: Letting a team set a monthly budget and alert threshold for metered spend.; Showing how close current and forecast spend are to an alert line.; Choosing where cost alerts go and previewing the Slack message before saving.
- Avoid when: Read-only usage reporting with no settings; use usage-forecast or usage-billing instead.
- Related: `usage-forecast`, `usage-billing`, `billing-overview`, `switch`, `slider`

### `spotlight-grid` — Spotlight grid
A feature grid where light follows the pointer, cards play live demos, and a click morphs a card into its detail.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/spotlight-grid.md
- Main export in the spec's usage: SpotlightGrid
- Use when: A product landing page section that shows four features with live, hands-on previews.; Developer tool marketing where a small working demo explains a feature better than copy.; Pages that want a bento grid with one wide card per row and a detail view that ope…
- Avoid when: Use use-case-gallery for a browsable set of customer or use case stories.
- Related: `expandable-card`, `scroll-story`

### `support-conversation` — Support conversation
A responsive message thread with useful quick replies and live feedback.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/support-conversation.md
- Main export in the spec's usage: SupportConversation
- Use when: A support chat or ticket thread with quick replies and attachments.; Help flows that should show a typing indicator and a resolve toggle.
- Avoid when: Use support-widget for a floating help launcher.
- Related: `support-widget`, `ai-composer`, `inbox-triage`, `textarea`

### `support-widget` — Support widget
An in-app help launcher that grows into live article search, reading, and a chat with your team.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/support-widget.md
- Main export in the spec's usage: SupportWidget
- Use when: An in-app help launcher with article search, an article reader, and chat.; SaaS products that want one help entry point mounted near the app root.
- Avoid when: Use support-conversation for a full page support chat.
- Related: `search-field`, `avatar`, `text-morph`, `dialog`, `ai-composer`

### `task-breakdown` — Task breakdown
A goal input where AI breaks one sentence into a plan: tasks stream in with estimates, owners and dependencies, and a live timeline shows whether the deadline holds. Reorder, edit or regenerate any task, then send the plan to Linear or Jira with progress for each issue and links.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/task-breakdown.md
- Main export in the spec's usage: TaskBreakdown
- Use when: Turning a goal or brief into a scoped project plan inside a PM, CRM or internal tool.; Exporting AI drafted work to Linear or Jira with a review step before anything is created.; Showing whether a plan fits a deadline and updating that as people edit estimate…
- Avoid when: Showing an agent working through steps live; use agent-plan.
- Related: `agent-plan`, `agent-tasks`, `tool-call`, `agent-status`

### `team-directory` — Team directory
Searchable people, team filters, and a focused profile panel.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/team-directory.md
- Main export in the spec's usage: TeamDirectory
- Use when: An internal directory where people search colleagues and copy contact details.; Team pages with department filters and a profile pane.
- Avoid when: Use team-members to manage roles and invitations.
- Related: `team-members`, `team-showcase`, `search-field`, `avatar`

### `team-members` — Team members
A members list where typed emails turn into chips and fly into pending invites as seats roll.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/team-members.md
- Main export in the spec's usage: TeamMembers
- Use when: The team or workspace settings page of a SaaS app.; Inviting several people at once by typing or pasting emails.; Member lists with roles, pending invites, and seat counts.
- Avoid when: Use team-directory for a browsable people directory.
- Related: `team-directory`, `roles-permissions`, `tag-input`, `settings-page`, `avatar`

### `team-showcase` — Team showcase
An image led team introduction with profiles that open in place.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/team-showcase.md
- Main export in the spec's usage: TeamShowcase, TeamShowcaseReview
- Use when: About or company pages that introduce the team with portraits.; Sections that need one of four layouts: gallery, filmstrip, directory, or spotlight.
- Avoid when: Use team-directory for an internal, searchable people list.
- Related: `team-directory`, `testimonial-stage`, `team-members`, `avatar`

### `testimonial-stage` — Studio perspectives
Portrait led editorial stories with a focused reading state.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/testimonial-stage.md
- Main export in the spec's usage: TestimonialStage
- Use when: Testimonials or editorial stories where the person's portrait matters.; Landing sections that rotate through a few quotes on demand.
- Avoid when: Use logo-marquee when logos are enough social proof.
- Related: `team-showcase`, `logo-marquee`, `carousel`, `tabs`

### `two-factor-setup` — Two-factor setup
A two-factor setup card where you scan a real, working authenticator QR code, type the 6-digit code into slots that move to the next box on their own, and save your backup codes before it turns on. Every step shares one fixed-size card, so it moves between steps with a short slide and never changes size.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/two-factor-setup.md
- Main export in the spec's usage: TwoFactorSetup
- Use when: Turning on authenticator app two-factor from account or workspace security settings.; Enforced two-factor onboarding for admins after sign-in.; Re-enrolling a new phone, with fresh backup codes.
- Avoid when: SMS or email one-time codes only: use otp-input in a sign-in form.
- Related: `security-settings`, `otp-input`, `copy-button`, `checkbox`

### `uptime-status` — Uptime status
A status page with 90 day uptime bars, a morphing latency chart and an incident timeline.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/uptime-status.md
- Main export in the spec's usage: UptimeStatus
- Use when: A public or internal status page with per-service uptime history.; Pages that combine 90 day uptime strips, response time, and an incident timeline.
- Avoid when: Use activity-heatmap for activity counts rather than availability.
- Related: `activity-heatmap`, `badge`, `timeline`, `sparkline`

### `usage-billing` — Usage billing
A usage based billing dashboard with a projected spend line, meters against limits, alerts, and an upgrade that morphs into a confirm sheet.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/usage-billing.md
- Main export in the spec's usage: UsageBilling
- Use when: A billing page for usage priced SaaS or infrastructure products.; Admin dashboards where finance needs spend alerts and invoice history in one place.; Upgrade moments driven by limits, where the upgrade should explain what changes.
- Avoid when: Use billing-overview for flat seat based plans without meters.
- Related: `billing-overview`, `usage-forecast`, `usage-pricing`, `plan-comparison`, `usage-meter`

### `usage-forecast` — Usage forecast
A billing period usage chart with a forecast cone and a draggable budget that dates the crossing.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/usage-forecast.md
- Main export in the spec's usage: UsageForecast
- Use when: Billing or usage pages that warn customers before they hit a budget.; Metered products that show month to date usage with a forecast range.
- Avoid when: Use usage-meter for a simple progress bar against a limit.
- Related: `usage-meter`, `usage-pricing`, `billing-overview`, `segmented-control`, `metric-explorer`

### `usage-pricing` — Usage pricing
A pricing calculator that finds your plan as you drag seats and traffic.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/usage-pricing.md
- Main export in the spec's usage: UsagePricing
- Use when: Pricing pages for plans priced by seats plus usage.; Calculators that should recommend a plan as people move sliders.; Monthly and yearly toggles where the saving should be visible in the breakdown.
- Avoid when: Use plan-comparison for a side by side table of fixed tiers.
- Related: `plan-comparison`, `slider`, `animated-counter`, `segmented-control`, `usage-forecast`

### `wallet-card` — Wallet card
A compact account view with balance, recent activity, and focused money actions.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/wallet-card.md
- Main export in the spec's usage: WalletCard
- Use when: A personal or business balance summary with quick send, deposit, swap, and buy actions.; Dashboards that pair a balance with a small history chart and recent activity.; Apps with a main and a reserve account shown in one card.
- Avoid when: Use billing-overview for subscription billing and invoices.
- Related: `billing-overview`, `wallet-stack`, `animated-counter`

### `webhook-tester` — Webhook tester
A developer webhook tester where you pick an event, edit its JSON payload and send a signed test event. You watch it go from signed to sent to 200 OK in 184 ms, then read the response body, headers and exact request, and retry failed deliveries from a recent list.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/webhook-tester.md
- Main export in the spec's usage: WebhookTester
- Use when: A developer settings page where customers test a webhook endpoint before going live.; Integration onboarding that asks people to prove their handler returns 2xx and verifies signatures.; Internal tools for replaying failed deliveries with a retry.
- Avoid when: Managing many endpoints, filters and event subscriptions: use the webhooks block and link here for testing one.
- Related: `webhooks`, `api-keys`, `tool-call`, `copy-button`, `text-shimmer`

### `webhooks` — Webhooks
A webhooks console with delivery history, a payload inspector and retries that roll the rate.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/webhooks.md
- Main export in the spec's usage: Webhooks
- Use when: A developer settings page for webhook endpoints, delivery history, and retries.; Consoles that need a payload and headers inspector next to the delivery list.
- Avoid when: Use api-keys for managing tokens.
- Related: `api-keys`, `code-block`, `copy-button`, `integrations`

### `week-calendar` — Week calendar
A week calendar where you drag to create, move, and resize events, with color coded calendars, day and agenda views, and swipes on phones.
- Spec (read fully before building): uiarc-pro-markdowns/blocks/week-calendar.md
- Main export in the spec's usage: WeekCalendar
- Use when: Scheduling and planning screens where people create, move and resize time blocks across a week.; Team or personal calendars that need several color coded calendars, all day events and an agenda on phones.
- Avoid when: Use month-calendar for a month overview with events per day.
- Related: `calendar`, `date-picker`, `time-picker`, `popover`, `availability-picker`
