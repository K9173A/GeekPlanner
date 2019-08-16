"""
Module for plannerapp pagination classes.
"""
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class ProjectPageNumberPagination(PageNumberPagination):
    """Pagination class for list of project previews."""
    page_size = 10
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
            'total_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
        })
