from scipy.stats import gaussian_kde
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import psycopg2

def generate_referee_assignments_graphic(conn):    
    query = """
            SELECT a.nome, COUNT(*) AS qtd_partidas
            FROM equipe_arbitragem ea
            JOIN arbitro a ON a.idarbitro = ea.idarbitro
            JOIN funcaoarbitro f ON f.idfuncaoarbitro = f.idfuncaoarbitro		
            WHERE f.descricao = 'Arbitro'
            GROUP BY a.nome
            ORDER BY qtd_partidas DESC            
            """
    df = pd.read_sql(query, conn).head(50)    

    plt.clf()
    plt.figure(figsize=(12, 8))
    plt.barh(df['nome'], df['qtd_partidas'], color='steelblue')
    plt.xlabel("Quantidade de partidas")
    plt.ylabel("Árbitro")
    plt.title("Árbitros que mais atuaram")
    plt.gca().invert_yaxis()  # Coloca o mais atuante no topo
    plt.tight_layout()
    plt.savefig('./main/static/escalacoes-arbitros.png')

def generate_lineup_players_graphic(conn):
    query = """
            select j.nome, count(*) quantidade_escalacoes
            from escalacao e 
            join jogador j on j.idjogador = e.idjogador            
            group by j.nome
            """

    df = pd.read_sql(query, conn)    

    dados = df['quantidade_escalacoes'].values

    kde = gaussian_kde(dados)
    x = np.linspace(min(dados), max(dados), 1000)
    y = kde(x)

    plt.clf()
    plt.plot(x, y, label="Densidade")
    plt.fill_between(x, y, alpha=0.3)
    plt.title("Densidade de escalações como titular")
    plt.xlabel("Quantidade de escalações")
    plt.ylabel("Densidade")
    plt.grid(True)
    plt.legend()
    plt.savefig('./main/static/escalacoes-jogadores.png')

def generate_team_evolution_graphics(conn):    
    query = """
            select
                ano,
                rodada,
                clube,
                row_number() over (
                    partition by ano, rodada 
                    order by pontos_acumulados desc, gols_acumulados desc, clube asc
                ) as posicao
            from (
                select
                    to_char(data, 'yyyy') as ano,
                    rodada,
                    nome as clube,
                    sum(pontos) over (
                        partition by nome, to_char(data, 'yyyy')
                        order by rodada
                        rows between unbounded preceding and current row
                    ) as pontos_acumulados,
                    sum(gols) over (
                        partition by nome, to_char(data, 'yyyy')
                        order by rodada
                        rows between unbounded preceding and current row
                    ) as gols_acumulados
                from (
                                select
                            j.data,
                            j.rodada,
                            cm.nome,
                            em.gols,
                            case 
                            when em.gols > ev.gols then 3
                            when em.gols < ev.gols then 0
                            else 1
                        end as pontos
                        from cbf.jogo j
                            join cbf.evento em on em.id_jogo = j.id_jogo and em.id_clube = j.id_clube_mandante
                            join cbf.evento ev on ev.id_jogo = j.id_jogo and ev.id_clube = j.id_clube_visitante
                            join cbf.clube cm on cm.id_clube = j.id_clube_mandante

                    union all

                        select
                            j.data,
                            j.rodada,
                            cv.nome,
                            ev.gols,
                            case 
                            when ev.gols > em.gols then 3
                            when ev.gols < em.gols then 0
                            else 1
                        end as pontos
                        from cbf.jogo j
                            join cbf.evento em on em.id_jogo = j.id_jogo and em.id_clube = j.id_clube_mandante
                            join cbf.evento ev on ev.id_jogo = j.id_jogo and ev.id_clube = j.id_clube_visitante
                            join cbf.clube cv on cv.id_clube = j.id_clube_visitante        
                ) as partidas
            ) as acumulado
            where ano in ('2018', '2022', '2023', '2024')
            order by ano, rodada, posicao;
            """

    df = pd.read_sql(query, conn)    

    df['rodada'] = df['rodada'].astype(int)
    df['posicao'] = df['posicao'].astype(int)

    anos = df['ano'].tail(1)

    plt.clf()
    
    plt.figure(figsize=(14, 8))
    for clube in df['clube'].unique():
        dados_clube = df[df['clube'] == clube]
        plt.plot(dados_clube['rodada'], dados_clube['posicao'], label=clube)

    plt.gca().invert_yaxis()  # Posição 1 no topo
    plt.title(f"Evolução da Classificação - {ano}")
    plt.xlabel("Rodada")
    plt.ylabel("Posição")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small', ncol=1)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('./main/static/evolucao-clubes.png')

def generate_graphics():
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='admin',
        host='localhost',
        port='5432'
    )

    generate_referee_assignments_graphic(conn)
    generate_lineup_players_graphic(conn)
    generate_team_evolution_graphics(conn)

    conn.close()