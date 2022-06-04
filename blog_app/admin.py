from django.contrib import admin
from setuptools import sic

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'status', 'criado_em')
    list_filter = ('status',)
    search_fields = ['titulo','conteudo']
    prepopulated_fields = {'slug':('titulo',)}


admin.site.register(Post, PostAdmin)