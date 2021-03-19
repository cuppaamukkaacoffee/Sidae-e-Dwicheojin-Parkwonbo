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


class Whoiss(models.Model):
    id = models.TextField(primary_key=True)
    scan_session_id = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.TextField(max_length=15, default="")
    target = models.TextField(default="")
    domain_name = models.TextField(default="", null=True)
    registrar = models.TextField(default="", null=True)
    whois_server = models.TextField(default="", null=True)
    referral_url = models.TextField(default="", null=True)
    updated_date = models.TextField(default="", null=True)
    creation_date = models.TextField(default="", null=True)
    expiration_date = models.TextField(default="", null=True)
    name_servers = models.TextField(default="", null=True)
    status = models.TextField(default="", null=True)
    emails = models.TextField(default="", null=True)
    dnssec = models.TextField(default="", null=True)
    name = models.TextField(default="", null=True)
    org = models.TextField(default="", null=True)
    address = models.TextField(default="", null=True)
    city = models.TextField(default="", null=True)
    state = models.TextField(default="", null=True)
    zipcode = models.TextField(default="", null=True)
    country = models.TextField(default="", null=True)


class Targets(models.Model):
    id = models.TextField(primary_key=True)
    target = models.TextField(default="")
    username = models.TextField(default="")
    scan_session_id = models.TextField(default="")
    open_ports = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)