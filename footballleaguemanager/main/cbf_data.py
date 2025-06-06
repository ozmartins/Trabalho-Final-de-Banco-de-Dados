import json

def insert_league(cur):
    cur.execute(f"""
                INSERT INTO Campeonato (IdCampeonato, Nome, Premiacao, IdFederacao) VALUES
                (1, 'Campeonato Brasileiro', 481600000, null)
                """)
    
def insert_season(cur):    
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
    for jogo in jogos:
        local = jogo['local'].replace('Beira-Rio', 'Beira Rio').split('-')
        nome_estadio = local[0].strip()
        cidade_estadio = local[1].strip()
        cur.execute(f"""
                    INSERT INTO Estadio (Nome, Capacidade, IdCidade) 
                    VALUES ('{nome_estadio}', 0, (select idcidade from cidade where nome = '{cidade_estadio}'))
                    ON CONFLICT (Nome) DO NOTHING
                    """)
        
def insert_teams(cur, jogos):
    for jogo in jogos:
        id_mandante = jogo['mandante']['id']
        nome_mandante = jogo['mandante']['nome']

        id_visitante = jogo['visitante']['id']
        nome_visitante = jogo['visitante']['nome']

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
                INSERT INTO Posicao (Descricao) VALUES
                ('Goleiro'),
                ('Lateral Direito'),
                ('Lateral Esquerdo'),
                ('Zagueiro'),
                ('Volante'),
                ('Meia'),
                ('Atacante')
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
            id_jogo = jogo['idjogo']
            id_arbrito = arbitro['id']
            nome_funcao = arbitro['funcao']
            
            cur.execute(f"""
                        INSERT INTO EquipeArbitragem (IdPartida, IdArbitro, IdFuncaoArbitro)
                        VALUES ({id_jogo}, '{id_arbrito}', (select ifduncaoarbitro from funcaoarbitro where nome = '{nome_funcao}'))
                        ON CONFLICT (idarbitro) DO NOTHING
                        """)

def insert_players(cur, jogos):
    for jogo in jogos:
        atletas_mandante = jogo['mandante']['atletas']
        atletas_visitante = jogo['visitante']['atletas']
        
        for atleta in atletas_mandante:
            nome_atleta = atleta['nome'].split('-')[1].strip()
            cur.execute(f"""
                        INSERT INTO Jogador (IdJogador, Nome, DataNascimento, IdNacionalidade, IdPosicao) 
                        VALUES ({atleta['id']}, '{nome_atleta}', '1900-01-01', null, null)
                        ON CONFLICT (IdJogador) DO NOTHING
                        """)
            
        for atleta in atletas_visitante:
            nome_atleta = atleta['nome'].split('-')[1].strip()
            cur.execute(f"""
                        INSERT INTO Jogador (IdJogador, Nome, DataNascimento, IdNacionalidade, IdPosicao) 
                        VALUES ({atleta['id']}, '{nome_atleta}', '1900-01-01', null, null)
                        ON CONFLICT (IdJogador) DO NOTHING
                        """)
            
def insert_lineup(cur, jogos):
    for jogo in jogos:
        id_jogo = jogo['id_jogo']
        atletas_mandante = jogo['mandante']['atletas']
        atletas_visitante = jogo['visitante']['atletas']
        
        for atleta in atletas_mandante:
            id_atleta = atleta['id']
            cur.execute(f"""
                        INSERT INTO Escalacao (IdPartida, IdJogador, IdPosicao)
                        VALUES ({id_jogo}, {id_atleta}, null)
                        ON CONFLICT (IdPartida, IdJogador) DO NOTHING
                        """)
            
        for atleta in atletas_visitante:
            id_atleta = atleta['id']
            cur.execute(f"""
                        INSERT INTO Escalacao (IdPartida, IdJogador, IdPosicao)
                        VALUES ({id_jogo}, {id_atleta}, null)
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

def insert_player_contract(cur, jogos):
    for jogo in jogos:
        id_jogo = jogo['id_jogo']

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
    cur.execute("""
                INSERT INTO ContratoTecnico (IdTecnico, IdTime, DataAssinatura, DataRescisao, MultaRescisoria) VALUES
                (1, (select idtime from time where nome = 'Athletico Paranense'), '2024-04-13', '2024-12-08', 0),
                (2, (select idtime from time where nome = 'Atletico Goiniense'), '2024-04-13', '2024-12-08', 0),
                (3, (select idtime from time where nome = 'Atletico Mineiro'), '2024-04-13', '2024-12-08', 0),
                (4, (select idtime from time where nome = 'Bahia'), '2024-04-13', '2024-12-08', 0),
                (5, (select idtime from time where nome = 'Botafogo'), '2024-04-13', '2024-12-08', 0),
                (6, (select idtime from time where nome = 'Corinthians'), '2024-04-13', '2024-12-08', 0),
                (7, (select idtime from time where nome = 'Criciúma'), '2024-04-13', '2024-12-08', 0),
                (8, (select idtime from time where nome = 'Cruzeiro'), '2024-04-13', '2024-12-08', 0),
                (9, (select idtime from time where nome = 'Cuiabá'), '2024-04-13', '2024-12-08', 0),
                (10, (select idtime from time where nome = 'Flamengo'), '2024-04-13', '2024-12-08', 0),
                (11, (select idtime from time where nome = 'Fluminense'), '2024-04-13', '2024-12-08', 0),
                (12, (select idtime from time where nome = 'Fortaleza'), '2024-04-13', '2024-12-08', 0),
                (13, (select idtime from time where nome = 'Grêmio'), '2024-04-13', '2024-12-08', 0),
                (14, (select idtime from time where nome = 'Internacional'), '2024-04-13', '2024-12-08', 0),
                (15, (select idtime from time where nome = 'Juventude'), '2024-04-13', '2024-12-08', 0),
                (16, (select idtime from time where nome = 'Palmeiras'), '2024-04-13', '2024-12-08', 0),
                (17, (select idtime from time where nome = 'São Paulo'), '2024-04-13', '2024-12-08', 0),
                (18, (select idtime from time where nome = 'Vasco da Gama'), '2024-04-13', '2024-12-08', 0),
                (19, (select idtime from time where nome = 'Vitória'), '2024-04-13', '2024-12-08', 0),
                (20, (select idtime from time where nome = 'Santos'), '2024-04-13', '2024-12-08', 0)
                """)

def insert_data_from_cbf_json(cur):
    insert_league(cur)
    insert_season(cur)
    insert_rounds(cur)
    insert_nationalities(cur)
    insert_positions(cur)
    insert_federations(cur)
    #insert_coach_contract(cur)
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
            insert_players(cur, jogos)
            insert_lineup(cur, jogos)
            insert_player_contract(cur, jogos)