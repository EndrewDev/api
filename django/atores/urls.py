from django.urls import path
from . import views

urlpatterns = [
    path('atores/', views.AtorListCreate.as_view(), name='ator-list'),
    path('atores/<int:pk>/', views.AtorRestrieveUpdateDestroy.as_view(), name='update-destroy'),
]