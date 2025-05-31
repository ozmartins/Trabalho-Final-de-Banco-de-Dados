def create_all_tables(cur):
    cur.execute("CREATE SCHEMA IF NOT EXISTS footballleaguemanager")

    cur.execute("""CREATE TABLE Campeonato (
        IdCampeonato serial PRIMARY KEY,
        Nome varchar(100),
        Premiacao numeric(14,2),
        IdFederacao integer
    )""")

    cur.execute("""CREATE TABLE Federacao (
        IdFederacao serial PRIMARY KEY,
        Nome varchar(100),
        UF varchar(2)
    )""")

    cur.execute("""CREATE TABLE Arbitro (
        IdArbitro serial PRIMARY KEY,
        Nome varchar(100),
        DataNascimento date,
        IdFederacao integer
    )""")

    cur.execute("""CREATE TABLE Cidade (
        IdCidade serial PRIMARY KEY,
        Nome varchar(100),
        UF varchar(2)
    )""")

    cur.execute("""CREATE TABLE Estadio (
        IdEstadio serial PRIMARY KEY,
        Nome varchar(100),
        Capacidade integer,
        IdCidade integer
    )""")

    cur.execute("""CREATE TABLE FuncaoArbitro (
        IdFuncaoArbitro serial PRIMARY KEY,
        Descricao varchar(100)
    )""")

    cur.execute("""CREATE TABLE Temporada (
        IdTemporada serial PRIMARY KEY,
        QuantidadeRodadas integer,
        DataInicio date,
        DataFim date,
        Ano integer,
        IdCampeonato integer
    )""")

    cur.execute("""CREATE TABLE Rodada (
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

    cur.execute("""CREATE TABLE Time (
        IdTime serial PRIMARY KEY,
        Nome varchar(100),
        IdCidade integer
    )""")

    cur.execute("""CREATE TABLE Jogador (
        IdJogador serial PRIMARY KEY,
        Nome varchar(100),
        DataNascimento date,
        IdNacionalidade integer,
        IdPosicao integer
    )""")

    cur.execute("""CREATE TABLE Tecnico (
        Id serial PRIMARY KEY,
        Nome varchar(100),
        DataNascimento date,
        IdNacionalidade integer
    )""")

    cur.execute("""CREATE TABLE Nacionalidade (
        IdNacionalidade serial PRIMARY KEY,
        Descricao varchar(100)
    )""")

    cur.execute("""CREATE TABLE Posicao (
        IdPosicao serial PRIMARY KEY,
        Descricao varchar(100)
    )""")

    cur.execute("""CREATE TABLE Evento (
        IdEvento serial PRIMARY KEY,
        TipoEvento integer,
        Minuto integer,
        IdPartida integer,
        IdJogador integer
    )""")

    cur.execute("""CREATE TABLE Participacao (
        Participacao serial PRIMARY KEY,
        IdTime integer,
        IdTemporada integer
    )""")

    cur.execute("""CREATE TABLE EquipeArbitragem (
        EquipeArbitragem serial PRIMARY KEY,
        IdPartida integer,
        IdArbitro integer,
        IdFuncaoArbitro integer
    )""")

    cur.execute("""CREATE TABLE ContratoTecnico (
        Numero serial PRIMARY KEY,
        IdTecnico integer,
        IdTime integer,
        DataAssinatura date,
        DataRescisao date,
        MultaRescisoria numeric(14,2)
    )""")

    cur.execute("""CREATE TABLE ContratoJogador (
        Numero varchar(50) PRIMARY KEY,
        IdJogador integer,
        IdTime integer,
        DataRescisao date,
        DataAssinatura date,
        MultaRescisoria numeric(14,2)    
    )""")

    cur.execute("""CREATE TABLE Escalacao (
        Escalacao serial PRIMARY KEY,
        IdPartida integer,
        IdJogador integer,
        IdPosicao integer    
    )""")
    
    cur.execute("""ALTER TABLE Campeonato ADD CONSTRAINT FK_Campeonato_Federacao
        FOREIGN KEY (IdFederacao)
        REFERENCES Federacao (IdFederacao)
        ON DELETE SET NULL""")
    
    cur.execute("""ALTER TABLE Arbitro ADD CONSTRAINT FK_Arbitro_Federacao
        FOREIGN KEY (IdFederacao)
        REFERENCES Federacao (IdFederacao)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Estadio ADD CONSTRAINT FK_Estadio_Cidade
        FOREIGN KEY (IdCidade)
        REFERENCES Cidade (IdCidade)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Temporada ADD CONSTRAINT FK_Temporada_Campeonato
        FOREIGN KEY (IdCampeonato)
        REFERENCES Campeonato (IdCampeonato)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Rodada ADD CONSTRAINT FK_Rodada_Temporada
        FOREIGN KEY (IdTemporada)
        REFERENCES Temporada (IdTemporada)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Partida ADD CONSTRAINT FK_Partida_Rodada
        FOREIGN KEY (IdRodada)
        REFERENCES Rodada (IdRodada)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Partida ADD CONSTRAINT FK_Partida_Estadio
        FOREIGN KEY (IdEstadio)
        REFERENCES Estadio (IdEstadio)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Partida ADD CONSTRAINT FK_Partida_TimeMandante
        FOREIGN KEY (IdTimeMandante)
        REFERENCES Time (IdTime)
        ON DELETE CASCADE""")

    cur.execute("""ALTER TABLE Partida ADD CONSTRAINT FK_Partida_TimeVisitante
        FOREIGN KEY (IdTimeVisitante)
        REFERENCES Time (IdTime)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Time ADD CONSTRAINT FK_Time_Cidade
        FOREIGN KEY (IdCidade)
        REFERENCES Cidade (IdCidade)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Jogador ADD CONSTRAINT FK_Jogador_Nacionalidade
        FOREIGN KEY (IdNacionalidade)
        REFERENCES Nacionalidade (IdNacionalidade)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Jogador ADD CONSTRAINT FK_Jogador_Posicao
        FOREIGN KEY (IdPosicao)
        REFERENCES Posicao (IdPosicao)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Tecnico ADD CONSTRAINT FK_Tecnico_Nacionalidade
        FOREIGN KEY (IdNacionalidade)
        REFERENCES Nacionalidade (IdNacionalidade)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Evento ADD CONSTRAINT FK_Evento_Partida
        FOREIGN KEY (IdPartida)
        REFERENCES Partida (IdPartida)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Evento ADD CONSTRAINT FK_Evento_Jogador
        FOREIGN KEY (IdJogador)
        REFERENCES Jogador (IdJogador)
        ON DELETE CASCADE""")
    
    cur.execute("""ALTER TABLE Participacao ADD CONSTRAINT FK_Participacao_Time
        FOREIGN KEY (IdTime)
        REFERENCES Time (IdTime)
        ON DELETE RESTRICT""")
    
    cur.execute("""ALTER TABLE Participacao ADD CONSTRAINT FK_Participacao_Temporada
        FOREIGN KEY (IdTemporada)
        REFERENCES Temporada (IdTemporada)
        ON DELETE SET NULL""")
    
    cur.execute("""ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_Partida
        FOREIGN KEY (IdPartida)
        REFERENCES Partida (IdPartida)
        ON DELETE NO ACTION""")
    
    cur.execute("""ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_Arbitro
        FOREIGN KEY (IdArbitro)
        REFERENCES Arbitro (IdArbitro)
        ON DELETE NO ACTION""")
    
    cur.execute("""ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_FuncaoArbitro
        FOREIGN KEY (IdFuncaoArbitro)
        REFERENCES FuncaoArbitro (IdFuncaoArbitro)
        ON DELETE RESTRICT""")
    
    cur.execute("""ALTER TABLE ContratoTecnico ADD CONSTRAINT FK_ContratoTecnico_Tecnico
        FOREIGN KEY (IdTecnico)
        REFERENCES Tecnico (Id)
        ON DELETE SET NULL""")
    
    cur.execute("""ALTER TABLE ContratoTecnico ADD CONSTRAINT FK_ContratoTecnico_3
        FOREIGN KEY (IdTime)
        REFERENCES Time (IdTime)
        ON DELETE SET NULL""")
    
    cur.execute("""ALTER TABLE ContratoJogador ADD CONSTRAINT FK_ContratoJogador_Jogador
        FOREIGN KEY (IdJogador)
        REFERENCES Jogador (IdJogador)
        ON DELETE SET NULL""")
    
    cur.execute("""ALTER TABLE ContratoJogador ADD CONSTRAINT FK_ContratoJogador_Time
        FOREIGN KEY (IdTime)
        REFERENCES Time (IdTime)
        ON DELETE SET NULL""")
    
    cur.execute("""ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_Partida
        FOREIGN KEY (IdPartida)
        REFERENCES Partida (IdPartida)
        ON DELETE NO ACTION""")
    
    cur.execute("""ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_Jogador
        FOREIGN KEY (IdJogador)
        REFERENCES Jogador (IdJogador)
        ON DELETE NO ACTION""")
    
    cur.execute("""ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_Posicao
        FOREIGN KEY (IdPosicao)
        REFERENCES Posicao (IdPosicao)
        ON DELETE NO ACTION""")

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
    cur.execute("""INSERT INTO Nacionalidade (Descricao) VALUES
                ('Brasileiro'),
                ('Argentino'),
                ('Uruguaio')""")

    cur.execute("""INSERT INTO Posicao (Descricao) VALUES
                ('Goleiro'),
                ('Zagueiro'),
                ('Meio-Campo'),
                ('Atacante')""")

    cur.execute("""INSERT INTO Federacao (Nome, UF) VALUES
                ('Federação Catarinense de Futebol', 'SC'),
                ('Federação Paulista de Futebol', 'SP')""")

    cur.execute("""INSERT INTO Cidade (Nome, UF) VALUES
                ('Florianópolis', 'SC'),
                ('São Paulo', 'SP')""")

    cur.execute("""INSERT INTO Estadio (Nome, Capacidade, IdCidade) VALUES
                ('Estádio da Ressacada', 18000, 1),
                ('Morumbi', 67000, 2)""")

    cur.execute("""INSERT INTO Arbitro (Nome, DataNascimento, IdFederacao) VALUES
                ('Carlos Silva', '1985-03-10', 1),
                ('João Pereira', '1990-06-22', 2)""")

    cur.execute("""INSERT INTO FuncaoArbitro (Descricao) VALUES
                ('Árbitro Principal'),
                ('Bandeirinha')""")

    cur.execute("""INSERT INTO Time (Nome, IdCidade) VALUES
                ('Avaí FC', 1),
                ('São Paulo FC', 2)""")

    cur.execute("""INSERT INTO Jogador (Nome, DataNascimento, IdNacionalidade, IdPosicao) VALUES
                ('Lucas Silva', '1998-05-22', 1, 4),
                ('Juan Pérez', '1996-11-10', 2, 3)""")

    cur.execute("""INSERT INTO Tecnico (Nome, DataNascimento, IdNacionalidade) VALUES
                ('José da Silva', '1975-04-15', 1),
                ('Miguel Herrera', '1968-08-09', 2)""")

    cur.execute("""INSERT INTO Campeonato (Nome, Premiacao, IdFederacao) VALUES
                ('Campeonato Catarinense 2024', 500000.00, 1)""")

    cur.execute("""INSERT INTO Temporada (QuantidadeRodadas, DataInicio, DataFim, Ano, IdCampeonato) VALUES
                (10, '2024-01-15', '2024-04-15', 2024, 1)""")

    cur.execute("""INSERT INTO Rodada (NumeroRodada, IdTemporada) VALUES
                (1, 1)""")

    cur.execute("""INSERT INTO Partida (DataHora, Publico, Renda, IdRodada, IdEstadio, IdTimeMandante, IdTimeVisitante) VALUES
                ('2024-01-20 16:00:00', 15000, 250000.00, 1, 1, 1, 2)""")

    cur.execute("""INSERT INTO Evento (TipoEvento, Minuto, IdPartida, IdJogador) VALUES
                (1, 23, 1, 1), -- Gol
                (2, 45, 1, 2); -- Cartão""")

    cur.execute("""INSERT INTO Participacao (IdTime, IdTemporada) VALUES
                (1, 1),
                (2, 1);""")

    cur.execute("""INSERT INTO EquipeArbitragem (IdPartida, IdArbitro, IdFuncaoArbitro) VALUES
                (1, 1, 1),
                (1, 2, 2);""")

    cur.execute("""INSERT INTO ContratoTecnico (IdTecnico, IdTime, DataAssinatura, DataRescisao, MultaRescisoria) VALUES
                (1, 1, '2023-12-01', NULL, 100000.00);""")

    cur.execute("""INSERT INTO ContratoJogador (Numero, IdJogador, IdTime, DataRescisao, DataAssinatura, MultaRescisoria) VALUES
                ('CJ001', 1, 1, NULL, '2023-12-15', 50000.00);""")

    cur.execute("""INSERT INTO Escalacao (IdPartida, IdJogador, IdPosicao) VALUES
                (1, 1, 4),
                (1, 2, 3);""")