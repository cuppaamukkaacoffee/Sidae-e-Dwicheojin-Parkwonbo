from django.urls import path, include
# from .views import ReportsAPIView, ReportsQueryAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    # path("scan/", ReportsAPIView.as_view()),
    # path("scan/query/", ReportsQueryAPIView.as_view()),
]
