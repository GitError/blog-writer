import argparse
from blog_sources import CATEGORIES
from generator import generate_post
from utils import fetch_articles, load_env, save_draft_to_md
from datetime import datetime
from keybert import KeyBERT
import subprocess

load_env()

parser = argparse.ArgumentParser(description="Generate blog posts from RSS feeds using LLMs + Stable Diffusion")
parser.add_argument("--category", help="Run for a specific category only (e.g., ai, cloud)", default=None)
parser.add_argument("--publish", action="store_true", help="Enable WordPress publishing")
parser.add_argument("--no-image", action="store_true", help="Skip image generation")
args = parser.parse_args()

categories = {args.category: CATEGORIES[args.category]} if args.category else CATEGORIES

kw_model = KeyBERT()

for category, feeds in categories.items():
    print(f"\n--- Generating post for category: {category} ---")
    summary, links = fetch_articles(feeds)
    if not summary:
        print(f"No articles found for category '{category}'. Skipping.")
        continue

    content = generate_post(category, summary)
    title = f"{category.capitalize()} Digest"

    keywords = kw_model.extract_keywords(content, stop_words='english', top_n=5)
    tags = [kw for kw, _ in keywords]

    safe_title = "-".join(title.lower().split()).replace("--", "-").replace("(", "").replace(")", "")
    date_str = datetime.now().strftime("%Y-%m-%d")
    md_file = f"drafts/{date_str}-{safe_title}.md"

    save_draft_to_md(title, content, category, filename=md_file, tags=tags, sources=links)

    if not args.no_image:
        prompt = f"{category} concept: {', '.join(tags)}"
        print(f"🎨 Generating image for prompt: '{prompt}'...")
        subprocess.run(["python", "image_gen_cli.py", prompt, md_file])

    if args.publish:
        from publisher import publish_to_wordpress_from_file
        publish_to_wordpress_from_file(md_file)
