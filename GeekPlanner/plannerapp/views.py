from django.shortcuts import render

from plannerapp.models import Project


def projects(request):
    projects_list = Project.objects.filter(is_active=True)
    context = {
        'title': 'Доступные проекты',
        'projects': projects_list
    }
    return render(request, 'plannerapp/projects.html', context)
