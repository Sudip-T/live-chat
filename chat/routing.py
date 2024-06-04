from django.urls import path
from .consumer import ChatConsumer

websocket_urlpattern = [
    path('chat/', ChatConsumer.as_asgi())
]