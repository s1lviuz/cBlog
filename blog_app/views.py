from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from user_app.forms import UserCreationForm, UserLogInForm, UserChangeForm

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-criado_em')
    template_name: 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name: 'index.html'


def cadastrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuário criado com Sucesso!')
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()   
    return render(request, 'blog_app/cadastro.html', {'form': form})


def entrar(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = UserLogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Sucesso!')
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, 'Usuario ou senha incorretos')
    else:
        form = UserLogInForm()
    messages.error(request, 'Usuario ou senha incorretos')
    return render(request, 'blog_app/minhaConta.html',
           {'form': form})

def alterar(request):
    if request.method == 'POST':
        form = UserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações Salvas')
            return HttpResponseRedirect(reverse('Minha Conta'))
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog_app/minhaConta.html',
           {'form': form})

def sair(request):
    logout(request)
    messages.success(request, 'Usuario saiu com sucesso!')
    return HttpResponseRedirect(reverse('index'))

def index(request):
    return render(request, 'blog_app/login.html',
           {})

def home(request):
    return render(request, 'blog_app/pubPerfil.html',
           {})

def cadastro(request):
    return render(request, 'blog_app/cadastro.html',
           {})

def minhaconta(request):
    form = UserChangeForm(instance=request.user)
    return render(request, 'blog_app/minhaConta.html',
           {'form': form})