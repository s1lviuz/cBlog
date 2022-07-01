from django.contrib import admin

from .models import Comentario, Post, Seguir


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("descricao_curta", "autor", "criado_em")
    search_fields = [
        "autor",
    ]


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("post", "descricao_curta", "autor", "criado_em")
    search_fields = [
        "autor",
    ]


admin.site.register(Seguir)
