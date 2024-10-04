from django.urls import path
from . import views

urlpatterns = [
    path('', views.filmes_view, name='filmes'),
    path('detalhe/<int:pk>/', views.detalhe_filme, name='detalhe-filme'),
    path('atualizar/<int:pk>/', views.atualizar_filme, name='atualizar-filme'),
]