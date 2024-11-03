from django.urls import path
from . import views


urlpatterns = [
    path('generos/', views.GenerosListCreateView.as_view(), name='generos-list'),
    path('generos/<int:pk>/', views.GenerosUpdateDestroyView.as_view(), name='generos-update-destroy')
]