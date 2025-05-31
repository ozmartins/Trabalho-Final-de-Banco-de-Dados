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

@admin.register(ContratoJogador)
class ContratoJogadorAdmin(admin.ModelAdmin):
    list_display = ('numero', 'idjogador', 'idtime', 'dataassinatura', 'datarescisao', 'multarescisoria')
    search_fields = ('numero',)
    list_filter = ('idjogador', 'idtime')

@admin.register(ContratoTecnico)
class ContratoTecnicoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'idtecnico', 'idtime', 'dataassinatura', 'datarescisao', 'multarescisoria')
    search_fields = ('numero',)
    list_filter = ('idtecnico', 'idtime')

@admin.register(EquipeArbitragem)
class EquipeArbitragemAdmin(admin.ModelAdmin):
    list_display = ('idpartida', 'idarbitro', 'idfuncaoarbitro')    
    list_filter = ('idarbitro', 'idfuncaoarbitro')

@admin.register(Escalacao)
class EscalacaoAdmin(admin.ModelAdmin):
    list_display = ('idpartida', 'idjogador', 'idposicao')
    list_filter = ('idjogador', 'idposicao')

@admin.register(Estadio)
class EstadioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'capacidade', 'idcidade')
    search_fields = ('nome',)
    list_filter = ('idcidade',)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('tipoevento', 'minuto', 'idpartida', 'idjogador')    
    list_filter = ('idpartida', 'idjogador')

@admin.register(Federacao)
class FederacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    search_fields = ('nome',)
    list_filter = ('uf',)

@admin.register(FuncaoArbitro)
class FuncaoArbitroAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)    

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'datanascimento', 'idnacionalidade', 'idposicao')
    search_fields = ('nome',)
    list_filter = ('idnacionalidade', 'idposicao')

@admin.register(Nacionalidade)
class NacionalidadeAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)    

@admin.register(Participacao)
class ParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('idtime', 'idtemporada')
    list_filter = ('idtime', 'idtemporada')

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ('datahora', 'publico', 'renda', 'idrodada', 'idestadio', 'idtimemandante', 'idtimevisitante')
    search_fields = ('numero',)
    list_filter = ('idrodada', 'idestadio', 'idtimemandante', 'idtimevisitante')

@admin.register(Posicao)
class PosicaoAdmin(admin.ModelAdmin):
    list_display = ('idposicao', 'descricao')
    search_fields = ('descricao',)    

@admin.register(Rodada)
class RodadaAdmin(admin.ModelAdmin):
    list_display = ('numerorodada', 'idtemporada')
    search_fields = ('numerorodada',)
    list_filter = ('idtemporada',)

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'datanascimento', 'idnacionalidade')
    search_fields = ('nome',)
    list_filter = ('idnacionalidade',)

@admin.register(Temporada)
class TemporadaAdmin(admin.ModelAdmin):
    list_display = ('quantidaderodadas', 'datainicio', 'datafim', 'ano', 'idcampeonato')
    list_filter = ('ano', 'idcampeonato')

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idcidade')
    search_fields = ('nome',)
    list_filter = ('idcidade',)