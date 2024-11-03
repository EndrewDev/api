from django.urls import path
from . import views

urlpatterns = [
    path('ator/', views.AtorListCreateView.as_view(), name='ator-list'),
    path('ator/<int:pk>/', views.AtorUpdateDestroy.as_view(), name='ator-update-destroy'),
]