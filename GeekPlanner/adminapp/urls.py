"""
Module for adminapp URLs.
"""
from django.urls import path

import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path(
        'users/',
        adminapp.UserListView.as_view(),
        name='users'
    ),
    # path(
    #     'create_user/<int:pk>/',
    #     adminapp.UserCreateView.as_view(),
    #     name='create_user'
    # ),
    # path(
    #     'read_user/<int:pk>/',
    #     adminapp.UserDetailView.as_view(),
    #     name='read_user'
    # ),
    path(
        'update_user/<int:pk>/',
        adminapp.UserUpdateView.as_view(),
        name='update_user'
    ),
    path(
        'delete_user/<int:pk>/',
        adminapp.UserDeleteView.as_view(),
        name='delete_user'
    ),
    path(
        'projects/',
        adminapp.ProjectListView.as_view(),
        name='projects'
    ),
    # path(
    #     'create_project/',
    #     adminapp.ProjectCreateView.as_view(),
    #     name='create_project'
    # ),
    # path(
    #     'read_project/',
    #     adminapp.ProjectDetailView.as_view(),
    #     name='read_project'
    # ),
    path(
        'update_project/<int:pk>/',
        adminapp.ProjectUpdateView.as_view(),
        name='update_project'
    ),
    path(
        'delete_project/<int:pk>/',
        adminapp.ProjectDeleteView.as_view(),
        name='delete_project'
    ),
]
