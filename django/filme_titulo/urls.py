from django.urls import path
from . import views

urlpatterns = [
    path('filmetitulo/', views.FilmeListaCriaView.as_view(), name='filmetitulo-list'),
    path('filmetitulo/<int:pk>/', views.FilmeDetalhaAtualizaDeletaView.as_view(), name='filmetitulo-updatedestroy'),
]