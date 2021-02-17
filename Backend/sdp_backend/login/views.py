from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher as BCrypt
from .serializers import UsersSerializer
from rest_framework.exceptions import ValidationError
from .models import Users
from .jwt import JwtHelper
import jwt, datetime

# Create your views here.


class UsersAPIView(APIView):
    def get(self, request):
        username = request.GET["username"]
        password = request.GET["password"]
        hasher = BCrypt()
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            return Response(
                data="username does not exists", status=status.HTTP_400_BAD_REQUEST
            )
        if hasher.verify(password, user.password):
            timestamp = datetime.datetime.utcnow()
            jwt = JwtHelper()
            data = {
                "JWT": jwt.tokenize(user=user, timestamp=timestamp),
                "timestamp": timestamp,
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(
            data="password does not match", status=status.HTTP_400_BAD_REQUEST
        )

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        hasher = BCrypt()

        salt = hasher.salt()
        password_encoded = hasher.encode(password, salt)

        data = {"username": username, "password": password_encoded}
        serializer = UsersSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = "user created"
            return Response(data=data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            data = str(e.__dict__["detail"]["username"][0])
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

class UsersLoginAPIView(APIView):

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        hasher = BCrypt()
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            return Response(
                data="username does not exists", status=status.HTTP_400_BAD_REQUEST
            )
        if hasher.verify(password, user.password):
            timestamp = datetime.datetime.utcnow()
            jwt = JwtHelper()
            data = {
                "JWT": jwt.tokenize(user=user, timestamp=timestamp),
                "timestamp": timestamp,
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(
            data="password does not match", status=status.HTTP_400_BAD_REQUEST
        )
