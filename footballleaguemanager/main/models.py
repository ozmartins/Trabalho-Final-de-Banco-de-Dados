# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Arbitro(models.Model):
    id_arbitro = models.AutoField(primary_key=True, verbose_name="Código")
    nome = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome")
    uf = models.CharField(max_length=2, blank=True, null=True, verbose_name="UF")
    categoria = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        managed = False
        db_table = 'arbitro'
        verbose_name = "Árbitro"
        verbose_name_plural = "Árbitros"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'        


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)        


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)        


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'        


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)        


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)        


class Campeonato(models.Model):
    id_campeonato = models.AutoField(primary_key=True, verbose_name="Código")
    nome = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome")

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        managed = False
        db_table = 'campeonato'
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"


class Cidade(models.Model):
    id_cidade = models.AutoField(primary_key=True, verbose_name="Código")
    nome = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome")
    uf = models.CharField(max_length=2, blank=True, null=True, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        managed = False
        db_table = 'cidade'
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'
        verbose_name = "Árbitro"
        verbose_name_plural = "Árbitros"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
        verbose_name = "Árbitro"
        verbose_name_plural = "Árbitros"


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        verbose_name = "Árbitro"
        verbose_name_plural = "Árbitros"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        verbose_name = "Árbitro"
        verbose_name_plural = "Árbitros"


class EquipeArbitragem(models.Model):
    id_jogo = models.IntegerField(blank=True, null=True, verbose_name="Jogo")
    id_arbitro = models.IntegerField(blank=True, null=True, verbose_name="Árbitro")
    funcao = models.CharField(max_length=100, blank=True, null=True, verbose_name="Função")

    def __str__(self):
        return f"{self.funcao} {self.id_arbitro} atuando no jogo {self.id_jogo}"

    class Meta:
        managed = False
        db_table = 'equipe_arbitragem'
        verbose_name = "Equipe Arbitragem"
        verbose_name_plural = "Equipes Arbitragens"
        unique_together = ('id_jogo', 'id_arbitro')


class Escalacao(models.Model):
    id_escalacao = models.AutoField(primary_key=True, verbose_name="Código")
    numero_camisa = models.IntegerField(blank=True, null=True, verbose_name="Número camisa")
    reserva = models.BooleanField(blank=True, null=True, verbose_name="Reserva")
    goleiro = models.BooleanField(blank=True, null=True, verbose_name="Goleiro")
    entrou_jogando = models.BooleanField(blank=True, null=True, verbose_name="Entrou jogando")
    id_clube = models.ForeignKey('Clube', models.DO_NOTHING, db_column='id_clube', blank=True, null=True, verbose_name="Clube")
    id_atleta = models.ForeignKey('Atleta', models.DO_NOTHING, db_column='id_atleta', blank=True, null=True, verbose_name="Atleta")
    id_jogo = models.ForeignKey('Jogo', models.DO_NOTHING, db_column='id_jogo', blank=True, null=True, verbose_name="Jogo")

    def __str__(self):
        return f"{self.id_escalacao}"

    class Meta:
        managed = False
        db_table = 'escalacao'
        verbose_name = "Escalação"
        verbose_name_plural = "Escalações"


class Estadio(models.Model):
    id_estadio = models.AutoField(primary_key=True, verbose_name="Código")
    nome = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome")    
    id_cidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='id_cidade', blank=True, null=True, verbose_name="Cidade")
    
    def __str__(self):
        return f"{self.nome}"

    class Meta:
        managed = False
        db_table = 'estadio'
        verbose_name = "Estádio"
        verbose_name_plural = "Estádios"

class Evento(models.Model):
    id_jogo = models.ForeignKey('Jogo', models.DO_NOTHING, db_column='id_jogo', blank=True, null=True, verbose_name="Jogo")
    id_clube = models.ForeignKey('Clube', models.DO_NOTHING, db_column='id_clube', blank=True, null=True, verbose_name="Clube")
    gols = models.IntegerField(blank=True, null=True, verbose_name="Gols")
    penaltis = models.IntegerField(blank=True, null=True, verbose_name="Penaltis")    

    def __str__(self):
        return f"{self.id_jogo}: clube {self.id_clube} marcou {self.gols} gol(s) e teve {self.penaltis} penalti(s)"

    class Meta:
        managed = False
        db_table = 'evento'
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"


class Atleta(models.Model):
    id_atleta = models.AutoField(primary_key=True, verbose_name="Código")
    nome = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome")
    apelido = models.CharField(max_length=100, blank=True, null=True, verbose_name="Apelido")
    foto = models.CharField(max_length=500, blank=True, null=True, verbose_name="Foto")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        managed = False
        db_table = 'atleta'
        verbose_name = "Atleta"
        verbose_name_plural = "Atletas"


