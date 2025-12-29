# Image Embed Search

A Django-based weekend fun project that enables semantic image search using AI-powered captioning and vector embeddings. Upload images, automatically generate captions using OpenAI's vision model, and search through your image collection using natural language queries.


https://github.com/user-attachments/assets/0df9fab3-7710-4a9d-8e12-1042b73df175


## Features

- 🖼️ **Image Upload**: Upload images with automatic processing and storage
- 🤖 **AI-Powered Captioning**: Automatically generates descriptive captions using OpenAI's GPT-4o-mini vision model
- 🔍 **Semantic Search**: Search images using natural language queries powered by ChromaDB and OpenAI embeddings
- ☁️ **Cloud Storage**: Images are stored in AWS S3 for scalable and reliable storage
- 📊 **Image Gallery**: Browse all uploaded images with pagination
- 🐳 **Docker Support**: Containerized deployment with Docker

## Tech Stack

- **Backend**: Django 5.2.5
- **Database**: PostgreSQL
- **Vector Database**: ChromaDB (for semantic search)
- **AI Services**: OpenAI API (GPT-4o-mini for captioning, text-embedding-3-small for embeddings)
- **Storage**: AWS S3 (via django-storages)
- **Server**: Uvicorn (ASGI)
- **Containerization**: Docker

## Prerequisites

- Python 3.10+
- PostgreSQL database
- AWS S3 bucket and credentials
- OpenAI API key
- Docker (optional, for containerized deployment)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd image_embed_search
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
POSTGRES_DB=your_database_name
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=your_database_password
POSTGRES_HOST=your_database_host
POSTGRES_PORT=5432

# AWS S3 Configuration
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name
AWS_S3_REGION_NAME=eu-north-1

# OpenAI API
OPENAI_API_KEY=your_openai_api_key
```

### 5. Database Setup

Create the PostgreSQL database and run migrations:

```bash
python manage.py migrate
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

## Running the Application

### Development Mode

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

### Using Docker

Build and run the Docker container:

```bash
docker build -t image-embed-search .
docker run -p 8000:8000 --env-file .env image-embed-search
```

### Using Uvicorn (Production-like)

```bash
uvicorn config.asgi:application --host 0.0.0.0 --port 8000
```

## Usage

### Upload Images

1. Navigate to the home page (`/` or `/upload/`)
2. Select an image file
3. Click upload
4. The system will:
   - Generate a caption using OpenAI's vision model
   - Upload the image to AWS S3
   - Store metadata in PostgreSQL
   - Create embeddings and add to ChromaDB for search

### Search Images

1. Navigate to `/search/`
2. Enter a text query describing what you're looking for
3. View matching images based on semantic similarity

### Browse All Images

1. Navigate to `/all_images/`
2. Browse through all uploaded images with pagination (4 images per page)

