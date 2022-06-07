from django.contrib import admin

from .models import Post


@admin.register
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'criado_em')
    search_fields = ['titulo','conteudo']
    prepopulated_fields = {'slug':('titulo',)}

