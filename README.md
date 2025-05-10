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