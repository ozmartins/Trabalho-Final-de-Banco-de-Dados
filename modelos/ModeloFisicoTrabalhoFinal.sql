/* ModeloLogicolTrabalhoFinal: */

CREATE TABLE Campeonato (
    IdCampeonato integer PRIMARY KEY,
    Nome varchar(100),
    Premiacao numeric(14,2),
    IdFederacao integer
);

CREATE TABLE Federacao (
    IdFederacao integer PRIMARY KEY,
    Nome varchar(100),
    UF varchar(2)
);

CREATE TABLE Arbitro (
    IdArbitro integer PRIMARY KEY,
    Nome varchar(100),
    DataNascimento date,
    IdFederacao integer
);

CREATE TABLE Cidade (
    IdCidade integer PRIMARY KEY,
    Nome varchar(100),
    UF varchar(2)
);

CREATE TABLE Estadio (
    IdEstadio integer PRIMARY KEY,
    Nome varchar(100),
    Capacidade integer,
    IdCidade integer
);

CREATE TABLE FuncaoArbitro (
    IdFuncaoArbitro integer PRIMARY KEY,
    Descricao varchar(100)
);

CREATE TABLE Temporada (
    IdTemporada integer PRIMARY KEY,
    QuantidadeRodadas integer,
    DataInicio date,
    DataFim date,
    Ano integer,
    IdCampeonato integer
);

CREATE TABLE Rodada (
    IdRodada integer PRIMARY KEY,
    NumeroRodada integer,
    IdTemporada integer
);

CREATE TABLE Partida (
    IdPartida integer PRIMARY KEY,
    DataHora timestamp,
    Publico integer,
    Renda numeric(14,2),
    IdRodada integer,
    IdEstadio integer,
    IdTimeMandante integer,
    IdTimeVisitante integer
);

CREATE TABLE Time (
    IdTime integer PRIMARY KEY,
    Nome varchar(100),
    IdCida de integer
);

CREATE TABLE Jogador (
    IdJogador integer PRIMARY KEY,
    Nome varchar(100),
    DataNascimento date,
    IdNacionalidade integer,
    IdPosicao integer
);

CREATE TABLE Tecnico (
    Id integer PRIMARY KEY,
    Nome varchar(100),
    DataNascimento date,
    IdNacionalidade integer
);

CREATE TABLE Nacionalidade (
    IdNacionalidade integer PRIMARY KEY,
    Descricao varchar(100)
);

CREATE TABLE Posicao (
    IdPosicao integer PRIMARY KEY,
    Descricao varchar(100)
);

CREATE TABLE Evento (
    IdEvento integer PRIMARY KEY,
    TipoEvento integer,
    Minuto integer,
    IdPartida integer,
    IdJogador integer
);

CREATE TABLE Participacao (
    IdTime integer,
    IdTemporada integer
);

CREATE TABLE EquipeArbitragem (
    IdPartida integer,
    IdArbitro integer,
    IdFuncaoArbitro integer,
    PRIMARY KEY (IdArbitro, IdPartida)
);

CREATE TABLE ContratoTecnico (
    IdTecnico integer,
    IdTime integer,
    DataAssinatura date,
    DataRescisao date,
    MultaRescisoria numeric(14,2),
    Numero integer PRIMARY KEY
);

CREATE TABLE ContratoJogador (
    IdJogador integer,
    IdTime integer,
    DataRescisao date,
    DataAssinatura date,
    MultaRescisoria numeric(14,2),
    Numero varchar(50) PRIMARY KEY
);

CREATE TABLE Escalacao (
    IdPartida integer,
    IdJogador integer,
    IdPosicao integer,
    PRIMARY KEY (IdJogador, IdPartida)
);
 
ALTER TABLE Campeonato ADD CONSTRAINT FK_Campeonato_2
    FOREIGN KEY (IdFederacao)
    REFERENCES Federacao (IdFederacao)
    ON DELETE SET NULL;
 
ALTER TABLE Arbitro ADD CONSTRAINT FK_Arbitro_2
    FOREIGN KEY (IdFederacao)
    REFERENCES Federacao (IdFederacao)
    ON DELETE CASCADE;
 
ALTER TABLE Estadio ADD CONSTRAINT FK_Estadio_2
    FOREIGN KEY (IdCidade)
    REFERENCES Cidade (IdCidade)
    ON DELETE CASCADE;
 
ALTER TABLE Temporada ADD CONSTRAINT FK_Temporada_2
    FOREIGN KEY (IdCampeonato)
    REFERENCES Campeonato (IdCampeonato)
    ON DELETE CASCADE;
 
