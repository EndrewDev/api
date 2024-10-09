from django.urls import path
from . import views

urlpatterns = [
    path('', views.filmes_view, name='filmes'),
    path('detalhes/<int:pk>/', views.view_detalhes_ataulizar_deleta, name='detalhes-filmes'),

]