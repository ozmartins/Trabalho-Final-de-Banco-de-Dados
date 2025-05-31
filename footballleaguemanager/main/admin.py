from django.contrib import admin
from .models import *

admin.site.site_header = "Cadastros do sistema"
admin.site.site_title = "Cadastros do sistema"
admin.site.index_title = "Bem-vindo ao módulo de cadastros"

@admin.register(Arbitro)
class ArbitroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'datanascimento', 'idfederacao')
    search_fields = ('nome',)
    list_filter = ('idfederacao',)    

@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'premiacao', 'idfederacao')
    search_fields = ('nome',)
    list_filter = ('idfederacao',)

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    search_fields = ('nome',)
    list_filter = ('uf',)

admin.site.register(ContratoJogador)
admin.site.register(ContratoTecnico)
admin.site.register(EquipeArbitragem)
admin.site.register(Escalacao)
admin.site.register(Estadio)
admin.site.register(Evento)
admin.site.register(Federacao)
admin.site.register(FuncaoArbitro)
admin.site.register(Jogador)
admin.site.register(Nacionalidade)
admin.site.register(Participacao)
admin.site.register(Partida)
admin.site.register(Posicao)
admin.site.register(Rodada)
admin.site.register(Tecnico)
admin.site.register(Temporada)
admin.site.register(Time)
