from django.db import models

# Create your models here.


class Reports(models.Model):
    timestamp = models.DateTimeField()
    user = models.TextField(max_length=15)
    target = models.TextField(default="")
    sub_path = models.TextField(default="")
    url = models.TextField(default="")
    status = models.IntegerField(default=0)
    result_string = models.TextField(default="")
    vulnerability = models.TextField(default="")

    # def get_filtered(self, **kwargs):


class RequestHeaders(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.TextField(default="")
    urls_path = models.TextField(default="")


class ResponseHeaders(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.TextField(default="")
    csv_path = models.TextField(default="")
    json_path = models.TextField(default="")
