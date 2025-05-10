from blog_sources import CATEGORIES
from generator import generate_post
from publisher import publish_to_wordpress
from utils import fetch_articles, load_env, save_draft_to_md
from datetime import datetime

load_env()

for category, feeds in CATEGORIES.items():
    print(f"\n--- Generating post for category: {category} ---")
    articles = fetch_articles(feeds)
    if not articles:
        print(f"No articles found for category '{category}'. Skipping.")
        continue

    content = generate_post(category, articles)
    title = f"{category.capitalize()} Digest (Dry Run)"

    print(f"\nTITLE: {title}\n")
    print("CONTENT:\n")
    print(content)
    print("\n--- End of post ---\n")

    save_draft_to_md(title, content, category)

    # publish_to_wordpress(title, content, tags=[category])
