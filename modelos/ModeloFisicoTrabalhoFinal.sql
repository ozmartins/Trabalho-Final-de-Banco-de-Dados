DROP TABLE Cidade;
DROP TABLE Estadio;
DROP TABLE FuncaoArbitro;
DROP TABLE Posicao;
DROP TABLE ContratoTecnico;
DROP TABLE ContratoJogador;
DROP TABLE Escalacao;
DROP TABLE EquipeArbitragem;
DROP TABLE Participacao;
DROP TABLE Tecnico;
DROP TABLE Arbitro;
DROP TABLE Federacao;
DROP TABLE Partida;
DROP TABLE Rodada;
DROP TABLE Temporada;
DROP TABLE Time;
DROP TABLE Jogador;
DROP TABLE Nacionalidade;
DROP TABLE Evento;
DROP TABLE Campeonato;

CREATE TABLE Campeonato (
    IdCampeonato serial PRIMARY KEY,
    Nome varchar(100),
    Premiacao numeric(14,2),
    IdFederacao integer
);

CREATE TABLE Federacao (
    IdFederacao serial PRIMARY KEY,
    Nome varchar(100),
    UF varchar(2)
);

CREATE TABLE Arbitro (
    IdArbitro serial PRIMARY KEY,
    Nome varchar(100),
    DataNascimento date,
    IdFederacao integer
);

CREATE TABLE Cidade (
    IdCidade serial PRIMARY KEY,
    Nome varchar(100),
    UF varchar(2)
);

CREATE TABLE Estadio (
    IdEstadio serial PRIMARY KEY,
    Nome varchar(100),
    Capacidade integer,
    IdCidade integer
);

CREATE TABLE FuncaoArbitro (
    IdFuncaoArbitro serial PRIMARY KEY,
    Descricao varchar(100)
);

CREATE TABLE Temporada (
    IdTemporada serial PRIMARY KEY,
    QuantidadeRodadas integer,
    DataInicio date,
    DataFim date,
    Ano integer,
    IdCampeonato integer
);

CREATE TABLE Rodada (
    IdRodada serial PRIMARY KEY,
    NumeroRodada integer,
    IdTemporada integer
);

CREATE TABLE Partida (
    IdPartida serial PRIMARY KEY,
    DataHora timestamp,
    Publico integer,
    Renda numeric(14,2),
    IdRodada integer,
    IdEstadio integer,
    IdTimeMandante integer,
    IdTimeVisitante integer
);

CREATE TABLE Time (
    IdTime serial PRIMARY KEY,
    Nome varchar(100),
    IdCidade integer
);

CREATE TABLE Jogador (
    IdJogador serial PRIMARY KEY,
    Nome varchar(100),
    DataNascimento date,
    IdNacionalidade integer,
    IdPosicao integer
);

CREATE TABLE Tecnico (
    IdTecnico serial PRIMARY KEY,
    Nome varchar(100),
    DataNascimento date,
    IdNacionalidade integer
);

CREATE TABLE Nacionalidade (
    IdNacionalidade serial PRIMARY KEY,
    Descricao varchar(100)
);

CREATE TABLE Posicao (
    IdPosicao serial PRIMARY KEY,
    Descricao varchar(100)
);

CREATE TABLE Evento (
    IdEvento serial PRIMARY KEY,
    TipoEvento integer,
    Minuto integer,
    IdPartida integer,
    IdJogador integer
);

CREATE TABLE Participacao (
    IdParticipacao serial PRIMARY KEY,
	IdTime integer,
    IdTemporada integer
);

CREATE TABLE EquipeArbitragem (
	IdEquipeArbitragem serial PRIMARY KEY,
    IdPartida integer,
    IdArbitro integer,
    IdFuncaoArbitro integer
);

CREATE TABLE ContratoTecnico (
    Numero serial PRIMARY KEY,
	IdTecnico integer,
    IdTime integer,
    DataAssinatura date,
    DataRescisao date,
    MultaRescisoria numeric(14,2)
);

CREATE TABLE ContratoJogador (
    Numero varchar(50) PRIMARY KEY,
	IdJogador integer,
    IdTime integer,
    DataRescisao date,
    DataAssinatura date,
    MultaRescisoria numeric(14,2)    
);

CREATE TABLE Escalacao (
    IdEscalacao serial PRIMARY KEY,
	IdPartida integer,
    IdJogador integer,
    IdPosicao integer    
);
 
ALTER TABLE Campeonato ADD CONSTRAINT FK_Campeonato_Federacao
    FOREIGN KEY (IdFederacao)
    REFERENCES Federacao (IdFederacao)
    ON DELETE SET NULL;
 
ALTER TABLE Arbitro ADD CONSTRAINT FK_Arbitro_Federacao
    FOREIGN KEY (IdFederacao)
    REFERENCES Federacao (IdFederacao)
    ON DELETE CASCADE;
 
ALTER TABLE Estadio ADD CONSTRAINT FK_Estadio_Cidade
    FOREIGN KEY (IdCidade)
    REFERENCES Cidade (IdCidade)
    ON DELETE CASCADE;
 
