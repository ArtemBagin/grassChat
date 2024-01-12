"""
ASGI config for grass project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat_app.consumers import PersonalChatConsumer, OnlineStatusConsumer, NotificationConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grass.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/', PersonalChatConsumer),
            path('ws/online/', OnlineStatusConsumer),
            path('ws/notify/', NotificationConsumer)
        ])
    )
})
