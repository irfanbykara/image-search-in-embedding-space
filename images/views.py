# images/views.py
from django.shortcuts import render, redirect

from config import settings
from .models import ImageData
from .utils import get_caption_from_image, add_to_chroma, search_images
from django.core.files.storage import FileSystemStorage

def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        img_file = request.FILES["image"]
        fs = FileSystemStorage()
        filename = fs.save(img_file.name, img_file)
        file_path = fs.path(filename)
        uploaded_image_url = fs.url(filename)
        caption = get_caption_from_image(file_path)
        img_obj = ImageData.objects.create(image=filename, caption=caption)

        add_to_chroma(
            str(img_obj.id),
            caption,
            f"{settings.MEDIA_URL}{img_obj.image.name}"
        )
        return render(request, "images/upload.html", {"success": True,
                                                      "caption": caption,
                                                      "uploaded_image_url":uploaded_image_url})

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
