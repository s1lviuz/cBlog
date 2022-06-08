from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('descricao_curta', 'autor' , 'criado_em')
    search_fields = ['autor', 'conteudo']

