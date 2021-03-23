from django.db import models
from django.contrib.postgres.fields import ArrayField


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
    domain_name = ArrayField(models.TextField(blank=True), default=list)
    registrar = ArrayField(models.TextField(blank=True), default=list)
    whois_server = ArrayField(models.TextField(blank=True), default=list)
    referral_url = ArrayField(models.TextField(blank=True), default=list)
    updated_date = ArrayField(models.TextField(blank=True), default=list)
    creation_date = ArrayField(models.TextField(blank=True), default=list)
    expiration_date = ArrayField(models.TextField(blank=True), default=list)
    name_servers = ArrayField(models.TextField(blank=True), default=list)
    status = ArrayField(models.TextField(blank=True), default=list)
    emails = ArrayField(models.TextField(blank=True), default=list)
    dnssec = ArrayField(models.TextField(blank=True), default=list)
    name = ArrayField(models.TextField(blank=True), default=list)
    org = ArrayField(models.TextField(blank=True), default=list)
    address = ArrayField(models.TextField(blank=True), default=list)
    city = ArrayField(models.TextField(blank=True), default=list)
    state = ArrayField(models.TextField(blank=True), default=list)
    zipcode = ArrayField(models.TextField(blank=True), default=list)
    country = ArrayField(models.TextField(blank=True), default=list)


class Robots(models.Model):
    id = models.TextField(primary_key=True)
    scan_session_id = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.TextField(max_length=15, default="")
    target = models.TextField(default="")
    txt = models.TextField(blank=True, default="")


class Targets(models.Model):
    id = models.TextField(primary_key=True)
    target = models.TextField(default="")
    username = models.TextField(default="")
    scan_session_id = models.TextField(default="")
    open_ports = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)