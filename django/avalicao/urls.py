from django.urls import path
from . import views

urlpatterns = [
    path(
        "avalicoes/", views.AvalicaoListCriaView.as_view(), name='list-create-assessment'
        ),
    path(
        'avalicoes/<int:pk>/', views.AvaliacaoDetelheAtualizarDeletaleView.as_view, name='update-deleta'
        ),
]
