def create_all_tables(cur):
    cur.execute("CREATE SCHEMA IF NOT EXISTS footballleaguemanager")

    cur.execute("""
                CREATE TABLE Campeonato (
                IdCampeonato serial PRIMARY KEY,
                Nome varchar(100),
                Premiacao numeric(14,2),
                IdFederacao integer
                )""")

    cur.execute("""
                CREATE TABLE Federacao (
                IdFederacao serial PRIMARY KEY,
                Nome varchar(100),
                UF varchar(2)
                )""")

    cur.execute("""
                CREATE TABLE Arbitro (
                IdArbitro serial PRIMARY KEY,
                Nome varchar(100),
                DataNascimento date,
                IdFederacao integer
                )""")

    cur.execute("""
                CREATE TABLE Cidade (
                IdCidade serial PRIMARY KEY,
                Nome varchar(100),
                UF varchar(2)
                )""")

    cur.execute("""
                CREATE TABLE Estadio (
                IdEstadio serial PRIMARY KEY,
                Nome varchar(100),
                Capacidade integer,
                IdCidade integer
                )""")

    cur.execute("""
                CREATE TABLE FuncaoArbitro (
                IdFuncaoArbitro serial PRIMARY KEY,
                Descricao varchar(100)
                )""")

    cur.execute("""
                CREATE TABLE Temporada (
                IdTemporada serial PRIMARY KEY,
                QuantidadeRodadas integer,
                DataInicio date,
                DataFim date,
                Ano integer,
                IdCampeonato integer
                )""")

    cur.execute("""
                CREATE TABLE Rodada (
                IdRodada serial PRIMARY KEY,
                NumeroRodada integer,
                IdTemporada integer
                )""")

    cur.execute("""CREATE TABLE Partida (
                IdPartida serial PRIMARY KEY,
                DataHora timestamp,
                Publico integer,
                Renda numeric(14,2),
                IdRodada integer,
                IdEstadio integer,
                IdTimeMandante integer,
                IdTimeVisitante integer
                )""")

    cur.execute("""
                CREATE TABLE Time (
                IdTime serial PRIMARY KEY,
                Nome varchar(100),
                IdCidade integer
                )""")

    cur.execute("""
                CREATE TABLE Jogador (
                IdJogador serial PRIMARY KEY,
                Nome varchar(100),
                DataNascimento date,
                IdNacionalidade integer,
                IdPosicao integer
                )""")

    cur.execute("""
                CREATE TABLE Tecnico (
                IdTecnico serial PRIMARY KEY,
                Nome varchar(100),
                DataNascimento date,
                IdNacionalidade integer
                )""")

    cur.execute("""
                CREATE TABLE Nacionalidade (
                IdNacionalidade serial PRIMARY KEY,
                Descricao varchar(100)
                )""")

    cur.execute("""
                CREATE TABLE Posicao (
                IdPosicao serial PRIMARY KEY,
                Descricao varchar(100)
                )""")

    cur.execute("""
                CREATE TABLE Evento (
                IdEvento serial PRIMARY KEY,
                TipoEvento integer,
                Minuto integer,
                IdPartida integer,
                IdJogador integer
                )""")

    cur.execute("""
                CREATE TABLE Participacao (
                IdParticipacao serial PRIMARY KEY,
                IdTime integer,
                IdTemporada integer
                )""")

    cur.execute("""
                CREATE TABLE EquipeArbitragem (
                IdEquipeArbitragem serial PRIMARY KEY,
                IdPartida integer,
                IdArbitro integer,
                IdFuncaoArbitro integer
                )""")

    cur.execute("""
                CREATE TABLE ContratoTecnico (
                Numero serial PRIMARY KEY,
                IdTecnico integer,
                IdTime integer,
                DataAssinatura date,
                DataRescisao date,
                MultaRescisoria numeric(14,2)
                )""")

    cur.execute("""
                CREATE TABLE ContratoJogador (
                Numero varchar(50) PRIMARY KEY,
                IdJogador integer,
                IdTime integer,
                DataRescisao date,
                DataAssinatura date,
                MultaRescisoria numeric(14,2)
                )""")

    cur.execute("""
                CREATE TABLE Escalacao (
                IdEscalacao serial PRIMARY KEY,
                IdPartida integer,
                IdJogador integer,
                IdPosicao integer
                )""")
    
    cur.execute("""
                ALTER TABLE Campeonato ADD CONSTRAINT FK_Campeonato_Federacao
                FOREIGN KEY (IdFederacao)
                REFERENCES Federacao (IdFederacao)
                ON DELETE SET NULL
                """)
    
    cur.execute("""
                ALTER TABLE Arbitro ADD CONSTRAINT FK_Arbitro_Federacao
                FOREIGN KEY (IdFederacao)
                REFERENCES Federacao (IdFederacao)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Estadio ADD CONSTRAINT FK_Estadio_Cidade
                FOREIGN KEY (IdCidade)
                REFERENCES Cidade (IdCidade)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Temporada ADD CONSTRAINT FK_Temporada_Campeonato
                FOREIGN KEY (IdCampeonato)
                REFERENCES Campeonato (IdCampeonato)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Rodada ADD CONSTRAINT FK_Rodada_Temporada
                FOREIGN KEY (IdTemporada)
                REFERENCES Temporada (IdTemporada)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Partida ADD CONSTRAINT FK_Partida_Rodada
                FOREIGN KEY (IdRodada)
                REFERENCES Rodada (IdRodada)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Partida ADD CONSTRAINT FK_Partida_Estadio
                FOREIGN KEY (IdEstadio)
                REFERENCES Estadio (IdEstadio)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Partida ADD CONSTRAINT FK_Partida_TimeMandante
                FOREIGN KEY (IdTimeMandante)
                REFERENCES Time (IdTime)
                ON DELETE CASCADE
                """)

    cur.execute("""
                ALTER TABLE Partida ADD CONSTRAINT FK_Partida_TimeVisitante
                FOREIGN KEY (IdTimeVisitante)
                REFERENCES Time (IdTime)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Time ADD CONSTRAINT FK_Time_Cidade
                FOREIGN KEY (IdCidade)
                REFERENCES Cidade (IdCidade)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Jogador ADD CONSTRAINT FK_Jogador_Nacionalidade
                FOREIGN KEY (IdNacionalidade)
                REFERENCES Nacionalidade (IdNacionalidade)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Jogador ADD CONSTRAINT FK_Jogador_Posicao
                FOREIGN KEY (IdPosicao)
                REFERENCES Posicao (IdPosicao)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Tecnico ADD CONSTRAINT FK_Tecnico_Nacionalidade
                FOREIGN KEY (IdNacionalidade)
                REFERENCES Nacionalidade (IdNacionalidade)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Evento ADD CONSTRAINT FK_Evento_Partida
                FOREIGN KEY (IdPartida)
                REFERENCES Partida (IdPartida)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Evento ADD CONSTRAINT FK_Evento_Jogador
                FOREIGN KEY (IdJogador)
                REFERENCES Jogador (IdJogador)
                ON DELETE CASCADE
                """)
    
    cur.execute("""
                ALTER TABLE Participacao ADD CONSTRAINT FK_Participacao_Time
                FOREIGN KEY (IdTime)
                REFERENCES Time (IdTime)
                ON DELETE RESTRICT
                """)
    
    cur.execute("""
                ALTER TABLE Participacao ADD CONSTRAINT FK_Participacao_Temporada
                FOREIGN KEY (IdTemporada)
                REFERENCES Temporada (IdTemporada)
                ON DELETE SET NULL
                """)
    
    cur.execute("""
                ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_Partida
                FOREIGN KEY (IdPartida)
                REFERENCES Partida (IdPartida)
                ON DELETE NO ACTION
                """)
    
    cur.execute("""
                ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_Arbitro
                FOREIGN KEY (IdArbitro)
                REFERENCES Arbitro (IdArbitro)
                ON DELETE NO ACTION
                """)
    
    cur.execute("""
                ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_FuncaoArbitro
                FOREIGN KEY (IdFuncaoArbitro)
                REFERENCES FuncaoArbitro (IdFuncaoArbitro)
                ON DELETE RESTRICT
                """)
    
    cur.execute("""
                ALTER TABLE ContratoTecnico ADD CONSTRAINT FK_ContratoTecnico_Tecnico
                FOREIGN KEY (IdTecnico)
                REFERENCES Tecnico (IdTecnico)
                ON DELETE SET NULL
                """)
    
    cur.execute("""
                ALTER TABLE ContratoTecnico ADD CONSTRAINT FK_ContratoTecnico_3
                FOREIGN KEY (IdTime)
                REFERENCES Time (IdTime)
                ON DELETE SET NULL
                """)
    
    cur.execute("""
                ALTER TABLE ContratoJogador ADD CONSTRAINT FK_ContratoJogador_Jogador
                FOREIGN KEY (IdJogador)
                REFERENCES Jogador (IdJogador)
                ON DELETE SET NULL
                """)
    
    cur.execute("""
                ALTER TABLE ContratoJogador ADD CONSTRAINT FK_ContratoJogador_Time
                FOREIGN KEY (IdTime)
                REFERENCES Time (IdTime)
                ON DELETE SET NULL
                """)
    
    cur.execute("""
                ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_Partida
                FOREIGN KEY (IdPartida)
                REFERENCES Partida (IdPartida)
                ON DELETE NO ACTION
                """)
    
    cur.execute("""
                ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_Jogador
                FOREIGN KEY (IdJogador)
                REFERENCES Jogador (IdJogador)
                ON DELETE NO ACTION
                """)
    
    cur.execute("""
                ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_Posicao
                FOREIGN KEY (IdPosicao)
                REFERENCES Posicao (IdPosicao)
                ON DELETE NO ACTION
                """)

