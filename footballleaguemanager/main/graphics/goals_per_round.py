import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

def generate_graphic(conn):
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