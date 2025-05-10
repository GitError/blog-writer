# 🧠 Auto Blog Writer

A fully automated Python tool that turns tech news into AI-generated blog posts with images. It fetches RSS content, summarizes it with local LLMs via Ollama, extracts keywords with KeyBERT, generates realistic images using Stable Diffusion, saves it all as Markdown, and optionally publishes to WordPress.

---

## 🚀 Features

- ✅ Pulls fresh tech articles from RSS feeds  
- 🧠 Summarizes stories with local **LLMs (Ollama + Mistral)**  
- 🗝️ Extracts smart image prompts using **KeyBERT**  
- 🎨 Generates images locally using **Stable Diffusion** (e.g., `RealisticVision`)  
- ✍️ Embeds image and content into Markdown blog posts  
- 💾 Saves drafts into `drafts/` folder  
- 🌐 Optionally publishes to **WordPress** via REST API  
- 🧠 CLI flags for category targeting and publishing  

---

## 🧱 Requirements

- Python 3.8+
- [Ollama](https://ollama.com)
- [KeyBERT](https://github.com/MaartenGr/KeyBERT)
- [HuggingFace Diffusers](https://github.com/huggingface/diffusers)
- A [Stable Diffusion model](https://huggingface.co/runwayml/stable-diffusion-v1-5) or custom one (e.g., `RealisticVision`)
- WordPress site with Application Password enabled (optional)

---

## 📦 Installation

```bash
git clone https://github.com/giterror/blog-writer.git
cd blog-writer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Create a `.env` file:

```env
WP_URL=https://yourdomain.com/wp-json/wp/v2/posts
WP_USER=your_wp_username
WP_APP_PASS=your_wordpress_app_password
OLLAMA_MODEL=mistral
OLLAMA_URL=http://localhost:11434/api/chat
SD_MODEL_ID=SG161222/Realistic_Vision_V5.1_noVAE
```

---

## 🧪 Usage

### Run all categories (no publishing):
```bash
python main.py
```

### Run a specific category:
```bash
python main.py --category ai
```

### Publish to WordPress:
```bash
python main.py --publish
```

### Run a specific category and publish:
```bash
python main.py --category cloud --publish
```

---

## 🎨 Standalone Image CLI

You can manually generate and inject images with:

```bash
python image_gen_cli.py "AI-powered cybersecurity" drafts/2025-05-10-cybersecurity-digest.md
```

---

## 📂 Output

- Markdown drafts: `drafts/YYYY-MM-DD-category-digest.md`
- Generated images: `generated_images/*.png`
- Prompts are intelligently extracted from blog content

---

## 🧠 Powered By

- [Ollama](https://ollama.com)
- [Stable Diffusion](https://huggingface.co/models)
- [Feedparser](https://pythonhosted.org/feedparser/)
- [KeyBERT](https://github.com/MaartenGr/KeyBERT)
- [WordPress REST API](https://developer.wordpress.org/rest-api/)

---

## 📌 Roadmap

- [ ] Add `--dry-run` to skip image generation/publishing  
- [ ] Add front matter/YAML metadata to Markdown  
- [ ] Support custom tag injection  
- [ ] Add scheduler via cron or APScheduler  
- [ ] Optional Unsplash image fallback once API is approved  

---

## 👨‍💻 Author

Built by [@giterror](https://giterror.com) — automate your content pipeline like a boss.