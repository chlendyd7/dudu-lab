from django.urls import path
from .sync import sync_views

urlpatterns = [
    path('chat/<str:room_id>/', sync_views.sync_connect, name='sync_connect'),
    path('chat/<str:room_id>/send/', sync_views.send_chat_message, name='send_chat_message'),
]
