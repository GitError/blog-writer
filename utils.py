import feedparser
import os
from dotenv import load_dotenv
from datetime import datetime

def load_env():
    load_dotenv()

def fetch_articles(feed_urls, max_articles=3):
    articles = []
    for feed_url in feed_urls:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:max_articles]:
            title = entry.title.strip()
            summary = entry.summary.strip() if hasattr(entry, 'summary') else ""
            articles.append(f"{title}\n{summary}")
            if len(articles) >= max_articles:
                break
        if len(articles) >= max_articles:
            break
    return "\n\n".join(f"{i+1}. {a}" for i, a in enumerate(articles))

def save_draft_to_md(title, content, category):
    """Save generated content to a Markdown file."""
    safe_title = "-".join(title.lower().split()).replace("--", "-")
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"drafts/{date_str}-{safe_title}.md"

    os.makedirs("drafts", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(content.strip())

    print(f"📄 Draft saved: {filename}")