from django.urls import path
from . import views





urlpatterns = [
path("<int:id>", views.index, name="index"),
path("spin/", views.spin, name="spin"),
]     