# B2B SaaS Newsletter & Email Marketing Research

**Topic:** Newsletter / Email Marketing for B2B SaaS
**Stage:** 100Hires Junior Growth Marketing Specialist — Round 2
**Researcher:** Thi Vu
**Deadline:** June 23, 2026

---

## Why This Topic

Email is the only marketing channel B2B SaaS companies
fully own. No algorithm changes. No platform risk.
No ad spend required to reach your own list.

For SaaS businesses, email directly impacts the two
metrics that determine company valuation:
- Activation rate (trial to paid)
- Retention rate (churn prevention)

A 5% improvement in retention increases SaaS valuation
by 25-95% (Bain and Company). Email is the primary lever
for both metrics — yet most B2B SaaS companies treat it
as a broadcast channel instead of a relationship system.

This repository documents the research process of building
a knowledge base that could become an operational email
marketing playbook.

---

## Research Scope

- 23 experts evaluated, 10 selected, 13 rejected with reasoning
- 19 YouTube video IDs collected, 14 transcripts fetched via API
- LinkedIn posts collected per expert
- 8 patterns identified across all sources
- 5 contradictions analyzed with evidence
- Draft playbook built from research synthesis

---

## Expert Selection Standard

**Selected if ALL true:**
- Directly operated email programs at B2B SaaS companies
- Publishes specific numbers, frameworks, or teardowns
- Active content output within last 6 months
- Cited or recommended by other practitioners

**Rejected if ANY true:**
- Generic influencer without SaaS operator experience
- Theory-heavy without hands-on execution results
- Inactive for 6+ months

Full rejection audit: /research/rejected-experts.md

---

## Selected Experts

| # | Expert | Company | Focus |
|---|--------|---------|-------|
| 01 | Val Geisler | Independent (fmr. Klaviyo) | Retention Email |
| 02 | Brennan Dunn | RightMessage | Email Personalization |
| 03 | Kath Pay | Holistic Email Marketing | Email Strategy |
| 04 | Emily Kramer | MKT1 | Newsletter Strategy |
| 05 | Matt McGarry | GrowLetter | Newsletter Growth |
| 06 | Katelyn Bourgoin | UNIGNORABLE | Buyer Psychology |
| 07 | Kyle Poyar | Growth Unhinged | PLG and SaaS GTM |
| 08 | Dave Gerhardt | Exit Five | Founder-led Email |
| 09 | Gaetano DiNardi | Independent | SEO-to-Email Funnel |
| 10 | Peep Laja | Wynter / CXL | B2B Message Testing |

Full profiles with verification data: /research/sources.md

---

## Technical Architecture

**YouTube Transcript Collection:**
- Script: scripts/fetch_youtube_transcripts.js
- Package: youtube-transcript (npm)
- Videos processed: 19 video IDs across 8 experts
- Transcripts successfully fetched: 14
- Skipped: 4 (subtitles disabled, handled gracefully)

Run the script:

npm install youtube-transcript
node scripts/fetch_youtube_transcripts.js

**LinkedIn Posts:**
- Collected per expert
- Stored in /research/linkedin-posts/[expert-name]/

---

## Key Findings

**Finding 01 — Email is the only owned channel**
Dave Gerhardt, Exit Five: "Email is still one of the last
channels where you can truly own your audience."
Consistent across 6 of 8 experts researched.

**Finding 02 — Write to one person, not a list**
The highest-performing B2B SaaS newsletters treat each
send as a one-on-one conversation. Dave Gerhardt and
Gaetano DiNardi both structure newsletters with a
personal note section before any promotional content.

**Finding 03 — Email lurkers are buyers in disguise**
A brand tracked email opens against purchase history.
Found that email opens in the 10 weeks before purchase
predicted conversion even without link clicks.
Reply rate and influenced pipeline are better metrics
than open rate or CTR alone.

**Finding 04 — Deliverability is a strategy problem**
Kath Pay case study: a SaaS company had chronic
deliverability problems from emailing 5-year-old
free trial users who never converted. Fix was not
technical. It was strategic: stop emailing people
who are not interested.

**Finding 05 — AI helps execution, not strategy**
Kath Pay: AI trained on generic web content produces
regurgitated advice. AI trained on proprietary
frameworks accelerates execution without diluting
strategic thinking.

---

## Repository Structure

b2b-saas-email-marketing-research/
│
├── README.md
│
├── research/
│   ├── sources.md                   10 verified expert profiles
│   ├── rejected-experts.md          13 rejected with reasoning
│   ├── linkedin-posts/              Posts organized by expert
│   ├── youtube-transcripts/         14 transcripts fetched via API
│   └── other/
│
├── insights/
│   ├── patterns.md                  8 patterns across experts
│   ├── contradictions.md            5 tensions identified
│   └── emerging-trends.md
│
├── playbooks/
│   └── email-playbook-draft.md      Draft v0.1
│
├── scripts/
│   ├── fetch_youtube_transcripts.js
│   └── scrape_linkedin_posts.py
│
└── project-context/
    └── repository-structure.md

---

## Playbook Status

Draft v0.1 complete: /playbooks/email-playbook-draft.md

Covers:
- Newsletter structure and cadence (from Dave Gerhardt evidence)
- SaaS onboarding email sequence Day 0 to Day 21 (Val Geisler)
- Re-engagement sequence for inactive subscribers (Kath Pay)
- Lifecycle email map across 6 user stages

---

## What This Repository Demonstrates

This is not a data dump.

It is a structured knowledge base built to answer one question:
What do the best B2B SaaS email marketing practitioners
actually do, and how can those practices be systematized
into a repeatable playbook?

The research process:
1. Evaluated 23 experts, selected 10 by strict criteria
2. Automated content collection via YouTube Transcript API
3. Extracted patterns and contradictions from real transcript data
4. Synthesized findings into actionable frameworks
5. Built a draft playbook ready for operational use

The result is a foundation strong enough to inform real
email marketing decisions at a B2B SaaS company.