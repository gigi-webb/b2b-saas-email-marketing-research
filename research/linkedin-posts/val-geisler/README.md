# LinkedIn Posts — Val Geisler

**LinkedIn:** https://www.linkedin.com/in/lovevalgeisler/  
**Followers:** ~9,857 (as of June 2026)  
**Last verified active:** June 19, 2026  
**Collection status:** Not yet collected — use scraper or manual review

---

## What to Collect

Val posts actively on LinkedIn (verified active June 19, 2026). Priority content categories:

### High priority
- **Subject line teardowns** — Val has been posting in-depth breakdowns of real email subject lines, analyzing what works and why. Look for posts with subject line screenshots.
- **Retention email frameworks** — Posts referencing the Vampire/Ghost/Zombie customer framework, dinner party strategy, or win-back campaign structures.
- **Onboarding sequence critiques** — Val critiques real onboarding flows, which directly maps to the SaaS lifecycle email research.
- **"Flip the script" copy examples** — Posts on changing "we built this" to "you asked for this" in product emails.

### Medium priority
- Posts referencing her work at Klaviyo or Digioh
- Customer interview methodology posts (incentivizing feedback, Starbucks gift card examples)
- Churn reduction and MRR impact posts

### Skip
- Generic motivational content
- Personal life posts with no email/retention angle
- Reposts of other people's content without Val's commentary

---

## Collection Method

**Option 1: Automated** — Run the LinkedIn scraper:
```bash
cd /path/to/repo
export LI_AT="your_cookie_value"
python scripts/scrape_linkedin_posts.py --expert val-geisler
```

**Option 2: Manual** — Visit https://www.linkedin.com/in/lovevalgeisler/recent-activity/all/ and save posts manually. Format each post as `post-001.md`, `post-002.md` etc. using the template below.

---

## File Naming Convention

`post-NNN.md` where NNN is a zero-padded sequence number (001, 002 ...).

## Post Template

```markdown
# Post NNN — Val Geisler

**Date:** [date visible on LinkedIn, e.g. "2026-06-15" or "about 3 weeks ago"]
**Source:** [LinkedIn post URL if available]
**Scraped:** [ISO timestamp]

---

## Content

[Full post text, preserving line breaks]

---

## Research Notes

- [ ] Key claim or tactic identified:
- [ ] Relevant to email strategy? Yes / No / Partial
- [ ] Connects to transcript insight: [reference if applicable]
- [ ] Follow-up action:
```

---

## Context for Research Use

Val's LinkedIn posts often expand on concepts from her YouTube talks. The key lens for this research is her **retention email methodology**: she has documented specific email types (ghost re-engagement, zombie win-back, subscription upgrade nudge) with real-world examples from SaaS and e-commerce brands. Her LinkedIn posts tend to be more current and specific than her older video content.

Cross-reference her posts against the transcripts in:
- `/research/youtube-transcripts/val-geisler/better-email-marketing-customer-retention.md`
- `/research/youtube-transcripts/val-geisler/retention-email-tactics-and-strategies.md`
