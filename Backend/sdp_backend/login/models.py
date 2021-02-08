from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.TextField(max_length=15, primary_key=True)
    password = models.CharField(max_length=100)
    datetime = models.DateField(auto_now_add=True)
