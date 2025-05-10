import requests
import os
from requests.auth import HTTPBasicAuth

def publish_to_wordpress(title, content, tags=None):
    wp_url = os.getenv("WP_URL")
    wp_user = os.getenv("WP_USER")
    wp_pass = os.getenv("WP_APP_PASS")

    post_data = {
        "title": title,
        "content": content,
        "status": "draft",
        "tags": tags or []
    }

    response = requests.post(
        wp_url,
        auth=HTTPBasicAuth(wp_user, wp_pass),
        json=post_data
    )

    if response.status_code == 201:
        print(f"✅ Posted: {title}")
    else:
        print(f"❌ Failed to post '{title}':", response.status_code, response.text)