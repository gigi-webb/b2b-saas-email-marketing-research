#!/usr/bin/env python3
"""
LinkedIn public post scraper for B2B SaaS email marketing research.

IMPORTANT LIMITATIONS:
  - LinkedIn actively blocks automated scraping and requires authentication for
    most profile content. This script uses session cookies from a logged-in
    browser session — you must supply your own li_at cookie value.
  - Respect LinkedIn's Terms of Service. Use only for personal research on
    profiles you are authorized to access. Do not run at high frequency.
  - LinkedIn's HTML structure changes without notice; selectors may need
    updating if the script stops working.

SETUP:
  1. Install dependencies:  pip install requests beautifulsoup4 lxml
  2. Log into LinkedIn in your browser.
  3. Open DevTools → Application → Cookies → copy the value of `li_at`.
  4. Set it as an environment variable:  export LI_AT="your_cookie_value"
     Or pass it directly via --cookie flag when running the script.

USAGE:
  python scrape_linkedin_posts.py
  python scrape_linkedin_posts.py --cookie "your_li_at_value" --output ./research/linkedin-posts
  python scrape_linkedin_posts.py --expert brennan-dunn
"""

import argparse
import os
import re
import time
import json
import unicodedata
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# ── Expert registry ─────────────────────────────────────────────────────────
EXPERTS = [
    {
        "slug": "val-geisler",
        "display_name": "Val Geisler",
        "linkedin_id": "lovevalgeisler",
    },
    {
        "slug": "brennan-dunn",
        "display_name": "Brennan Dunn",
        "linkedin_id": "brennandunn",
    },
    {
        "slug": "kath-pay",
        "display_name": "Kath Pay",
        "linkedin_id": "kathpay",
    },
    {
        "slug": "dave-gerhardt",
        "display_name": "Dave Gerhardt",
        "linkedin_id": "daveegerhardt",
    },
    {
        "slug": "emily-kramer",
        "display_name": "Emily Kramer",
        "linkedin_id": "emilykramer",
    },
    {
        "slug": "gaetano-dinardi",
        "display_name": "Gaetano DiNardi",
        "linkedin_id": "gaetanodinardi",
    },
    {
        "slug": "katelyn-bourgoin",
        "display_name": "Katelyn Bourgoin",
        "linkedin_id": "katelynbourgoin",
    },
    {
        "slug": "kyle-poyar",
        "display_name": "Kyle Poyar",
        "linkedin_id": "kylepoyar",
    },
    {
        "slug": "matt-mcgarry",
        "display_name": "Matt McGarry",
        "linkedin_id": "mattmcgarry",
    },
    {
        "slug": "peep-laja",
        "display_name": "Peep Laja",
        "linkedin_id": "peeplaja",
    },
]

# ── HTTP session setup ───────────────────────────────────────────────────────
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.linkedin.com/",
    "DNT": "1",
}

# Seconds to wait between requests to avoid rate limiting
REQUEST_DELAY = 4


def build_session(li_at_cookie: str) -> requests.Session:
    session = requests.Session()
    session.headers.update(HEADERS)
    session.cookies.set("li_at", li_at_cookie, domain=".linkedin.com")
    return session


def profile_url(linkedin_id: str) -> str:
    return f"https://www.linkedin.com/in/{linkedin_id}/recent-activity/all/"


def fetch_page(session: requests.Session, url: str) -> str | None:
    try:
        resp = session.get(url, timeout=15)
        if resp.status_code == 200:
            return resp.text
        if resp.status_code == 429:
            print(f"  [rate-limited] Waiting 60s before retrying {url}")
            time.sleep(60)
            resp = session.get(url, timeout=15)
            return resp.text if resp.status_code == 200 else None
        print(f"  [HTTP {resp.status_code}] {url}")
        return None
    except requests.RequestException as e:
        print(f"  [error] {e}")
        return None


