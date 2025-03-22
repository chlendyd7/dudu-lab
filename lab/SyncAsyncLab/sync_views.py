import time
from django.http import StreamingHttpResponse
from django.http import JsonResponse

chat_rooms = {}
def event_stream(room_id):
    global chat_rooms

    if room_id not in chat_rooms:
        chat_rooms[room_id] = []

    try:
        while True:
            if chat_rooms[room_id]:
                message = chat_rooms[room_id].pop(0)
                yield f"data: {message}\n\n"
    except GeneratorExit:
        pass

def sync_connect(request, room_id):
    response = StreamingHttpResponse(
        event_stream(room_id),
        content_type="text/event-stream",
    )
    response["Cache-Control"] = "no-cache"
    print(f"Sync connect: {room_id}")
    return response


def send_message(room_id, message):
    global chat_rooms
    if room_id not in chat_rooms:
        chat_rooms[room_id] = []
    chat_rooms[room_id].append(message)


def send_chat_message(request, room_id):
    """ 채팅방에 메시지 보내기 """
    message = request.GET.get("message", "")
    send_message(room_id, message)
    return JsonResponse({"status": "Message sent"})
