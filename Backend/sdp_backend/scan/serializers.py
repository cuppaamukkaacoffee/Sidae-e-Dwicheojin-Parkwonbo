from rest_framework import serializers
from .models import Reports, RequestHeaders, ResponseHeaders


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

    # def create(self, validated_data):
    #     return Reports.objects.create(**validated_data)
