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
