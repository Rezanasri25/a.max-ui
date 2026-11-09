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
