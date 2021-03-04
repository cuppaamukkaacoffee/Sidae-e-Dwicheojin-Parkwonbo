from rest_framework import serializers
from .models import Reports, RequestHeaders, ResponseHeaders, Targets, CrawledUrls


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        # fields = ['id', 'title', 'author', 'email']
        fields = "__all__"

class RequestHeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestHeaders
        fields = "__all__"

class ResponseHeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseHeaders
        fields = "__all__"

class TargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Targets
        fields = "__all__"

class CrawledUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawledUrls
        fields = "__all__"

    # def create(self, validated_data):
    #     return Reports.objects.create(**validated_data)
