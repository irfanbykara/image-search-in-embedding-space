# images/views.py
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile

from config import settings
from .models import ImageData
from .utils import get_caption_from_image, add_to_chroma, search_images
from django.core.files.storage import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage

def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        img_file = request.FILES["image"]

        # Step 1: Save locally (temporary) to get path
        fs = FileSystemStorage()
        local_filename = fs.save(img_file.name, img_file)
        file_path = fs.path(local_filename)

        # Step 2: Generate caption
        caption = get_caption_from_image(file_path)

        # Step 3: Upload same file to S3
        s3 = S3Boto3Storage()
        with open(file_path, "rb") as f:
            content = ContentFile(f.read())
            file_name = s3.save(f"uploads/{img_file.name}", content)

        # Step 4: Save DB entry
        img_obj = ImageData.objects.create(
            image=file_name,
            caption=caption
        )

        # Step 5: Add to chroma
        add_to_chroma(
            str(img_obj.id),
            caption,
            img_obj.image.url,
        )

        return render(
            request,
            "images/upload.html",
            {"success": True, "caption": caption, "uploaded_image_url": img_obj.image.url},
        )

    return render(request, "images/upload.html")

def search(request):
    results = None
    if request.method == "POST":
        query = request.POST.get("query")
        results = search_images(query)
        if results["ids"]:
            results = [
                {"caption": cap, "image": meta["image_path"]}
                for cap, meta in zip(results["documents"][0], results["metadatas"][0])
            ]
    return render(request, "images/search.html", {"results": results})


# images/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import ImageData

def all_images(request):
    # get all images ordered by newest first
    images = ImageData.objects.all().order_by("-id")

    # how many per page
    paginator = Paginator(images, 4)  # show 12 images per page

    # get ?page= query param from request
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "images/all_images.html", {"page_obj": page_obj})
