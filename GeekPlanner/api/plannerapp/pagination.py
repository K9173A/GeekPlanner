"""
Module for plannerapp pagination classes.
"""
from rest_framework.pagination import LimitOffsetPagination


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    """Pagination class for list of project previews."""
    # Amount of items, displayed on one (can be set by user)
    default_limit = 10
    # Maximum amount of items, which can not be exceeded
    max_limit = 100
    # Params names (default)
    limit_query_param = 'limit'
    offset_query_param = 'offset'
