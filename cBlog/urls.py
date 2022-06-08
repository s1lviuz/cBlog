"""cBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from blog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name="Cadastro"),
    path('cadastro/cadastrar/', views.cadastrar, name="Cadastrar"),
    path('cadastro/sucesso/', views.cadastroSucesso, name="Sucesso"),
    path('entrar/', views.entrar, name="Login"),
    path('home/', views.home, name="home"),
    path('minhaConta/', views.minhaconta, name="Minha Conta" ),
    path('minhaConta/alterar/', views.alterar, name="Alterar Conta" ),
    path('sair/', views.sair, name="sair"),
    path('colaborador/<str:username>/', views.perfilColaborador, name="Perfil Colaborador"),
    path('publicar/', views.publicarPost, name="Publicar post"),

]
