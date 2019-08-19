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
            'next': self.get_next_page_number(),
            'curr': self.page.number,
            'prev': self.get_previous_page_number(),
            'results': data,
            'total_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
        })

    def get_next_page_number(self):
        if self.page.has_next():
            return self.page.next_page_number()
        return None

    def get_previous_page_number(self):
        if self.page.has_previous():
            return self.page.previous_page_number()
        return None
