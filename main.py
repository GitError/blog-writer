import argparse
from blog_sources import CATEGORIES
from generator import generate_post
from publisher import publish_to_wordpress
from utils import fetch_articles, load_env, save_draft_to_md, build_image_prompt
from datetime import datetime
import subprocess
import os

load_env()

parser = argparse.ArgumentParser(description="Generate blog posts from RSS feeds using LLMs + Stable Diffusion")
parser.add_argument("--category", help="Run for a specific category only (e.g., ai, cloud)", default=None)
parser.add_argument("--publish", action="store_true", help="Enable WordPress publishing")
args = parser.parse_args()

categories = {args.category: CATEGORIES[args.category]} if args.category else CATEGORIES

for category, feeds in categories.items():
    print(f"\n--- Generating post for category: {category} ---")
    articles = fetch_articles(feeds)
    if not articles:
        print(f"No articles found for category '{category}'. Skipping.")
        continue

    content = generate_post(category, articles)
    title = f"{category.capitalize()} Digest"

    # Generate consistent filename
    safe_title = "-".join(title.lower().split()).replace("--", "-").replace("(", "").replace(")", "")
    date_str = datetime.now().strftime("%Y-%m-%d")
    md_file = f"drafts/{date_str}-{safe_title}.md"

    # Save draft file with explicit filename
    save_draft_to_md(title, content, category, filename=md_file)

    # Extract prompt from content using KeyBERT
    prompt = build_image_prompt(category, content)
    print(f"🎨 Generating image for prompt: '{prompt}'...")
    subprocess.run(["python", "image_gen_cli.py", prompt, md_file])

    if args.publish:
        with open(md_file, "r", encoding="utf-8") as f:
            content_with_image = f.read()
        publish_to_wordpress(title, content_with_image, tags=[category])