def parse_posts(html: str) -> list[dict]:
    """
    Extract posts from LinkedIn's activity feed page.

    LinkedIn renders most content client-side via React. This parser targets
    the server-side rendered fragments that survive in the raw HTML.
    If LinkedIn updates their markup, these selectors will need revisiting.
    """
    soup = BeautifulSoup(html, "lxml")
    posts = []

    # Try the server-side rendered feed containers first
    # LinkedIn uses data-urn attributes to identify content entities
    containers = soup.find_all(
        "div",
        attrs={"data-urn": re.compile(r"urn:li:activity:")},
    )

    for container in containers:
        text_el = container.find(class_=re.compile(r"feed-shared-text|break-words"))
        date_el = container.find(class_=re.compile(r"feed-shared-actor__sub-description"))
        link_el = container.find("a", attrs={"data-control-name": "actor"})

        text = text_el.get_text(" ", strip=True) if text_el else ""
        date = date_el.get_text(strip=True) if date_el else ""
        url = link_el["href"] if link_el and link_el.get("href") else ""

        if text:
            posts.append({"text": text, "date": date, "url": url})

    # Fallback: look for JSON-LD or embedded __NEXT_DATA__ / voyager blobs
    if not posts:
        scripts = soup.find_all("script", type="application/ld+json")
        for script in scripts:
            try:
                data = json.loads(script.string or "")
                if isinstance(data, dict) and data.get("@type") == "SocialMediaPosting":
                    posts.append(
                        {
                            "text": data.get("articleBody", ""),
                            "date": data.get("datePublished", ""),
                            "url": data.get("url", ""),
                        }
                    )
            except (json.JSONDecodeError, AttributeError):
                pass

    return posts


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)


def post_to_markdown(post: dict, index: int, expert_name: str) -> str:
    lines = [
        f"# Post {index} — {expert_name}",
        "",
        f"**Date:** {post['date'] or 'Unknown'}",
        f"**Source:** {post['url'] or 'N/A'}",
        f"**Scraped:** {datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "",
        "---",
        "",
        "## Content",
        "",
        post["text"],
        "",
        "---",
        "",
        "## Research Notes",
        "",
        "- [ ] Key claim or tactic identified",
        "- [ ] Relevant to email strategy?",
        "- [ ] Follow-up action",
        "",
    ]
    return "\n".join(lines)


def scrape_expert(
    expert: dict,
    session: requests.Session,
    output_root: Path,
) -> int:
    name = expert["display_name"]
    slug = expert["slug"]
    lid = expert["linkedin_id"]

    print(f"\n→ {name} (linkedin.com/in/{lid})")

    url = profile_url(lid)
    html = fetch_page(session, url)

    if html is None:
        print(f"  [skip] Could not fetch page.")
        return 0

    posts = parse_posts(html)

    if not posts:
        print(
            f"  [warn] No posts parsed — LinkedIn may have returned a login wall "
            f"or changed markup. Check the raw HTML manually."
        )
        # Save raw HTML for debugging
        debug_dir = output_root / slug / "_debug"
        debug_dir.mkdir(parents=True, exist_ok=True)
        (debug_dir / "raw_response.html").write_text(html, encoding="utf-8")
        print(f"  Raw HTML saved to {debug_dir}/raw_response.html for inspection.")
        return 0

    expert_dir = output_root / slug
    expert_dir.mkdir(parents=True, exist_ok=True)

    saved = 0
    for i, post in enumerate(posts, start=1):
        filename = f"post-{i:03d}.md"
        content = post_to_markdown(post, i, name)
        (expert_dir / filename).write_text(content, encoding="utf-8")
        saved += 1

    print(f"  Saved {saved} post(s) to {expert_dir}/")
    return saved


def main():
    parser = argparse.ArgumentParser(description="Scrape LinkedIn posts for B2B email research experts.")
    parser.add_argument(
        "--cookie",
        default=os.environ.get("LI_AT", ""),
        help="Value of the li_at session cookie (or set LI_AT env var).",
    )
    parser.add_argument(
        "--output",
        default="research/linkedin-posts",
        help="Root directory for saving markdown files (default: research/linkedin-posts).",
    )
    parser.add_argument(
        "--expert",
        default="",
        help="Slug of a single expert to scrape (e.g. brennan-dunn). Omit to scrape all.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=REQUEST_DELAY,
        help=f"Seconds between requests (default: {REQUEST_DELAY}).",
    )
    args = parser.parse_args()

    if not args.cookie:
        print(
            "ERROR: No LinkedIn session cookie provided.\n"
            "Set the LI_AT environment variable or pass --cookie.\n"
            "See the module docstring for instructions."
        )
        raise SystemExit(1)

    output_root = Path(args.output)
    session = build_session(args.cookie)

    targets = EXPERTS
    if args.expert:
        targets = [e for e in EXPERTS if e["slug"] == args.expert]
        if not targets:
            print(f"ERROR: No expert with slug '{args.expert}' found in registry.")
            raise SystemExit(1)

    print(f"Scraping {len(targets)} expert(s)…")
    total = 0
    for i, expert in enumerate(targets):
        total += scrape_expert(expert, session, output_root)
        if i < len(targets) - 1:
            time.sleep(args.delay)

    print(f"\nDone. {total} post(s) saved across {len(targets)} expert(s).")


if __name__ == "__main__":
    main()
