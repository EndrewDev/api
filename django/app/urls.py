from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('generos.urls')),
    path('', include('atores.urls')),
    path('', include('filme_titulo.urls')),
]