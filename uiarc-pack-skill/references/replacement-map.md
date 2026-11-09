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
