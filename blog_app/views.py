from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from user_app.forms import UserChangeForm, UserCreationForm, UserLogInForm
from user_app.models import User

from .forms import PostForm
from .models import Post


class PostDetail(generic.DetailView):
    model = Post
    template_name: 'index.html'


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'blog_app/login.html',
           {})

def home(request):
    if request.user.is_authenticated:
        colaboradores = User.objects.all()
        eu = request.user.get_username()
        meusposts = Post.objects.filter(autor__username__contains=eu).order_by('-criado_em')
        return render(request, 'blog_app/home.html',
           {'colaboradores':colaboradores, 'meusposts':meusposts})
    else:
        raise Http404

def minhaconta(request):
    colaboradores = User.objects.all()
    if request.user.is_authenticated:
        form = UserChangeForm(instance=request.user)
        return render(request, 'blog_app/minhaConta.html',
            {'form': form, 'colaboradores':colaboradores})
    else:
        raise Http404

def publicarPost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                candidate = form.save(commit=False)
                candidate.autor = User.objects.get(username=request.user.get_username())
                candidate.save()
                return HttpResponseRedirect(reverse('home'))
            else:
               raise Http404
        else:
            raise Http404
    else:
        raise Http404

def perfilColaborador(request, username):
    if request.user.is_authenticated:
        colaboradores = User.objects.all()
        posts = Post.objects.filter(autor__username__contains=username).order_by('-criado_em')
        return render(request, 'blog_app/perfilcolab.html',
            {'posts':posts, 'colaboradores':colaboradores})
    else:
        raise Http404



#Cadastro e Login de usuários

def cadastro(request,):
    return render(request, 'blog_app/cadastro.html',
           {})

def cadastrar(request):
    dados={}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        erros = form.check()
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuário criado com Sucesso!')
            return HttpResponseRedirect(reverse('Sucesso'))
        else:
            dados['form'] = form
            messages.error(request, erros)
            return render(request, 'blog_app/cadastro.html', dados)
    else:
        messages.error(request, erros)
        dados = UserCreationForm()
        return render(request, 'blog_app/cadastro.html', dados)

def cadastroSucesso(request):
    if request.user.is_authenticated:
        return render(request, 'blog_app/cadastroSucesso.html',
           {})
    else:
        raise Http404

def entrar(request):
    if request.method == "POST":
        form = UserLogInForm(request.POST)
        erros = form.check()
        if erros == 0:
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))  
                messages.error(request, 'login incorreto')
        else:
            messages.error(request, erros)                        
    else:
        pass
    return redirect('index')

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