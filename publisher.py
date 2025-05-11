import os
import requests
import yaml
from dotenv import load_dotenv

load_dotenv()

WP_URL = os.getenv("WP_URL")
WP_USER = os.getenv("WP_USER")
WP_APP_PASS = os.getenv("WP_APP_PASS")


def parse_front_matter(md_file):
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if lines[0].strip() != "---":
        return {}, "".join(lines)

    fm_end = lines.index("---\n", 1)
    front_matter = yaml.safe_load("".join(lines[1:fm_end]))
    content = "".join(lines[fm_end + 1:])
    return front_matter, content


def publish_to_wordpress_from_file(md_file):
    front_matter, content = parse_front_matter(md_file)

    title = front_matter.get("title", "Untitled")
    category = front_matter.get("category", "blog")
    tags = front_matter.get("tags", [])
    image_url = front_matter.get("image")

    # Optional: Create tags if they don't exist
    tag_ids = []
    for tag in tags:
        tag_resp = requests.post(
            f"{WP_URL}/tags",
            auth=(WP_USER, WP_APP_PASS),
            json={"name": tag},
            headers={"Content-Type": "application/json"}
        )
        if tag_resp.status_code in [200, 201]:
            tag_ids.append(tag_resp.json().get("id"))

    # Optional: Upload image if supported (else use plugin to set from URL)
    # Here we'll pass the URL to a custom field or plugin if image_url is set

    post_data = {
        "title": title,
        "content": content,
        "status": "publish",
        "tags": tag_ids,
    }

    resp = requests.post(WP_URL, auth=(WP_USER, WP_APP_PASS), json=post_data, headers={"Content-Type": "application/json"})

    if resp.status_code == 201:
        print(f"✅ Published '{title}' to WordPress")
    else:
        print(f"❌ Failed to publish '{title}':", resp.status_code, resp.text)