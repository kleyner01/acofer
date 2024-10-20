from django.contrib import admin
from .models import Candidato


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'email', 'cpf', 'telefone', 'cidade', 'estado', 'cargo_pretendido')
    search_fields = ('nome', 'email', 'cpf', 'cidade', 'cargo_pretendido')
    list_filter = ('estado_civil', 'sexo', 'estado', 'formacao')
    ordering = ('nome',)

    list_editable = ('telefone', 'cargo_pretendido')

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'telefone', 'celular', 'data_nasc', 'estado_civil', 'sexo', 'foto_perfil')
        }),
        ('Endereço', {
            'fields': ('endereco', 'numero', 'bairro', 'cep', 'cidade', 'estado')
        }),
        ('Documentos', {
            'fields': ('rg', 'cpf')
        }),
        ('Profissão e Formação', {
            'fields': ('cargo_pretendido', 'faixa_salarial_desejada', 'formacao', 'curso', 'ano_conclusao')
        }),
        ('Experiência Atual', {
            'fields': ('empresa_atual', 'segmento_atual', 'cargo_atual', 'data_inicio_atual', 'data_saida_atual', 'atribuicoes_atual')
        }),
        ('Experiência Anterior 1', {
            'fields': ('empresa_anterior_1', 'segmento_anterior_1', 'cargo_anterior_1', 'data_inicio_anterior_1', 'data_saida_anterior_1', 'atribuicoes_anterior_1')
        }),
        ('Experiência Anterior 2', {
            'fields': ('empresa_anterior_2', 'segmento_anterior_2', 'cargo_anterior_2', 'data_inicio_anterior_2', 'data_saida_anterior_2', 'atribuicoes_anterior_2')
        }),
        ('Habilitação e Carteira Profissional', {
            'fields': ('possui_habilitacao', 'tipo_habilitacao', 'possui_carteira_profissional', 'serie_carteira_profissional')
        }),
        ('Outros', {
            'fields': ('mensagem', 'curriculo')
        }),
    )
