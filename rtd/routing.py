from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, include
from rtdApp import routing as dashboard_routing

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        dashboard_routing.websocket_urlpatterns
    ),
})
