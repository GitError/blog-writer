# 🧠 Auto Blog Writer

An automated Python tool that fetches trending tech articles from RSS feeds, uses a local LLM (via Ollama) to generate blog posts in Markdown, injects AI-generated images via Stable Diffusion, and (optionally) publishes them to a WordPress blog.

---

## 🚀 Features

- ✅ Pulls fresh tech content from curated RSS feeds  
- 🧠 Uses **Ollama** + open-source LLMs (e.g., Mistral) to generate blog content  
- 🎨 Generates images locally with **Stable Diffusion** based on category/topic  
- ✍️ Saves posts in **Markdown** with embedded images  
- 💾 Drafts saved locally under `drafts/` with timestamped filenames  
- 🌐 WordPress publishing via REST API (optional toggle)  
- 📰 Supports multiple tech categories: AI, Cybersecurity, Startups, Gadgets, Programming, Cloud  

---

## 🧱 Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- [HuggingFace Diffusers](https://github.com/huggingface/diffusers) for image generation
- [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5) (default model)
- WordPress site with Application Password enabled (optional)

---

## 📦 Installation

```bash
git clone https://github.com/youruser/auto-blog-writer.git
cd auto-blog-writer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Also install image generation dependencies:
```bash
pip install diffusers transformers accelerate safetensors torch pillow
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
SD_MODEL_ID=runwayml/stable-diffusion-v1-5
```

---

## 🧪 Usage

### Run in Dry Mode (generate only)
```bash
python main.py
```

This will:
- Pull RSS stories for each tech category
- Summarize them via LLM (Ollama)
- Generate a local image using Stable Diffusion
- Save the blog post with embedded image to `/drafts/*.md`

### Publish to WordPress
Uncomment this line in `main.py`:
```python
# publish_to_wordpress(title, content_with_image, tags=[category])
```

---

## 🖼️ Image Generation

We use `image_gen_cli.py` to:
- Generate an image using a prompt (e.g., the category name)
- Save it to `generated_images/`
- Inject it at the top of the corresponding `.md` file

You can run it independently:
```bash
python image_gen_cli.py "cloud infrastructure" drafts/2024-05-10-cloud-digest.md
```

---

## 📂 Output

- Markdown blog drafts saved to `drafts/`
- Images saved to `generated_images/`
- Files are cleanly timestamped and formatted

---

## 🧠 Powered By

- [Ollama](https://ollama.com)
- [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- [Feedparser](https://pythonhosted.org/feedparser/)
- [WordPress REST API](https://developer.wordpress.org/rest-api/)
- Markdown + Local AI 🔥

---

## 📌 Roadmap

- [ ] CLI flags (`--category`, `--no-image`, `--publish`)
- [ ] Tag extraction from content
- [ ] Category subfolders
- [ ] Metadata front matter support
- [ ] Optional remote image fallback (Unsplash API)

---

## 👨‍💻 Author

Made by [@giterror](https://giterror.com) — write less, post more, automate everything.