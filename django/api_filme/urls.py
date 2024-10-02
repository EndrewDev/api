from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='pagina-inicial'),
    path("formulario/", views.formulario, name='formulario'),
    path('json/', views.json, name='json')
]