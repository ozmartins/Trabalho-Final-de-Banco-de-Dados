import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import os
import requests

def generate_graphic(conn, context):
        plt.clf()

        query = """
                select c.uf, count(*) as qtd
                from jogo j
                join estadio e on e.id_estadio = j.id_estadio
                join cidade c on c.id_cidade = e.id_cidade
                group by c.uf
                """
        
        df = pd.read_sql(query, conn)

        ufs = df['uf'].values
        jogos = df['qtd'].values

        dados_jogos = pd.DataFrame({
                'uf': ufs,
                'qtd_jogos': jogos
        })
        
        url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
        filename = "brazil-states.geojson"
        
        if not os.path.exists(filename):
                with open(filename, 'wb') as f:
                        f.write(requests.get(url).content)
        
        estados = gpd.read_file(filename)

        estados['uf'] = estados['name'].map({
                'Acre': 'AC', 
                'Alagoas': 'AL', 
                'Amapá': 'AP', 
                'Amazonas': 'AM',
                'Bahia': 'BA', 
                'Ceará': 'CE', 
                'Distrito Federal': 'DF', 
                'Espírito Santo': 'ES',
                'Goiás': 'GO', 
                'Maranhão': 'MA', 
                'Mato Grosso': 'MT', 
                'Mato Grosso do Sul': 'MS',
                'Minas Gerais': 'MG', 
                'Pará': 'PA', 
                'Paraíba': 'PB', 
                'Paraná': 'PR',
                'Pernambuco': 'PE', 
                'Piauí': 'PI', 
                'Rio de Janeiro': 'RJ', 
                'Rio Grande do Norte': 'RN',
                'Rio Grande do Sul': 'RS', 
                'Rondônia': 'RO', 
                'Roraima': 'RR', 
                'Santa Catarina': 'SC',
                'São Paulo': 'SP', 
                'Sergipe': 'SE', 
                'Tocantins': 'TO'
        })        

        estados = estados.merge(dados_jogos, on='uf', how='left')
        estados['qtd_jogos'] = estados['qtd_jogos'].fillna(0)

        _, ax = plt.subplots(figsize=(12, 10))
        estados.plot(
        column='qtd_jogos',
        cmap='OrRd',
        linewidth=0.8,
        edgecolor='black',
        legend=True,
        ax=ax
        )

        ax.set_title('Quantidade de Jogos por Estado', fontsize=16)
        ax.axis('off')
        
        plt.savefig('./main/static/jogos-por-estados.jpg')

        for item in df.values:
                context['dados']['jogos_por_estado'].append({'uf': item[0], 'qtd': item[1]})