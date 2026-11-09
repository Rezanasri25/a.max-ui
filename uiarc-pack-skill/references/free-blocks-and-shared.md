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
