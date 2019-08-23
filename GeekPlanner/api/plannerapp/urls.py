"""
Module for plannerapp URLs.
"""
from django.urls import path

import api.plannerapp.views as planner_api


app_name = 'plannerapp'

urlpatterns = [
    path(
        'projects/',
        planner_api.ProjectListAPIView.as_view(),
        name='projects'
    ),
    path(
        'participate_project/<int:pk>/',
        planner_api.set_project_participation,
        name='participate_project',
    ),
    path(
        'create_project/',
        planner_api.ProjectCreateAPIView.as_view(),
        name='create_project'
    ),
    path(
        'project_details/<int:pk>/',
        planner_api.ProjectRetrieveAPIView.as_view(),
        name='project_details'
    ),
    path(
        'update_project/<int:pk>/',
        planner_api.ProjectUpdateAPIView.as_view(),
        name='update_project'
    ),
    path(
        'delete_project/<int:pk>/',
        planner_api.ProjectDestroyAPIView.as_view(),
        name='delete_project'
    ),
    # path(
    #     'create_card/project/<int:project_pk>/category/<int:category_pk>/',
    #     planner_api.CardCreateView.as_view(),
    #     name='create_card'
    # ),
    # path(
    #     'delete_card/<int:pk>/',
    #     planner_api.CardDeleteView.as_view(),
    #     name='delete_card'
    # ),
    # path(
    #     'update_card/<int:pk>/project/<int:project_pk>/',
    #     planner_api.CardUpdateView.as_view(),
    #     name='update_card'
    # ),
]
