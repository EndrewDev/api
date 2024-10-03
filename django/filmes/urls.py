from django.urls import path
from . import views

urlpatterns = [
    path('', views.filmes_view, name='filmes')
]