from django.contrib import admin
from .models import *

@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(FormServicos)
class FormServicosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'numero', 'servico', 'data', 'aceita')
    list_filter = ('servico', 'data', 'aceita')
    search_fields = ('nome', 'email', 'detalhes')
    ordering = ('-data',)