ALTER TABLE Rodada ADD CONSTRAINT FK_Rodada_2
    FOREIGN KEY (IdTemporada)
    REFERENCES Temporada (IdTemporada)
    ON DELETE CASCADE;
 
ALTER TABLE Partida ADD CONSTRAINT FK_Partida_2
    FOREIGN KEY (IdRodada)
    REFERENCES Rodada (IdRodada)
    ON DELETE CASCADE;
 
ALTER TABLE Partida ADD CONSTRAINT FK_Partida_3
    FOREIGN KEY (IdEstadio)
    REFERENCES Estadio (IdEstadio)
    ON DELETE CASCADE;
 
ALTER TABLE Partida ADD CONSTRAINT FK_Partida_4
    FOREIGN KEY (IdTimeMandante, IdTimeVisitante)
    REFERENCES Time (IdTime, IdTime)
    ON DELETE CASCADE;
 
ALTER TABLE Time ADD CONSTRAINT FK_Time_2
    FOREIGN KEY (IdCida de)
    REFERENCES Cidade (IdCidade)
    ON DELETE CASCADE;
 
ALTER TABLE Jogador ADD CONSTRAINT FK_Jogador_2
    FOREIGN KEY (IdNacionalidade)
    REFERENCES Nacionalidade (IdNacionalidade)
    ON DELETE CASCADE;
 
ALTER TABLE Jogador ADD CONSTRAINT FK_Jogador_3
    FOREIGN KEY (IdPosicao)
    REFERENCES Posicao (IdPosicao)
    ON DELETE CASCADE;
 
ALTER TABLE Tecnico ADD CONSTRAINT FK_Tecnico_2
    FOREIGN KEY (IdNacionalidade)
    REFERENCES Nacionalidade (IdNacionalidade)
    ON DELETE CASCADE;
 
ALTER TABLE Evento ADD CONSTRAINT FK_Evento_2
    FOREIGN KEY (IdPartida)
    REFERENCES Partida (IdPartida)
    ON DELETE CASCADE;
 
ALTER TABLE Evento ADD CONSTRAINT FK_Evento_3
    FOREIGN KEY (IdJogador)
    REFERENCES Jogador (IdJogador)
    ON DELETE CASCADE;
 
ALTER TABLE Participacao ADD CONSTRAINT FK_Participacao_1
    FOREIGN KEY (IdTime)
    REFERENCES Time (IdTime)
    ON DELETE RESTRICT;
 
ALTER TABLE Participacao ADD CONSTRAINT FK_Participacao_2
    FOREIGN KEY (IdTemporada)
    REFERENCES Temporada (IdTemporada)
    ON DELETE SET NULL;
 
ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_1
    FOREIGN KEY (IdPartida)
    REFERENCES Partida (IdPartida)
    ON DELETE NO ACTION;
 
ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_2
    FOREIGN KEY (IdArbitro)
    REFERENCES Arbitro (IdArbitro)
    ON DELETE NO ACTION;
 
ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_3
    FOREIGN KEY (IdFuncaoArbitro)
    REFERENCES FuncaoArbitro (IdFuncaoArbitro)
    ON DELETE RESTRICT;
 
ALTER TABLE EquipeArbitragem ADD CONSTRAINT FK_EquipeArbitragem_4
    FOREIGN KEY (IdFuncaoArbitro???)
    REFERENCES ??? (???);
 
ALTER TABLE ContratoTecnico ADD CONSTRAINT FK_ContratoTecnico_2
    FOREIGN KEY (IdTecnico)
    REFERENCES Tecnico (Id)
    ON DELETE SET NULL;
 
ALTER TABLE ContratoTecnico ADD CONSTRAINT FK_ContratoTecnico_3
    FOREIGN KEY (IdTime)
    REFERENCES Time (IdTime)
    ON DELETE SET NULL;
 
ALTER TABLE ContratoJogador ADD CONSTRAINT FK_ContratoJogador_2
    FOREIGN KEY (IdJogador)
    REFERENCES Jogador (IdJogador)
    ON DELETE SET NULL;
 
ALTER TABLE ContratoJogador ADD CONSTRAINT FK_ContratoJogador_3
    FOREIGN KEY (IdTime)
    REFERENCES Time (IdTime)
    ON DELETE SET NULL;
 
ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_1
    FOREIGN KEY (IdPartida)
    REFERENCES Partida (IdPartida)
    ON DELETE NO ACTION;
 
ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_2
    FOREIGN KEY (IdJogador)
    REFERENCES Jogador (IdJogador)
    ON DELETE NO ACTION;
 
ALTER TABLE Escalacao ADD CONSTRAINT FK_Escalacao_3
    FOREIGN KEY (IdPosicao)
    REFERENCES Posicao (IdPosicao)
    ON DELETE NO ACTION;