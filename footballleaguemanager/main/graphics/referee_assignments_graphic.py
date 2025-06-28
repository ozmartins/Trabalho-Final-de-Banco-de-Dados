import pandas as pd
import matplotlib.pyplot as plt

def generate_graphic(conn):
    plt.clf()

    query = """
            SELECT a.nome, COUNT(*) AS qtd_partidas
            FROM equipe_arbitragem ea
            JOIN arbitro a ON a.id_arbitro = ea.id_arbitro
            WHERE funcao = 'Arbitro'
            GROUP BY a.nome
            ORDER BY qtd_partidas DESC
            """

    df = pd.read_sql(query, conn)    

    df = df.head(50)
    
    plt.figure(figsize=(12, 8))
    plt.barh(df['nome'], df['qtd_partidas'], color='steelblue')
    plt.xlabel("Quantidade de partidas")
    plt.ylabel("Árbitro")
    plt.title("Árbitros que mais atuaram")
    plt.gca().invert_yaxis()  # Coloca o mais atuante no topo
    plt.tight_layout()        
    plt.savefig('./main/static/escalacoes-arbitros.jpg')