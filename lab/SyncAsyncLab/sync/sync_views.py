import time
from django.http import StreamingHttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sys
from collections import defaultdict

chat_rooms = defaultdict(list)
message_queue = defaultdict(list)
def event_stream(room_id):
    try:
        current_message = None
        for res in chat_rooms[room_id]:
            if res == current_message:
                current_message = res
                break

        while True:
            if message_queue[room_id]:
                message = message_queue[room_id].pop(0)
                print(f'방 {room_id}에서 메시지 {message}를 전송합니다.')
                sys.stdout.flush()
                yield f"data: {message}\n\n"
            else:
                yield "data: ping\n\n"
                time.sleep(5)
    finally:
        if current_message and room_id in chat_rooms and current_message in chat_rooms[room_id]:
            chat_rooms[room_id].remove(current_message)
            print(f'방 {room_id}의 클라이언트 연결이 종료되었습니다. 남은 연결 수: {len(chat_rooms[room_id])}')
            sys.stdout.flush()


@csrf_exempt
def sync_connect(request, room_id):
    global chat_rooms

    response = StreamingHttpResponse(
        event_stream(room_id),
        content_type="text/event-stream",
    )

    response["Cache-Control"] = "no-cache"
    chat_rooms[room_id].append(response)
    print(f'방 {room_id}에 연결된 클라이언트 수: {len(chat_rooms[room_id])}')
    request.META["wsgi.input_terminated"] = True

    sys.stdout.flush()

    return response


def send_message(room_id, message):
    global chat_rooms
    if room_id in chat_rooms:
        message_queue[room_id].append(message)
    else:
        message_queue[room_id] = [message]
    print(f'방 {room_id}에 메시지 {message}가 추가되었습니다.')
    print(f'방 {room_id}의 메시지 갯수: {len(chat_rooms[room_id])}')
    sys.stdout.flush()


@csrf_exempt
def send_chat_message(request, room_id):
    message = request.POST.get("message", "")
    send_message(room_id, message)
    return JsonResponse({"status": "Message sent"})

