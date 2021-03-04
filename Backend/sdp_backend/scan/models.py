from django.db import models

# Create your models here.


class Reports(models.Model):
    id = models.TextField(primary_key=True)
    timestamp = models.DateTimeField()
    username = models.TextField(max_length=15, default="")
    target = models.TextField(default="")
    sub_path = models.TextField(default="")
    url = models.TextField(default="")
    status = models.IntegerField(default=0)
    result_string = models.TextField(default="")
    vulnerability = models.TextField(default="")

    # def get_filtered(self, **kwargs):


class RequestHeaders(models.Model):
    id = models.TextField(primary_key=True)
    #"('Host': 'www.daum.net', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'Python/3.9 aiohttp/3.7.3')"
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
    target = models.TextField(primary_key=True)
    username = models.TextField(default="")

class CrawledUrls(models.Model):
    id = models.TextField(primary_key=True)
    url = models.TextField(default="")
    target = models.TextField(default="")
    username = models.TextField(default="")