import django
django.setup()

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sdp_backend.settings")

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import scan.routing
import netscan.routing

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                scan.routing.websocket_urlpatterns +
                netscan.routing.websocket_urlpatterns
            )
        )
    }
)