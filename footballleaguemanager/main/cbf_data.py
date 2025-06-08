import json
import os
from .models import TipoEvento

def to_pascal_case(s):
    return ''.join(word.capitalize()+' ' for word in s.split()).strip()

def insert_leagues(cur):
    cur.execute(f"""
                INSERT INTO Campeonato (IdCampeonato, Nome, Premiacao, IdFederacao) VALUES
                (1, 'Campeonato Brasileiro', 481600000, null)
                """)
    
def insert_seasons(cur):    
    cur.execute(f"""
                INSERT INTO Temporada (IdTemporada, QuantidadeRodadas, DataInicio, DataFim, Ano, IdCampeonato) VALUES
                (1, 38, '2024-04-13', '2024-12-08', 2024, 1)
                """)
        
def insert_cities(cur, jogos):
    for jogo in jogos:
        local = jogo['local'].replace('Beira-Rio', 'Beira Rio').split('-')
        nome_cidade = local[1].strip()
        uf_cidade = local[2].strip()
        cur.execute(f"""
                    INSERT INTO Cidade (Nome, UF)
                    VALUES ('{nome_cidade}', '{uf_cidade}')   
                    ON CONFLICT (Nome, UF) DO NOTHING
                    """)
        
def insert_stadiums(cur, jogos):
    capacidade_estadios = [
        {"nome": "Brinco de Ouro", "capacidade": 29130},
        {"nome": "Arena Condá", "capacidade": 20589},
        {"nome": "Mané Garrincha", "capacidade": 72788},
        {"nome": "Independência", "capacidade": 23000},
        {"nome": "Centenário", "capacidade": 22132},
        {"nome": "Orlando Scarpelli", "capacidade": 19584},
        {"nome": "Presidente Vargas", "capacidade": 20166},
        {"nome": "Couto Pereira", "capacidade": 40310},
        {"nome": "Kleber Andrade", "capacidade":  21000},
        {"nome": "Antônio Accioly", "capacidade": 12500},
        {"nome": "Allianz Parque", "capacidade": 43713},
        {"nome": "Arena Pantanal", "capacidade": 44097},
        {"nome": "Nilton Santos", "capacidade": 46831},
        {"nome": "Arena Castelão", "capacidade": 63903},
        {"nome": "ARENA MRV", "capacidade": 44892},
        {"nome": "Arena Barueri", "capacidade": 31000},
        {"nome": "Alfredo Jaconi", "capacidade": 23726},
        {"nome": "Nabi Abi Chedid", "capacidade": 17000},
        {"nome": "Arena do Grêmio", "capacidade": 55662},
        {"nome": "Arena Fonte Nova", "capacidade": 50025},
        {"nome": "Manoel Barradas", "capacidade": 30618},
        {"nome": "Mineirão", "capacidade": 61846},
        {"nome": "Ligga Arena", "capacidade": 42372},
        {"nome": "São Januário", "capacidade": 24000},
        {"nome": "Neo Química Arena", "capacidade": 48905},
        {"nome": "Serra Dourada", "capacidade": 50049},
        {"nome": "Morumbi", "capacidade": 66795},
        {"nome": "Maracanã", "capacidade": 78838},
        {"nome": "Beira Rio", "capacidade": 51300},
        {"nome": "Heriberto Hulse", "capacidade": 19255}
    ]    

    for jogo in jogos:
        local = jogo['local'].replace('Beira-Rio', 'Beira Rio').split('-')
        nome_estadio = local[0].strip()
        cidade_estadio = local[1].strip()
        capacidade = 0

        for estadio in capacidade_estadios:
            if estadio["nome"].lower() == nome_estadio.lower():
                capacidade = estadio["capacidade"]

        cur.execute(f"""
                    INSERT INTO Estadio (Nome, Capacidade, IdCidade) 
                    VALUES ('{nome_estadio}', {capacidade}, (select idcidade from cidade where nome = '{cidade_estadio}'))
                    ON CONFLICT (Nome) DO NOTHING
                    """)
        
def insert_teams(cur, jogos):
    for jogo in jogos:
        id_mandante = jogo['mandante']['id']
        nome_mandante = to_pascal_case(jogo['mandante']['nome'])

        id_visitante = jogo['visitante']['id']
        nome_visitante = to_pascal_case(jogo['visitante']['nome'])

        local = jogo['local'].replace('Beira-Rio', 'Beira Rio').split('-')
        cidade_estadio = local[1].strip()                

        cur.execute(f"""
                    INSERT INTO Time (IdTime, Nome, IdCidade) 
                    VALUES ({id_mandante}, '{nome_mandante}', (select idcidade from cidade where nome = '{cidade_estadio}'))
                    ON CONFLICT (Nome) DO NOTHING
                    """)
        
        cur.execute(f"""
                    INSERT INTO Time (IdTime, Nome, IdCidade) 
                    VALUES ({id_visitante}, '{nome_visitante}', (select idcidade from cidade where nome = '{cidade_estadio}'))
                    ON CONFLICT (Nome) DO NOTHING
                    """)
                
