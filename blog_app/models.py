from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatechars


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField(max_length=200, blank=False, null=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    @property
    def descricao_curta(self):
        return truncatechars(self.conteudo, 60)

    def __str__(self):
        return self.descricao_curta

    def get_comentarios(self):
        comentarios = Comentario.objects.filter(post_id=self.pk)
        return comentarios


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    conteudo = models.CharField(max_length=200, blank=False, null=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["criado_em"]

    def __str__(self):
        return self.conteudo

    @property
    def descricao_curta(self):
        return truncatechars(self.conteudo, 60)


class Seguir(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seguindo = models.ManyToManyField(User, related_name="seguindo", blank=True)

    class Meta:
        verbose_name = "Seguir"
        verbose_name_plural = "Seguir"

    def __str__(self):
        seguindo = ", ".join(str(i) for i in self.seguindo.all())
        return "{}".format(seguindo)
