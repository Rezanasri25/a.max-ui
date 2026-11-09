# Arc UI (uiarc.dev) — Free source code, item by item

Downloaded from the public shadcn registry on uiarc.dev on 2026-11-05.
121 free components + 22 free blocks = 143 items, plus 3 shared items (arc-foundation, arc-motion-tokens, arc-skill).
Total: 146 items, 334 files.

How it was built: the item list is the site's own catalog filtered to tier = free;
each item's code comes from its public registry JSON (https://uiarc.dev/r/<name>.json),
the exact payload `npx shadcn@latest add @uiarc/<name>` installs. Every file the site
lists for an item is saved in that item's folder with its real name and format
(.tsx, .ts, .module.css, .css, .md). Files an item shares with others (lib/* helpers)
are copied into each item that uses them, so every folder is self-contained.

Notes:
- The 4 theme-switch variants (theme-switch, -eclipse, -split, -rise) ship identical
  code on the site itself (same files, verified by checksum); each still has its own folder.
- Blocks built from components (e.g. hero-section) list those components under
  registryDependencies in manifest.json; the components themselves are in components/.
- Install order that works: shared/arc-foundation + shared/arc-motion-tokens first,
  then any component/block. npm dependencies per item are listed in manifest.json.
- Pro items are NOT here: their registry is token-gated. This zip is only the free (MIT) set.

## Components (free) — 121

- **Accordion** (`accordion`) — 2 files: `accordion.tsx`, `accordion.module.css` — page: https://uiarc.dev/components/accordion
- **Action button** (`action-button`) — 2 files: `action-button.tsx`, `action-button.module.css` — page: https://uiarc.dev/components/action-button
- **Action swap** (`action-swap`) — 2 files: `action-swap.tsx`, `action-swap.module.css` — page: https://uiarc.dev/components/action-swap
- **Activity heatmap** (`activity-heatmap`) — 2 files: `activity-heatmap.tsx`, `activity-heatmap.module.css` — page: https://uiarc.dev/components/activity-heatmap
- **Alert** (`alert`) — 2 files: `alert.tsx`, `alert.module.css` — page: https://uiarc.dev/components/alert
- **Animated counter** (`animated-counter`) — 2 files: `animated-counter.tsx`, `animated-counter.module.css` — page: https://uiarc.dev/components/animated-counter
- **Announcement bar** (`announcement-bar`) — 2 files: `announcement-bar.tsx`, `announcement-bar.module.css` — page: https://uiarc.dev/components/announcement-bar
- **Avatar** (`avatar`) — 3 files: `avatar.tsx`, `avatar.module.css`, `arc-provider.tsx` — page: https://uiarc.dev/components/avatar
- **Avatar group** (`avatar-group`) — 2 files: `avatar-group.tsx`, `avatar-group.module.css` — page: https://uiarc.dev/components/avatar-group
- **Badge** (`badge`) — 2 files: `badge.tsx`, `badge.module.css` — page: https://uiarc.dev/components/badge
- **Bar chart** (`bar-chart`) — 2 files: `bar-chart.tsx`, `bar-chart.module.css` — page: https://uiarc.dev/components/bar-chart
- **Billing toggle** (`billing-toggle`) — 2 files: `billing-toggle.tsx`, `billing-toggle.module.css` — page: https://uiarc.dev/components/billing-toggle
- **Bottom sheet** (`bottom-sheet`) — 2 files: `bottom-sheet.tsx`, `bottom-sheet.module.css` — page: https://uiarc.dev/components/bottom-sheet
- **Breadcrumb** (`breadcrumb`) — 3 files: `breadcrumb.tsx`, `breadcrumb.module.css`, `arc-provider.tsx` — page: https://uiarc.dev/components/breadcrumb
- **Brush chart** (`brush-chart`) — 2 files: `brush-chart.tsx`, `brush-chart.module.css` — page: https://uiarc.dev/components/brush-chart
- **Button** (`button`) — 2 files: `button.tsx`, `button.module.css` — page: https://uiarc.dev/components/button
- **Button group** (`button-group`) — 2 files: `button-group.tsx`, `button-group.module.css` — page: https://uiarc.dev/components/button-group
- **Calendar** (`calendar`) — 3 files: `calendar.tsx`, `use-today.ts`, `calendar.module.css` — page: https://uiarc.dev/components/calendar
- **Card** (`card`) — 2 files: `card.tsx`, `card.module.css` — page: https://uiarc.dev/components/card
- **Card stack** (`card-stack`) — 2 files: `card-stack.tsx`, `card-stack.module.css` — page: https://uiarc.dev/components/card-stack
- **Carousel** (`carousel`) — 2 files: `carousel.tsx`, `carousel.module.css` — page: https://uiarc.dev/components/carousel
- **Chat thread** (`chat-thread`) — 2 files: `chat-thread.tsx`, `chat-thread.module.css` — page: https://uiarc.dev/components/chat-thread
- **Checkbox** (`checkbox`) — 2 files: `checkbox.tsx`, `checkbox.module.css` — page: https://uiarc.dev/components/checkbox
- **Chip group** (`chip-group`) — 2 files: `chip-group.tsx`, `chip-group.module.css` — page: https://uiarc.dev/components/chip-group
- **Code block** (`code-block`) — 2 files: `code-block.tsx`, `code-block.module.css` — page: https://uiarc.dev/components/code-block
- **Color picker** (`color-picker`) — 2 files: `color-picker.tsx`, `color-picker.module.css` — page: https://uiarc.dev/components/color-picker
- **Combobox** (`combobox`) — 2 files: `combobox.tsx`, `combobox.module.css` — page: https://uiarc.dev/components/combobox
- **Comment thread** (`comment-thread`) — 2 files: `comment-thread.tsx`, `comment-thread.module.css` — page: https://uiarc.dev/components/comment-thread
- **Confirm morph** (`confirm-morph`) — 2 files: `confirm-morph.tsx`, `confirm-morph.module.css` — page: https://uiarc.dev/components/confirm-morph
- **Context menu** (`context-menu`) — 2 files: `context-menu.tsx`, `context-menu.module.css` — page: https://uiarc.dev/components/context-menu
- **Cookie consent** (`cookie-consent`) — 2 files: `cookie-consent.tsx`, `cookie-consent.module.css` — page: https://uiarc.dev/components/cookie-consent
- **Copy button** (`copy-button`) — 3 files: `copy-button.tsx`, `copy-button.module.css`, `use-copy-feedback.ts` — page: https://uiarc.dev/components/copy-button
- **Countdown** (`countdown`) — 2 files: `countdown.tsx`, `countdown.module.css` — page: https://uiarc.dev/components/countdown
- **Date picker** (`date-picker`) — 2 files: `date-picker.tsx`, `date-picker.module.css` — page: https://uiarc.dev/components/date-picker
- **Date range picker** (`date-range-picker`) — 3 files: `date-range-picker.tsx`, `use-today.ts`, `date-range-picker.module.css` — page: https://uiarc.dev/components/date-range-picker
- **Dialog** (`dialog`) — 2 files: `dialog.tsx`, `dialog.module.css` — page: https://uiarc.dev/components/dialog
- **Donut chart** (`donut-chart`) — 2 files: `donut-chart.tsx`, `donut-chart.module.css` — page: https://uiarc.dev/components/donut-chart
- **Drawer** (`drawer`) — 2 files: `drawer.tsx`, `drawer.module.css` — page: https://uiarc.dev/components/drawer
- **Dropdown menu** (`dropdown-menu`) — 2 files: `dropdown-menu.tsx`, `dropdown-menu.module.css` — page: https://uiarc.dev/components/dropdown-menu
- **Elastic slider** (`elastic-slider`) — 2 files: `elastic-slider.tsx`, `elastic-slider.module.css` — page: https://uiarc.dev/components/elastic-slider
- **Empty state** (`empty-state`) — 2 files: `empty-state.tsx`, `empty-state.module.css` — page: https://uiarc.dev/components/empty-state
- **Expandable card** (`expandable-card`) — 2 files: `expandable-card.tsx`, `expandable-card.module.css` — page: https://uiarc.dev/components/expandable-card
- **Expandable text** (`expandable-text`) — 2 files: `expandable-text.tsx`, `expandable-text.module.css` — page: https://uiarc.dev/components/expandable-text
- **Expanding button group** (`expanding-button-group`) — 2 files: `expanding-button-group.tsx`, `expanding-button-group.module.css` — page: https://uiarc.dev/components/expanding-button-group
- **Expanding search** (`expanding-search`) — 2 files: `expanding-search.tsx`, `expanding-search.module.css` — page: https://uiarc.dev/components/expanding-search
- **File dropzone** (`file-dropzone`) — 2 files: `file-dropzone.tsx`, `file-dropzone.module.css` — page: https://uiarc.dev/components/file-dropzone
- **Filter toolbar** (`filter-toolbar`) — 2 files: `filter-toolbar.tsx`, `filter-toolbar.module.css` — page: https://uiarc.dev/components/filter-toolbar
- **Floating button group** (`floating-button-group`) — 2 files: `floating-button-group.tsx`, `floating-button-group.module.css` — page: https://uiarc.dev/components/floating-button-group
- **Gauge** (`gauge`) — 2 files: `gauge.tsx`, `gauge.module.css` — page: https://uiarc.dev/components/gauge
- **Hold to confirm** (`hold-to-confirm`) — 2 files: `hold-to-confirm.tsx`, `hold-to-confirm.module.css` — page: https://uiarc.dev/components/hold-to-confirm
- **Hover card** (`hover-card`) — 2 files: `hover-card.tsx`, `hover-card.module.css` — page: https://uiarc.dev/components/hover-card
- **Icon morph** (`icon-morph`) — 2 files: `icon-morph.tsx`, `icon-morph.module.css` — page: https://uiarc.dev/components/icon-morph
- **Image compare** (`image-compare`) — 2 files: `image-compare.tsx`, `image-compare.module.css` — page: https://uiarc.dev/components/image-compare
- **In-view title** (`in-view-title`) — 2 files: `in-view-title.tsx`, `in-view-title.module.css` — page: https://uiarc.dev/components/in-view-title
- **Inline edit** (`inline-edit`) — 2 files: `inline-edit.tsx`, `inline-edit.module.css` — page: https://uiarc.dev/components/inline-edit
- **Input** (`input`) — 2 files: `input.tsx`, `input.module.css` — page: https://uiarc.dev/components/input
- **JSON viewer** (`json-viewer`) — 2 files: `json-viewer.tsx`, `json-viewer.module.css` — page: https://uiarc.dev/components/json-viewer
- **Line chart** (`line-chart`) — 2 files: `line-chart.tsx`, `line-chart.module.css` — page: https://uiarc.dev/components/line-chart
- **Mention input** (`mention-input`) — 2 files: `mention-input.tsx`, `mention-input.module.css` — page: https://uiarc.dev/components/mention-input
- **Metric card** (`metric-card`) — 2 files: `metric-card.tsx`, `metric-card.module.css` — page: https://uiarc.dev/components/metric-card
- **Money input** (`money-input`) — 2 files: `money-input.tsx`, `money-input.module.css` — page: https://uiarc.dev/components/money-input
- **Morph select** (`morph-select`) — 2 files: `morph-select.tsx`, `morph-select.module.css` — page: https://uiarc.dev/components/morph-select
- **Multi-select** (`multi-select`) — 2 files: `multi-select.tsx`, `multi-select.module.css` — page: https://uiarc.dev/components/multi-select
- **Number field** (`number-field`) — 2 files: `number-field.tsx`, `number-field.module.css` — page: https://uiarc.dev/components/number-field
- **Onboarding checklist** (`onboarding-checklist`) — 2 files: `onboarding-checklist.tsx`, `onboarding-checklist.module.css` — page: https://uiarc.dev/components/onboarding-checklist
- **Pagination** (`pagination`) — 2 files: `pagination.tsx`, `pagination.module.css` — page: https://uiarc.dev/components/pagination
- **Password field** (`password-field`) — 2 files: `password-field.tsx`, `password-field.module.css` — page: https://uiarc.dev/components/password-field
- **Password strength** (`password-strength`) — 2 files: `password-strength.tsx`, `password-strength.module.css` — page: https://uiarc.dev/components/password-strength
- **Phone input** (`phone-input`) — 2 files: `phone-input.tsx`, `phone-input.module.css` — page: https://uiarc.dev/components/phone-input
- **Popover** (`popover`) — 2 files: `popover.tsx`, `popover.module.css` — page: https://uiarc.dev/components/popover
- **Progress** (`progress`) — 2 files: `progress.tsx`, `progress.module.css` — page: https://uiarc.dev/components/progress
- **Radio cards** (`radio-cards`) — 2 files: `radio-cards.tsx`, `radio-cards.module.css` — page: https://uiarc.dev/components/radio-cards
- **Radio group** (`radio-group`) — 2 files: `radio-group.tsx`, `radio-group.module.css` — page: https://uiarc.dev/components/radio-group
- **Range histogram slider** (`range-histogram-slider`) — 2 files: `range-histogram-slider.tsx`, `range-histogram-slider.module.css` — page: https://uiarc.dev/components/range-histogram-slider
- **Rating** (`rating`) — 2 files: `rating.tsx`, `rating.module.css` — page: https://uiarc.dev/components/rating
- **Reactions** (`reactions`) — 2 files: `reactions.tsx`, `reactions.module.css` — page: https://uiarc.dev/components/reactions
- **Reorderable list** (`reorderable-list`) — 2 files: `reorderable-list.tsx`, `reorderable-list.module.css` — page: https://uiarc.dev/components/reorderable-list
- **Resizable panels** (`resizable-panels`) — 2 files: `resizable-panels.tsx`, `resizable-panels.module.css` — page: https://uiarc.dev/components/resizable-panels
- **Rich text editor** (`rich-text-editor`) — 2 files: `rich-text-editor.tsx`, `rich-text-editor.module.css` — page: https://uiarc.dev/components/rich-text-editor
- **Ridgeline** (`ridgeline`) — 2 files: `ridgeline.tsx`, `ridgeline.module.css` — page: https://uiarc.dev/components/ridgeline
- **Ruler slider** (`ruler-slider`) — 2 files: `ruler-slider.tsx`, `ruler-slider.module.css` — page: https://uiarc.dev/components/ruler-slider
- **Scroll area** (`scroll-area`) — 2 files: `scroll-area.tsx`, `scroll-area.module.css` — page: https://uiarc.dev/components/scroll-area
- **Scrub input** (`scrub-input`) — 2 files: `scrub-input.tsx`, `scrub-input.module.css` — page: https://uiarc.dev/components/scrub-input
- **Search field** (`search-field`) — 2 files: `search-field.tsx`, `search-field.module.css` — page: https://uiarc.dev/components/search-field
- **Segmented control** (`segmented-control`) — 2 files: `segmented-control.tsx`, `segmented-control.module.css` — page: https://uiarc.dev/components/segmented-control
- **Select** (`select`) — 2 files: `select.tsx`, `select.module.css` — page: https://uiarc.dev/components/select
- **Shortcut recorder** (`shortcut-recorder`) — 2 files: `shortcut-recorder.tsx`, `shortcut-recorder.module.css` — page: https://uiarc.dev/components/shortcut-recorder
- **Signature pad** (`signature-pad`) — 2 files: `signature-pad.tsx`, `signature-pad.module.css` — page: https://uiarc.dev/components/signature-pad
- **Skeleton** (`skeleton`) — 2 files: `skeleton.tsx`, `skeleton.module.css` — page: https://uiarc.dev/components/skeleton
- **Slider** (`slider`) — 2 files: `slider.tsx`, `slider.module.css` — page: https://uiarc.dev/components/slider
- **Slope chart** (`slope-chart`) — 2 files: `slope-chart.tsx`, `slope-chart.module.css` — page: https://uiarc.dev/components/slope-chart
- **Slot text** (`slot-text`) — 2 files: `slot-text.tsx`, `slot-text.module.css` — page: https://uiarc.dev/components/slot-text
- **Sortable data table** (`sortable-data-table`) — 2 files: `sortable-data-table.tsx`, `sortable-data-table.module.css` — page: https://uiarc.dev/components/sortable-data-table
- **Sparkline** (`sparkline`) — 2 files: `sparkline.tsx`, `sparkline.module.css` — page: https://uiarc.dev/components/sparkline
- **Split button** (`split-button`) — 2 files: `split-button.tsx`, `split-button.module.css` — page: https://uiarc.dev/components/split-button
- **Stepper** (`stepper`) — 2 files: `stepper.tsx`, `stepper.module.css` — page: https://uiarc.dev/components/stepper
- **Streamgraph** (`streamgraph`) — 2 files: `streamgraph.tsx`, `streamgraph.module.css` — page: https://uiarc.dev/components/streamgraph
- **Swipe actions** (`swipe-actions`) — 2 files: `swipe-actions.tsx`, `swipe-actions.module.css` — page: https://uiarc.dev/components/swipe-actions
- **Switch** (`switch`) — 2 files: `switch.tsx`, `switch.module.css` — page: https://uiarc.dev/components/switch
- **Tabs** (`tabs`) — 2 files: `tabs.tsx`, `tabs.module.css` — page: https://uiarc.dev/components/tabs
- **Tag input** (`tag-input`) — 2 files: `tag-input.tsx`, `tag-input.module.css` — page: https://uiarc.dev/components/tag-input
- **Text morph** (`text-morph`) — 2 files: `text-morph.tsx`, `text-morph.module.css` — page: https://uiarc.dev/components/text-morph
- **Text reveal** (`text-reveal`) — 2 files: `text-reveal.tsx`, `text-reveal.module.css` — page: https://uiarc.dev/components/text-reveal
- **Text shimmer** (`text-shimmer`) — 2 files: `text-shimmer.tsx`, `text-shimmer.module.css` — page: https://uiarc.dev/components/text-shimmer
- **Textarea** (`textarea`) — 2 files: `textarea.tsx`, `textarea.module.css` — page: https://uiarc.dev/components/textarea
- **Theme switcher** (`theme-switch`) — 2 files: `theme-switch.tsx`, `theme-switch.module.css` — page: https://uiarc.dev/components/theme-switch
- **Eclipse** (`theme-switch-eclipse`) — 2 files: `theme-switch.tsx`, `theme-switch.module.css` — page: https://uiarc.dev/components/theme-switch-eclipse
- **Rise** (`theme-switch-rise`) — 2 files: `theme-switch.tsx`, `theme-switch.module.css` — page: https://uiarc.dev/components/theme-switch-rise
- **Split** (`theme-switch-split`) — 2 files: `theme-switch.tsx`, `theme-switch.module.css` — page: https://uiarc.dev/components/theme-switch-split
- **Time picker** (`time-picker`) — 2 files: `time-picker.tsx`, `time-picker.module.css` — page: https://uiarc.dev/components/time-picker
- **Timeline** (`timeline`) — 2 files: `timeline.tsx`, `timeline.module.css` — page: https://uiarc.dev/components/timeline
- **Toast** (`toast`) — 2 files: `toast.tsx`, `toast.module.css` — page: https://uiarc.dev/components/toast
- **Toast stack** (`toast-stack`) — 2 files: `toast-stack.tsx`, `toast-stack.module.css` — page: https://uiarc.dev/components/toast-stack
- **Toggle group** (`toggle-group`) — 2 files: `toggle-group.tsx`, `toggle-group.module.css` — page: https://uiarc.dev/components/toggle-group
- **Tooltip** (`tooltip`) — 2 files: `tooltip.tsx`, `tooltip.module.css` — page: https://uiarc.dev/components/tooltip
- **Tree table** (`tree-table`) — 2 files: `tree-table.tsx`, `tree-table.module.css` — page: https://uiarc.dev/components/tree-table
- **Tree view** (`tree-view`) — 2 files: `tree-view.tsx`, `tree-view.module.css` — page: https://uiarc.dev/components/tree-view
- **Treemap** (`treemap`) — 2 files: `treemap.tsx`, `treemap.module.css` — page: https://uiarc.dev/components/treemap
- **Usage meter** (`usage-meter`) — 2 files: `usage-meter.tsx`, `usage-meter.module.css` — page: https://uiarc.dev/components/usage-meter
- **User menu** (`user-menu`) — 2 files: `user-menu.tsx`, `user-menu.module.css` — page: https://uiarc.dev/components/user-menu
- **Waffle chart** (`waffle-chart`) — 2 files: `waffle-chart.tsx`, `waffle-chart.module.css` — page: https://uiarc.dev/components/waffle-chart

## Blocks (free) — 22

- **Blog grid** (`blog-grid`) — 3 files: `blog-grid.tsx`, `blog-grid-data.ts`, `blog-grid.module.css` — page: https://uiarc.dev/components/blocks/blog-grid
- **Changelog feed** (`changelog-feed`) — 3 files: `changelog-feed.tsx`, `changelog-feed.module.css`, `media.ts` — page: https://uiarc.dev/components/blocks/changelog-feed
- **Command palette** (`command-palette`) — 2 files: `command-palette.tsx`, `command-palette.module.css` — page: https://uiarc.dev/components/blocks/command-palette
- **Comparison table** (`comparison-table`) — 3 files: `comparison-table.tsx`, `comparison-table-data.ts`, `comparison-table.module.css` — page: https://uiarc.dev/components/blocks/comparison-table
- **Contact section** (`contact-section`) — 3 files: `contact-section.tsx`, `contact-section.module.css`, `media.ts` — page: https://uiarc.dev/components/blocks/contact-section
- **CTA section** (`cta-section`) — 4 files: `cta-section.tsx`, `cta-section-data.ts`, `media.ts`, `cta-section.module.css` — page: https://uiarc.dev/components/blocks/cta-section
- **Empty states** (`empty-states`) — 3 files: `empty-states.tsx`, `empty-states.module.css`, `empty-states-art.ts` — page: https://uiarc.dev/components/blocks/empty-states
- **FAQ section** (`faq-section`) — 2 files: `faq-section.tsx`, `faq-section.module.css` — page: https://uiarc.dev/components/blocks/faq-section
- **File upload** (`file-upload`) — 2 files: `file-upload.tsx`, `file-upload.module.css` — page: https://uiarc.dev/components/blocks/file-upload
- **Hero section** (`hero-section`) — 15 files: `hero-section.tsx`, `hero-section.module.css`, `hero-content.tsx`, `hero-content.module.css`, `hero-motion.ts`, `hero-mesh.tsx`, `hero-mesh.module.css`, `hero-cadence.tsx`, `hero-cadence.module.css`, `hero-relay.tsx`, `hero-relay.module.css`, `hero-lumen.tsx`, `hero-lumen.module.css`, `hero-lumen-data.ts`, `media.ts` — page: https://uiarc.dev/components/blocks/hero-section
- **Centered login** (`login-centered`) — 2 files: `login-centered.tsx`, `login-centered.module.css` — page: https://uiarc.dev/components/blocks/login-centered
- **Logo marquee** (`logo-marquee`) — 2 files: `logo-marquee.tsx`, `logo-marquee.module.css` — page: https://uiarc.dev/components/blocks/logo-marquee
- **Newsletter signup** (`newsletter-signup`) — 4 files: `newsletter-signup.tsx`, `newsletter-signup-data.ts`, `media.ts`, `newsletter-signup.module.css` — page: https://uiarc.dev/components/blocks/newsletter-signup
- **Notification center** (`notification-center`) — 2 files: `notification-center.tsx`, `notification-center.module.css` — page: https://uiarc.dev/components/blocks/notification-center
- **OTP input** (`otp-input`) — 2 files: `otp-input.tsx`, `otp-input.module.css` — page: https://uiarc.dev/components/blocks/otp-input
- **Page header** (`page-header`) — 3 files: `page-header.tsx`, `use-copy-feedback.ts`, `page-header.module.css` — page: https://uiarc.dev/components/blocks/page-header
- **Plan comparison** (`plan-comparison`) — 2 files: `plan-comparison.tsx`, `plan-comparison.module.css` — page: https://uiarc.dev/components/blocks/plan-comparison
- **Sign in** (`sign-in`) — 3 files: `sign-in.tsx`, `sign-in.module.css`, `media.ts` — page: https://uiarc.dev/components/blocks/sign-in
- **Sign up form** (`signup-form`) — 2 files: `signup-form.tsx`, `signup-form.module.css` — page: https://uiarc.dev/components/blocks/signup-form
- **Site footer** (`site-footer`) — 2 files: `site-footer.tsx`, `site-footer.module.css` — page: https://uiarc.dev/components/blocks/site-footer
- **Site header** (`site-header`) — 3 files: `site-header.tsx`, `site-header.module.css`, `media.ts` — page: https://uiarc.dev/components/blocks/site-header
- **Stats band** (`stats-band`) — 4 files: `stats-band.tsx`, `stats-band-data.ts`, `stats-band.module.css`, `stats-band-world.ts` — page: https://uiarc.dev/components/blocks/stats-band

## Shared (required by the items above) — 3

- **Arc foundation** (`arc-foundation`) — 1 files: `foundation.css` — page: https://uiarc.dev
- **Arc motion tokens** (`arc-motion-tokens`) — 2 files: `motion-tokens.ts`, `motion-tokens.ts` — page: https://uiarc.dev
- **Arc agent skill** (`arc-skill`) — 13 files: `SKILL.md`, `INSTRUCTIONS.md`, `accessibility.md`, `checklist.md`, `components.md`, `composition.md`, `copy.md`, `design.md`, `example-dashboard.md`, `example-pricing.md`, `example-settings.md`, `motion.md`, `responsive.md` — page: https://uiarc.dev
