from django.urls import re_path
from .consumers import ReportsConsumer

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/scan/", ReportsConsumer.as_asgi()),
]
