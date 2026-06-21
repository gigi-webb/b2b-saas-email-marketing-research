# Email Marketing Tools Stack

Tools mentioned across the 14 YouTube transcripts and LinkedIn posts collected in this research. Organized by category.

**Last updated:** June 21, 2026  
**Source transcripts:** research/youtube-transcripts/ (all 14 files)

---

## Email Service Providers (ESPs)

### 1. Klaviyo
**What it does:** Data-centric email and SMS platform for e-commerce and DTC brands. Strong behavioral segmentation, predictive analytics, and deep Shopify integration. Also used by B2B SaaS companies for lifecycle automation.  
**Who mentioned it:** Val Geisler (worked there as Customer Evangelist; used extensively with clients at Fix My Churn and as a consultant)  
**Key insight:** Val describes Klaviyo as "really a data tool but largely used for email marketing" — its value is in the behavioral data layer, not just the send infrastructure. Segmenting ghost/zombie customer types inside Klaviyo was central to her retention framework.

### 2. Customer.io
**What it does:** Behavioral messaging platform designed for SaaS and product-driven companies. Triggers emails and in-app messages based on user actions (events) sent from the product via API. Best-in-class for lifecycle automation tied to product signals.  
**Who mentioned it:** Val Geisler (SaaS client work; example of a "you told us you needed this feature, we built it" email); Brennan Dunn (Vigeo case study: 400K+ Customer.io subscribers after behavioral personalization)  
**Key insight:** Customer.io is the ESP of choice when email must reflect real-time product behavior. Unlike Klaviyo (optimized for e-commerce events), Customer.io is built for SaaS event streams (trial started, feature activated, billing page visited).

