from django.urls import path
from . import views





urlpatterns = [
path("spin/", views.spin, name="spin"),
path("", views.index, name="index"),
]     