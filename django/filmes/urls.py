from django.urls import path
from . import views

urlpatterns = [
    path('filmes/', views.FilmeCreateListView.as_view(), name='filmes'),
    path('filmes/<int:pk>/', views.FilmeDetalheAtualizarDeletaView.as_view(), name='detalhes-filmes'),
]