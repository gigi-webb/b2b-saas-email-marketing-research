# Brennan Dunn — Behavioral Segmentation Framework

**Source:** research/youtube-transcripts/brennan-dunn/mastering-email-marketing-brennan-dunn.md  
**Expert:** Brennan Dunn, Founder of RightMessage and Palladio

---

## Core Philosophy

Demographic segmentation (company size, industry, job title) tells you who someone is. Behavioral segmentation tells you what they're actually doing — and action is the only reliable signal of intent. Brennan's framework is built on a single observation: every email is technically a unique, individually generated document. Unlike a social post seen by thousands simultaneously, an email to you and an email to someone else are two separate objects that can be completely different. This makes email the only channel where true 1:1 personalization is technically possible — but almost no one exploits it, because they're still treating email as a broadcast medium.

---

## The Framework

### Step 1 — Map Behavioral Signals

Identify the actions in your product and on your website that indicate intent, readiness, or lifecycle stage. These signals fall into two categories:

**High-intent product signals:**
- Pages visited (pricing page, upgrade page, billing page)
- Features activated (onboarding steps completed, key feature first use)
- Inaction signals (logged in but never triggered feature X; visited billing page twice in 30 days without upgrading)
- Subscription/billing events (trial started, trial expiring, downgraded, cancelled)

**Relationship signals:**
- Email engagement history (last opened, last clicked, number of opens in 30 days)
- Survey or quiz responses collected via email
- Support ticket topics submitted
- Content consumed (which blog posts, which video series, which use case pages)

### Step 2 — Build Behavioral Segments (Not Lists)

A segment is a dynamic, rule-based group — not a static list. The distinction matters: a static list reflects who someone was when it was built; a dynamic segment reflects who they are right now.

Rules for healthy segments:
- Segment by the most recent meaningful action, not the oldest tag
- A subscriber should be in exactly one segment per automation track at any given time (avoid conflicting triggers)
- Build segments at the intersection of multiple signals for higher precision (e.g., "visited pricing page AND has been a trial user for 7+ days AND has NOT activated the core feature")

### Step 3 — Connect Website and Email to the Same Behavioral Layer

This is the step most teams skip. Email platforms and websites typically run on separate data models. Behavioral personalization at scale requires both to share the same profile:

- **RightMessage pattern:** JavaScript embed on the website reads the subscriber's email platform profile (segments, tags, field values) in real time → renders personalised on-site content (CTAs, headlines, testimonials matched to the visitor's segment) → writes new behavioral signals back to the email platform as subscribers take actions on the site
- **Result:** Website and email reinforce the same narrative for the same subscriber. A subscriber tagged as "small team, feature X user" sees different homepage copy, different upgrade CTA, and different email sequence than a "solo founder, not yet activated" subscriber

### Step 4 — Personalise the Email Content

With behavioral segments defined and website/email data unified, email personalization is a templating problem:

1. Write the "default" version of the email for the largest or most generic segment
2. Add conditional blocks: IF [segment = trial_user_feature_activated] THEN show block A ELSE show block B
3. Use merge tags for: first name, company name, feature they've used, plan they're on, days remaining in trial
4. The subject line can also be conditional — most ESPs support dynamic subject line content

The output: subscribers receive emails that reference their actual situation rather than a fictional average user.

### Step 5 — The Personalization Flywheel

Each email interaction produces new behavioral data → which refines segments → which improves the next email's relevance → which increases engagement → which produces more behavioral data. The flywheel compounds over months. The VIGEO case study (Megan's fitness business, documented in Brennan's LinkedIn posts) showed this over 3+ years: 850% increase in average customer value, 2,067% revenue growth, 789% subscriber growth — all attributed to the behavioral personalization layer.

---

## Key Quote from Transcript

> "I can personalize these emails because they're all effectively individual entities, right? Like the email I sent to you versus the email sent to Justin are two separate generated beings that have no relation to each other. So assuming you've got an email platform that's processing these emails being sent, you can do kind of cool stuff and, you know, make these emails a little more dynamic based on who's receiving it."

---

## Application for B2B SaaS

**The minimal viable behavioral segmentation system (for teams starting from scratch):**

1. **Identify three lifecycle segments** — New (signed up in last 14 days), Active (logged in in last 30 days, completed core activation), At-Risk (no login in 30+ days). Build one dedicated email sequence per segment. This alone separates you from 80% of B2B SaaS email programs.

2. **Add one behavioral trigger** — The single highest-value behavioral trigger in most B2B SaaS products is "trial user who completed [core activation step]." Build a specific email that fires within 24 hours of that trigger, acknowledging the milestone and pointing to the next high-value action. Conversion rates from this single email typically exceed any batch campaign.

3. **Connect your product database to your email platform** — Even a simple nightly CSV sync of key user attributes (plan, features activated, days since last login) into your ESP unlocks conditional email content. Most modern ESPs (Customer.io, Klaviyo) have native integrations with product analytics tools (Segment, Snowflake) that make this a configuration task, not an engineering project.

4. **Build a pricing page visitor segment** — Any trial user who visits your pricing page but does not upgrade is expressing intent. Build an automation that fires a personalised "I saw you were looking at our plans" email within 2 hours. This is the SaaS equivalent of a cart abandonment email and typically converts at 3–5x the rate of a generic nurture email.

5. **Long-term: unify website and email** — Once email behavioral segmentation is working, implement website personalisation that reads the same segments. A trial user who visits your homepage for the third time should see a "continue where you left off" CTA, not a generic "start your free trial" hero.
