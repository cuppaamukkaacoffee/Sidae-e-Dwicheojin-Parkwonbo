from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .vuln import shmlackShmidow
from .spider import asyncCrawl
from .models import Reports, RequestHeaders, ResponseHeaders, Targets, CrawledUrls
import asyncio
from .serializers import (
    ReportsSerializer,
    RequestHeadersSerializer,
    ResponseHeadersSerializer,
    TargetsSerializer,
    CrawledUrlsSerializer,
)
from login.jwt import JwtHelper


class ReportsAPIView(APIView):
    def get(self, request):

        username = ""
        target = ""
        sub_path = ""
        result_string = ""
        vulnerability = ""

        try:
            token = request.META["HTTP_AUTHORIZATION"]
        except KeyError:
            return Response(data="no token bitch")

        for key in request.data:
            if key == "username":
                username = request.data["username"]
            if key == "target":
                target = request.data["target"]
            if key == "subpath":
                sub_path = request.data["sub_path"]
            if key == "result_string":
                result_string = request.data["result_string"]
            if key == "vulnerability":
                vulnerability = request.data["vulnerability"]

        jwt = JwtHelper()

        verification = jwt.validate(token)
        # print(verification)
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

        reports = Reports.objects.filter(
            user__contains=username,
            target__contains=target,
            sub_path__contains=sub_path,
            vulnerability__contains=vulnerability,
            result_string__contains=result_string,
        )
        requests = []
        responses = []
        for report in reports:
            request = RequestHeaders.objects.filter(id__exact=report.id)
            requests.append(request)
            response = ResponseHeaders.objects.filter(id__exact=report.id)
            responses.append(response)
        report_serializers = ReportsSerializer(reports, many=True)
        request_serializers = RequestHeadersSerializer(requests, many=True)
        response_serializers = ResponseHeadersSerializer(responses, many=True)

        result = {}
        result["reports"] = report_serializers.data
        result["requests"] = request_serializers.data
        result["responses"] = response_serializers.data
        return Response(data=result)

    def post(self, request):

        try:
            token = request.META["HTTP_AUTHORIZATION"]
            target = request.data["target"]
            fuzz = request.data["fuzz"]
        except KeyError:
            return Response(
                data="missing body attribute", status=status.HTTP_400_BAD_REQUEST
            )

        jwt = JwtHelper()

        verification = jwt.validate(token)
        print(verification)
        if not verification:
            return Response(data="error")
        elif type(verification) == str:
            return Response(data=verification)

        result = []

        if target:
            urlList = asyncio.run(asyncCrawl.main(target))
            print("doing scan...")
        if fuzz:
            result = asyncio.run(
                shmlackShmidow.wrapperMain(urlList, username=verification.username)
            )

            for json in result:
                serializers = ReportsSerializer(data=json)
                if serializers.is_valid(raise_exception=True):
                    serializers.save()

            return Response(data=result, status=status.HTTP_200_OK)
        return Response(data=urlList, status=status.HTTP_200_OK)


class ReportsQueryAPIView(APIView):
    def post(self, request):
        username = ""
        target = ""
        scan_session_id = ""
        sub_path = ""
        result_string = ""
        vulnerability = ""
        with_headers = True
        targets_only = False
        urls_only = False

        try:
            token = request.META["HTTP_AUTHORIZATION"]
        except KeyError:
            return Response(data="no token bitch")

        for key in request.data:
            if key == "username":
                username = request.data["username"]
            if key == "target":
                target = request.data["target"]
            if key == "scan_session_id":
                scan_session_id = request.data["scan_session_id"]
            if key == "subpath":
                sub_path = request.data["sub_path"]
            if key == "result_string":
                result_string = request.data["result_string"]
            if key == "vulnerability":
                vulnerability = request.data["vulnerability"]
            if key == "with_headers":
                with_headers = request.data["with_headers"]
            if key == "targets_only":
                targets_only = request.data["targets_only"]
            if key == "urls_only":
                urls_only = request.data["urls_only"]

        jwt = JwtHelper()

        verification = jwt.validate(token)
        # print(verification)
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

        if targets_only:
            targets = Targets.objects.filter(
                username__contains=username,
                target__contains=target,
                id__contains=scan_session_id,
            )
            targets_serializer = TargetsSerializer(targets, many=True)

            return Response(data={"targets": targets_serializer.data})

        if urls_only:
            urls = CrawledUrls.objects.filter(
                target__contains=target,
                scan_session_id__contains=scan_session_id,
                username__contains=username,
            )
            urls_serializer = CrawledUrlsSerializer(urls, many=True)

            return Response(data={"urls": urls_serializer.data})

        reports = Reports.objects.filter(
            scan_session_id__contains=scan_session_id,
            username__contains=username,
            target__contains=target,
            sub_path__contains=sub_path,
            vulnerability__contains=vulnerability,
            result_string__contains=result_string,
        )

        report_serializers = ReportsSerializer(reports, many=True)

        if not with_headers:
            return Response(data={"reports": report_serializers.data})

        requests = RequestHeaders.objects.none()
        responses = ResponseHeaders.objects.none()
        for report in reports:
            requests |= RequestHeaders.objects.filter(id__exact=report.id)
            responses |= ResponseHeaders.objects.filter(id__exact=report.id)

        request_serializers = RequestHeadersSerializer(requests, many=True)
        response_serializers = ResponseHeadersSerializer(responses, many=True)

        result = {}
        result["reports"] = report_serializers.data
        result["requests"] = request_serializers.data
        result["responses"] = response_serializers.data
        return Response(data=result)
