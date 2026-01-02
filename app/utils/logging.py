from flask import request, g, has_request_context
import logging
import uuid
import pythonjsonlogger.jsonlogger

# Middleware: Request ID 생성 및 Response 헤더 주입
class RequestIDMiddleware:
    def __init__(self, app):
        self.app = app
        self.app.before_request(self.before_request)
        self.app.after_request(self.after_request)

    def before_request(self):
        request_id = request.headers.get("X-Request-ID")
        if not request_id:
            request_id = str(uuid.uuid4())
        g.request_id = request_id

    def after_request(self, response):
        if hasattr(g, "request_id"):
            response.headers["X-Request-ID"] = g.request_id
        return response

# Filter: 로그 레코드에 Request ID 주입
class RequestIdFilter(logging.Filter):
    def filter(self, record):
        if has_request_context() and hasattr(g, "request_id"):
            record.request_id = g.request_id
        else:
            record.request_id = "-"
        return True
