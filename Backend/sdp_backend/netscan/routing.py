from django.urls import re_path
from .consumers import NetscanConsumer

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/netscan/", NetscanConsumer.as_asgi()),
]