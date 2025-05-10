import feedparser
from dotenv import load_dotenv

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