def insert_rounds(cur):
    cur.execute("""
                INSERT INTO Rodada (IdRodada, NumeroRodada, IdTemporada) VALUES
                (01, 01, 1),
                (02, 02, 1),
                (03, 03, 1),
                (04, 04, 1),
                (05, 05, 1),
                (06, 06, 1),
                (07, 07, 1),
                (08, 08, 1),
                (09, 09, 1),
                (10, 10, 1),
                (11, 11, 1),
                (12, 12, 1),
                (13, 13, 1),
                (14, 14, 1),
                (15, 15, 1),
                (16, 16, 1),
                (17, 17, 1),
                (18, 18, 1),
                (19, 19, 1),
                (20, 20, 1),
                (21, 21, 1),
                (22, 22, 1),
                (23, 23, 1),
                (24, 24, 1),
                (25, 25, 1),
                (26, 26, 1),
                (27, 27, 1),
                (28, 28, 1),
                (29, 29, 1),
                (30, 30, 1),
                (31, 31, 1),
                (32, 32, 1),
                (33, 33, 1),
                (34, 34, 1),
                (35, 35, 1),
                (36, 36, 1),
                (37, 37, 1),
                (38, 38, 1)
                """)
    
def insert_nationalities(cur):
    cur.execute("""
                INSERT INTO Nacionalidade (IdNacionalidade, Descricao) VALUES
                (01, 'Brasileira'),
                (02, 'Argentina'),
                (03, 'Uruguaia'),
                (04, 'Colômbiana'),
                (05, 'Paraguaia'),
                (06, 'Equatoriana'),
                (07, 'Chilena'),
                (08, 'Venezuelana'),
                (09, 'Peruana'),
                (10, 'Portuguesa')
                """)  

def insert_positions(cur):
    cur.execute("""
                INSERT INTO Posicao (IdPosicao, Descricao) VALUES
                (1, 'Goleiro'),
                (2, 'Lateral Direito'),
                (3, 'Lateral Esquerdo'),
                (4, 'Zagueiro'),
                (5, 'Volante'),
                (6, 'Meia'),
                (7, 'Atacante'),
                (8, 'Desconhecida')
                """)
    
def insert_federations(cur):
    cur.execute("""
                INSERT INTO Federacao (Nome, UF) VALUES
                ('Federação Acreana de Futebol (FAF)', 'AC'),
                ('Federação Alagoana de Futebol (FAF)', 'AL'),
                ('Federação Amapaense de Futebol (FAF)', 'AP'),
                ('Federação Amazonense de Futebol (FAF)', 'AM'),
                ('Federação Bahiana de Futebol (FBF)', 'BA'),
                ('Federação Cearense de Futebol (FCF)', 'CE'),
                ('Federação de Futebol do Distrito Federal (FFDF)', 'DF'),
                ('Federação Capixaba de Futebol (FCF)', 'ES'),
                ('Federação Goiana de Futebol (FGF)', 'GO'),
                ('Federação Maranhense de Futebol (FMF)', 'MA'),
                ('Federação Mato-Grossense de Futebol (FMF)', 'MT'),
                ('Federação Mato-Grossense do Sul de Futebol (FMF)', 'MS'),
                ('Federação Mineira de Futebol (FMF)', 'MG'),
                ('Federação do Pará de Futebol (FPF)', 'PA'),
                ('Federação Paraibana de Futebol (FPF)', 'PB'),
                ('Federação Paranaense de Futebol (FPR)', 'PR'),
                ('Federação Pernambucana de Futebol (FPF)', 'PE'),
                ('Federação Piauiense de Futebol (FPF)', 'PI'),
                ('Federação de Futebol do Estado do Rio de Janeiro (FERJ)', 'RJ'),
                ('Federação Norte-Rio-Grandense de Futebol (FNRF)', 'RN'),
                ('Federação Gaúcha de Futebol (FGF)', 'RS'),
                ('Federação Rondoniense de Futebol (FRF)', 'RO'),
                ('Federação Roraimense de Futebol (FRF)', 'RR'),
                ('Federação Catarinense de Futebol (FCA)', 'SC'),
                ('Federação Paulista de Futebol (FPF)', 'SP'),
                ('Federação Sergipana de Futebol (FSF)', 'SE'),
                ('Federação Tocantinense de Futebol (FTF) ', 'TO')
                """)

