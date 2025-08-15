from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload'),  # root → upload page

    path('upload/', views.upload_image, name="upload"),
    path('search/', views.search, name="search"),
]
