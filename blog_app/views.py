from xml.etree.ElementInclude import include

from django.shortcuts import render
from django.views import generic

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-criado_em')
    template_name: 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name: 'index.html'


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
    return render(request, 'blog_app/minhaConta.html',
           {})