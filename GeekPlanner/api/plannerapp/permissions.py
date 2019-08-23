"""
Module for plannerapp custom permission classes.
"""
from django.db.models import Q

from rest_framework import permissions

from .models import (
    Project,
    Card,
    Category,
    Participation,
)


class ProjectPermissions(permissions.BasePermission):
    """
    Permissions allows to delete/modify project information
    only for its owner.
    """
    def has_object_permission(self, request, view, obj):
        """
        Checks whether user can modify project objects (categories and cards)
        or not.
        :param request: request object.
        :param view: view object.
        :param obj: object which user tries to modify.
        :return: boolean result of permissions checking.
        """
        # Modification/Deleting of Projects is allowed only for owners
        if request.method in ['POST', 'PATCH', 'PUT', "DELETE"]:
            participation = Participation.objects.get(
                Q(project=obj.id) &
                Q(user=request.user) &
                Q(is_owner=True)
            )
            return participation is not None
        elif request.method in ['GET']:
            return True
        else:
            return False


class ProjectDataPermissions(permissions.BasePermission):
    """
    Permissions which allow users to modify content when they
    are part of a project.
    """
    def has_object_permission(self, request, view, obj):
        # Modification/Deleting of Cards
        if isinstance(obj, Card):
            participation = Participation.objects.get(
                Q(project=obj.project) &
                Q(user=request.user)
            )
            return participation is not None
        # Modification/Deleting of Categories (currently unavailable)
        elif isinstance(obj, Category):
            participation = Participation.objects.get(
                Q(project=obj.projects) &
                Q(user=request.user)
            )
            return participation is not None
        else:
            return False