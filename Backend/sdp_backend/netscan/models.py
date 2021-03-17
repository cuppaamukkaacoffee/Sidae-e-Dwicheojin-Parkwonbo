from django.db import models


class CrawledIPs(models.Model):
    id = models.TextField(primary_key=True)
    scan_session_id = models.TextField(default="")
    username = models.TextField(default="")
    target = models.TextField(default="")
    ip_address = models.TextField(default="")


class Ports(models.Model):
    id = models.TextField(primary_key=True)
    scan_session_id = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.TextField(max_length=15, default="")
    target = models.TextField(default="")
    ip_address = models.TextField(default="")
    port_number = models.IntegerField(default=0)
    port_protocol = models.TextField(default="")
    port_status = models.TextField(default="")


class Targets(models.Model):
    id = models.TextField(primary_key=True)
    target = models.TextField(default="")
    username = models.TextField(default="")
    open_ports = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)