from django.db import models
from django.template.defaultfilters import truncatechars

from user_app.models import User


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    conteudo = models.TextField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    
    def __str__(self):
        return str(self.pk) + ' post de ' + self.autor.get_username()

    @property
    def descricao_curta(self):
        return truncatechars(self.conteudo, 60) 


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    conteudo = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    
    def __str__(self):
        return self.titulo