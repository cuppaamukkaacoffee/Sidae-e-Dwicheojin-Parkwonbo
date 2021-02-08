from django.urls import path, include
from .views import UsersAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("auth/login/", UsersAPIView.as_view()),
]
