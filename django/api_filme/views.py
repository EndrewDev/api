from django.shortcuts import render, redirect
from .forms import FilmeModelForm
from .models import FILME
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')

def formulario(request):
    if request.method == 'POST':
        formulario = FilmeModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('pagina-inicial')
    else:
        formulario = FilmeModelForm()
    return render(request, 'formulario.html', {'formulario': formulario})

def json(request):
    filmes = FILME.objects.all()
    data = [{'id': filme.id, 'nome': filme.nome} for filme in filmes]
    return JsonResponse(data, safe=False)