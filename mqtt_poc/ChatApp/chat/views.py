import queue

import paho.mqtt.client as mqtt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Message

clients = {}


def on_connect(client, userdata, flags, rc):
    client.subscribe("chat/#")


def on_message(client, userdata, msg):
    room = msg.topic.split("/")[1]
    content = msg.payload.decode()
    Message.objects.create(room=room, content=content)
    notify_clients(room, content)


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.loop_start()


def notify_clients(room, message):
    if room in clients:
        for client in clients[room]:
            client.put(message)


# Create your views here.
class ChatView(LoginRequiredMixin, TemplateView):
    template_name = "chat/index.html"


def chat_room(request, room_name):
    messages = Message.objects.filter(room=room_name)
    return render(request, "chat/chat.html", {"messages": messages, "room": room_name})


@api_view(["POST"])
def send_message(request):
    room = request.data.get("room")
    content = request.data.get("content")
    mqtt_client.publish(f"chat/{room}", content)
    _ = Message.objects.create(room=room, content=content)
    return Response({"success": True})


def event_stream(room):
    print("streaming response", room)
    q = queue.Queue()
    if room not in clients:
        clients[room] = []
    clients[room].append(q)
    try:
        while True:
            result = q.get()
            print("result", result)
            yield f"data: {result}\n\n"
    except GeneratorExit:
        clients[room].remove(q)


def sse_view(request, room_name):
    return StreamingHttpResponse(
        event_stream(room_name), content_type="text/event-stream"
    )
