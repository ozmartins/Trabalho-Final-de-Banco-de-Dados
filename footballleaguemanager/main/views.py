from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .tables import create_all_tables, drop_all_tables
from .fill_database import insert_data_from_cbf_datasets
from .graphics import referee_assignments_graphic, lineup_players_graphic, teams_evolution, goals_per_round, games_per_state
from .inteligencia_artificial import ask_gpt
import psycopg2
import os


def index(request):        
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host='localhost',
            port='5432'
        )
            
        cur = conn.cursor()
        cur.execute("SELECT to_regclass('public.campeonato');")
        resultado = cur.fetchone()

        if resultado[0] is not None:
            request.session['tables_created'] = 1
            context = {}
            context['dados'] = {
                'escalacoes_arbitros': [],
                'escalacoes_jogadores': [],
                'evolucao_clubes': [],
                'gols_por_rodada': [],
                'jogos_por_estado': []
                }            
            referee_assignments_graphic.generate_graphic(conn, context)
            lineup_players_graphic.generate_graphic(conn, context)
            teams_evolution.generate_graphic(conn, context)
            goals_per_round.generate_graphic(conn, context)
            games_per_state.generate_graphic(conn, context)
        else:
            request.session['tables_created'] = 0
            return redirect('bd')
        
        cur.close()
        conn.close()
    except Exception as e:
        messages.error(request, f'Erro ao conectar no banco: {e}')
        return redirect('bd')

    return render(request, 'index.html', context)


def bd(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host='localhost',
            port='5432'
        )
            
        cur = conn.cursor()
        cur.execute("SELECT to_regclass('public.campeonato');")
        resultado = cur.fetchone()

        if resultado[0] is not None:
            request.session['tables_created'] = 1
        else:
            request.session['tables_created'] = 0            
    except Exception as e:
        messages.error(request, f'Erro ao conectar no banco: {e}')
        return render(request, 'bd.html')
    
    if request.method == 'POST':
        db_user = request.POST.get('db_user')
        db_password = request.POST.get('db_password')                          
                
        try:
            conn = psycopg2.connect(
                dbname=settings.DATABASES['default']['NAME'],
                user=db_user,
                password=db_password,
                host='localhost',
                port='5432'
            )
            
            conn.autocommit = True
            cur = conn.cursor()
        except Exception as e:
            messages.error(request, f'Erro ao conectar no banco: {e}')
            return redirect('bd')

        if 'criar_tabelas' in request.POST:            
            try:
                create_all_tables(cur)
                insert_data_from_cbf_datasets(conn, cur)
                cur.close()
                conn.close()
                messages.success(request, 'Tabelas criadas com sucesso!')
                return redirect('/admin')
            except psycopg2.errors.DatabaseDropped:
                messages.warning(request, 'O banco de dados não existe.')
            except Exception as e:
                messages.error(request, f'Erro ao criar tabelas: {e}')

        if 'destruir_tabelas' in request.POST:                        
            try:                      
                drop_all_tables(cur)
                cur.close()
                conn.close()
                messages.success(request, 'Tabelas destruídas com sucesso!')
            except psycopg2.errors.DatabaseDropped:
                messages.warning(request, 'O banco de dados não existe.')
            except Exception as e:
                messages.error(request, f'Erro ao destruir tabelas: {e}')
        
        return redirect('bd')
    
    return render(request, 'bd.html')

def llm(request):
    if 'perguntar' in request.POST:            
        try:
            year = request.POST.get('year')
            round = request.POST.get('round')
            question = request.POST.get('question')
            if (question == "" or year == "" or round == ""):
                messages.error(request, 'Informe todos os campos do formulário')
            messages.success(request, ask_gpt(year, round, question))                    
        except Exception as e:
            messages.error(request, f'Erro na comunição com o LLM: {e}')

    return render(request, 'llm.html')
