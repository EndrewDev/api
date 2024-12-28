from django.urls import path
from . import views

urlpatterns = [
    path(
        'filmes/', views.FilmeListCreateView.as_view(), name='filmes-list'
        ),
    path(
        'filmes/<int:pk>/', views.FilmeUpdateDestroy.as_view(), name='filmes-update-destroy'
        ),
]