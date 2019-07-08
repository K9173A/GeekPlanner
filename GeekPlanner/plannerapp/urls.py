from django.urls import path

import plannerapp.views as plannerapp


app_name = 'plannerapp'

urlpatterns = [
    path('projects/', plannerapp.ProjectListView.as_view(), name='projects'),
    path('create_project/', plannerapp.ProjectCreateView.as_view(), name='create_project'),
    path('update_project/<int:pk>/', plannerapp.ProjectUpdateView.as_view(), name='update_project'),
    path('delete_project/<int:pk>/', plannerapp.ProjectDeleteView.as_view(), name='delete_project'),
]
