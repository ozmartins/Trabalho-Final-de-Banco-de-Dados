from django.contrib import admin
from .models import *

admin.site.site_header = "Cadastros do sistema"
admin.site.site_title = "Cadastros do sistema"
admin.site.index_title = "Bem-vindo ao módulo de cadastros"

@admin.register(Arbitro)
class ArbitroAdmin(admin.ModelAdmin):
    list_display = ('id_arbitro', 'nome', 'uf', 'categoria')
    search_fields = ('nome',)
    list_filter = ('uf','categoria')    

@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('id_campeonato', 'nome')
    search_fields = ('nome',)    

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id_cidade', 'nome', 'uf')
    search_fields = ('nome',)
    list_filter = ('uf',)

@admin.register(EquipeArbitragem)
class EquipeArbitragemAdmin(admin.ModelAdmin):
    list_display = ('id_equipe_arbitragem', 'id_jogo', 'id_arbitro', 'funcao')    
    list_filter = ('funcao',)

@admin.register(Escalacao)
class EscalacaoAdmin(admin.ModelAdmin):
    list_display = ('id_escalacao', 'id_jogo', 'id_clube', 'id_atleta', 'numero_camisa', 'reserva', 'goleiro', 'entrou_jogando')
    list_filter = ('id_jogo', 'id_clube', 'id_atleta', 'reserva', 'goleiro', 'entrou_jogando')

@admin.register(Estadio)
class EstadioAdmin(admin.ModelAdmin):
    list_display = ('id_estadio', 'nome', 'id_cidade')
    search_fields = ('nome',)
    list_filter = ('id_cidade',)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id_jogo', 'id_clube', 'gols', 'penaltis')
    list_filter = ('id_jogo', 'id_clube', 'penaltis')

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ('id_atleta', 'nome', 'apelido', 'foto')
    search_fields = ('nome', 'apelido')    

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('id_jogo', 'num_jogo', 'rodada', 'data', 'hora', 'qtd_alteracoes_jogo', 'id_estadio', 'id_clube_mandante', 'id_clube_visitante')
    list_filter = ('rodada', 'data', 'hora', 'id_estadio', 'id_clube_mandante', 'id_clube_visitante')

@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ('id_clube', 'nome', 'url_escudo')
    search_fields = ('nome',)    

@admin.register(Alteracao)
class AlteracaoAdmin(admin.ModelAdmin):
    list_display = ('id_alteracao', 'id_jogo', 'id_clube', 'codigo_jogador_saiu', 'codigo_jogador_entrou', 'tempo_jogo', 'tempo_subs', 'tempo_acrescimo')
    list_filter = ('id_jogo', 'id_clube', 'codigo_jogador_saiu', 'codigo_jogador_entrou', 'tempo_subs')

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id_documento', 'url', 'title', 'id_jogo')
    search_fields = ('title',)
    list_filter = ('id_jogo',)

@admin.register(Penalidade)
class PenalidadeAdmin(admin.ModelAdmin):
    list_display = ('id_penalidade', 'id_jogo', 'id_clube', 'id_atleta', 'tipo', 'resultado', 'tempo_jogo', 'minutos')
    list_filter = ('id_jogo', 'id_clube', 'id_atleta', 'id_penalidade', 'tipo', 'resultado')