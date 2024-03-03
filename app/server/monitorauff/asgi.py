from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import os
import monitor.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitorauff.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(monitor.routing.websocket_urlpatterns))
})