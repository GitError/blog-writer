from blog_sources import CATEGORIES
from generator import generate_post
from publisher import publish_to_wordpress
from utils import fetch_articles, load_env, save_draft_to_md
from datetime import datetime
import subprocess
import os

load_env()

for category, feeds in CATEGORIES.items():
    print(f"\n--- Generating post for category: {category} ---")
    articles = fetch_articles(feeds)
    if not articles:
        print(f"No articles found for category '{category}'. Skipping.")
        continue

    content = generate_post(category, articles)
    title = f"{category.capitalize()} Digest (Dry Run)"

    # Save draft file first
    save_draft_to_md(title, content, category)

    # Build the filename based on title and date
    safe_title = "-".join(title.lower().split()).replace("--", "-")
    date_str = datetime.now().strftime("%Y-%m-%d")
    md_file = f"drafts/{date_str}-{safe_title}.md"

    # Generate image locally using CLI wrapper and inject into markdown
    subprocess.run(["python", "image_gen_cli.py", category, md_file])

    # Uncomment below to enable live publishing
    # with open(md_file, "r", encoding="utf-8") as f:
    #     content_with_image = f.read()
    # publish_to_wordpress(title, content_with_image, tags=[category])