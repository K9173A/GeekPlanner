from django.shortcuts import render


def index(request):
    context = {
        'title': 'IndexPage'
    }
    return render(request, 'mainapp/index.html', context)
