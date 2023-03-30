from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # root url = ''
    path('about', views.about, name='about')
]