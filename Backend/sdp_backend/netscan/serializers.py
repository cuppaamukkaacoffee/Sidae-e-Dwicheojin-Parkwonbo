from rest_framework import serializers
from .models import Ports, CrawledIPs, Targets


class PortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ports
        fields = "__all__"


class CrawledIPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawledIPs
        fields = "__all__"


class TargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Targets
        fields = "__all__"