ALTER TABLE Temporada ADD CONSTRAINT FK_Temporada_Campeonato
    FOREIGN KEY (IdCampeonato)
    REFERENCES Campeonato (IdCampeonato)
    ON DELETE CASCADE;
 
ALTER TABLE Rodada ADD CONSTRAINT FK_Rodada_Temporada
    FOREIGN KEY (IdTemporada)
    REFERENCES Temporada (IdTemporada)
    ON DELETE CASCADE;
 
ALTER TABLE Partida ADD CONSTRAINT FK_Partida_Rodada
    FOREIGN KEY (IdRodada)
    REFERENCES Rodada (IdRodada)
    ON DELETE CASCADE;
 
ALTER TABLE Partida ADD CONSTRAINT FK_Partida_Estadio
    FOREIGN KEY (IdEstadio)
    REFERENCES Estadio (IdEstadio)
    ON DELETE CASCADE;
 
ALTER TABLE Partida ADD CONSTRAINT FK_Partida_TimeMandante
    FOREIGN KEY (IdTimeMandante)
    REFERENCES Time (IdTime)
    ON DELETE CASCADE;

ALTER TABLE Partida ADD CONSTRAINT FK_Partida_TimeVisitante
    FOREIGN KEY (IdTimeVisitante)
    REFERENCES Time (IdTime)
    ON DELETE CASCADE;
 
ALTER TABLE Time ADD CONSTRAINT FK_Time_Cidade
    FOREIGN KEY (IdCidade)
    REFERENCES Cidade (IdCidade)
    ON DELETE CASCADE;
 
ALTER TABLE Jogador ADD CONSTRAINT FK_Jogador_Nacionalidade
    FOREIGN KEY (IdNacionalidade)
    REFERENCES Nacionalidade (IdNacionalidade)
    ON DELETE CASCADE;
 
ALTER TABLE Jogador ADD CONSTRAINT FK_Jogador_Posicao
    FOREIGN KEY (IdPosicao)
    REFERENCES Posicao (IdPosicao)
    ON DELETE CASCADE;
 
ALTER TABLE Tecnico ADD CONSTRAINT FK_Tecnico_Nacionalidade
    FOREIGN KEY (IdNacionalidade)
    REFERENCES Nacionalidade (IdNacionalidade)
    ON DELETE CASCADE;
 
ALTER TABLE Evento ADD CONSTRAINT FK_Evento_Partida
    FOREIGN KEY (IdPartida)
    REFERENCES Partida (IdPartida)
    ON DELETE CASCADE;
 
ALTER TABLE Evento ADD CONSTRAINT FK_Evento_Jogador
    FOREIGN KEY (IdJogador)
    REFERENCES Jogador (IdJogador)
    ON DELETE CASCADE;
 
ALTER TABLE Participacao ADD CONSTRAINT FK_Participacao_Time
    FOREIGN KEY (IdTime)
    REFERENCES Time (IdTime)
    ON DELETE RESTRICT;
 
ALTER TABLE Participacao ADD CONSTRAINT FK_Participacao_Temporada
    FOREIGN KEY (IdTemporada)
    REFERENCES Temporada (IdTemporada)
    ON DELETE SET NULL;
 
ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_Partida
    FOREIGN KEY (IdPartida)
    REFERENCES Partida (IdPartida)
    ON DELETE NO ACTION;
 
ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_Arbitro
    FOREIGN KEY (IdArbitro)
    REFERENCES Arbitro (IdArbitro)
    ON DELETE NO ACTION;
 
ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_FuncaoArbitro
    FOREIGN KEY (IdFuncaoArbitro)
    REFERENCES FuncaoArbitro (IdFuncaoArbitro)
    ON DELETE RESTRICT;
 
ALTER TABLE ContratoTecnico ADD CONSTRAINT FK_ContratoTecnico_Tecnico
    FOREIGN KEY (IdTecnico)
    REFERENCES Tecnico (IdTecnico)
    ON DELETE SET NULL;
 
ALTER TABLE ContratoTecnico ADD CONSTRAINT FK_ContratoTecnico_3
    FOREIGN KEY (IdTime)
    REFERENCES Time (IdTime)
    ON DELETE SET NULL;
 
ALTER TABLE ContratoJogador ADD CONSTRAINT FK_ContratoJogador_Jogador
    FOREIGN KEY (IdJogador)
    REFERENCES Jogador (IdJogador)
    ON DELETE SET NULL;
 
ALTER TABLE ContratoJogador ADD CONSTRAINT FK_ContratoJogador_Time
    FOREIGN KEY (IdTime)
    REFERENCES Time (IdTime)
    ON DELETE SET NULL;
 
ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_Partida
    FOREIGN KEY (IdPartida)
    REFERENCES Partida (IdPartida)
    ON DELETE NO ACTION;
 
ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_Jogador
    FOREIGN KEY (IdJogador)
    REFERENCES Jogador (IdJogador)
    ON DELETE NO ACTION;
 
ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_Posicao
    FOREIGN KEY (IdPosicao)
    REFERENCES Posicao (IdPosicao)
    ON DELETE NO ACTION;