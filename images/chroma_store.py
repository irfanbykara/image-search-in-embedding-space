# images/chroma_store.py
import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(name="image_search")
