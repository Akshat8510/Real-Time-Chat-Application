from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Note the r before the string for raw regex
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]