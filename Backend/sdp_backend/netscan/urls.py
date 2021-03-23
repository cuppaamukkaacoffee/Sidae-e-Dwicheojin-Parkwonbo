from django.urls import path, include
from .views import TargetsAPIView, ResultsAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("netscan/target/", TargetsAPIView.as_view()),
    path("netscan/result/", ResultsAPIView.as_view())
]
