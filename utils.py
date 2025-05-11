import feedparser
import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from keybert import KeyBERT


def load_env():
    load_dotenv()


def fetch_articles(feed_urls, max_articles=3):
    articles = []
    links = []
    for feed_url in feed_urls:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:max_articles]:
            title = entry.title.strip()
            summary = entry.summary.strip() if hasattr(entry, 'summary') else ""
            link = entry.link.strip() if hasattr(entry, 'link') else ""
            articles.append(f"{title}\n{summary}")
            links.append((title, link))
            if len(articles) >= max_articles:
                break
        if len(articles) >= max_articles:
            break
    return "\n\n".join(f"{i+1}. {a}" for i, a in enumerate(articles)), links


def save_draft_to_md(title, content, category, filename=None, tags=None, image_path=None, sources=None):
    if not filename:
        safe_title = "-".join(title.lower().split()).replace("--", "-").replace("(", "").replace(")", "")
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"drafts/{date_str}-{safe_title}.md"

    os.makedirs("drafts", exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")

    front_matter = "---\n"
    front_matter += f"title: \"{title}\"\n"
    front_matter += f"date: {date_str}\n"
    front_matter += f"category: {category}\n"
    if tags:
        front_matter += f"tags: [{', '.join(f'\"{t}\"' for t in tags)}]\n"
    if image_path:
        front_matter += f"image: {image_path}\n"
    front_matter += "---\n\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write(f"# {title}\n\n")
        f.write(content.strip())

        if sources:
            f.write("\n\n## Sources\n")
            for s_title, s_link in sources:
                f.write(f"- [{s_title}]({s_link})\n")

    print(f"📄 Draft saved: {filename}")
    return filename


def get_unsplash_image(query):
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    if not access_key or access_key == "DEMO_ACCESS_KEY":
        print(f"⚠️ Using placeholder image for '{query}'")
        return f"https://via.placeholder.com/800x400.png?text={query.replace(' ', '+').title()}"

    try:
        response = requests.get(
            "https://api.unsplash.com/photos/random",
            params={"query": query, "orientation": "landscape"},
            headers={"Authorization": f"Client-ID {access_key}"}
        )
        data = response.json()
        return data.get("urls", {}).get("regular")
    except Exception as e:
        print("⚠️ Failed to fetch image:", e)
        return f"https://via.placeholder.com/800x400.png?text={query.replace(' ', '+').title()}"


def insert_image_markdown(content, image_url, alt_text="Related image"):
    if image_url:
        return f"![{alt_text}]({image_url})\n\n" + content
    return content


def build_image_prompt(category, content):
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(content, stop_words='english', top_n=5)
    if not keywords:
        return category
    keyword_str = ", ".join([kw for kw, _ in keywords])
    return f"{category} concept: {keyword_str}"
