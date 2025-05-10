import os
import argparse
from datetime import datetime
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

def load_model():
    model_id = os.getenv("SD_MODEL_ID", "SG161222/Realistic_Vision_V5.1_noVAE")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32,
        safety_checker=None,
        feature_extractor=None
    ).to("cuda" if torch.cuda.is_available() else "cpu")
    def dummy_checker(images, device, dtype=None):
        return images, [False] * len(images)
    pipe.run_safety_checker = dummy_checker
    return pipe

def generate_image(prompt, output_dir="generated_images"):
    pipe = load_model()
    os.makedirs(output_dir, exist_ok=True)
    image = pipe(prompt, height=384, width=640).images[0]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{output_dir}/{prompt.replace(' ', '_')[:40]}_{timestamp}.png"
    print(f"✅ Image generated, attempting to save to: {filename}")
    image.save(filename)
    return filename

def inject_image_to_markdown(md_file, image_path):
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    image_markdown = f"![Generated image](../{image_path})\n\n"
    if image_markdown not in content:
        content = image_markdown + content

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Injected image into: {md_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate image from prompt and inject into .md file")
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("md_file", help="Markdown file to inject image into")
    parser.add_argument("--out", default="generated_images", help="Output image directory")
    args = parser.parse_args()

    print(f"🎨 Generating image for prompt: '{args.prompt}'...")
    img_path = generate_image(args.prompt, args.out)
    inject_image_to_markdown(args.md_file, img_path)
