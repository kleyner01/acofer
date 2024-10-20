# admin.py
from django.contrib import admin
from .models import Loja

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'bairro', 'cep', 'telefone')
    search_fields = ('nome', 'bairro')

admin.site.register(Loja, LojaAdmin)