def insert_referee_roles(cur, jogos):
    for jogo in jogos:
        for arbitro in jogo['arbitros']:
            nome_funcao = arbitro['funcao']
            cur.execute(f"""
                        INSERT INTO FuncaoArbitro (Descricao) 
                        VALUES ('{nome_funcao}')
                        ON CONFLICT (Descricao) DO NOTHING
                        """)

def insert_referees(cur, jogos):
    for jogo in jogos:
        for arbitro in jogo['arbitros']:
            id_arbitro = arbitro['id']
            nome_arbitro = arbitro['nome']
            uf_arbitro = arbitro['uf']
            
            cur.execute(f"""
                        INSERT INTO Arbitro (idarbitro, nome, datanascimento, idfederacao) 
                        VALUES ({id_arbitro}, '{nome_arbitro}', '1900-01-01', (select idfederacao from federacao where uf = '{uf_arbitro}'))
                        ON CONFLICT (idarbitro) DO NOTHING
                        """)        
            
def insert_referee_teams(cur, jogos):
    for jogo in jogos:
        for arbitro in jogo['arbitros']:
            id_jogo = jogo['id_jogo']
            id_arbrito = arbitro['id']
            nome_funcao = arbitro['funcao']                    

            cur.execute(f"""
                        INSERT INTO EquipeArbitragem (IdPartida, IdArbitro, IdFuncaoArbitro)
                        VALUES ({id_jogo}, {id_arbrito}, (select idfuncaoarbitro from funcaoarbitro where descricao = '{nome_funcao}'))
                        ON CONFLICT (IdPartida, IdArbitro, IdFuncaoArbitro) DO NOTHING
                        """)

def insert_players(cur, jogos):    
    for jogo in jogos:    
        atletas_mandante = jogo['mandante']['atletas']
        atletas_visitante = jogo['visitante']['atletas']
        
        for atleta in atletas_mandante:
            nome_atleta = atleta['nome'].split('-')[1].strip()
            numero_camisa = int(atleta['numero_camisa']) % 11
            posicao = calc_position(numero_camisa)
            cur.execute(f"""
                        INSERT INTO Jogador (IdJogador, Nome, DataNascimento, IdNacionalidade, IdPosicao) 
                        VALUES ({atleta['id']}, '{nome_atleta}', '1900-01-01', null, {posicao})
                        ON CONFLICT (IdJogador) DO NOTHING
                        """)
            
        for atleta in atletas_visitante:
            nome_atleta = atleta['nome'].split('-')[1].strip()
            numero_camisa = int(atleta['numero_camisa']) % 11
            posicao = calc_position(numero_camisa)
            cur.execute(f"""
                        INSERT INTO Jogador (IdJogador, Nome, DataNascimento, IdNacionalidade, IdPosicao) 
                        VALUES ({atleta['id']}, '{nome_atleta}', '1900-01-01', null, {posicao})
                        ON CONFLICT (IdJogador) DO NOTHING
                        """)
                
            
