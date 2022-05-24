from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("family", views.flia),
    path("alta_flia/", views.alta_flia)
]