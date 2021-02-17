from django.urls import path, include
from .views import UsersAPIView, UsersLoginAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("auth/register/", UsersAPIView.as_view()),
    path("auth/login/", UsersLoginAPIView.as_view()),
]
