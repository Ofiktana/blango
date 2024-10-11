from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("post/<slug>/", views.post_detail, name="blog-post-detail"),
    path("api/v1/", include("blog.api_urls")),
]