def drop_all_tables(cur):
    cur.execute("DROP TABLE Cidade CASCADE")
    cur.execute("DROP TABLE Estadio CASCADE")
    cur.execute("DROP TABLE FuncaoArbitro CASCADE")
    cur.execute("DROP TABLE Posicao CASCADE")
    cur.execute("DROP TABLE ContratoTecnico CASCADE")
    cur.execute("DROP TABLE ContratoJogador CASCADE")
    cur.execute("DROP TABLE Escalacao CASCADE")
    cur.execute("DROP TABLE EquipeArbitragem CASCADE")
    cur.execute("DROP TABLE Participacao CASCADE")
    cur.execute("DROP TABLE Tecnico CASCADE")
    cur.execute("DROP TABLE Arbitro CASCADE")
    cur.execute("DROP TABLE Federacao CASCADE")
    cur.execute("DROP TABLE Partida CASCADE")
    cur.execute("DROP TABLE Rodada CASCADE")
    cur.execute("DROP TABLE Temporada CASCADE")
    cur.execute("DROP TABLE Time CASCADE")
    cur.execute("DROP TABLE Jogador CASCADE")
    cur.execute("DROP TABLE Nacionalidade CASCADE")
    cur.execute("DROP TABLE Evento CASCADE")
    cur.execute("DROP TABLE Campeonato CASCADE")

