from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .tables import create_all_tables, drop_all_tables
from .cbf_data import insert_data_from_cbf_json
from .example_data import insert_example_data
import psycopg2


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
        else:
            request.session['tables_created'] = 0
            return redirect('bd')
    except Exception as e:
        messages.error(request, f'Erro ao conectar no banco: {e}')
        return redirect('bd')
    return render(request, 'index.html')


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
                insert_data_from_cbf_json(cur)
                #insert_example_data(cur)
                cur.close()
                conn.close()
                messages.success(request, 'Tabelas criadas com sucesso!')
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
