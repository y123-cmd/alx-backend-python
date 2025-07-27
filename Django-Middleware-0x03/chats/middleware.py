# chats/middleware.py

from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        path = request.path
        timestamp = datetime.now()

        with open('requests.log', 'a') as log_file:
            log_file.write(f"{timestamp} - User: {user} - Path: {path}\n")

        response = self.get_response(request)
        return response
