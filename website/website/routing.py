from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from . import consumers

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path("ws/some_path/", consumers.YourConsumer.as_asgi()),
                # Add other WebSocket paths as needed
            ]
        )
    ),
})