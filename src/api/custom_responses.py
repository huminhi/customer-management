from rest_framework import pagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # data['status'] = renderer_context['response'].status_code
        # data['error'] = renderer_context['response'].exception
        # data['message'] = 'success'
        return super(CustomJSONRenderer, self).render(data, accepted_media_type, renderer_context)


class CustomPagination(pagination.LimitOffsetPagination):
    limit_query_param = 'length'
    offset_query_param = 'start'

    def get_paginated_response(self, data):
        return Response({
            'total': self.count,
            'nextPage': self.get_next_link(),
            'previousPage': self.get_previous_link(),
            'data': data
        })