class Jogo(models.Model):
    id_jogo = models.AutoField(primary_key=True, verbose_name="Código")
    num_jogo = models.IntegerField(blank=True, null=True, verbose_name="Número do jogo")
    rodada = models.IntegerField(blank=True, null=True, verbose_name="Rodada")
    grupo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Grupo")
    data = models.DateTimeField(blank=True, null=True, verbose_name="Data")
    hora = models.DateTimeField(blank=True, null=True, verbose_name="Hora")
    qtd_alteracoes_jogo = models.IntegerField(blank=True, null=True, verbose_name="Quantidade de alterações")
    id_campeonato = models.ForeignKey('Campeonato', models.DO_NOTHING, db_column='id_campeonato', blank=True, null=True, verbose_name="Campeonato")
    id_estadio = models.ForeignKey(Estadio, models.DO_NOTHING, db_column='id_estadio', blank=True, null=True, verbose_name="Estádio")
    id_clube_mandante = models.ForeignKey('Clube',  models.DO_NOTHING, related_name='jogo_como_mandante', db_column='id_clube_mandante', blank=True, null=True, verbose_name="Mandante")
    id_clube_visitante = models.ForeignKey('Clube', models.DO_NOTHING, related_name='jogo_como_visitante', db_column='id_clube_visitante', blank=True, null=True, verbose_name="Visitante")    

    def __str__(self):
        return f"{self.id_jogo}"

    class Meta:
        managed = False
        db_table = 'jogo'
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"


class Clube(models.Model):
    id_clube = models.AutoField(primary_key=True, verbose_name="Código")
    nome = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome")
    url_escudo = models.CharField(max_length=100, blank=True, null=True, verbose_name="URL escudo")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        managed = False
        db_table = 'clube'
        verbose_name = "Clube"
        verbose_name_plural = "Clubes"


class Alteracao(models.Model):
    id_alteracao = models.AutoField(primary_key=True, verbose_name="Código")
    codigo_jogador_saiu = models.IntegerField(blank=True, null=True, verbose_name="Código jogador saiu")
    codigo_jogador_entrou = models.IntegerField(blank=True, null=True, verbose_name="Código jogador entrou")
    tempo_jogo = models.DateTimeField(blank=True, null=True, verbose_name="Tempo jogo")
    tempo_subs = models.CharField(max_length=3, blank=True, null=True, verbose_name="Tempos subst.")
    tempo_acrescimo = models.DateTimeField(blank=True, null=True, verbose_name="Tempo acréscimo")
    id_jogo = models.ForeignKey('Jogo', models.DO_NOTHING, db_column='id_jogo', blank=True, null=True, verbose_name="Jogo")
    id_clube = models.ForeignKey('Clube', models.DO_NOTHING, db_column='id_clube', blank=True, null=True, verbose_name="Clube")

    def __str__(self):
        return f"{self.id_alteracao}"

    class Meta:
        managed = False
        db_table = 'alteracao'
        verbose_name = "Alteração"
        verbose_name_plural = "Alterações"


class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True, verbose_name="Código")
    url = models.CharField(max_length=500, blank=True, null=True, verbose_name="URL")
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name="Título")
    id_jogo = models.ForeignKey('Jogo', models.DO_NOTHING, db_column='id_jogo', blank=True, null=True, verbose_name="Jogo")    

    def __str__(self):
        return f"{self.title}"

    class Meta:
        managed = False
        db_table = 'documento'
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"


class Penalidade(models.Model):
    id_penalidade = models.AutoField(primary_key=True, verbose_name="Código")
    tipo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tipo")
    resultado = models.CharField(max_length=100, blank=True, null=True, verbose_name="Resultado")
    tempo_jogo = models.CharField(max_length=3, blank=True, null=True, verbose_name="Tempo jogo")
    minutos = models.DateTimeField(blank=True, null=True, verbose_name="Minutos")
    id_jogo = models.ForeignKey('Jogo', models.DO_NOTHING, db_column='id_jogo', blank=True, null=True, verbose_name="Jogo")
    id_clube = models.ForeignKey('Clube', models.DO_NOTHING, db_column='id_clube', blank=True, null=True, verbose_name="Clube")
    id_atleta = models.ForeignKey('Atleta', models.DO_NOTHING, db_column='id_atleta', blank=True, null=True, verbose_name="Atleta")

    def __str__(self):
        return f"{self.id_penalidade}"

    class Meta:
        managed = False
        db_table = 'penalidade'
        verbose_name = "Penalidade"
        verbose_name_plural = "Penalidades"