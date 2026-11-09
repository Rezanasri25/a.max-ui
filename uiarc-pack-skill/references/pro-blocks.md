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
