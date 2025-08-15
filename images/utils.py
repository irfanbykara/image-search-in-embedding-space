# images/utils.py
from .chroma_store import collection
import base64
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_caption_from_image(image_path):
    # Read and encode image
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    # Send to OpenAI Vision model
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image in one sentence."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img_base64}"
                        }
                    }
                ]
            }
        ],
        max_tokens=50
    )

    return response.choices[0].message.content.strip()


def embed_text(text):
    resp = openai.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return resp.data[0].embedding

def add_to_chroma(id, caption, image_path):
    embedding = embed_text(caption)
    collection.add(
        ids=[id],
        embeddings=[embedding],
        documents=[caption],
        metadatas=[{"image_path": image_path}]
    )

def search_images(query, top_k=1):
    embedding = embed_text(query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )
    return results
