"""
Module for plannerapp custom permission classes.
Actions:
* POST = CREATE
* PUT/PATCH = UPDATE
* DELETE = DELETE
* GET = RETRIEVE
"""
from django.db.models import Q

from rest_framework import permissions

from .models import Participation, Card


def is_project_owner(project_id, user_id, is_owner=True):
    """
    Checks if the user is an owner of the project.
    :param project_id: project Id.
    :param user_id: user Id.
    :param is_owner: owner flag.
    :return: boolean result of checking.
    """
    participation = Participation.objects.get(
        Q(project_id=project_id) &
        Q(user_id=user_id) &
        Q(is_owner=is_owner)
    )
    return participation is not None


def is_project_participant(project_id, user_id):
    """
    Checks if the user is a participant of the project.
    :param project_id: project Id.
    :param user_id: user Id.
    :return: boolean result of checking.
    """
    participation = Participation.objects.get(
        Q(project_id=project_id) &
        Q(user_id=user_id)
    )
    return participation is not None


class ProjectPermissions(permissions.BasePermission):
    """
    Permissions which restricts project participants from making
    inappropriate actions with Project instances.
    """
    def has_object_permission(self, request, view, obj):
        """
        Checks whether user can modify project object or not.
        :param request: Request object.
        :param view: view object.
        :param obj: object which user tries to modify.
        :return: boolean result of permissions checking.
        """
        # Project admin can delete project
        if request.method in ['DELETE']:
            return is_project_owner(obj.id, request.user.id)
        # Regular participants can modify projects and retrieve its content
        if request.method in ['PATCH', 'PUT', 'GET', 'OPTIONS']:
            return is_project_participant(obj.id, request.user.id)
        # Any other options are not implemented yet, so return False
        return False


class ProjectContentPermissions(permissions.BasePermission):
    """
    Permissions which restricts project participants from making
    inappropriate actions with project content (Categories and Cards).
    """
    def has_object_permission(self, request, view, obj):
        """
        Checks whether user can modify object of project content or not.
        :param request: Request object.
        :param view: view object.
        :param obj: object which user tries to modify.
        :return: boolean result of permissions checking.
        """
        # Both admins and project participants can perform these actions
        if request.method in ['POST', 'PATCH', 'PUT', 'GET', 'DELETE', 'OPTIONS']:
            if isinstance(obj, Card):
                return is_project_participant(obj.project_id, request.user.id)
            # if isinstance(obj, Category):
            #     return None
        return False
