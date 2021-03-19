from django.urls import path, include
from .views import TargetsAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("netscan/target/", TargetsAPIView.as_view()),
]
