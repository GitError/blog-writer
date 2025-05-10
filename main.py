from blog_sources import CATEGORIES
from generator import generate_post
from publisher import publish_to_wordpress
from utils import fetch_articles, load_env, save_draft_to_md, get_unsplash_image, insert_image_markdown
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

    image_url = get_unsplash_image(category)
    content_with_image = insert_image_markdown(content, image_url)

    print(f"\nTITLE: {title}\n")
    print("CONTENT:\n")
    print(content_with_image)
    print("\n--- End of post ---\n")

    save_draft_to_md(title, content_with_image, category)

    # publish_to_wordpress(title, content_with_image, tags=[category])