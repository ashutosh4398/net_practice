from django.urls import path

from .views import ChatView, chat_room, send_message, sse_view

urlpatterns = [
    path("rooms/", ChatView.as_view(), name="chat"),
    path("rooms/send_message/", send_message, name="send_message"),
    path("rooms/<str:room_name>/", chat_room, name="room"),
    path("events/<str:room_name>/", sse_view, name="sse_view"),
]
