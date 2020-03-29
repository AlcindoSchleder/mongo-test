# *-* coding: utf-8 *-*
from django.http import QueryDict
from django.utils.deprecation import MiddlewareMixin


class HttpPostConvertMiddleware:

    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = request
        if request.method == 'POST' and hasattr(self, 'process_request'):
            response = self.process_request(request)
        return self.get_response(response)

    def process_request(self, request):
        if request.META.get('HTTP_X_METHODOVERRIDE') is not None:
            http_method = request.META.get('HTTP_X_METHODOVERRIDE')
            if http_method.lower() == 'path':
                request.method = 'PATH'
                request.META['REQUEST_METHOD'] = 'PATH'
                request.PUT = QueryDict(request.body)
            if http_method.lower() == 'put':
                request.method = 'PUT'
                request.META['REQUEST_METHOD'] = 'PUT'
                request.PUT = QueryDict(request.body)
            if http_method.lower() == 'delete':
                request.method = 'DELETE'
                request.META['REQUEST_METHOD'] = 'DELETE'
                request.DELETE = QueryDict(request.body)
        return request
