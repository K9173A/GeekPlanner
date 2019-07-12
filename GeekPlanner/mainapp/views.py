from django.shortcuts import render
from django.views import View


class IndexPageView(View):
    template_name = 'mainapp/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Главная'})
