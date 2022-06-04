from django.db import models

from user_app.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    editado_em = models.DateTimeField(auto_now=True)
    conteudo = models.TextField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    
    def __str__(self):
        return self.titulo