from rest_framework import serializers
from .models import Ports, CrawledIPs


class PortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ports
        fields = "__all__"


class CrawledIPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawledIPs
        fields = "__all__"
