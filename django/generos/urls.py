from django.urls import path
from . import views


urlpatterns = [
    path("generos/", views.GeneroCreateListView.as_view(), name="cria-lista-generos"),
    path(
        "generos/<int:pk>/",
        views.GeneroDetalhaAtualizaDeletaView.as_view(),
        name="detalha-atualiza-genero",
    ),
]