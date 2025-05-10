import requests
import os
import json

def generate_post(category, summaries):
    model = os.getenv("OLLAMA_MODEL", "mistral")
    url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")

    prompt = f"""
    Write a casual, informative blog post in **Markdown** format for the '{category}' section of a tech blog.
    Use a knowledgeable tone and summarize the following stories into one cohesive article:

    {summaries}
    """

    try:
        response = requests.post(
            url,
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt.strip()}],
                "stream": True
            },
            stream=True
        )

        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line)
                    content_piece = chunk.get("message", {}).get("content") or chunk.get("response", "")
                    full_response += content_piece
                except json.JSONDecodeError as e:
                    print("⚠️ Skipping line due to decode error:", line)

        return full_response or "[Error: No content generated]"

    except Exception as e:
        print("⚠️ Ollama error:", e)
        return "[Error: Unable to generate content]"