DROP TABLE jogo CASCADE;
DROP TABLE clube CASCADE;
DROP TABLE atleta CASCADE;
DROP TABLE alteracao CASCADE;
DROP TABLE evento CASCADE;
DROP TABLE campeonato CASCADE;
DROP TABLE documento CASCADE;
DROP TABLE arbitro CASCADE;
DROP TABLE equipe_arbitragem CASCADE;
DROP TABLE penalidade CASCADE;
DROP TABLE estadio CASCADE;
DROP TABLE cidade CASCADE;
DROP TABLE escalacao CASCADE;

CREATE TABLE jogo (
    id_jogo int,
    num_jogo int,
    rodada int,
    grupo varchar(100),
    data date,
    hora timestamp,
    qtd_alteracoes_jogo int,
    id_campeonato int,
    id_estadio int,
    id_clube_mandante int,
    id_clube_visitante int
);
 
ALTER TABLE jogo ADD CONSTRAINT pk_jogo PRIMARY KEY (id_jogo);

CREATE TABLE clube (
    id_clube int,
    nome varchar(100),
    url_escudo varchar(500)
);
 
ALTER TABLE clube ADD CONSTRAINT pk_clube PRIMARY KEY (id_clube);

CREATE TABLE atleta (
    id_atleta int,
    nome varchar(100),
    apelido varchar(100),
    foto varchar(500)
);
 
ALTER TABLE atleta ADD CONSTRAINT pk_atleta PRIMARY KEY (id_atleta);

CREATE TABLE alteracao (
    id_alteracao serial,
    codigo_jogador_saiu int,
    codigo_jogador_entrou int,
    tempo_jogo timestamp,
    tempo_subs varchar(3),
    tempo_acrescimo timestamp,
    id_jogo int,
    id_clube int
);
 
ALTER TABLE alteracao ADD CONSTRAINT pk_alteracao PRIMARY KEY (id_alteracao);

CREATE TABLE evento (
    id_jogo int,
    id_clube int,
    gols int,
    penaltis int
);
 
ALTER TABLE evento ADD CONSTRAINT pk_evento PRIMARY KEY (id_clube, id_jogo);

CREATE TABLE campeonato (
    id_campeonato int,
    nome varchar(100) UNIQUE
);
 
ALTER TABLE campeonato ADD CONSTRAINT pk_campeonato PRIMARY KEY (id_campeonato);

CREATE TABLE documento (
    id_documento serial,
    url varchar(500),
    title varchar(100),
    id_jogo int
);
 
ALTER TABLE documento ADD CONSTRAINT pk_documento PRIMARY KEY (id_documento);

CREATE TABLE arbitro (
    id_arbitro int,
    nome varchar(100),
    uf varchar(2),
    categoria varchar(100)
);
 
ALTER TABLE arbitro ADD CONSTRAINT pk_arbitro PRIMARY KEY (id_arbitro);

CREATE TABLE equipe_arbitragem (
    id_arbitro int,
    id_jogo int,
    funcao varchar(100)
);
 
ALTER TABLE equipe_arbitragem ADD CONSTRAINT pk_equipe_arbitragem PRIMARY KEY (id_jogo, id_arbitro);

CREATE TABLE penalidade (
    id_penalidade int,
    tipo varchar(100),
    resultado varchar(100),
    tempo_jogo varchar(3),
    minutos timestamp,
    id_jogo int,
    id_clube int,
    id_atleta int
);
 
ALTER TABLE penalidade ADD CONSTRAINT pk_penalidade PRIMARY KEY (id_penalidade);

CREATE TABLE estadio (
    id_estadio serial,
    nome varchar(100) UNIQUE,
    id_cidade serial
);
 
ALTER TABLE estadio ADD CONSTRAINT pk_estadio PRIMARY KEY (id_estadio);

CREATE TABLE cidade (
    id_cidade serial,
    nome varchar(100) UNIQUE,
    uf varchar(2)
);
 
ALTER TABLE cidade ADD CONSTRAINT pk_cidade PRIMARY KEY (id_cidade);

