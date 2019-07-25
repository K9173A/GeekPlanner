"""
Module for plannerapp URLs.
"""
from django.urls import path

import plannerapp.views as plannerapp


app_name = 'plannerapp'

urlpatterns = [
    path(
        'projects/',
        plannerapp.ProjectListView.as_view(),
        name='projects'
    ),
    path(
        'create_project/',
        plannerapp.ProjectCreateView.as_view(),
        name='create_project'
    ),
    path(
        'update_project/<int:pk>/',
        plannerapp.ProjectUpdateView.as_view(),
        name='update_project'
    ),
    path(
        'delete_project/<int:pk>/',
        plannerapp.ProjectDeleteView.as_view(),
        name='delete_project'
    ),
    path(
        'project_details/<int:pk>/',
        plannerapp.ProjectDetailView.as_view(),
        name='project_details'
    ),
    path(
        'create_card/project/<int:project_pk>/category/<int:category_pk>/',
        plannerapp.CardCreateView.as_view(),
        name='create_card'
    ),
    path(
        'delete_card/<int:pk>/project/<int:project_pk>/',
        plannerapp.CardDeleteView.as_view(),
        name='delete_card'
    ),
    path(
        'update_card/<int:pk>/project/<int:project_pk>/',
        plannerapp.CardUpdateView.as_view(),
        name='update_card'
    ),
    path(
        'create_category/<int:pk>/project/<int:project_pk>/',
        plannerapp.CategoryCreateView.as_view(),
        name='create_category',
    ),
    # path(
    #     'update_category/<int:pk>/project/<int:project_pk>/',
    #     plannerapp.CategoryUpdateView.as_view(),
    #     name='update_category',
    # ),
    path(
        'delete_category/<int:pk>/project/<int:project_pk>/',
        plannerapp.CategoryDeleteView.as_view(),
        name='delete_category',
    )
]
