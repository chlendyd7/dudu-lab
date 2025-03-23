import sys
import time
from locust import HttpUser, task, between, events

class MessageOnlyUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://127.0.0.1:8000"  # 정확히 Postman과 동일한 URL 사용
    
    @task
    def send_message(self):
        """메시지 전송 (메인 태스크)"""
        message = "helloworld"  # Postman과 동일한 메시지 사용
        
        print(f"Attempting to send message: {message}")
        sys.stdout.flush()
        
        try:
            # Multipart form-data로 전송
            with self.client.post(
                "/lab/chat/test/send/",  # 정확한 URL 사용
                files={'message': (None, message)},  # multipart/form-data 형식으로 전송
                name="/lab/chat/test/send/",
                catch_response=True
            ) as response:
                print(f"Response status: {response.status_code}")
                print(f"Response content: {response.text}")
                sys.stdout.flush()
                
                if response.status_code == 200:
                    response.success()
                    print("Message sent successfully")
                else:
                    response.failure(f"Send failed: {response.status_code}")
        except Exception as e:
            print(f"Send error: {str(e)}")
            sys.stdout.flush()


# locust -f lab/SyncAsyncLab/sync/sync_locust.py --class-picker --host=http://localhost:8000   