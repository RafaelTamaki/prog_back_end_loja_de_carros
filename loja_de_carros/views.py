from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def contato_view(request):
    return render(request, 'contato.html')

def carrosnovos_view(request):
    return render(request, 'carrosnovos.html')

def carrosusados_view(request):
    return render(request, 'carrosusados.html')

def sobre_view(request):
    return render(request, 'sobre.html')