CREATE TABLE escalacao (
    id_escalacao serial,
    numero_camisa int,
    reserva bool,
    goleiro bool,
    entrou_jogando bool,
    id_clube int,
    id_atleta int,
    id_jogo int
);
 
ALTER TABLE escalacao ADD CONSTRAINT pk_escalacao PRIMARY KEY (id_escalacao);
 
ALTER TABLE jogo ADD CONSTRAINT fk_jogo_campeonato
    FOREIGN KEY (id_campeonato)
    REFERENCES campeonato (id_campeonato)
    ON DELETE CASCADE;
 
ALTER TABLE jogo ADD CONSTRAINT fk_jogo_estadio
    FOREIGN KEY (id_estadio)
    REFERENCES estadio (id_estadio)
    ON DELETE CASCADE;
 
ALTER TABLE jogo ADD CONSTRAINT fk_jogo_mandante
    FOREIGN KEY (id_clube_mandante)
    REFERENCES clube (id_clube)
    ON DELETE CASCADE;
 
ALTER TABLE jogo ADD CONSTRAINT fk_jogo_visitante
    FOREIGN KEY (id_clube_visitante)
    REFERENCES clube (id_clube);
 
ALTER TABLE alteracao ADD CONSTRAINT fk_alteracao_jogo
    FOREIGN KEY (id_jogo)
    REFERENCES jogo (id_jogo)
    ON DELETE CASCADE;
 
ALTER TABLE alteracao ADD CONSTRAINT fk_alteracao_clube
    FOREIGN KEY (id_clube)
    REFERENCES clube (id_clube)
    ON DELETE CASCADE;
 
ALTER TABLE evento ADD CONSTRAINT fk_evento_jogo
    FOREIGN KEY (id_jogo)
    REFERENCES jogo (id_jogo)
    ON DELETE CASCADE;
 
ALTER TABLE evento ADD CONSTRAINT fk_evento_clube
    FOREIGN KEY (id_clube)
    REFERENCES clube (id_clube)
    ON DELETE CASCADE;
 
ALTER TABLE documento ADD CONSTRAINT fk_documento_jogo
    FOREIGN KEY (id_jogo)
    REFERENCES jogo (id_jogo)
    ON DELETE CASCADE;
 
ALTER TABLE equipe_arbitragem ADD CONSTRAINT fk_equipe_arbitragem_arbitro
    FOREIGN KEY (id_arbitro)
    REFERENCES arbitro (id_arbitro);
 
ALTER TABLE equipe_arbitragem ADD CONSTRAINT fk_equipe_arbitragem_jogo
    FOREIGN KEY (id_jogo)
    REFERENCES jogo (id_jogo);
 
ALTER TABLE penalidade ADD CONSTRAINT fk_penalidade_jogo
    FOREIGN KEY (id_jogo)
    REFERENCES jogo (id_jogo)
    ON DELETE CASCADE;
 
ALTER TABLE penalidade ADD CONSTRAINT fk_penalidade_clube
    FOREIGN KEY (id_clube)
    REFERENCES clube (id_clube)
    ON DELETE CASCADE;
 
ALTER TABLE penalidade ADD CONSTRAINT fk_penalidade_atleta
    FOREIGN KEY (id_atleta)
    REFERENCES atleta (id_atleta)
    ON DELETE CASCADE;
 
ALTER TABLE estadio ADD CONSTRAINT fk_estadio_cidade
    FOREIGN KEY (id_cidade)
    REFERENCES cidade (id_cidade)
    ON DELETE CASCADE;
 
ALTER TABLE escalacao ADD CONSTRAINT fk_escalacao_clube
    FOREIGN KEY (id_clube)
    REFERENCES clube (id_clube)
    ON DELETE CASCADE;
 
ALTER TABLE escalacao ADD CONSTRAINT fk_escalacao_atleta
    FOREIGN KEY (id_atleta)
    REFERENCES atleta (id_atleta)
    ON DELETE CASCADE;
 
ALTER TABLE escalacao ADD CONSTRAINT fk_escalacao_jogo
    FOREIGN KEY (id_jogo)
    REFERENCES jogo (id_jogo)
    ON DELETE CASCADE;