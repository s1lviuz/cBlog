from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView

from .forms import ComentarioForm, PostForm, SeguirForm, UserCreationForm
from .models import Comentario, Post, Seguir


class HomePageView(LoginRequiredMixin, ListView):
    model = Post
    login_url = "login"
    template_name = "blog_app/home.html"
    paginate_by = 30

    def get_queryset(self):
        seguindo = Seguir.objects.filter(user=self.request.user).values("seguindo")
        tupla_seguindo_id = []
        for i in seguindo:
            tupla_seguindo_id.append(i["seguindo"])
        return Post.objects.filter(autor__in=tupla_seguindo_id)


class UserCreationView(FormView):
    template_name = "registration/cadastro.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("cadastro_sucesso")


class UserCreationSucessView(TemplateView):
    template_name = "registration/cadastroSucesso.html"


class PostCreationView(LoginRequiredMixin, FormView):
    login_url = "login"
    template_name = "blog_app/publicarPost.html"
    form_class = PostForm

    def form_valid(self, form):
        form = form.save(commit=False)
        form.autor = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "perfil_usuario",
            kwargs={"username": self.request.user.get_username()},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_old"] = self.request.POST
        return context


class UserPostsView(ListView, FormView):
    model = Post
    form_class = SeguirForm
    template_name = "blog_app/perfilusuario.html"
    paginate_by = 30

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        queryset_perfil = User.objects.get(username=self.kwargs["username"])
        form.save()
        form.seguindo.add(queryset_perfil)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["usuario"] = User.objects.get(username=self.kwargs["username"])
            segue = False
            seguindo = Seguir.objects.filter(user=self.request.user)
            seguindo_string = seguindo.__str__()
            perfil = User.objects.get(username=self.kwargs["username"])
            username = perfil.get_username()
            if username in seguindo_string:
                segue = True
            context["segue"] = segue
        except:
            pass
        return context

    def get_queryset(self):
        return Post.objects.filter(autor__username=self.kwargs["username"])

    def get_success_url(self):
        return reverse(
            "perfil_usuario",
            kwargs={"username": self.kwargs["username"]},
        )


class ComentarioCreationView(LoginRequiredMixin, FormView, ListView):
    login_url = "login"
    template_name = "blog_app/postDetalhes.html"
    form_class = ComentarioForm
    Model = Comentario
    paginate_by = 30

    def form_valid(self, form):
        form = form.save(commit=False)
        form.autor = self.request.user
        form.post = Post.objects.get(pk=self.kwargs["pk"])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "post_detalhes",
            kwargs={"pk": self.kwargs["pk"], "username": self.kwargs["username"]},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.get(pk=self.kwargs["pk"])
        return context

    def get_queryset(self):
        return Comentario.objects.filter(post__pk=self.kwargs["pk"])
