import json
from pathlib import Path

def insert_data_from_cbf_datasets(conn, cur):
    cur.execute("DELETE FROM penalidade")
    cur.execute("DELETE FROM evento")
    cur.execute("DELETE FROM equipe_arbitragem")
    cur.execute("DELETE FROM arbitro")
    cur.execute("DELETE FROM alteracao")
    cur.execute("DELETE FROM documento")
    cur.execute("DELETE FROM escalacao")
    cur.execute("DELETE FROM jogo")
    cur.execute("DELETE FROM clube")
    cur.execute("DELETE FROM atleta")
    cur.execute("DELETE FROM estadio")
    cur.execute("DELETE FROM cidade")
    cur.execute("DELETE FROM campeonato")

    round = 38
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

    for year in years:    
        for round in range(round):        
            if Path(f'./main/datasets/{year}.{round+1}.json').exists():
                print(f'Processamento rodada {round+1} de {year}...')
                with open(f'./main/datasets/{year}.{round+1}.json', 'r', encoding='utf-8') as file:
                    dataset = json.load(file)
                    
                    jogos = dataset['jogos'][0]['jogo']

                    for jogo in jogos:
                        cur.execute(f"""
                                    INSERT INTO campeonato(id_campeonato, nome) 
                                    VALUES (1, '{jogos[0]['campeonato']}')
                                    ON CONFLICT (nome) DO NOTHING
                                    """)    

                        cur.execute(f"""
                                    INSERT INTO cidade(nome, uf) VALUES ('{jogo['cidade']}', '{jogo['uf']}')
                                    ON CONFLICT (nome) DO NOTHING
                                    """)
                        
                        cur.execute(f"""
                                    INSERT INTO estadio(nome, id_cidade) 
                                    VALUES ('{jogo['estadio']}', (select id_cidade from cidade where nome = '{jogo['cidade']}'))
                                    ON CONFLICT (nome) DO NOTHING
                                    """)
                        
                        cur.execute(f"""
                                    INSERT INTO clube(
                                    id_clube, nome, url_escudo)
                                    VALUES 
                                    (
                                        {jogo['mandante']['id']},
                                        '{jogo['mandante']['nome']}',
                                        '{jogo['mandante']['url_escudo']}'                            
                                    )
                                    ON CONFLICT (id_clube) DO NOTHING
                                    """)
                                            
                        cur.execute(f"""
                                    INSERT INTO clube(
                                    id_clube, nome, url_escudo)
                                    VALUES 
                                    (
                                        {jogo['visitante']['id']},
                                        '{jogo['visitante']['nome']}',
                                        '{jogo['visitante']['url_escudo']}'                            
                                    )
                                    ON CONFLICT (id_clube) DO NOTHING
                                    """)
                        
                        data_jogo = jogo['data'].strip().replace('/','')
                        data_jogo = data_jogo[4:8]+'-'+data_jogo[2:4]+'-'+data_jogo[0:2]
                        hora_jogo = '0001-01-01 '+jogo['hora']
                        
                        cur.execute(f"""
                                    INSERT INTO jogo
                                    (
                                        id_jogo, 
                                        num_jogo, 
                                        rodada, 
                                        grupo, 
                                        data, 
                                        hora, 
                                        qtd_alteracoes_jogo, 
                                        id_campeonato, 
                                        id_estadio,
                                        id_clube_mandante,
                                        id_clube_visitante
                                    )
                                    VALUES 
                                    (
                                        {jogo['id_jogo']},
                                        {jogo['num_jogo']},
                                        {jogo['rodada']},
                                        '{jogo['grupo']}', 
                                        '{data_jogo}',
                                        '{hora_jogo}', 
                                        {jogo['qtd_alteracoes_jogo']},
                                        1,
                                        (select id_estadio from estadio where nome = '{jogo['estadio']}'),
                                        {jogo['mandante']['id']},
                                        {jogo['visitante']['id']}                                    
                                    )       
                                    ON CONFLICT (id_jogo) DO NOTHING
                                    """)
                        
                        for arbitro in jogo['arbitros']:
                            cur.execute(f"""
                                        INSERT INTO arbitro(id_arbitro, nome, uf, categoria)
                                        VALUES
                                        (
                                        {arbitro['id']},
                                        '{arbitro['nome']}',
                                        '{"" if arbitro['uf'] == None else arbitro['uf']}',
                                        '{arbitro['categoria']}'
                                        )
                                        ON CONFLICT (id_arbitro) DO NOTHING
                                        """)
                            
                            cur.execute(f"""
                                        INSERT INTO equipe_arbitragem(id_arbitro, id_jogo, funcao)
                                        VALUES 
                                        (
                                        {arbitro['id']},
                                        {jogo['id_jogo']},
                                        '{arbitro['funcao']}'
                                        )
                                        ON CONFLICT (id_arbitro, id_jogo) DO NOTHING
                                        """)
                        
                        cur.execute(f"""    
                                    INSERT INTO evento(gols, penaltis, id_jogo, id_clube)
                                    VALUES 
                                    (
                                        {jogo['mandante']['gols']},
                                        {jogo['mandante']['panaltis']},
                                        {jogo['id_jogo']},
                                        {jogo['mandante']['id']}
                                    )
                                    ON CONFLICT (id_jogo, id_clube) DO NOTHING
                                    """)
                        
                        cur.execute(f"""    
                                    INSERT INTO evento(gols, penaltis, id_jogo, id_clube)
                                    VALUES 
                                    (
                                        {jogo['visitante']['gols']},
                                        {jogo['visitante']['panaltis']},
                                        {jogo['id_jogo']},
                                        {jogo['visitante']['id']}
                                    )
                                    ON CONFLICT (id_jogo, id_clube) DO NOTHING
                                    """)
                                
                        for atleta in jogo['mandante']['atletas']:
                            cur.execute(f"""
                                        INSERT INTO atleta(id_atleta, nome, apelido, foto)
                                        VALUES 
                                        (
                                            {atleta['id']},
                                            '{atleta['nome']}',
                                            '{atleta['apelido']}',
                                            '{atleta['foto']}'
                                        )
                                        ON CONFLICT (id_atleta) DO NOTHING
                                        """)
                            
                            cur.execute(f"""
                                        INSERT INTO escalacao
                                        (
                                            numero_camisa, 
                                            reserva, 
                                            goleiro, 
                                            entrou_jogando, 
                                            id_atleta, 
                                            id_clube, 
                                            id_jogo
                                        )
                                        VALUES 
                                        (
                                            {atleta['numero_camisa']},
                                            {atleta['reserva']},
                                            {atleta['goleiro']},
                                            {atleta['entrou_jogando']},
                                            {atleta['id']},
                                            {jogo['mandante']['id']},
                                            {jogo['id_jogo']}
                                        )
                                        """)
                                    
                        for atleta in jogo['visitante']['atletas']:
                            cur.execute(f"""
                                        INSERT INTO atleta(id_atleta, nome, apelido, foto)
                                        VALUES 
                                        (
                                            {atleta['id']},
                                            '{atleta['nome']}',
                                            '{atleta['apelido']}',
                                            '{atleta['foto']}'
                                        )
                                        ON CONFLICT (id_atleta) DO NOTHING
                                        """)
                            
                            cur.execute(f"""
                                        INSERT INTO escalacao
                                        (
                                            numero_camisa, 
                                            reserva, 
                                            goleiro, 
                                            entrou_jogando, 
                                            id_atleta, 
                                            id_clube, 
                                            id_jogo
                                        )
                                        VALUES 
                                        (
                                            {atleta['numero_camisa']},
                                            {atleta['reserva']},
                                            {atleta['goleiro']},
                                            {atleta['entrou_jogando']},
                                            {atleta['id']},
                                            {jogo['visitante']['id']},
                                            {jogo['id_jogo']}
                                        )
                                        """)            
                                        
                        for alteracao in jogo['mandante']['alteracoes']:
                            cur.execute(f"""
                                        INSERT INTO alteracao
                                        (
                                            codigo_jogador_saiu, 
                                            codigo_jogador_entrou, 
                                            tempo_jogo, 
                                            tempo_subs, 
                                            tempo_acrescimo, 
                                            id_jogo, 
                                            id_clube
                                        )
                                        VALUES 
                                        (
                                            {alteracao['codigo_jogador_saiu']}, 
                                            {alteracao['codigo_jogador_entrou']}, 
                                            '0001-01-01 00:{"00:00" if alteracao['tempo_jogo'] == None else alteracao['tempo_jogo']}', 
                                            '{alteracao['tempo_subs']}', 
                                            '0001-01-01 00:{"00:00" if alteracao['tempo_acrescimo'] == None else alteracao['tempo_acrescimo']}', 
                                            {jogo['id_jogo']},
                                            {jogo['mandante']['id']}
                                        );
                                        """)
                                    
                        for alteracao in jogo['visitante']['alteracoes']:
                            cur.execute(f"""
                                        INSERT INTO alteracao
                                        (
                                            codigo_jogador_saiu, 
                                            codigo_jogador_entrou, 
                                            tempo_jogo, 
                                            tempo_subs, 
                                            tempo_acrescimo, 
                                            id_jogo, 
                                            id_clube
                                        )
                                        VALUES 
                                        (
                                            {alteracao['codigo_jogador_saiu']}, 
                                            {alteracao['codigo_jogador_entrou']}, 
                                            '0001-01-01 00:{"00:00" if alteracao['tempo_jogo'] == None else alteracao['tempo_jogo']}', 
                                            '{alteracao['tempo_subs']}', 
                                            '0001-01-01 00:{"00:00" if alteracao['tempo_acrescimo'] == None else alteracao['tempo_acrescimo']}', 
                                            {jogo['id_jogo']},
                                            {jogo['visitante']['id']}
                                        );
                                        """)        
                            
                        for documento in jogo['documentos']:
                            cur.execute(f"""
                                        INSERT INTO documento(url, title, id_jogo)
                                        VALUES 
                                        (                        
                                        '{documento['url']}', 
                                        '{documento['title']}', 
                                        {jogo['id_jogo']}
                                        )
                                        """)
                            
                        for penalidade in jogo['penalidades']:
                            try:   
                                    cur.execute(f"""
                                        INSERT INTO penalidade
                                        (
                                            id_penalidade, 
                                            tipo, 
                                            resultado, 
                                            tempo_jogo, 
                                            minutos,
                                            id_jogo,
                                            id_clube,
                                            id_atleta
                                        )
                                        VALUES 
                                        (
                                            {penalidade['id']}, 
                                            '{penalidade['tipo']}',
                                            '{penalidade['resultado']}',
                                            '{penalidade['tempo_jogo']}', 
                                            '0001-01-01 00:{penalidade['minutos'][0:4]}',
                                            '{jogo['id_jogo']}', 
                                            '{penalidade['clube_id']}', 
                                            '{penalidade['atleta_id']}'
                                        )
                                        ON CONFLICT (id_penalidade) DO NOTHING
                                        """)                             
                            except Exception as e: 
                                print(e)
                        
                    conn.commit()