from rest_framework.renderers import JSONRenderer
from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 60
    page_query_param = 'page'


class PrettyJsonRenderer(JSONRenderer):
    def get_indent(self, accepted_media_type, renderer_context):
        return 3
