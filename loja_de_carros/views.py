from atexit import register
from django.shortcuts import render
from django.shortcuts import redirect
from loja_de_carros.forms import LoginForm, CadastroForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def contato_view(request):
    return render(request, 'contato.html')

def estoque_view(request):
    return render(request, 'estoque.html')

def sobre_view(request):
    return render(request, 'sobre.html')

def cadastro_view(request):
    if request.POST:
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            request.session['message'] = 'Registro bem sucedido'
            return redirect('/home')
    else: 
        form = CadastroForm()

    return render(request, 'registration/cadastro.html', {'form': form})

def login_view(request):
    return render(request, 'registration/login.html')

def user_login(request):
    user = None
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logado com sucesso")
            return redirect('/home')
        else:
            messages.error(request, "Usuário ou Senha Inválidos")

    else:
        form = LoginForm()

    context = {'form': form}        
    return render(request, 'login.html', context)
    