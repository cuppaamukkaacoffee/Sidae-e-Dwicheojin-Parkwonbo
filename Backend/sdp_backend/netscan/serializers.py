from rest_framework import serializers
from .models import Ports, CrawledIPs, Targets, Whoiss, Robots


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


class WhoissSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whoiss
        fields = "__all__"


class RobotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robots
        fields = "__all__"
