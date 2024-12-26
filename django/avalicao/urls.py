from django.urls import path
from . import views

urlpatterns = [
    path(
        "avalicao/", views.AvalicaoListCriaView.as_view(), name='list-create-assessment'
        ),
    path(
        'avalicao/<int:pk>/', views.AvaliacaoDetelheAtualizarDeletaleView.as_view, name='update-deleta'
        ),
]
