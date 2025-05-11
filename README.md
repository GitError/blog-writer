# 🧠 Blog Writer

A fully automated Python tool that fetches tech news from RSS feeds, generates blog posts using local LLMs, extracts smart tags with KeyBERT, generates realistic images via Stable Diffusion, and saves it all in Markdown — optionally publishing to WordPress.

---

## 🚀 Features

- ✅ Pulls curated tech content from RSS feeds
- 🧠 Summarizes using local LLMs via Ollama
- 🗝️ Extracts SEO-friendly tags via KeyBERT
- 🎨 Optional image generation via Stable Diffusion
- ✍️ Saves clean Markdown with YAML front matter
- 🔗 Automatically appends source links for attribution
- 🌐 Optional one-click publishing to WordPress

---

## 🧱 Requirements

- Python 3.8+
- [Ollama](https://ollama.com) running locally (for LLM generation)
- [KeyBERT](https://github.com/MaartenGr/KeyBERT) for tags
- [Diffusers](https://github.com/huggingface/diffusers) for image generation
- WordPress site (REST API + Application Password)
- Optional: `RealisticVision` or similar high-quality Stable Diffusion model

---

## 📦 Installation

```bash
git clone https://github.com/giterror/blog-writer.git
cd blog-writer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install keybert sentence-transformers diffusers transformers accelerate safetensors torch pillow
```

---

## ⚙️ Configuration

Create a `.env` file in the root:

```env
WP_URL=https://yourdomain.com/wp-json/wp/v2/posts
WP_USER=your_wp_username
WP_APP_PASS=your_wordpress_app_password
OLLAMA_MODEL=mistral
OLLAMA_URL=http://localhost:11434/api/generate
SD_MODEL_ID=SG161222/Realistic_Vision_V5.1_noVAE
```

---

## 🧪 Usage

### Generate everything (default):
```bash
python main.py
```

### Run for a specific category:
```bash
python main.py --category ai
```

### Skip image generation:
```bash
python main.py --no-image
```

### Publish to WordPress:
```bash
python main.py --publish
```

### Combine flags:
```bash
python main.py --category cloud --no-image --publish
```

---

## 📂 Output

- `drafts/YYYY-MM-DD-category-digest.md`: your Markdown posts
- Front matter includes:
  ```yaml
  ---
  title: "AI Digest"
  date: 2025-05-10
  category: ai
  tags: ["ai", "innovation", "llms"]
  image: "generated_images/ai_digest.png"
  ---
  ```
- Markdown ends with a `## Sources` section linking original articles
- Images (if enabled) saved in `/generated_images/`

---

## 🧠 Powered By

- [Ollama](https://ollama.com)
- [Stable Diffusion](https://huggingface.co/models)
- [KeyBERT](https://github.com/MaartenGr/KeyBERT)
- [WordPress REST API](https://developer.wordpress.org/rest-api/)
- [Feedparser](https://pythonhosted.org/feedparser/)

---

## 📌 Roadmap

- [ ] Code snippet detection and formatting
- [ ] Post structuring with subheadings via LLM
- [ ] Image placement reasoning (top/mid/bottom)
- [ ] Tag enrichment using LLMs beyond KeyBERT
- [ ] Scheduled publishing (cron or APScheduler)
- [ ] Git commit + push each draft
- [ ] JSON feed export alongside Markdown

---

## 👨‍💻 Author

Made by [@giterror](https://giterror.com) — for devs who want to automate without compromising quality.