


import time

from django.http import HttpResponse



class TimeOfResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        timestamp = time.monotonic()

        return HttpResponse(f'X-Request-Timing: {time.monotonic() - timestamp}')