def insert_example_data(cur):
    cur.execute("""
                INSERT INTO Nacionalidade (Descricao) VALUES
                ('Argentina'),
                ('Uruguai'),
                ('Colômbia'),
                ('Paraguai'),
                ('Equador'),
                ('Chile'),
                ('Venezuela'),
                ('França'),
                ('Portugal'),
                ('República Democrática do Congo'),
                ('Angola'),
                ('Peru'),
                ('Senegal'),
                ('Irlanda do Norte'),
                ('Suíça'),
                ('Costa Rica'),
                ('Espanha'),
                ('Bulgária'),
                ('Nicarágua')
                """)

    cur.execute("""
                INSERT INTO Posicao (Descricao) VALUES
                ('Goleiro'),
                ('Lateral Direito'),
                ('Lateral Esquerdo'),
                ('Zagueiro'),
                ('Volante'),
                ('Meia Central'),
                ('Meia Ofensivo'),
                ('Ponta Direita'),
                ('Ponta Esquerda'),
                ('Atacante'),
                ('Segundo Atacante'),
                ('Centro Avante')
                """)

    cur.execute("""
                INSERT INTO Federacao (Nome, UF) VALUES
                ('Federação Acreana de Futebol', 'AC'),
                ('Federação Alagoana de Futebol', 'AL'),
                ('Federação Amapaense de Futebol', 'AP'),
                ('Federação Amazonense de Futebol', 'AM'),
                ('Federação Baiana de Futebol', 'BA'),
                ('Federação Cearense de Futebol', 'CE'),
                ('Federação Brasiliense de Futebol', 'DF'),
                ('Federação Espírito-Santense de Futebol', 'ES'),
                ('Federação Goiana de Futebol', 'GO'),
                ('Federação Maranhense de Futebol', 'MA'),
                ('Federação Mineira de Futebol', 'MG'),
                ('Federação Matogrossense de Futebol', 'MT'),
                ('Federação Mato-Grossense do Futebol', 'MS'),
                ('Federação Paraense de Futebol', 'PA'),
                ('Federação Paraibana de Futebol', 'PB'),
                ('Federação Paranaense de Futebol', 'PR'),
                ('Federação Pernambucana de Futebol', 'PE'),
                ('Federação Piauiense de Futebol', 'PI'),
                ('Federação Futebol do Rio de Janeiro', 'RJ'),
                ('Federação Futebol do Rio Grande do Norte', 'RN'),
                ('Federação Gaúcha de Futebol', 'RS'),
                ('Federação Rondônia de Futebol', 'RO'),
                ('Federação Roraimense de Futebol', 'RR'),
                ('Federação Paulista de Futebol', 'SP'),
                ('Federação Sergipana de Futebol', 'SE'),
                ('Federação Tocantinense de Futebol', 'TO');
                """)    

    cur.execute("""
                INSERT INTO Cidade (Nome, UF) VALUES
                ('Belo Horizonte', 'MG'),
                ('Curitiba', 'PR'),
                ('Salvador', 'BA'),
                ('Rio de Janeiro', 'RJ'),
                ('São Paulo', 'SP'),
                ('Cuiabá', 'MT'),
                ('Fortaleza', 'CE'),
                ('Goiânia', 'GO'),
                ('Porto Alegre', 'RS'),
                ('Caxias do Sul', 'RS'),
                ('Bragança Paulista', 'RS'),
                ('Santos', 'SP'),
                ('Criciúma', 'SC');
                """)    

    cur.execute("""
                INSERT INTO Estadio (Nome, Capacidade, IdCidade) VALUES
                ('Ligga Arena', 42370, (select idcidade from cidade where nome = 'Curitiba')),
                ('Antônio Accioly', 12500, (select idcidade from cidade where nome = 'Goiânia')),
                ('Arena MRV', 44892, (select idcidade from cidade where nome = 'Belo Horizonte')),
                ('Fonte Nova', 50025, (select idcidade from cidade where nome = 'Salvador')),
                ('Nilton Santos', 44661, (select idcidade from cidade where nome = 'Rio de Janeiro')),
                ('Neo Química Arena', 47605, (select idcidade from cidade where nome = 'São Paulo')),
                ('Heriberto Hülse', 19225, (select idcidade from cidade where nome = 'Criciúma')),
                ('Mineirão', 61927, (select idcidade from cidade where nome = 'Belo Horizonte')),
                ('Arena Pantanal', 44097, (select idcidade from cidade where nome = 'Cuiabá')),
                ('Maracanã', 78838, (select idcidade from cidade where nome = 'Rio de Janeiro')),
                ('Arena Castelão', 63903, (select idcidade from cidade where nome = 'Fortaleza')),
                ('Beira-Rio', 50842, (select idcidade from cidade where nome = 'Porto Alegre')),
                ('Arena do Grêmio', 55662, (select idcidade from cidade where nome = 'Porto Alegre')),
                ('Alfredo Jaconi', 19924, (select idcidade from cidade where nome = 'Caxias do Sul')),
                ('Allianz Parque', 43713, (select idcidade from cidade where nome = 'São Paulo')),
                ('Nabi Abi Chedid', 15010, (select idcidade from cidade where nome = 'Bragança Paulista')),
                ('MorumBIS', 72039 , (select idcidade from cidade where nome = 'São Paulo')),
                ('São Januário', 21680 , (select idcidade from cidade where nome = 'Rio de Janeiro')),
                ('Barradão', 29168 , (select idcidade from cidade where nome = 'Salvador'))
                """)

    cur.execute("""
                INSERT INTO Arbitro (Nome, DataNascimento, IdFederacao) VALUES
                ('Wilton Pereira Sampaio', '1981-12-28', 17),
                ('Anderson Daronco', '1981-04-23', 21),
                ('Raphael Claus', '1980-11-15', 13),
                ('Bruno Arleu de Araújo', '1972-09-06', 19),
                ('Marcelo Aparecido de Souza', '1970-05-30', 25),
                ('Paulo Roberto Alves Junior', '1978-06-12', 12),
                ('Ricardo Marques Ribeiro', '1986-09-22', 13),
                ('Sandro Meira Ricci', '1974-08-21', 9),
                ('Rodrigo Nunes de Sá', '1985-03-18', 4),
                ('Fabricio Vilarinho da Silva', '1986-07-25', 22),
                ('João Batista de Arruda', '1973-01-10', 23),
                ('Bruno Michel Godoy Bueno', '1984-11-05', 18),
                ('Leandro Pedro Vuaden', '1971-02-09', 9),
                ('Thiago Henrique Gomes Ribeiro', '1987-04-15', 16),
                ('Gleidson Santos', '1988-12-02', 1),
                ('André Luiz de Freitas Castro', '1974-06-20', 15),
                ('Marcelo de Lima Henrique', '1971-09-07', 6),
                ('Ricardo Gaciba', '1971-06-20', 10),
                ('Sávio Pereira Sampaio', '1984-10-22', 14),
                ('Wilton Pereira Sampaio', '1981-12-28', 17);
                """)    

    cur.execute("""
                INSERT INTO FuncaoArbitro (Descricao) VALUES
                ('Árbitro Principal'),
                ('Árbitro Assistente'),
                ('Quarto Árbitro'),
                ('Árbitro de vídeo')
                """)

    cur.execute("""
                INSERT INTO Time (Nome, IdCidade) VALUES
                ('Athletico Paranaense', (select idcidade from cidade where nome = 'Curitiba')),
                ('Atlético Goianiense', (select idcidade from cidade where nome = 'Goiânia')),
                ('Atlético Mineiro', (select idcidade from cidade where nome = 'Belo Horizonte')),
                ('Bahia', (select idcidade from cidade where nome = 'Salvador')),
                ('Botafogo', (select idcidade from cidade where nome = 'Rio de Janeiro')),
                ('Corinthians', (select idcidade from cidade where nome = 'São Paulo')),
                ('Criciúma', (select idcidade from cidade where nome = 'Criciúma')),
                ('Cruzeiro', (select idcidade from cidade where nome = 'Belo Horizonte')),
                ('Cuiabá', (select idcidade from cidade where nome = 'Cuiabá')),
                ('Flamengo', (select idcidade from cidade where nome = 'Rio de Janeiro')),
                ('Fluminense', (select idcidade from cidade where nome = 'Rio de Janeiro')),
                ('Fortaleza', (select idcidade from cidade where nome = 'Fortaleza')),
                ('Grêmio', (select idcidade from cidade where nome = 'Porto Alegre')),
                ('Internacional', (select idcidade from cidade where nome = 'Porto Alegre')),
                ('Juventude', (select idcidade from cidade where nome = 'Caxias do Sul')),                
                ('Palmeiras', (select idcidade from cidade where nome = 'São Paulo')),
                ('Red Bull Bragantino', (select idcidade from cidade where nome = 'Bragança Paulista')),
                ('São Paulo', (select idcidade from cidade where nome = 'São Paulo')),
                ('Vasco da Gama', (select idcidade from cidade where nome = 'Rio de Janeiro')),
                ('Vitória', (select idcidade from cidade where nome = 'Salvador'))
                """)    

    cur.execute("""
                INSERT INTO Jogador (Nome, DataNascimento, IdNacionalidade, IdPosicao) VALUES
                
                -- Athletico Paranaense

                -- Goleiros
                ('Leonardo Linck', '2001-03-03', 1, 1),
                ('Mycael Pontes Moreira', '2004-03-12', 1, 1),
                ('Matheus Soares Rocha', NULL, 1, 1),

                -- Defensores
                ('Kaique Rocha', '2001-02-28', 1, 2),
                ('Lucas Esquivel', '2002-04-22', 2, 5),
                ('Thiago Heleno', '1988-09-17', 1, 2),
                ('Leonardo Godoy', '1995-04-28', 2, 5),
                ('Mateo Gamarra', '2000-07-20', 3, 2),
                ('Madson', '1992-01-13', 1, 5),
                ('Fernando Bueno', '1999-09-14', 1, 5),
                ('Luan Patrick', '2002-01-20', 1, 2),
                ('Lucas Belezi', '2003-01-01', 1, 2),
                ('Marcos Victor', '2003-01-01', 1, 2),

                -- Meio-campistas
                ('Erick', '1997-11-14', 1, 3),
                ('Fernandinho', '1985-05-04', 1, 3),
                ('Christian', '2000-06-19', 1, 3),
                ('Bruno Zapelli', '2002-05-16', 2, 3),
                ('Nikão', '1992-07-29', 1, 3),
                ('Gabriel Girotto', '1992-07-29', 1, 3),
                ('João Victor Machado Cruz', '2005-01-01', 1, 3),
                ('Antonio Costa', '2001-01-01', 1, 3),
                ('José Vitor Silva Neves', '2000-01-01', 1, 3),
                ('Bruno Praxedes', '2002-02-08', 1, 3),
                ('Eduardo Kogitzki Anastacio', '2004-01-01', 1, 3),

                -- Atacantes
                ('Julimar', '2001-01-01', 1, 4),
                ('Tomás Cuello', '2000-03-05', 2, 4),
                ('Pablo Felipe', '1992-06-23', 1, 4),
                ('Agustín Canobbio', '1998-10-01', 4, 4),
                ('Gonzalo Mastriani', '1993-04-28', 4, 4),
                ('Lucas Di Yorio', '1996-04-18', 2, 4),

                -- Athletico Goianiense
                
                -- Goleiros
                ('Lucas Gomes Fonseca Barreto', '2002-02-18', 1, 1),
                ('Ronaldo Vieira', '1996-01-01', 1, 1),
                ('Pedro Henrique Silva', '1998-01-01', 1, 1),

                -- Defensores
                ('Marcão', '2001-05-15', 1, 2),
                ('Luiz Felipe do Nascimento', '1993-09-09', 1, 2),
                ('Pedro Henrique Pereira da Silva', '1992-12-18', 1, 2),
                ('Adriano Martins', '1995-01-01', 1, 2),
                ('Gustavo Daniel', '1997-01-01', 1, 5),
                ('Yeferson Rodallega', '1995-01-01', 2, 5),
                ('Alix', '1998-01-01', 1, 5),
                ('Magalhães', '1996-01-01', 1, 5),

                -- Meio-campistas
                ('Gustavo Campanharo', '1992-04-04', 1, 3),
                ('Gabriel Baralhas', '1998-01-01', 1, 3),
                ('Shaylon', '1997-01-01', 1, 3),
                ('Rhaldney', '1999-01-01', 1, 3),
                ('Robert dos Santos Conceição', '2003-07-20', 1, 3),
                ('Jorginho', '1991-01-01', 1, 3),

                -- Atacantes
                ('Luiz Fernando Moraes dos Santos', '1996-01-01', 1, 4),
                ('Derek', '1997-01-01', 1, 4),
                ('Yony González', '1994-07-20', 3, 4),
                ('Emiliano Rodríguez', '1995-01-01', 2, 4),
                ('Alejo Cruz', '1998-01-01', 2, 4),
                ('Vagner Love', '1984-06-11', 1, 4),

                -- Atletico Mineiro
				
                -- Goleiros
                ('Gabriel Delfim', '1999-03-15', 1, 1),
                ('Everson', '1990-07-22', 1, 1),
                ('Gabriel Átila', '2002-11-10', 1, 1),
                ('Robert', '2001-05-05', 1, 1),

                -- Zagueiros
                ('Igor Rabello', '1995-08-28', 1, 2),
                ('Rômulo', '2000-04-12', 1, 2),
                ('Lyanco', '1997-02-01', 1, 2),
                ('Júnior Alonso', '1993-02-09', 2, 2),
                ('Ivan Román', '1998-06-18', 2, 2),
                ('Vitor Hugo', '2000-09-30', 1, 2),

                -- Laterais
                ('Guilherme Arana', '1997-04-14', 1, 5),
                ('Saravia', '1993-06-16', 2, 5),
                ('Natanael', '2002-12-20', 1, 5),
                ('Caio', '2001-07-25', 1, 5),

                -- Meio-campistas
                ('Rubens', '2000-10-10', 1, 3),
                ('Igor Gomes', '1999-03-17', 1, 3),
                ('Alan Franco', '1998-08-21', 3, 3),
                ('Gustavo Scarpa', '1994-01-05', 1, 3),
                ('Bernard', '1992-09-08', 1, 3),
                ('Fausto Vera', '2000-03-26', 2, 3),
                ('Gabriel Menino', '2000-09-29', 1, 3),
                ('Patrick', '1992-03-13', 1, 3),

                -- Atacantes
                ('Hulk', '1986-07-25', 1, 4),
                ('Cadu', '2000-11-11', 1, 4),
                ('Brahian Palacios', '2001-02-10', 3, 4),
                ('Júnior Santos', '1994-10-11', 1, 4),
                ('Cuello', '1999-03-19', 2, 4),
                ('Caio Maia', '2002-06-15', 1, 4),
                ('Rony', '1995-05-11', 1, 4),
                ('João Marcelo', '2001-04-15', 1, 4),
                ('Dudu', '1992-01-01', 1, 4),

                -- Bahia
                
                -- Goleiros
                ('Danilo Fernandes', '1988-04-03', 1, 1),
                ('Marcos Felipe', '1996-04-13', 1, 1),
                ('Gabriel Souza', '2000-06-15', 1, 1),
                ('Ronaldo', '1997-08-10', 1, 1),

                -- Laterais
                ('Zé Guilherme', '1999-02-20', 1, 5),
                ('Kauã Davi', '2002-09-05', 1, 5),
                ('Santiago Arias', '1992-01-13', 2, 5),
                ('Luciano Juba', '1999-08-29', 1, 5),
                ('Iago Borduchi', '1997-03-23', 1, 5),
                ('Gilberto', '1993-03-07', 1, 5),

                -- Zagueiros
                ('Ramos Mingo', '1995-11-11', 3, 2),
                ('Kanu', '1997-03-22', 1, 2),
                ('David Duarte', '1995-05-24', 1, 2),
                ('Gabriel Xavier', '2001-04-15', 1, 2),

                -- Meio-campistas
                ('Michel Araújo', '1996-09-28', 4, 3),
                ('Rodrigo Nestor', '2000-08-09', 1, 3),
                ('Erick Vitinho', '1998-02-17', 1, 3),
                ('Jota', '2002-12-12', 1, 3),
                ('Rezende', '1995-01-10', 1, 3),
                ('Jean Lucas', '1998-06-22', 1, 3),
                ('Cauly', '1995-09-15', 1, 3),
                ('Caio Alexandre', '1999-02-24', 1, 3),
                ('Nicolás Acevedo', '1999-04-14', 5, 3),
                ('Everton Ribeiro', '1989-04-10', 1, 3),

                -- Atacantes
                ('Kayky', '2003-06-11', 1, 4),
                ('Willian José', '1991-11-23', 1, 4),
                ('Erick Pulga', '2000-07-07', 1, 4),
                ('Tiago', '2002-10-10', 1, 4),
                ('Luciano Rodríguez', '2003-07-16', 5, 4),
                ('Ademir', '1995-02-16', 1, 4),
                
                -- Botafogo

                -- Goleiros
                ('Gatito Fernández', '1988-03-29', 2, 1),
                ('John Victor', '1996-03-13', 1, 1),
                ('Douglas Borges', '1990-03-30', 1, 1),

                -- Laterais
                ('Mateo Ponte', '2003-05-24', 3, 5),
                ('Alex Telles', '1992-12-15', 1, 5),
                ('Hugo', '1997-03-25', 1, 5),
                ('Rafael', '1990-07-09', 1, 5),

                -- Zagueiros
                ('Lucas Halter', '2000-05-02', 1, 2),
                ('Alexander Barboza', '1995-03-16', 4, 2),
                ('Bastos', '1996-05-23', 5, 2),
                ('Victor Cuesta', '1988-11-19', 4, 2),

                -- Meio-campistas
                ('Danilo Barbosa', '1996-02-28', 1, 3),
                ('Marlon Freitas', '1995-03-27', 1, 3),
                ('Gregore', '1994-03-02', 1, 3),
                ('Tchê Tchê', '1992-08-30', 1, 3),
                ('Patrick de Paula', '1999-09-08', 1, 3),
                ('Matías Segovia', '2003-05-09', 6, 3),
                ('Thiago Almada', '2001-04-26', 4, 3),

                -- Atacantes
                ('Luiz Henrique', '2001-01-02', 1, 4),
                ('Jefferson Savarino', '1996-11-11', 7, 4),
                ('Igor Jesus', '2001-03-07', 1, 4),
                ('Tiquinho Soares', '1991-01-17', 1, 4),
                ('Júnior Santos', '1994-10-11', 1, 4),
                ('Elias Manoel', '2001-11-12', 1, 4),

                -- Corinthians
                
                -- Goleiros
                ('Carlos Miguel', '1999-06-04', 1, 1),
                ('Matheus Donelli', '2002-05-17', 1, 1),

                -- Zagueiros
                ('Félix Torres', '1997-01-11', 2, 2),
                ('Gustavo Henrique', '1993-03-24', 1, 2),
                ('Cacá', '1999-04-25', 1, 2),
                ('André Ramalho', '1992-02-16', 1, 2),
                ('Caetano', '1999-09-06', 1, 2),

                -- Laterais
                ('Diego Palacios', '1999-07-12', 3, 5),
                ('Fabrizio Angileri', '1994-03-15', 4, 5),
                ('Matheus Bidu', '1999-02-18', 1, 5),
                ('Léo Mana', '2004-03-06', 1, 5),
                ('Matheuzinho', '2000-09-08', 1, 5),

                -- Meio-campistas
                ('Maycon', '1997-07-15', 1, 3),
                ('Raniele', '1997-12-31', 1, 3),
                ('Breno Bidon', '2003-08-10', 1, 3),
                ('Rodrigo Garro', '1998-01-04', 4, 3),
                ('Igor Coronado', '1992-08-18', 5, 3),
                ('José Martínez', '1994-06-19', 6, 3),
                ('Alex Santana', '1995-05-13', 1, 3),
                ('Charles', '1994-02-28', 1, 3),
                ('André Carrillo', '1991-06-14', 7, 3),

                -- Atacantes
                ('Yuri Alberto', '2001-03-18', 1, 4),
                ('Memphis Depay', '1994-02-13', 8, 4),
                ('Ángel Romero', '1992-07-04', 9, 4),
                ('Pedro Raul', '1996-11-11', 1, 4),
                ('Talles Magno', '2002-06-26', 1, 4),
                ('Giovane', '2003-03-01', 1, 4),
                ('Pedro Henrique', '1990-09-02', 1, 4),
                ('Héctor Hernández', '1995-05-14', 10, 4)
                """)

    cur.execute("""                
                INSERT INTO Tecnico (IdTecnico, Nome, DataNascimento, IdNacionalidade) VALUES
                (1, 'Cuca', DATE '1963-06-07', 1),                 -- Brasil
                (2, 'Anderson Gomes', DATE '1980-04-10', 1),       -- Brasil
                (3, 'Gabriel Milito', DATE '1980-09-07', 2),       -- Argentina
                (4, 'Rogério Ceni', DATE '1973-01-22', 1),         -- Brasil
                (5, 'Artur Jorge', DATE '1971-02-16', 3),          -- Portugal
                (6, 'Ramón Díaz', DATE '1959-08-29', 2),           -- Argentina
                (7, 'Cláudio Tencati', DATE '1973-12-09', 1),      -- Brasil
                (8, 'Fernando Seabra', DATE '1980-05-01', 1),      -- Brasil
                (9, 'Luiz Fernando Iubel', DATE '1989-07-16', 1),  -- Brasil
                (10, 'Filipe Luís', DATE '1985-08-09', 1),         -- Brasil
                (11, 'Mano Menezes', DATE '1962-06-11', 1),        -- Brasil
                (12, 'Juan Pablo Vojvoda', DATE '1975-07-22', 2),  -- Argentina
                (13, 'Renato Portaluppi', DATE '1962-09-09', 1),   -- Brasil
                (14, 'Roger Machado', DATE '1975-04-25', 1),       -- Brasil
                (15, 'Fábio Matias', DATE '1981-11-18', 1),        -- Brasil
                (16, 'Abel Ferreira', DATE '1978-12-22', 3),       -- Portugal
                (17, 'Luis Zubeldía', DATE '1981-01-13', 2),       -- Argentina
                (18, 'Rafael Paiva', DATE '1986-03-15', 1),        -- Brasil
                (19, 'Thiago Carpini', DATE '1984-07-16', 1),      -- Brasil
                (20, 'Fabio Carille', DATE '1989-07-16', 1)       -- Brasil
                """)

    cur.execute("""
                INSERT INTO Campeonato (Nome, Premiacao, IdFederacao) VALUES
                ('Campeonato Brasileiro', 481000000, null)
                """)    

    cur.execute("""
                INSERT INTO Temporada (QuantidadeRodadas, DataInicio, DataFim, Ano, IdCampeonato) VALUES
                (38, '2024-04-13', '2024-12-08', 2024, (select idcampeonato from campeonato where nome = 'Campeonato Brasileiro'))
                """)
    
    cur.execute("""
                INSERT INTO Rodada (NumeroRodada, IdTemporada) VALUES
                (1, (select idtemporada from temporada)),
                (2, (select idtemporada from temporada)),
                (3, (select idtemporada from temporada)),
                (4, (select idtemporada from temporada)),
                (5, (select idtemporada from temporada)),
                (6, (select idtemporada from temporada)),
                (7, (select idtemporada from temporada)),
                (8, (select idtemporada from temporada)),
                (9, (select idtemporada from temporada)),
                (10, (select idtemporada from temporada)),
                (11, (select idtemporada from temporada)),
                (12, (select idtemporada from temporada)),
                (13, (select idtemporada from temporada)),
                (14, (select idtemporada from temporada)),
                (15, (select idtemporada from temporada)),
                (16, (select idtemporada from temporada)),
                (17, (select idtemporada from temporada)),
                (18, (select idtemporada from temporada)),
                (19, (select idtemporada from temporada)),
                (20, (select idtemporada from temporada)),
                (21, (select idtemporada from temporada)),
                (22, (select idtemporada from temporada)),
                (23, (select idtemporada from temporada)),
                (24, (select idtemporada from temporada)),
                (25, (select idtemporada from temporada)),
                (26, (select idtemporada from temporada)),
                (27, (select idtemporada from temporada)),
                (28, (select idtemporada from temporada)),
                (29, (select idtemporada from temporada)),
                (30, (select idtemporada from temporada)),
                (31, (select idtemporada from temporada)),
                (32, (select idtemporada from temporada)),
                (33, (select idtemporada from temporada)),
                (34, (select idtemporada from temporada)),
                (35, (select idtemporada from temporada)),
                (36, (select idtemporada from temporada)),
                (37, (select idtemporada from temporada)),
                (38, (select idtemporada from temporada))
                """)    

    cur.execute("""                
                INSERT INTO Partida (DataHora, Publico, Renda, IdRodada, IdEstadio, IdTimeMandante, IdTimeVisitante) VALUES
                ('13/04/2024 18:30', 0, 0, 01, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Bahia')
                ('13/04/2024 18:30', 0, 0, 01, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Juventude')
                ('13/04/2024 21:00', 0, 0, 01, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('13/04/2024 21:00', 0, 0, 01, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Fortaleza')
                ('14/04/2024 16:00', 0, 0, 01, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Flamengo')
                ('14/04/2024 16:00', 0, 0, 01, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Grêmio')
                ('14/04/2024 16:00', 0, 0, 01, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Atlético Mineiro')
                ('14/04/2024 16:00', 0, 0, 01, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Cuiabá')
                ('14/04/2024 17:00', 0, 0, 01, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Botafogo')
                ('14/04/2024 18:30', 0, 0, 01, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Palmeiras')
                ('16/04/2024 21:30', 0, 0, 02, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Fluminense')
                ('17/04/2024 19:00', 0, 0, 02, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Atlético Paranaense')
                ('17/04/2024 19:00', 0, 0, 02, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Criciúma')
                ('17/04/2024 19:00', 0, 0, 02, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Vasco')
                ('17/04/2024 20:00', 0, 0, 02, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Cruzeiro')
                ('17/04/2024 20:00', 0, 0, 02, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Corinthians')
                ('17/04/2024 21:30', 0, 0, 02, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Internacional')
                ('17/04/2024 21:30', 0, 0, 02, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'São Paulo')
                ('18/04/2024 21:30', 0, 0, 02, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Atlético Goianiense')
                ('05/06/2024 20:00', 0, 0, 02, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Vitória')
                ('20/04/2024 16:00', 0, 0, 03, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Vasco')
                ('20/04/2024 18:30', 0, 0, 03, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Cuiabá')
                ('20/04/2024 18:30', 0, 0, 03, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Corinthians')
                ('20/04/2024 21:00', 0, 0, 03, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Cruzeiro')
                ('21/04/2024 16:00', 0, 0, 03, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Bahia')
                ('21/04/2024 16:00', 0, 0, 03, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Flamengo')
                ('21/04/2024 16:00', 0, 0, 03, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Internacional')
                ('21/04/2024 18:30', 0, 0, 03, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Juventude')
                ('21/04/2024 18:30', 0, 0, 03, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'São Paulo')
                ('24/07/2024 19:00', 0, 0, 03, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Fortaleza')
                ('27/04/2024 16:00', 0, 0, 04, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Criciúma')
                ('27/04/2024 18:30', 0, 0, 04, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Atlético Mineiro')
                ('27/04/2024 20:00', 0, 0, 04, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Grêmio')
                ('28/04/2024 11:00', 0, 0, 04, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Botafogo')
                ('28/04/2024 16:00', 0, 0, 04, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Vitória')
                ('28/04/2024 16:00', 0, 0, 04, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Fluminense')
                ('28/04/2024 18:30', 0, 0, 04, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('28/04/2024 18:30', 0, 0, 04, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Atlético Paranaense')
                ('28/04/2024 20:00', 0, 0, 04, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Atlético Goianiense')
                ('29/04/2024 20:00', 0, 0, 04, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Palmeiras')
                ('04/05/2024 16:00', 0, 0, 05, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Atlético Mineiro')
                ('04/05/2024 18:30', 0, 0, 05, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Flamengo')
                ('04/05/2024 20:00', 0, 0, 05, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Fortaleza')
                ('05/05/2024 16:00', 0, 0, 05, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'São Paulo')
                ('05/05/2024 16:00', 0, 0, 05, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Vasco')
                ('05/05/2024 18:30', 0, 0, 05, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Bahia')
                ('05/05/2024 18:30', 0, 0, 05, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Palmeiras')
                ('05/06/2024 19:00', 0, 0, 05, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Atlético Goianiense')
                ('28/08/2024 19h30', 0, 0, 05, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Internacional')
                ('11/05/2024 16:00', 0, 0, 06, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Corinthians')
                ('12/05/2024 11:00', 0, 0, 06, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Vitória')
                ('12/05/2024 16:00', 0, 0, 06, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Cruzeiro')
                ('12/05/2024 16:00', 0, 0, 06, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Atlético Paranaense')
                ('12/05/2024 16:00', 0, 0, 06, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Botafogo')
                ('12/05/2024 18:30', 0, 0, 06, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('13/05/2024 19:00', 0, 0, 06, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Fluminense')
                ('09/06/2024 20:00', 0, 0, 06, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Cuiabá')
                ('14/08/2024 19h30', 0, 0, 06, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Juventude')
                ('01/06/2024 16:00', 0, 0, 07, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Atlético Goianiense')
                ('01/06/2024 16:00', 0, 0, 07, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('01/06/2024 18:30', 0, 0, 07, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Internacional')
                ('01/06/2024 18:30', 0, 0, 07, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Juventude')
                ('01/06/2024 21:30', 0, 0, 07, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Botafogo')
                ('02/06/2024 16:00', 0, 0, 07, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Flamengo')
                ('02/06/2024 16:00', 0, 0, 07, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Palmeiras')
                ('02/06/2024 16:00', 0, 0, 07, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Bahia')
                ('02/06/2024 18:30', 0, 0, 07, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Atlético Paranaense')
                ('02/06/2024 18:30', 0, 0, 07, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Cruzeiro')
                ('11/06/2024 19:00', 0, 0, 08, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Vitória')
                ('11/06/2024 19:00', 0, 0, 08, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Corinthians')
                ('11/06/2024 20:00', 0, 0, 08, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Fluminense')
                ('11/06/2024 21:30', 0, 0, 08, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Atlético Mineiro')
                ('13/06/2024 19:00', 0, 0, 08, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Cuiabá')
                ('13/06/2024 20:00', 0, 0, 08, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Criciúma')
                ('13/06/2024 20:00', 0, 0, 08, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Grêmio')
                ('13/06/2024 20:00', 0, 0, 08, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'São Paulo')
                ('13/06/2024 21:30', 0, 0, 08, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Vasco')
                ('13/06/2024 21:30', 0, 0, 08, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Fortaleza')
                ('15/06/2024 18:30', 0, 0, 09, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Juventude')
                ('15/06/2024 21:00', 0, 0, 09, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Atlético Goianiense')
                ('16/06/2024 16:00', 0, 0, 09, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Internacional')
                ('16/06/2024 16:00', 0, 0, 09, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Flamengo')
                ('16/06/2024 16:00', 0, 0, 09, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'São Paulo')
                ('16/06/2024 18:30', 0, 0, 09, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Bahia')
                ('16/06/2024 18:30', 0, 0, 09, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Botafogo')
                ('16/06/2024 18:30', 0, 0, 09, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Cruzeiro')
                ('16/06/2024 18:30', 0, 0, 09, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Fortaleza')
                ('17/06/2024 21:30', 0, 0, 09, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Palmeiras')
                ('19/06/2024 19:00', 0, 0, 10, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Atlético Paranaense')
                ('19/06/2024 19:00', 0, 0, 10, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Criciúma')
                ('19/06/2024 20:00', 0, 0, 10, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Grêmio')
                ('19/06/2024 20:00', 0, 0, 10, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Vasco')
                ('19/06/2024 20:00', 0, 0, 10, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Cuiabá')
                ('19/06/2024 21:30', 0, 0, 10, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Corinthians')
                ('19/06/2024 21:30', 0, 0, 10, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Fluminense')
                ('20/06/2024 18:30', 0, 0, 10, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Atlético Mineiro')
                ('20/06/2024 20:00', 0, 0, 10, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Bahia')
                ('20/06/2024 21:30', 0, 0, 10, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('22/06/2024 16:00', 0, 0, 11, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Botafogo')
                ('22/06/2024 17h30', 0, 0, 11, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Internacional')
                ('22/06/2024 18:30', 0, 0, 11, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Atlético Goianiense')
                ('22/06/2024 21:30', 0, 0, 11, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'São Paulo')
                ('23/06/2024 16:00', 0, 0, 11, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Flamengo')
                ('23/06/2024 16:00', 0, 0, 11, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Corinthians')
                ('23/06/2024 16:00', 0, 0, 11, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Cruzeiro')
                ('23/06/2024 18:30', 0, 0, 11, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Juventude')
                ('23/06/2024 18:30', 0, 0, 11, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Vitória')
                ('23/06/2024 18:30', 0, 0, 11, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Fortaleza')
                ('26/06/2024 19:00', 0, 0, 12, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Atlético Paranaense')
                ('26/06/2024 19:00', 0, 0, 12, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('26/06/2024 20:00', 0, 0, 12, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Cuiabá')
                ('26/06/2024 20:00', 0, 0, 12, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Flamengo')
                ('26/06/2024 20:00', 0, 0, 12, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Grêmio')
                ('26/06/2024 21:30', 0, 0, 12, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Vasco')
                ('26/06/2024 21:30', 0, 0, 12, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Atlético Mineiro')
                ('26/06/2024 21:30', 0, 0, 12, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Palmeiras')
                ('27/06/2024 19:00', 0, 0, 12, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Vitória')
                ('27/06/2024 20:00', 0, 0, 12, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Criciúma')
                ('29/06/2024 18:30', 0, 0, 13, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('29/06/2024 19:00', 0, 0, 13, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Botafogo')
                ('30/06/2024 11:00', 0, 0, 13, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Atlético Goianiense')
                ('30/06/2024 16:00', 0, 0, 13, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Bahia')
                ('30/06/2024 16:00', 0, 0, 13, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Fluminense')
                ('30/06/2024 16:00', 0, 0, 13, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Juventude')
                ('30/06/2024 18:30', 0, 0, 13, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Atlético Paranaense')
                ('30/06/2024 18:30', 0, 0, 13, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Cruzeiro')
                ('30/06/2024 18:30', 0, 0, 13, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Internacional')
                ('01/07/2024 20:00', 0, 0, 13, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Corinthians')
                ('03/07/2024 19:00', 0, 0, 14, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Botafogo')
                ('03/07/2024 20:00', 0, 0, 14, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Cruzeiro')
                ('03/07/2024 20:00', 0, 0, 14, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Fortaleza')
                ('03/07/2024 21:30', 0, 0, 14, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Atlético Goianiense')
                ('03/07/2024 21:30', 0, 0, 14, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'São Paulo')
                ('03/07/2024 21:30', 0, 0, 14, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Flamengo')
                ('04/07/2024 19:00', 0, 0, 14, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Palmeiras')
                ('04/07/2024 19:00', 0, 0, 14, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Juventude')
                ('04/07/2024 20:00', 0, 0, 14, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Vitória')
                ('04/07/2024 20:00', 0, 0, 14, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Internacional')
                ('06/07/2024 20:00', 0, 0, 15, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Cuiabá')
                ('06/07/2024 20:00', 0, 0, 15, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('07/07/2024 16:00', 0, 0, 15, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Corinthians')
                ('07/07/2024 16:00', 0, 0, 15, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Grêmio')
                ('07/07/2024 16:00', 0, 0, 15, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Fluminense')
                ('07/07/2024 18:00', 0, 0, 15, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Vasco')
                ('07/07/2024 18:30', 0, 0, 15, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Criciúma')
                ('07/07/2024 18:30', 0, 0, 15, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Bahia')
                ('07/07/2024 18:30', 0, 0, 15, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Atlético Paranaense')
                ('07/07/2024 20:30', 0, 0, 15, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Atlético Mineiro')
                ('10/07/2024 18:30', 0, 0, 16, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Cruzeiro')
                ('10/07/2024 19:00', 0, 0, 16, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Bahia')
                ('10/07/2024 19:00', 0, 0, 16, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Corinthians')
                ('11/07/2024 19h30', 0, 0, 16, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Atlético Goianiense')
                ('11/07/2024 20:00', 0, 0, 16, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Fortaleza')
                ('11/07/2024 20:00', 0, 0, 16, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Fluminense')
                ('11/07/2024 21:30', 0, 0, 16, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'São Paulo')
                ('11/07/2024 21:30', 0, 0, 16, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Botafogo')
                ('05/09/2024 20:00', 0, 0, 16, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Juventude')
                ('13/07/2024 16:00', 0, 0, 17, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('13/07/2024 16:00', 0, 0, 17, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Cuiabá')
                ('16/07/2024 19:00', 0, 0, 17, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Atlético Mineiro')
                ('16/07/2024 21:00', 0, 0, 17, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Criciúma')
                ('17/07/2024 19:00', 0, 0, 17, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Vasco')
                ('17/07/2024 20:00', 0, 0, 17, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Grêmio')
                ('17/07/2024 21:30', 0, 0, 17, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Vitória')
                ('17/07/2024 21:30', 0, 0, 17, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Palmeiras')
                ('20/07/2024 16:00', 0, 0, 18, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Criciúma')
                ('20/07/2024 18:30', 0, 0, 18, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Internacional')
                ('20/07/2024 21:00', 0, 0, 18, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Cruzeiro')
                ('21/07/2024 11:00', 0, 0, 18, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Vitória')
                ('21/07/2024 16:00', 0, 0, 18, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Vasco')
                ('21/07/2024 16:00', 0, 0, 18, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Corinthians')
                ('21/07/2024 18:30', 0, 0, 18, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Atlético Paranaense')
                ('21/07/2024 18:30', 0, 0, 18, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Atlético Goianiense')
                ('21/07/2024 18:30', 0, 0, 18, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'São Paulo')
                ('21/07/2024 20:00', 0, 0, 18, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Fluminense')
                ('24/07/2024 19:00', 0, 0, 19, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Juventude')
                ('24/07/2024 19h30', 0, 0, 19, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Botafogo')
                ('24/07/2024 20:00', 0, 0, 19, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Flamengo')
                ('24/07/2024 21:30', 0, 0, 19, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Palmeiras')
                ('24/07/2024 21:30', 0, 0, 19, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Bahia')
                ('25/07/2024 20:00', 0, 0, 19, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Grêmio')
                ('28/08/2024 19h30', 0, 0, 19, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('27/07/2024 19:00', 0, 0, 20, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Vitória')
                ('27/07/2024 19:00', 0, 0, 20, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Criciúma')
                ('27/07/2024 20:00', 0, 0, 20, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Internacional')
                ('27/07/2024 21:30', 0, 0, 20, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'São Paulo')
                ('27/07/2024 21:30', 0, 0, 20, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Cruzeiro')
                ('28/07/2024 11:00', 0, 0, 20, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Fluminense')
                ('28/07/2024 16:00', 0, 0, 20, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Atlético Goianiense')
                ('28/07/2024 19:00', 0, 0, 20, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Vasco')
                ('28/07/2024 19:00', 0, 0, 20, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Atlético Paranaense')
                ('28/07/2024 19:00', 0, 0, 20, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Corinthians')
                ('03/08/2024 19:00', 0, 0, 21, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('03/08/2024 20:00', 0, 0, 21, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Cuiabá')
                ('03/08/2024 20:00', 0, 0, 21, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Atlético Mineiro')
                ('03/08/2024 21:30', 0, 0, 21, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Flamengo')
                ('04/08/2024 16:00', 0, 0, 21, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Bahia')
                ('04/08/2024 16:00', 0, 0, 21, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Juventude')
                ('04/08/2024 16:00', 0, 0, 21, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Grêmio')
                ('04/08/2024 16:00', 0, 0, 21, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Botafogo')
                ('04/08/2024 19:00', 0, 0, 21, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Palmeiras')
                ('05/08/2024 21:00', 0, 0, 21, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Fortaleza')
                ('10/08/2024 16:00', 0, 0, 22, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Criciúma')
                ('10/08/2024 19:00', 0, 0, 22, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Grêmio')
                ('10/08/2024 21:30', 0, 0, 22, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Atlético Mineiro')
                ('10/08/2024 21:30', 0, 0, 22, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Fluminense')
                ('10/08/2024 21:30', 0, 0, 22, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('11/08/2024 11:00', 0, 0, 22, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Botafogo')
                ('11/08/2024 16:00', 0, 0, 22, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Vitória')
                ('11/08/2024 16:00', 0, 0, 22, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Palmeiras')
                ('11/08/2024 16:00', 0, 0, 22, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Atlético Goianiense')
                ('11/08/2024 19:00', 0, 0, 22, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Atlético Paranaense')
                ('17/08/2024 16:00', 0, 0, 23, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Cuiabá')
                ('17/08/2024 18:30', 0, 0, 23, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Fortaleza')
                ('17/08/2024 18:30', 0, 0, 23, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Bahia')
                ('17/08/2024 21:00', 0, 0, 23, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Corinthians')
                ('18/08/2024 16:00', 0, 0, 23, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'São Paulo')
                ('18/08/2024 16:00', 0, 0, 23, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Internacional')
                ('18/08/2024 16:00', 0, 0, 23, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Vasco')
                ('18/08/2024 16:00', 0, 0, 23, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Juventude')
                ('18/08/2024 18:30', 0, 0, 23, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Flamengo')
                ('19/08/2024 20:00', 0, 0, 23, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Cruzeiro')
                ('24/08/2024 16:00', 0, 0, 24, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Juventude')
                ('24/08/2024 18:30', 0, 0, 24, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Cuiabá')
                ('24/08/2024 21:00', 0, 0, 24, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Fluminense')
                ('25/08/2024 11:00', 0, 0, 24, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Grêmio')
                ('25/08/2024 16:00', 0, 0, 24, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Botafogo')
                ('25/08/2024 16:00', 0, 0, 24, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Cruzeiro')
                ('25/08/2024 16:00', 0, 0, 24, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Corinthians')
                ('25/08/2024 18:30', 0, 0, 24, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Vitória')
                ('25/08/2024 20:00', 0, 0, 24, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('26/08/2024 21:00', 0, 0, 24, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Atlético Paranaense')
                ('31/08/2024 16:00', 0, 0, 25, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Bahia')
                ('31/08/2024 18:30', 0, 0, 25, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Criciúma')
                ('31/08/2024 21:00', 0, 0, 25, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Fortaleza')
                ('01/09/2024 11:00', 0, 0, 25, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Atlético Goianiense')
                ('01/09/2024 16:00', 0, 0, 25, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Atlético Mineiro')
                ('01/09/2024 16:00', 0, 0, 25, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Flamengo')
                ('01/09/2024 16:00', 0, 0, 25, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Palmeiras')
                ('01/09/2024 18:30', 0, 0, 25, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Vasco')
                ('01/09/2024 18:30', 0, 0, 25, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'São Paulo')
                ('01/09/2024 18:30', 0, 0, 25, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Internacional')
                ('14/09/2024 16:00', 0, 0, 26, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Vitória')
                ('14/09/2024 18:30', 0, 0, 26, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Fortaleza')
                ('14/09/2024 21:00', 0, 0, 26, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Corinthians')
                ('15/09/2024 16:00', 0, 0, 26, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Criciúma')
                ('15/09/2024 16:00', 0, 0, 26, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Grêmio')
                ('15/09/2024 16:00', 0, 0, 26, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Fluminense')
                ('15/09/2024 18:30', 0, 0, 26, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'São Paulo')
                ('15/09/2024 18:30', 0, 0, 26, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Atlético Mineiro')
                ('15/09/2024 18:30', 0, 0, 26, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Vasco')
                ('16/09/2024 20:00', 0, 0, 26, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Cuiabá')
                ('21/09/2024 16:00', 0, 0, 27, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Juventude')
                ('21/09/2024 16:00', 0, 0, 27, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Atlético Goianiense')
                ('21/09/2024 18:30', 0, 0, 27, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Botafogo')
                ('21/09/2024 21:00', 0, 0, 27, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Bahia')
                ('22/09/2024 16:00', 0, 0, 27, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('22/09/2024 16:00', 0, 0, 27, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Palmeiras')
                ('22/09/2024 18:30', 0, 0, 27, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Internacional')
                ('22/09/2024 18:30', 0, 0, 27, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Cruzeiro')
                ('22/09/2024 18:30', 0, 0, 27, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Atlético Paranaense')
                ('22/09/2024 18:30', 0, 0, 27, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Flamengo')
                ('28/09/2024 18:30', 0, 0, 28, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Atlético Mineiro')
                ('28/09/2024 21:00', 0, 0, 28, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Grêmio')
                ('29/09/2024 11:00', 0, 0, 28, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Vitória')
                ('29/09/2024 16:00', 0, 0, 28, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Corinthians')
                ('29/09/2024 16:00', 0, 0, 28, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Cuiabá')
                ('29/09/2024 16:00', 0, 0, 28, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Fluminense')
                ('29/09/2024 18:30', 0, 0, 28, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Vasco')
                ('29/09/2024 18:30', 0, 0, 28, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Criciúma')
                ('29/09/2024 18:30', 0, 0, 28, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('29/09/2024 20:00', 0, 0, 28, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Atlético Paranaense')
                ('03/10/2024 19:00', 0, 0, 29, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Atlético Goianiense')
                ('03/10/2024 21:30', 0, 0, 29, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Cruzeiro')
                ('04/10/2024 21:30', 0, 0, 29, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Fortaleza')
                ('05/10/2024 16h30', 0, 0, 29, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Vitória')
                ('05/10/2024 16h30', 0, 0, 29, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Palmeiras')
                ('05/10/2024 16h30', 0, 0, 29, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Botafogo')
                ('05/10/2024 19:00', 0, 0, 29, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Flamengo')
                ('05/10/2024 19:00', 0, 0, 29, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Internacional')
                ('05/10/2024 19:00', 0, 0, 29, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'São Paulo')
                ('05/10/2024 21:00', 0, 0, 29, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Juventude')
                ('16/10/2024 21:45', 0, 0, 30, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Vasco')
                ('16/10/2024 21:45', 0, 0, 30, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Atlético Mineiro')
                ('17/10/2024 20:00', 0, 0, 30, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Fluminense')
                ('17/10/2024 20:00', 0, 0, 30, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), Atlético-PR
                ('18/10/2024 19:00', 0, 0, 30, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Cuiabá')
                ('18/10/2024 20:00', 0, 0, 30, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Criciúma')
                ('18/10/2024 21:30', 0, 0, 30, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Bahia')
                ('19/10/2024 16:00', 0, 0, 30, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Grêmio')
                ('19/10/2024 16:00', 0, 0, 30, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('20/10/2024 20:00', 0, 0, 30, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Palmeiras')
                ('26/10/2024 16h30', 0, 0, 31, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Atlético Goianiense')
                ('26/10/2024 16h30', 0, 0, 31, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Fluminense')
                ('26/10/2024 16h30', 0, 0, 31, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Fortaleza')
                ('26/10/2024 18:30', 0, 0, 31, (select idestadio from estadio where nome = 'Ligga Arena'), Atlético-PR, (select idtime from time where nome = 'Cruzeiro')
                ('26/10/2024 19:00', 0, 0, 31, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Internacional')
                ('26/10/2024 19:00', 0, 0, 31, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Juventude')
                ('26/10/2024 19:00', 0, 0, 31, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Botafogo')
                ('26/10/2024 21:00', 0, 0, 31, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'São Paulo')
                ('28/10/2024 19:00', 0, 0, 31, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Corinthians')
                ('28/10/2024 21:00', 0, 0, 31, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Bahia')
                ('01/11/2024 21:00', 0, 0, 32, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Grêmio')
                ('02/11/2024 16:00', 0, 0, 32, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Cuiabá')
                ('02/11/2024 18:30', 0, 0, 32, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Vitória')
                ('02/11/2024 18:30', 0, 0, 32, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Fortaleza')
                ('04/11/2024 20:00', 0, 0, 32, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Palmeiras')
                ('05/11/2024 21:30', 0, 0, 32, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Criciúma')
                ('05/11/2024 21:30', 0, 0, 32, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'São Paulo')
                ('05/11/2024 21:30', 0, 0, 32, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Vasco')
                ('06/11/2024 21:00', 0, 0, 32, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Flamengo')
                ('06/11/2024 21:00', 0, 0, 32, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Atlético Mineiro')
                ('08/11/2024 19:00', 0, 0, 33, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Fluminense')
                ('08/11/2024 21:30', 0, 0, 33, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Grêmio')
                ('09/11/2024 16:30', 0, 0, 33, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Corinthians')
                ('09/11/2024 16:30', 0, 0, 33, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Cuiabá')
                ('09/11/2024 19:00', 0, 0, 33, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Criciúma')
                ('09/11/2024 19:00', 0, 0, 33, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Vasco')
                ('09/11/2024 19:00', 0, 0, 33, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('09/11/2024 19:00', 0, 0, 33, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Bahia')
                ('09/11/2024 21:00', 0, 0, 33, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Atlético Paranaense')
                ('13/11/2024 20:00', 0, 0, 33, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Atlético Mineiro')
                ('20/11/2024 11:00', 0, 0, 34, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Cruzeiro')
                ('20/11/2024 16:30', 0, 0, 34, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'São Paulo')
                ('20/11/2024 16:30', 0, 0, 34, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Atlético Goianiense')
                ('20/11/2024 16:30', 0, 0, 34, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Vitória')
                ('20/11/2024 19:00', 0, 0, 34, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Juventude')
                ('20/11/2024 19:00', 0, 0, 34, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Flamengo')
                ('20/11/2024 20:00', 0, 0, 34, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Palmeiras')
                ('20/11/2024 21:30', 0, 0, 34, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Botafogo')
                ('21/11/2024 20:00', 0, 0, 34, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Internacional')
                ('22/11/2024 21:30', 0, 0, 34, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Fortaleza')
                ('23/11/2024 19:30', 0, 0, 35, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'Vitória')
                ('23/11/2024 19:30', 0, 0, 35, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Palmeiras')
                ('23/11/2024 19:30', 0, 0, 35, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Cuiabá')
                ('23/11/2024 21:30', 0, 0, 35, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Atlético Mineiro')
                ('24/11/2024 16:00', 0, 0, 35, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('24/11/2024 16:00', 0, 0, 35, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Atlético Paranaense')
                ('24/11/2024 16:00', 0, 0, 35, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Vasco')
                ('26/11/2024 19:00', 0, 0, 35, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Criciúma')
                ('26/11/2024 20:00', 0, 0, 35, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Flamengo')
                ('27/11/2024 21:00', 0, 0, 35, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Grêmio')
                ('26/11/2024 21:30', 0, 0, 36, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Juventude')
                ('26/11/2024 21:30', 0, 0, 36, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Botafogo')
                ('30/11/2024 19:30', 0, 0, 36, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Bahia')
                ('30/11/2024 19:30', 0, 0, 36, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Corinthians')
                ('30/11/2024 21:30', 0, 0, 36, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Atlético Goianiense')
                ('01/12/2024 16:00', 0, 0, 36, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'São Paulo')
                ('01/12/2024 16:00', 0, 0, 36, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Internacional')
                ('01/12/2024 18:30', 0, 0, 36, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Fortaleza')
                ('01/12/2024 18:30', 0, 0, 36, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Cruzeiro')
                ('01/12/2024 18:30', 0, 0, 36, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Fluminense')
                ('03/12/2024 20:00', 0, 0, 37, (select idestadio from estadio where nome = 'Neo Química Arena'), (select idtime from time where nome = 'Corinthians'), (select idtime from time where nome = 'Bahia')
                ('04/12/2024 19:00', 0, 0, 37, (select idestadio from estadio where nome = 'São Januário'), (select idtime from time where nome = 'Vasco'), (select idtime from time where nome = 'Atlético Mineiro')
                ('04/12/2024 20:00', 0, 0, 37, (select idestadio from estadio where nome = 'Barradão'), (select idtime from time where nome = 'Vitória'), (select idtime from time where nome = 'Grêmio')
                ('04/12/2024 20:00', 0, 0, 37, (select idestadio from estadio where nome = 'MorumBIS'), (select idtime from time where nome = 'São Paulo'), (select idtime from time where nome = 'Juventude')
                ('04/12/2024 20:00', 0, 0, 37, (select idestadio from estadio where nome = 'Heriberto Hülse'), (select idtime from time where nome = 'Criciúma'), (select idtime from time where nome = 'Flamengo')
                ('04/12/2024 21:30', 0, 0, 37, (select idestadio from estadio where nome = 'Beira-Rio'), (select idtime from time where nome = 'Internacional'), (select idtime from time where nome = 'Botafogo')
                ('04/12/2024 21:30', 0, 0, 37, (select idestadio from estadio where nome = 'Mineirão'), (select idtime from time where nome = 'Cruzeiro'), (select idtime from time where nome = 'Palmeiras')
                ('04/12/2024 21:30', 0, 0, 37, (select idestadio from estadio where nome = 'Antônio Accioly'), (select idtime from time where nome = 'Atlético Goianiense'), (select idtime from time where nome = 'Fortaleza')
                ('05/12/2024 20:00', 0, 0, 37, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Fluminense'), (select idtime from time where nome = 'Cuiabá')
                ('05/12/2024 20:00', 0, 0, 37, (select idestadio from estadio where nome = 'Ligga Arena'), (select idtime from time where nome = 'Atlético Paranaense'), (select idtime from time where nome = 'Red Bull Bragantino')
                ('08/12/2024 16:00', 0, 0, 38, (select idestadio from estadio where nome = 'Arena do (select idtime from time where nome = 'Grêmio')'), (select idtime from time where nome = 'Grêmio'), (select idtime from time where nome = 'Corinthians')
                ('08/12/2024 16:00', 0, 0, 38, (select idestadio from estadio where nome = 'Arena MRV'), (select idtime from time where nome = 'Atlético Mineiro'), (select idtime from time where nome = 'Atlético Paranaense')
                ('08/12/2024 16:00', 0, 0, 38, (select idestadio from estadio where nome = 'Fonte Nova'), (select idtime from time where nome = 'Bahia'), (select idtime from time where nome = 'Atlético Goianiense')
                ('08/12/2024 16:00', 0, 0, 38, (select idestadio from estadio where nome = 'Maracanã'), (select idtime from time where nome = 'Flamengo'), (select idtime from time where nome = 'Vitória')
                ('08/12/2024 16:00', 0, 0, 38, (select idestadio from estadio where nome = 'Nilton Santos'), (select idtime from time where nome = 'Botafogo'), (select idtime from time where nome = 'São Paulo')
                ('08/12/2024 16:00', 0, 0, 38, (select idestadio from estadio where nome = 'Allianz Parque'), (select idtime from time where nome = 'Palmeiras'), (select idtime from time where nome = 'Fluminense')
                ('08/12/2024 16:00', 0, 0, 38, (select idestadio from estadio where nome = 'Nabi Abi Chedid'), (select idtime from time where nome = 'Red Bull Bragantino'), (select idtime from time where nome = 'Criciúma')
                ('08/12/2024 16:00', 0, 0, 38, (select idestadio from estadio where nome = 'Arena Castelão'), (select idtime from time where nome = 'Fortaleza'), (select idtime from time where nome = 'Internacional')
                ('08/12/2024 16:00', 0, 0, 38, (select idestadio from estadio where nome = 'Arena Pantanal'), (select idtime from time where nome = 'Cuiabá'), (select idtime from time where nome = 'Vasco')
                ('08/12/2024 16:00', 0, 0, 38, (select idestadio from estadio where nome = 'Alfredo Jaconi'), (select idtime from time where nome = 'Juventude'), (select idtime from time where nome = 'Cruzeiro')
                """)

    cur.execute("""
                INSERT INTO Evento (TipoEvento, Minuto, IdPartida, IdJogador) VALUES
                (1, 23, 1, 1), -- Gol
                (2, 45, 1, 2); -- Cartão
                """)

    cur.execute("""
                INSERT INTO Participacao (IdTime, IdTemporada) VALUES
                ((select idtime from time where nome = 'Athletico Paranaense'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Atlético Goianiense'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Atlético Mineiro'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Bahia'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Botafogo'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Corinthians'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Criciúma'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Cruzeiro'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Cuiabá'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Flamengo'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Fluminense'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Fortaleza'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Grêmio'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Internacional'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Juventude'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Palmeiras'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Red Bull Bragantino'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'São Paulo'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Vasco da Gama'), (select idtemporada from temporada)),
                ((select idtime from time where nome = 'Vitória'), (select idtemporada from temporada))
                """)    

    cur.execute("""
                INSERT INTO EquipeArbitragem (IdPartida, IdArbitro, IdFuncaoArbitro) VALUES
                (1, 1, 1),
                (1, 2, 2);
                """)

    cur.execute("""
                INSERT INTO ContratoTecnico (IdTecnico, IdTime, DataAssinatura, DataRescisao, MultaRescisoria) VALUES
                (1, (select idtime from time where nome = 'Athletico Paranense'), '2024-04-13', '2024-12-08', 1000000),
                (2, (select idtime from time where nome = 'Atletico Goiniense'), '2024-04-13', '2024-12-08', 1000000),
                (3, (select idtime from time where nome = 'Atletico Mineiro'), '2024-04-13', '2024-12-08', 1000000),
                (4, (select idtime from time where nome = 'Bahia'), '2024-04-13', '2024-12-08', 1000000),
                (5, (select idtime from time where nome = 'Botafogo'), '2024-04-13', '2024-12-08', 1000000),
                (6, (select idtime from time where nome = 'Corinthians'), '2024-04-13', '2024-12-08', 1000000),
                (7, (select idtime from time where nome = 'Criciúma'), '2024-04-13', '2024-12-08', 1000000),
                (8, (select idtime from time where nome = 'Cruzeiro'), '2024-04-13', '2024-12-08', 1000000),
                (9, (select idtime from time where nome = 'Cuiabá'), '2024-04-13', '2024-12-08', 1000000),
                (10, (select idtime from time where nome = 'Flamengo'), '2024-04-13', '2024-12-08', 1000000),
                (11, (select idtime from time where nome = 'Fluminense'), '2024-04-13', '2024-12-08', 1000000),
                (12, (select idtime from time where nome = 'Fortaleza'), '2024-04-13', '2024-12-08', 1000000),
                (13, (select idtime from time where nome = 'Grêmio'), '2024-04-13', '2024-12-08', 1000000),
                (14, (select idtime from time where nome = 'Internacional'), '2024-04-13', '2024-12-08', 1000000),
                (15, (select idtime from time where nome = 'Juventude'), '2024-04-13', '2024-12-08', 1000000),
                (16, (select idtime from time where nome = 'Palmeiras'), '2024-04-13', '2024-12-08', 1000000),
                (17, (select idtime from time where nome = 'São Paulo'), '2024-04-13', '2024-12-08', 1000000),
                (18, (select idtime from time where nome = 'Vasco da Gama'), '2024-04-13', '2024-12-08', 1000000),
                (19, (select idtime from time where nome = 'Vitória'), '2024-04-13', '2024-12-08', 1000000),
                (20, (select idtime from time where nome = 'Santos'), '2024-04-13', '2024-12-08', 1000000)
                """)

    cur.execute("""
                INSERT INTO ContratoJogador (Numero, IdJogador, IdTime, DataRescisao, DataAssinatura, MultaRescisoria) VALUES
                ('CJ001', 1, 1, NULL, '2023-12-15', 50000.00);
                """)

    cur.execute("""
                INSERT INTO Escalacao (IdPartida, IdJogador, IdPosicao) VALUES
                (1, 1, 4),
                (1, 2, 3);
                """)