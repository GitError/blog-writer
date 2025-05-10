# 🧠 Auto Blog Writer

An automated Python tool that fetches trending tech articles from RSS feeds, uses a local LLM (via Ollama) to generate blog posts in Markdown, and (optionally) publishes them to a WordPress blog.

---

## 🚀 Features

- ✅ Pulls fresh tech content from curated RSS feeds  
- 🧠 Uses **Ollama** + open-source LLMs (e.g., Mistral) to generate readable blog posts  
- ✍️ Outputs posts in **Markdown** format  
- 🔒 Supports **dry run mode** (no accidental publishing)  
- 📰 Multi-category support: AI, Cybersecurity, Startups, Gadgets  
- 🌐 WordPress integration via REST API (optional)  

---

## 🧱 Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed locally
- WordPress site with Application Password enabled
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
```

---

## 🧪 Usage

### Dry Run (Preview only)

```bash
python main.py
```

This will:
- Pull latest articles per category
- Generate blog content in Markdown
- Print results to the terminal

### Enable WordPress Publishing

In `main.py`, uncomment:

```python
# publish_to_wordpress(title, content, tags=[category])
```

Then run again.

---

## 🧠 Powered by

- [Ollama](https://ollama.com) – local LLMs made easy  
- [Feedparser](https://pythonhosted.org/feedparser/) – RSS parsing  
- [WordPress REST API](https://developer.wordpress.org/rest-api/)  
- Python + Markdown + Vibes

---

## 📌 To Do

- [ ] CLI flags (`--publish`, `--category`)
- [ ] Schedule with cron or `apscheduler`
- [ ] Add other LLM options (Codellama for dev posts, etc.)

---

## 🧠 Author

Built by [@giterror](https://giterror.com) — because real devs automate their blogs too.