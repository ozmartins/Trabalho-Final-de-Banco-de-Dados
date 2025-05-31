from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .tables import create_all_tables, drop_all_tables, insert_example_data
import psycopg2

def index(request):    
    return render(request, 'index.html')


def bd(request):
    if request.method == 'POST':
        db_user = request.POST.get('db_user')
        db_password = request.POST.get('db_password')                          
        
        if 'criar_banco' in request.POST:
            try:
                conn = psycopg2.connect(
                    dbname='postgres',
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
                        
            try:                      
                cur.execute("CREATE DATABASE footballleaguemanager")
                cur.close()
                conn.close()
                messages.success(request, 'Banco de dados criado com sucesso!')
            except psycopg2.errors.DuplicateDatabase:
                messages.warning(request, 'O banco de dados já existe.')
            except Exception as e:
                messages.error(request, f'Erro ao criar banco: {e}')

        if 'destruir_banco' in request.POST:
            try:
                conn = psycopg2.connect(
                    dbname='postgres',
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
                     
            try:
                cur.execute("DROP DATABASE footballleaguemanager")
                cur.close()
                conn.close()
                messages.success(request, 'Banco de dados destruído com sucesso!')
            except psycopg2.errors.DatabaseDropped:
                messages.warning(request, 'O banco de dados não existe.')
            except Exception as e:
                messages.error(request, f'Erro ao destruir banco: {e}')
        
        if 'criar_tabelas' in request.POST:
            try:
                conn = psycopg2.connect(
                    dbname='footballleaguemanager',
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
            
            try:
                create_all_tables(cur)
                insert_example_data(cur)
                cur.close()
                conn.close()
                messages.success(request, 'Tabelas criadas com sucesso!')
            except psycopg2.errors.DatabaseDropped:
                messages.warning(request, 'O banco de dados não existe.')
            except Exception as e:
                messages.error(request, f'Erro ao criar tabelas: {e}')

        if 'destruir_tabelas' in request.POST:
            try:
                conn = psycopg2.connect(
                    dbname='footballleaguemanager',
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
