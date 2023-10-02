"""
ASGI config for rtd project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rtd.settings')

# application = get_asgi_application()

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from rtdApp import routing as dashboard_routing
from rtdApp.consumers import *
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rtd.settings')

ws_patterns = [
    path('ws/dashboard/' , DashboardConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(dashboard_routing.websocket_urlpatterns),
    # 'websocket': URLRouter(ws_patterns),
})
