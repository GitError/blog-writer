# 🧠 Auto Blog Writer

An automated Python tool that fetches trending tech articles from RSS feeds, uses a local LLM (via Ollama) to generate blog posts in Markdown, optionally adds Unsplash images, and (optionally) publishes them to a WordPress blog.

---

## 🚀 Features

- ✅ Pulls fresh tech content from curated RSS feeds  
- 🧠 Uses **Ollama** + open-source LLMs (e.g., Mistral) to generate readable blog posts  
- 🖼️ Inserts relevant **Unsplash images** at the top of posts  
- ✍️ Outputs posts in **Markdown** format  
- 💾 Saves drafts locally as `.md` files (date-based, per category)  
- 🔒 Supports **dry run mode** (no accidental publishing)  
- 📰 Multi-category support: AI, Cybersecurity, Startups, Gadgets, Programming, Cloud  
- 🌐 WordPress integration via REST API (optional)  

---

## 🧱 Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- WordPress site with Application Password enabled
- [Unsplash API Key](https://unsplash.com/developers) (optional but recommended)
- (Optional) Virtual environment

---

## 📦 Installation

```bash
git clone https://github.com/youruser/auto-blog-writer.git
cd auto-blog-writer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Create a `.env` file in the root with the following:

```env
WP_URL=https://yourdomain.com/wp-json/wp/v2/posts
WP_USER=your_wp_username
WP_APP_PASS=your_wordpress_app_password
OLLAMA_MODEL=mistral
OLLAMA_URL=http://localhost:11434/api/chat
UNSPLASH_ACCESS_KEY=your_unsplash_api_key
```

---

## 🧪 Usage

### Dry Run (Preview only)

```bash
python main.py
```

This will:
- Pull latest articles per category
- Generate blog content in Markdown using Ollama
- Fetch a relevant image from Unsplash per category
- Print and save the draft locally to `/drafts/*.md`

### Enable WordPress Publishing

In `main.py`, uncomment:

```python
# publish_to_wordpress(title, content_with_image, tags=[category])
```

Then run again.

---

## 📂 Output

- Drafts saved under `/drafts/` directory
- Filename format: `YYYY-MM-DD-title-digest.md`
- Includes `# Title`, inserted image, and full post content

---

## 🧠 Powered by

- [Ollama](https://ollama.com) – Local LLMs made easy  
- [Feedparser](https://pythonhosted.org/feedparser/) – RSS parsing  
- [Unsplash API](https://unsplash.com/developers) – Image sourcing  
- [WordPress REST API](https://developer.wordpress.org/rest-api/) – Blog publishing  
- Python + Markdown + Local AI  

---

## 📌 To Do

- [ ] CLI flags (`--publish`, `--category`, `--no-image`)
- [ ] Retry handling for empty RSS feeds
- [ ] Image caching / alt text generation
- [ ] Cron integration or `schedule` module support

---

## 🧠 Author

Built by [@giterror](https://giterror.com) — because real devs automate their blogs too.