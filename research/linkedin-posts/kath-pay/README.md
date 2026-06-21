# LinkedIn Posts — Kath Pay

**LinkedIn:** https://www.linkedin.com/in/kathpay/  
**Followers:** ~11,111 (as of June 2026)  
**Last verified active:** June 19, 2026  
**Collection status:** Not yet collected — use scraper or manual review

---

## What to Collect

Kath is one of the most actively publishing experts on this list. She posts consistently on LinkedIn alongside her weekly Dear Marketer newsletter. Priority content:

### High priority
- **Inbox placement psychology** — Kath has posted about the psychological factors affecting inbox placement decisions (what makes subscribers open, what trains Gmail's algorithms). Verified she posted on this recently (June 2026).
- **Behavioral science applied to email copy** — Posts on Cialdini's persuasion principles (reciprocity, scarcity, social proof, authority, commitment/consistency, liking), cognitive biases, and bimodal buyer personas as applied to email
- **Gen AI prompting for email** — Kath has integrated AI into her email workflow and teaches this publicly. Posts on how to "converse with AI" rather than prompt, how to train a private AI model on your expertise
- **AB testing methodology** — Her holistic testing approach (hypothesis-driven, not just subject line splits) is distinctive and worth documenting
- **Deliverability case studies** — She shared a detailed case study in her YouTube content about a SaaS client with persistent deliverability problems. LinkedIn posts may contain more examples.

### Medium priority
- Dear Marketer newsletter issue announcements (capture the topic and hook)
- Conference talk announcements (reveals what she's currently teaching)
- Posts critiquing email industry "bad practices" being touted as best practices

### Skip
- Generic "email is not dead" posts without new evidence
- Event promotion posts with no substantive content

---

## Collection Method

**Option 1: Automated**
```bash
export LI_AT="your_cookie_value"
python scripts/scrape_linkedin_posts.py --expert kath-pay
```

**Option 2: Manual** — Visit https://www.linkedin.com/in/kathpay/recent-activity/all/

Kath's username on LinkedIn is simply "cath" (per her own transcript). If the slug `kathpay` doesn't resolve, try `cath` or search for "Kath Pay Holistic Email Marketing."

---

## File Naming Convention

`post-NNN.md` where NNN is zero-padded (001, 002 ...).

## Post Template

```markdown
# Post NNN — Kath Pay

**Date:** [date]
**Source:** [URL]
**Scraped:** [timestamp]

---

## Content

[Full post text]

---

## Research Notes

- [ ] Key claim or tactic:
- [ ] Behavioral science principle referenced: [if any]
- [ ] Relevant to email strategy? Yes / No / Partial
- [ ] Connects to transcript: [reference if applicable]
- [ ] Follow-up action:
```

---

## Context for Research Use

Kath's LinkedIn is a live feed of her 27-year email expertise applied to current problems. The most distinctive content for this research is her work at the intersection of behavioral psychology and email copy — she's one of the few practitioners who uses Cialdini's framework explicitly in email strategy rather than just referencing it abstractly.

Cross-reference against:
- `/research/youtube-transcripts/kath-pay/holistic-email-marketing-strategy-ai-growth.md`
- `/research/youtube-transcripts/kath-pay/mastering-email-marketing-gen-ai-kath-pay.md`
- `/research/youtube-transcripts/kath-pay/email-marketing-benchmarks-industry-stats.md`