### 3. ConvertKit / Kit
**What it does:** Creator-focused email platform with strong automation and subscriber tagging. Widely used by newsletter operators, course creators, and indie SaaS founders.  
**Who mentioned it:** Val Geisler (example of a product update email from ConvertKit used in her retention framework); Brennan Dunn (built the email marketing workshop specifically for ConvertKit's audience and community)  
**Key insight:** The ConvertKit example Val referenced illustrated the "flip the script" opportunity — their product update email said "we built this" when it could have said "you asked for this and we built it for you."

### 4. Substack
**What it does:** Newsletter platform combining publishing, subscriptions, payments, and recommendations network. Creator-native. Notable for its cross-recommendation feature that drives subscriber growth between newsletters.  
**Who mentioned it:** Emily Kramer (primary platform for MKT1, 75K+ subscribers; 30–40% of growth from Substack recommendations feature); Katelyn Bourgoin (referenced for newsletter growth research)  
**Key insight:** Emily's strongest critique: no API, no MCP server, and poor customer support. The recommendations network is its dominant moat — she won't leave until comparable network effects exist elsewhere. She calls it "the best product that has the worst customer support."

### 5. Beehiiv
**What it does:** Newsletter platform with built-in monetization (sponsorship network, paid subscriptions), growth tools (referral programme, paid recommendations), and analytics. Positioned as the operator-focused alternative to Substack.  
**Who mentioned it:** Kyle Poyar (moved Growth Unhinged newsletter from Substack to Beehiiv); Emily Kramer (seriously considering the move, waiting to see if Substack catches up on API/MCP); Matt McGarry (newsletter growth consultant who recommends it for creators focused on paid acquisition)  
**Key insight:** The Substack → Beehiiv migration pattern among serious newsletter operators is a signal worth tracking. Kyle Poyar went first; Emily Kramer is watching carefully. The deciding factor is not features but network effects.

---

## Email Design & Production

### 6. Beefree (formerly BEE Free)
**What it does:** Drag-and-drop email design tool with 2,000+ templates. Now includes an AI assistant for copy generation and has acquired Really Good Emails (15,000+ curated email design examples). Used by in-house teams and agencies.  
**Who mentioned it:** Kath Pay (used Beefree's AI assistant for her behavioral science email copy workshop; all three live examples were built inside Beefree)  
**Key insight:** Kath used Beefree's AI assistant to demonstrate prompting for persuasion-principle-driven email copy (Cialdini's six principles). The "apply" button within Beefree lets users regenerate and apply AI copy directly to the email template without copy-pasting.

### 7. Really Good Emails
**What it does:** Curated database of 15,000+ real email design examples, searchable by category (retention, win-back, onboarding, transactional, etc.). Industry standard swipe file resource. Acquired by Holistic Email Marketing/Beefree in 2024.  
**Who mentioned it:** Val Geisler (recommended for finding retention email examples; advised listeners to subscribe to brands and experience their retention flows directly); Kath Pay (acquisition announcement in transcript)  
**Key insight:** Val's advice was to subscribe to brands whose retention emails you want to study — not just browse the site — because you need to experience the full sequence in context. Really Good Emails shows individual emails; buying the product shows the sequence.

---

## Behavioral Personalization & Data

### 8. RightMessage
**What it does:** Behavioral personalization platform that connects email subscriber data to website experience. Reads a visitor's email platform segment/tags and uses them to personalize on-site copy, CTAs, and content blocks in real time. Also writes behavioral signals back to the email platform.  
**Who mentioned it:** Brennan Dunn (founder; built it to solve the email+website personalization gap he saw with consulting clients)  
**Key insight:** RightMessage is the only tool in this stack specifically designed to unify website behavior and email personalization into a single behavioral data layer. The VIGEO case study (850% customer value increase) documented the compounding effect of this approach over 3+ years.

---

## Workflow, Data Pipeline & AI

### 9. Claude (Anthropic)
**What it does:** Large language model used across multiple workflows: email copywriting, newsjacking brief generation, A/B test hypothesis writing, subject line optimization, newsletter editing, research analysis, and as the core of MCP-connected email operation systems.  
**Who mentioned it:** Tyler (Dave Gerhardt session — built a 5-step newsjacking system using Claude to monitor Google Alerts, generate email briefs, and produce copy in < 1 hour); Emily Kramer (uses Claude Code for newsletter production, Figma MCP for diagrams, skills for copy editing); Kath Pay (recommends training a private Claude instance on your email expertise; uses it for persuasion-principle copy generation); Brennan Dunn (customers using RightMessage MCP from Claude window); Kyle Poyar (4-layer AI GTM context system built on Claude)  
**Key insight:** Claude is the emerging operating system for advanced email teams — not as a writing assistant but as a workflow engine connected to ESPs, CRMs, and analytics via MCP. Teams that build context systems (foundational .md files + skills + orchestration) will operate faster than teams that prompt from scratch.

### 10. Help Scout
**What it does:** Shared inbox and customer support tool. Used by newsletter operators to route all subscriber replies to a monitored, team-accessible inbox with tagging and conversation history.  
**Who mentioned it:** Jana (Knack, Dave Gerhardt session — used Help Scout to route all newsletter replies to hello@lutmos.com, tagged by issue number, enabling manual reply-rate tracking)  
**Key insight:** Most ESPs do not natively track reply rate (replies go to a monitored email address, not back into the platform). Help Scout or Front are the practical solution — routing newsletter replies to a shared inbox allows the team to count replies by issue, identify high-engagement topics, and respond to readers personally.

---

## Honourable Mentions (Referenced but Not Primary Focus)

| Tool | Context | Who mentioned |
|---|---|---|
| Snowflake | Data warehouse used for year-in-review campaign SQL queries | Ben (Dave Gerhardt session) |
| Census / Pipetrain | Data sync from warehouse to Customer.io for personalization | Ben (Dave Gerhardt session) |
| QuickChart | Chart.js API used to generate personalised data visualizations in email | Ben (Dave Gerhardt session) |
| Google Alerts | Free news monitoring for newsjacking email triggers | Tyler (Dave Gerhardt session) |
| Figma | Design tool; Emily Kramer uses it with MCP server for newsletter diagrams | Emily Kramer |
| SparkLoop | Newsletter referral and paid recommendation network | Matt McGarry (LinkedIn context) |
| Knack | Email + landing page platform with built-in AI and MCP server | Dave Gerhardt session (sponsor) |

---

*Related:* See research/frameworks/ for how several of these tools are used within specific practitioner frameworks.
