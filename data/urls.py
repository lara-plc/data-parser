from django.urls import path
from . import views

urlpatterns = [
    path("data/", views.DataView.as_view()),
    path("", views.index),
]