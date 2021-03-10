from django.db import models

# Create your models here.


class Reports(models.Model):
    id = models.TextField(primary_key=True)
    scan_session_id = models.TextField(default="")
    scan_type = models.TextField(default="")
    timestamp = models.DateTimeField()
    username = models.TextField(max_length=15, default="")
    target = models.TextField(default="")
    sub_path = models.TextField(default="", blank=True)
    url = models.TextField(default="")
    status = models.IntegerField(default=0)
    result_string = models.TextField(default="")
    vulnerability = models.TextField(default="")
    form = models.TextField(default="", blank=True)

    # def get_filtered(self, **kwargs):


class RequestHeaders(models.Model):
    id = models.TextField(primary_key=True)
    # "('Host': 'www.daum.net', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'Python/3.9 aiohttp/3.7.3')"
    timestamp = models.DateTimeField(auto_now_add=True)
    host = models.TextField(default="")
    accept = models.TextField(default="*/*")
    accept_encoding = models.TextField(default="gzip, deflate")
    user_agent = models.TextField(default="Python/3.9 aiohttp/3.7.3")
    body = models.TextField(default="", blank=True)


class ResponseHeaders(models.Model):
    id = models.TextField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    headers_string = models.TextField(default="")


class Targets(models.Model):
    id = models.TextField(primary_key=True)
    target = models.TextField(default="")
    username = models.TextField(default="")
    #'SQL Injection', 'XSS', 'Open Redirect', 'Windows Directory Traversal', 'Linux Directory Traversal', LFI Check', 'RFI Check', 'RCE Linux Check', 'RCE PHP Check', 'SSTI Check'
    sqli = models.IntegerField(default=0)
    xss = models.IntegerField(default=0)
    open_redirect = models.IntegerField(default=0)
    windows_directory_traversal = models.IntegerField(default=0)
    linux_directory_traversal = models.IntegerField(default=0)
    lfi = models.IntegerField(default=0)
    rfi = models.IntegerField(default=0)
    rce_linux = models.IntegerField(default=0)
    rce_php = models.IntegerField(default=0)
    ssti = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


class CrawledUrls(models.Model):
    id = models.TextField(primary_key=True)
    scan_session_id = models.TextField(default="")
    url = models.TextField(default="")
    target = models.TextField(default="")
    username = models.TextField(default="")
