import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import json

def generate_graphic(conn, context):
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
                        from jogo j
                        join evento em on em.id_jogo = j.id_jogo and em.id_clube = j.id_clube_mandante
                        join evento ev on ev.id_jogo = j.id_jogo and ev.id_clube = j.id_clube_visitante
                        join clube cm on cm.id_clube = j.id_clube_mandante

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
                        from jogo j
                        join evento em on em.id_jogo = j.id_jogo and em.id_clube = j.id_clube_mandante
                        join evento ev on ev.id_jogo = j.id_jogo and ev.id_clube = j.id_clube_visitante
                        join clube cv on cv.id_clube = j.id_clube_visitante        
                ) as partidas
                ) as acumulado
                where ano in ('2018', '2022', '2023', '2024')
                order by ano, rodada, posicao;
                """

        df = pd.read_sql(query, conn)        

        df['rodada'] = df['rodada'].astype(int)
        df['posicao'] = df['posicao'].astype(int)

        anos = df['ano'].unique()
        for ano in sorted(anos):
                dados_ano = df[df['ano'] == ano]

                plt.figure(figsize=(14, 8))
                for clube in dados_ano['clube'].unique():
                        dados_clube = dados_ano[dados_ano['clube'] == clube]
                        plt.plot(dados_clube['rodada'], dados_clube['posicao'], label=clube)

                        plt.gca().invert_yaxis()  # Posição 1 no topo
                        plt.title(f"Evolução da Classificação - {ano}")
                        plt.xlabel("Rodada")
                        plt.ylabel("Posição")
                        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small', ncol=1)
                        plt.tight_layout()
                        plt.grid(True)
                        plt.savefig(f'./main/static/evolucao-clubes-{ano}.jpg')

                        evolucao_clubes = []
                        for item in df.values:
                                if item[0] == str(ano):
                                        evolucao_clubes.append({'ano': item[0], 'rodada': item[1], 'clube': item[2], 'posicao': item[3]})

                        with open(f"./main/static/evolucao-clubes-{ano}.json", "w", encoding="utf-8") as f:
                                json.dump(evolucao_clubes, f, ensure_ascii=False, indent=4)