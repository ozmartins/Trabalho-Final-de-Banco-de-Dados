def create_table_league(cur):
    cur.execute("""
                CREATE TABLE Campeonato (
                IdCampeonato serial PRIMARY KEY,
                Nome varchar(100),
                Premiacao numeric(14,2),
                IdFederacao integer
                )""")

def create_table_federation(cur):
    cur.execute("""
                CREATE TABLE Federacao (
                IdFederacao serial PRIMARY KEY,
                Nome varchar(100),
                UF varchar(2)
                )""")

def create_table_referee(cur):
    cur.execute("""
                CREATE TABLE Arbitro (
                IdArbitro serial PRIMARY KEY,
                Nome varchar(100),
                DataNascimento date,
                IdFederacao integer
                )""")

def create_table_city(cur):
    cur.execute("""
                CREATE TABLE Cidade (
                IdCidade serial PRIMARY KEY,
                Nome varchar(100),
                UF varchar(2),
                UNIQUE (Nome, UF)
                )""")

def create_table_stadium(cur):
    cur.execute("""
                CREATE TABLE Estadio (
                IdEstadio serial PRIMARY KEY,
                Nome varchar(100) UNIQUE,
                Capacidade integer,
                IdCidade integer
                )""")

def create_table_referee_role(cur):
    cur.execute("""
                CREATE TABLE FuncaoArbitro (
                IdFuncaoArbitro serial PRIMARY KEY,
                Descricao varchar(100) UNIQUE
                )""")

def create_table_season(cur):    
    cur.execute("""
                CREATE TABLE Temporada (
                IdTemporada serial PRIMARY KEY,
                QuantidadeRodadas integer,
                DataInicio date,
                DataFim date,
                Ano integer,
                IdCampeonato integer
                )""")

def create_table_round(cur):
    cur.execute("""
                CREATE TABLE Rodada (
                IdRodada serial PRIMARY KEY,
                NumeroRodada integer,
                IdTemporada integer
                )""")

def create_table_match(cur):    
    cur.execute("""CREATE TABLE Partida (
                IdPartida serial PRIMARY KEY,
                DataHora timestamp,
                Publico integer,
                Renda numeric(14,2),
                IdRodada integer,
                IdEstadio integer,
                IdTimeMandante integer,
                IdTimeVisitante integer,
                UNIQUE(IdTimeMandante, IdTimeVisitante)
                )""")

def create_table_team(cur):
    cur.execute("""
                CREATE TABLE Time (
                IdTime serial PRIMARY KEY,
                Nome varchar(100) UNIQUE,
                IdCidade integer
                )""")

def create_table_player(cur):
    cur.execute("""
                CREATE TABLE Jogador (
                IdJogador serial PRIMARY KEY,
                Nome varchar(100),
                DataNascimento date,
                IdNacionalidade integer,
                IdPosicao integer
                )""")

def create_table_coach(cur):
    cur.execute("""
                CREATE TABLE Tecnico (
                IdTecnico serial PRIMARY KEY,
                Nome varchar(100),
                DataNascimento date,
                IdNacionalidade integer
                )""")

def create_table_nationality(cur):
    cur.execute("""
                CREATE TABLE Nacionalidade (
                IdNacionalidade serial PRIMARY KEY,
                Descricao varchar(100)
                )""")

def create_table_event(cur):
    cur.execute("""
                CREATE TABLE Evento (
                IdEvento serial PRIMARY KEY,
                TipoEvento integer,
                Minuto integer,
                IdPartida integer,
                IdJogador integer
                )""")

def create_table_participation(cur):
    cur.execute("""
                CREATE TABLE Participacao (
                IdParticipacao serial PRIMARY KEY,
                IdTime integer,
                IdTemporada integer
                )""")

def create_table_referee_team(cur):
    cur.execute("""
                CREATE TABLE EquipeArbitragem (
                IdEquipeArbitragem serial PRIMARY KEY,
                IdPartida integer,
                IdArbitro integer,
                IdFuncaoArbitro integer
                )""")

def create_table_coach_contract(cur):
    cur.execute("""
                CREATE TABLE ContratoTecnico (
                Numero serial PRIMARY KEY,
                IdTecnico integer,
                IdTime integer,
                DataAssinatura date,
                DataRescisao date,
                MultaRescisoria numeric(14,2)
                )""")

def create_table_player_contract(cur):
    cur.execute("""
                CREATE TABLE ContratoJogador (
                Numero varchar(50) PRIMARY KEY,
                IdJogador integer,
                IdTime integer,
                DataRescisao date,
                DataAssinatura date,
                MultaRescisoria numeric(14,2)
                )""")

def create_table_lineup(cur):
    cur.execute("""
                CREATE TABLE Escalacao (
                IdEscalacao serial PRIMARY KEY,
                IdPartida integer,
                IdJogador integer,
                IdPosicao integer,
                UNIQUE(IdPartida, IdJogador)
                )""")
    
def create_table_position(cur):
    cur.execute("""
                CREATE TABLE Posicao (
                IdPosicao  serial PRIMARY KEY,
                Descricao varchar(100)
                )""")

def create_constraints(cur):    
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

def create_all_tables(cur):
    create_table_league(cur)
    create_table_federation(cur)
    create_table_referee(cur)
    create_table_city(cur)
    create_table_stadium(cur)
    create_table_referee_role(cur)
    create_table_season(cur)
    create_table_round(cur)
    create_table_match(cur)
    create_table_team(cur)
    create_table_player(cur)
    create_table_coach(cur)
    create_table_nationality(cur)    
    create_table_event(cur)
    create_table_participation(cur)
    create_table_referee_team(cur)
    create_table_coach_contract(cur)
    create_table_player_contract(cur)
    create_table_lineup(cur)
    create_table_position(cur)
    create_constraints(cur)    

def drop_all_tables(cur):
    cur.execute("DROP TABLE IF EXISTS Cidade CASCADE")
    cur.execute("DROP TABLE IF EXISTS Estadio CASCADE")
    cur.execute("DROP TABLE IF EXISTS FuncaoArbitro CASCADE")
    cur.execute("DROP TABLE IF EXISTS Posicao CASCADE")
    cur.execute("DROP TABLE IF EXISTS ContratoTecnico CASCADE")
    cur.execute("DROP TABLE IF EXISTS ContratoJogador CASCADE")
    cur.execute("DROP TABLE IF EXISTS Escalacao CASCADE")
    cur.execute("DROP TABLE IF EXISTS EquipeArbitragem CASCADE")
    cur.execute("DROP TABLE IF EXISTS Participacao CASCADE")
    cur.execute("DROP TABLE IF EXISTS Tecnico CASCADE")
    cur.execute("DROP TABLE IF EXISTS Arbitro CASCADE")
    cur.execute("DROP TABLE IF EXISTS Federacao CASCADE")
    cur.execute("DROP TABLE IF EXISTS Partida CASCADE")
    cur.execute("DROP TABLE IF EXISTS Rodada CASCADE")
    cur.execute("DROP TABLE IF EXISTS Temporada CASCADE")
    cur.execute("DROP TABLE IF EXISTS Time CASCADE")
    cur.execute("DROP TABLE IF EXISTS Jogador CASCADE")
    cur.execute("DROP TABLE IF EXISTS Nacionalidade CASCADE")
    cur.execute("DROP TABLE IF EXISTS Evento CASCADE")
    cur.execute("DROP TABLE IF EXISTS Campeonato CASCADE")