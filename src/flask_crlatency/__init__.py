import time 

from flask import request


class RouteLatencyLogger:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(self.app)

    def init_app(self, app):
        app.before_request(self.before_request)
        app.after_request(self.after_request)

    def before_request(self):
        request._start_time = time.time()

    def after_request(self, response):
        if hasattr(request, '_start_time'):
            latency = time.time() - request._start_time
            self.app.logger.info(f'Latency for route {request.endpoint}: {latency:.6f} seconds')
        return response