from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from . import consumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path("ws/some_path/", consumer.YourConsumer.as_asgi()),
                # Add other WebSocket paths as needed
            ]
        )
    ),
})