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
