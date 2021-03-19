from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import CrawledIPs, Ports, Targets
from .serializers import (
    CrawledIPsSerializer,
    PortsSerializer,
    TargetsSerializer
)
from login.jwt import JwtHelper


class TargetsAPIView(APIView):
    def get(self, request):

        timestamp = ""

        try:
            token = request.META["HTTP_AUTHORIZATION"]
        except KeyError:
            return Response(data="no token bitch")

        for key in request.data:
            if key == "username":
                username = request.data["username"]
            if key == "target":
                target = str(request.data["target"]).replace(' ', '').split(',')
            if key == "timestamp":
                timestamp = request.data["timestamp"]

        jwt = JwtHelper()

        verification = jwt.validate(token)

        if not verification:
            return Response(
                data="token payload not valid", status=status.HTTP_400_BAD_REQUEST
            )
        elif type(verification) == str:
            return Response(data=verification, status=status.HTTP_400_BAD_REQUEST)

        if verification.username != username:
            return Response(
                data="token user and query user does not match",
                status=status.HTTP_400_BAD_REQUEST,
            )

        target_result = Targets.objects.filter(
            username__exact=username,
            target__in=target,
            timestamp__contains=timestamp,
        )

        target_serializers = TargetsSerializer(target_result, many=True)

        return Response(data={"targets" : target_serializers.data})