def insert_coaches(cur):
    with open(f'main/datasets/treinadores.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for team in data:
            treinadores = team['treinadores']
            for treinador in treinadores:
                cur.execute(f"""
                            INSERT INTO Tecnico (Nome, DataNascimento, IdNacionalidade) 
                            VALUES ('{treinador['nome']}', '1900-01-01', 1)
                            ON CONFLICT (Nome) DO NOTHING
                            """)

def calc_position(numero_camisa):
    if numero_camisa == 1:
        return 1
    elif numero_camisa == 2:
        return 2
    elif numero_camisa in [3,4]:
        return 4
    elif numero_camisa == 5:
        return 5
    elif numero_camisa == 6:
        return 3
    elif numero_camisa in [7,8,10]:
        return 6
    elif numero_camisa in [0,9,11]:
        return 7
    else:
        return 8


def insert_lineups(cur, jogos):
    for jogo in jogos:
        id_jogo = jogo['id_jogo']
        
        atletas_mandante = jogo['mandante']['atletas']
        atletas_visitante = jogo['visitante']['atletas']            

        for atleta in atletas_mandante:                                    
            id_atleta = atleta['id']
            numero_camisa = int(atleta['numero_camisa']) % 11
            posicao = calc_position(numero_camisa)

            cur.execute(f"""
                        INSERT INTO Escalacao (IdPartida, IdJogador, IdPosicao)
                        VALUES ({id_jogo}, {id_atleta}, {posicao})
                        ON CONFLICT (IdPartida, IdJogador) DO NOTHING
                        """)
            
        for atleta in atletas_visitante:                        
            id_atleta = atleta['id'] 
            numero_camisa = int(atleta['numero_camisa']) % 11
            posicao = calc_position(numero_camisa)
            cur.execute(f"""
                        INSERT INTO Escalacao (IdPartida, IdJogador, IdPosicao)
                        VALUES ({id_jogo}, {id_atleta}, {posicao})
                        ON CONFLICT (IdPartida, IdJogador) DO NOTHING
                        """)         
            
def insert_participation(cur, jogos):
    cur.execute("""
                INSERT INTO Participacao (IdTime, IdTemporada)
                SELECT IdTime, 1 from time
                """)

def insert_matches(cur, jogos):
    for jogo in jogos:
        data = jogo['data'].replace('/','')
        ano = data[5:]
        mes = data[3:-4]
        dia = data[1:-6]        

        id_jogo = jogo['id_jogo']

        hora = jogo['hora']
        data_hora = f'{ano}-{mes}-{dia}:{hora}'        
        
        local = jogo['local'].replace('Beira-Rio', 'Beira Rio').split('-')
        nome_estadio = local[0].strip()        

        id_mandante = jogo['mandante']['id']
        id_visitante = jogo['visitante']['id']

        cur.execute(f"""
                    INSERT INTO Partida (IdPartida, DataHora, Publico, Renda, IdRodada, IdEstadio, IdTimeMandante, IdTimeVisitante) 
                    VALUES ({id_jogo}, '{data_hora}', 0, 0, {jogo['rodada']}, (select idestadio from estadio where nome = '{nome_estadio}'), {id_mandante}, {id_visitante})
                    ON CONFLICT (IdTimeMandante, IdTimeVisitante) DO NOTHING
                    """)

def insert_player_contracts(cur, jogos):
    for jogo in jogos:
        id_mandante = jogo['mandante']['id']
        id_visitante = jogo['visitante']['id']

        atletas_mandante = jogo['mandante']['atletas']
        atletas_visitante = jogo['visitante']['atletas']
        
        for atleta in atletas_mandante:
            id_atleta = atleta['id']                
            cur.execute(f"""
                        INSERT INTO ContratoJogador (Numero, IdJogador, IdTime, DataRescisao, DataAssinatura, MultaRescisoria) VALUES
                        ('{id_mandante}/{id_atleta}', {id_atleta}, {id_mandante}, NULL, '2024-01-01', 0)
                        ON CONFLICT (Numero) DO NOTHING
                        """)
            
        for atleta in atletas_visitante:
            id_atleta = atleta['id']
            cur.execute(f"""
                        INSERT INTO ContratoJogador (Numero, IdJogador, IdTime, DataRescisao, DataAssinatura, MultaRescisoria) VALUES
                        ('{id_visitante}/{id_atleta}', {id_atleta}, {id_visitante}, NULL, '2024-01-01', 0)
                        ON CONFLICT (Numero) DO NOTHING
                        """)                              

def insert_coach_contract(cur):
    with open(f'main/datasets/treinadores.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for time in data:
            for treinador in time['treinadores']:                                
                cur.execute(f"""
                            INSERT INTO ContratoTecnico (IdTecnico, IdTime, DataAssinatura, DataRescisao, MultaRescisoria) VALUES (                             
                             (select idtecnico from tecnico where lower(nome) = lower('{treinador['nome']}')), 
                             (select idtime from time where lower(nome) = lower('{time['clube']}')), 
                             '{treinador['inicio']}', NULL, 0)
                            """)
                fim = 'NULL' if treinador['fim'] == None else f"'{treinador['fim']}'"
                cur.execute(f"""
                            UPDATE ContratoTecnico 
                            SET DataRescisao = {fim} 
                            WHERE IdTime = (select idtime from time where nome = '{time['clube']}')
                            AND IdTecnico = (select idtecnico from tecnico where nome = '{treinador['nome']}')
                            """)

def insert_events(cur, jogos):    
    for jogo in jogos:
        id_jogo = jogo['id_jogo']
        
        substituicoes_mandante = jogo['mandante']['alteracoes']
        for substituicao in substituicoes_mandante:
            minuto = int(substituicao['tempo_jogo'].split(":")[0])
            id_jogador_saiu = substituicao['codigo_jogador_saiu']
            id_jogador_entrou = substituicao['codigo_jogador_entrou']

            cur.execute(f'select count(*) as qtd from jogador where idjogador in ({id_jogador_saiu}, {id_jogador_entrou})')
            result = cur.fetchone()            

            if result[0] == 2:
                cur.execute(f"""
                            INSERT INTO Evento (TipoEvento, Minuto, IdPartida, IdJogador) 
                            VALUES ({TipoEvento.SUBSTITUICAO_SAIDA.value}, {minuto}, {id_jogo}, {id_jogador_saiu})
                            """)
                cur.execute(f"""
                            INSERT INTO Evento (TipoEvento, Minuto, IdPartida, IdJogador) 
                            VALUES ({TipoEvento.SUBSTITUICAO_ENTRADA.value}, {minuto}, {id_jogo}, {id_jogador_entrou})
                            """)
            
        substituicoes_visitante = jogo['visitante']['alteracoes']
        for substituicao in substituicoes_visitante:
            minuto = int(substituicao['tempo_jogo'].split(":")[0])
            id_jogador_saiu = substituicao['codigo_jogador_saiu']
            id_jogador_entrou = substituicao['codigo_jogador_entrou']

            cur.execute(f'select count(*) as qtd from jogador where idjogador in ({id_jogador_saiu}, {id_jogador_entrou})')
            result = cur.fetchone()            

            if result[0] == 2:
                cur.execute(f"""
                            INSERT INTO Evento (TipoEvento, Minuto, IdPartida, IdJogador) 
                            VALUES ({TipoEvento.SUBSTITUICAO_SAIDA.value}, {minuto}, {id_jogo}, {id_jogador_saiu})
                            """)
                cur.execute(f"""
                            INSERT INTO Evento (TipoEvento, Minuto, IdPartida, IdJogador) 
                            VALUES ({TipoEvento.SUBSTITUICAO_ENTRADA.value}, {minuto}, {id_jogo}, {id_jogador_entrou})
                            """)

        penalidades = jogo['penalidades']
        for penalidade in penalidades:            
            if (penalidade['tipo'] == 'GOL'):
                if (penalidade['resultado'] == 'NR'):
                    evento = TipoEvento.GOL_NORMAL.value
                elif (penalidade['resultado'] == 'FT'):
                    evento = TipoEvento.GOL_FALTA.value                    
                elif (penalidade['resultado'] == 'PN'):
                    evento = TipoEvento.GOL_PENALTI.value                    
            elif (penalidade['tipo'] == 'PENALIDADE'):
                if (penalidade['resultado'] == 'AMARELO'):
                    evento = TipoEvento.CARTAO_AMARELO.value
                elif (penalidade['resultado'] == 'VERMELHO2AMARELO'):
                    evento = TipoEvento.CARTAO_VERMELHO.value
            
            if penalidade['tempo_jogo'] in ['AC1', 'TN1']:
                tempo_jogo = 1
            elif penalidade['tempo_jogo'] in ['AC2', 'TN2']:
                tempo_jogo = 1
            elif penalidade['tempo_jogo'].isdigit():
                tempo_jogo = int(penalidade['tempo_jogo'])                
            else:
                tempo_jogo = 0            

            minuto = tempo_jogo * int(penalidade['minutos'].split(":")[0])
            id_jogador = penalidade['atleta_id']

            cur.execute(f'select count(*) as qtd from jogador where idjogador = {id_jogador}')
            result = cur.fetchone()            

            if result[0] == 1:
                cur.execute(f"""
                            INSERT INTO Evento (TipoEvento, Minuto, IdPartida, IdJogador) 
                            VALUES ({evento}, {minuto}, {id_jogo}, {id_jogador})
                            """)

def insert_participation(cur):
    cur.execute("INSERT INTO Participacao (IdTime, IdTemporada) select idtime, 1 from time")


def insert_data_from_cbf_json(cur):
    insert_leagues(cur)
    insert_seasons(cur)
    insert_rounds(cur)
    insert_nationalities(cur)
    insert_positions(cur)
    insert_federations(cur)
    insert_coaches(cur)    
    for rodada in range(38):
        with open(f'main/datasets/rodada-{rodada+1}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            jogos = data['jogos'][0]['jogo']
            insert_cities(cur, jogos)
            insert_stadiums(cur, jogos)
            insert_teams(cur, jogos)
            insert_matches(cur, jogos)            
            insert_referee_roles(cur, jogos)
            insert_referees(cur, jogos)
            insert_referee_teams(cur, jogos)
            insert_players(cur, jogos)
            insert_lineups(cur, jogos)
            insert_player_contracts(cur, jogos)
            insert_events(cur, jogos)
    insert_coach_contract(cur)
    insert_participation(cur)