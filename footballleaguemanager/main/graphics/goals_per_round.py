import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import json

def generate_graphic(conn, context):
        plt.clf()

        query = """
        select to_char(j.data, 'yyyy') as ano, j.rodada, sum(e.gols) as total_gols
        from evento e
        join jogo j on (j.id_jogo = e.id_jogo)
        group by to_char(j.data, 'yyyy'), j.rodada
        order by 1,2
        """

        df = pd.read_sql(query, conn)        

        dados_agrupados = [grupo["total_gols"].values for _, grupo in df.groupby("ano")]

        rotulos = df["ano"].unique()

        plt.violinplot(dados_agrupados, showmeans=True, showextrema=True)

        plt.xticks(range(1, len(rotulos) + 1), rotulos, rotation=45)
        plt.xlabel("Ano")
        plt.ylabel("Total de gols por rodada")
        plt.title("Distribuição de gols por rodada e por ano")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('./main/static/gols-por-rodada.jpg')    

        for item in df.values:
                context['dados']['gols_por_rodada'].append({'ano': item[0], 'rodada': item[1], 'total_gols': item[2]})

        gols_por_rodada = []
        for item in df.values:
                gols_por_rodada.append({'ano': item[0], 'rodada': item[1], 'total_gols': item[2]})

        with open("./main/static/gols-por-rodada.json", "w", encoding="utf-8") as f:
                json.dump(gols_por_rodada, f, ensure_ascii=False, indent=4)