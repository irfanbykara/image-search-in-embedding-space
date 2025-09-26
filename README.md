# Image Search in Embedding Space


This dockerized Django project with CI/CD AWS pipelined project allows users to:


https://github.com/user-attachments/assets/68f8dec6-1484-417a-829e-2de242395582

1. Upload images.
2. Generate captions for uploaded images using the OpenAI API.
3. Embed captions and store them in a Chroma vector database.
4. Search for images based on text queries using ChromaDB.

---

## Prerequisites

- Python 3.10+
- Git
- Virtualenv (optional but recommended)
- OpenAI API key

---

## Setup Instructions

### 1. Clone the repository
git clone [https://github.com/USERNAME/REPO_NAME.git](https://github.com/irfanbykara/image-search-in-embedding-space.git)
cd image-search-in-embedding

### 2. Create a virtual environment
python -m venv tmp_venv

### 3. Activate the virtual environment

**Windows (PowerShell):**
.\tmp_venv\Scripts\Activate.ps1

**Windows (CMD):**
.\tmp_venv\Scripts\activate.bat

**macOS / Linux:**
source tmp_venv/bin/activate

---

### 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

---

### 5. Setup environment variables

Create a `.env` file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here

> **Important:** `.env` is included in `.gitignore` to avoid committing secrets.

---

---

### 6. Make migrations and migrate database
python manage.py makemigrations
python manage.py migrate

---


---

### 7. Run the development server
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to see the upload page.

---

## Usage

1. Upload an image using the upload form.  
2. The OpenAI API generates a caption for the image.  
3. Captions are embedded and stored in ChromaDB.  
4. Use the search form to query images by text — the best matches will be returned.

---

## Notes

- Ensure `.env` is never committed.  
- Uploaded images are stored in the `media/` folder.  
- Vector embeddings and ChromaDB data are stored in the `chroma_db/` folder.  
- Add new static assets (CSS, JS) to the `static/` folder.

---

## Dependencies
`requirements.txt`:

Django>=5.2
openai
chromadb
python-dotenv
Pillow

Adjust versions as needed.

---

## License

MIT License
