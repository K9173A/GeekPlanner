from django.urls import path

import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.IndexView.as_view(), name='index'),
]