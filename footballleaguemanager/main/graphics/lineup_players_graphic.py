import matplotlib
matplotlib.use('Agg')

from scipy.stats import gaussian_kde
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

def generate_graphic(conn, context):
    plt.clf()

    query = """
            select a.nome, count(*) quantidade_escalacoes
            from escalacao e 
            join atleta a on a.id_atleta = e.id_atleta
            where entrou_jogando = true
            group by a.nome
            """

    df = pd.read_sql(query, conn)

    dados = df['quantidade_escalacoes'].values

    kde = gaussian_kde(dados)
    x = np.linspace(min(dados), max(dados), 1000)
    y = kde(x)
        
    plt.plot(x, y, label="Densidade")
    plt.fill_between(x, y, alpha=0.3)
    plt.title("Densidade de escalações como titular")
    plt.xlabel("Quantidade de escalações")
    plt.ylabel("Densidade")
    plt.grid(True)
    plt.legend()    
    plt.savefig('./main/static/escalacoes-jogadores.jpg')    
        
    escalacoes_jogadores = []
    for item in df.sort_values(by='quantidade_escalacoes').values:
        escalacoes_jogadores.append({'nome': item[0], 'quantidade_escalacoes': item[1]})

    with open("./main/static/escalacoes-jogadores.json", "w", encoding="utf-8") as f:
        json.dump(escalacoes_jogadores, f, ensure_ascii=False, indent=4)