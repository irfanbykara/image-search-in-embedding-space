# Create your models here.
# images/models.py
from django.db import models


class ImageData(models.Model):
    image = models.ImageField(upload_to="uploads/")
    caption = models.TextField()

    def __str__(self):
        return self.caption[:50]
