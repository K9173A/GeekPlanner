"""
Module for adminapp URLs.
"""
from django.urls import path

import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    # ========================================================================
    # User URLs
    # ========================================================================
    path(
        'users/',
        adminapp.UserListView.as_view(),
        name='users'
    ),
    path(
        'create_user/',
        adminapp.UserCreateView.as_view(),
        name='create_user'
    ),
    path(
        'read_user/<int:pk>/',
        adminapp.UserReadView.as_view(),
        name='read_user'
    ),
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
    # ========================================================================
    # Project URLs
    # ========================================================================
    path(
        'projects/',
        adminapp.ProjectListView.as_view(),
        name='projects'
    ),
    path(
        'create_project/',
        adminapp.ProjectCreateView.as_view(),
        name='create_project'
    ),
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
    # ========================================================================
    # Category URLs
    # ========================================================================
    path(
        'categories/',
        adminapp.CategoryListView.as_view(),
        name='categories'
    ),
    path(
        'create_category/',
        adminapp.CategoryCreateView.as_view(),
        name='create_category'
    ),
    # path(
    #     'update_category/',
    #     adminapp.CategoryEditView.as_view(),
    #     name='update_category'
    # ),
    # path(
    #     'delete_category/',
    #     adminapp.CategoryDeleteView.as_view(),
    #     name='delete_category'
    # )
]
