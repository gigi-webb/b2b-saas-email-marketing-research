# LinkedIn Posts — Dave Gerhardt

**LinkedIn:** https://www.linkedin.com/in/daveegerhardt/  
**Followers:** Large (100K+, exact count not recorded)  
**Last verified active:** June 2026 (posts daily or near-daily)  
**Collection status:** Not yet collected — use scraper or manual review

---

## What to Collect

Dave Gerhardt is one of the most prolific B2B marketing voices on LinkedIn. His posts are short, opinionated, and frequently spark large comment threads. For this research, filter aggressively — not all of his content is email-specific.

### High priority
- **Email campaign examples** — When Dave shares an email he received that impressed him, or a campaign from his own Exit 5 newsletter
- **Newsletter operations** — Posts about how he runs the Exit 5 newsletter: what he measures (reply rates, DMs), how he writes it, what's working/not working
- **"Email is not dead" takes** — His regular pushback on the "email is dying" narrative, with data or examples
- **B2B marketing tactics with email angle** — Posts specifically about using email alongside other channels (LinkedIn, events) for B2B demand generation
- **Community/newsletter monetization** — Posts about Exit 5's subscription model and how email drives it

### Medium priority
- Posts about what B2B marketers get wrong (often reveals what's working by inversion)
- Mentions of specific email tools or ESPs with actual opinion
- Posts from Exit 5 live session recaps

### Skip
- General career advice posts
- Opinions on AI, startup culture, or marketing trends without direct email application
- Promotion posts for Exit 5 memberships (unless the copy itself is instructive)

---

## Collection Method

**Option 1: Automated**
```bash
export LI_AT="your_cookie_value"
python scripts/scrape_linkedin_posts.py --expert dave-gerhardt
```

**Option 2: Manual** — Visit https://www.linkedin.com/in/daveegerhardt/recent-activity/all/

Dave posts very frequently. Recommend filtering the last 3–6 months and selecting only email-relevant posts rather than collecting everything.

---

## File Naming Convention

`post-NNN.md` where NNN is zero-padded (001, 002 ...).

## Post Template

```markdown
# Post NNN — Dave Gerhardt

**Date:** [date]
**Source:** [URL]
**Scraped:** [timestamp]

---

## Content

[Full post text]

---

## Research Notes

- [ ] Key claim or tactic:
- [ ] Comment thread worth reviewing? Yes / No
- [ ] Relevant to email strategy? Yes / No / Partial
- [ ] Connects to transcript: [reference if applicable]
- [ ] Follow-up action:
```

---

## Context for Research Use

Dave's LinkedIn posts function as a real-time extension of his Exit 5 newsletter and podcast. His most valuable posts for this research are the ones where he shares *what he's doing right now* with the Exit 5 email — his metrics, his decisions, his frustrations. He also regularly shares the best B2B email examples he receives, which builds an up-to-date swipe file.

Cross-reference against:
- `/research/youtube-transcripts/dave-gerhardt/how-to-crush-email-marketing-b2b-2026.md`
