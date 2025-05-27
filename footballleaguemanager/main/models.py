# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arbitro(models.Model):
    idarbitro = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    datanascimento = models.DateField(blank=True, null=True)
    idfederacao = models.ForeignKey('Federacao', models.DO_NOTHING, db_column='idfederacao', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arbitro'


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
    idcampeonato = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    premiacao = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    idfederacao = models.ForeignKey('Federacao', models.DO_NOTHING, db_column='idfederacao', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campeonato'


class Cidade(models.Model):
    idcidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cidade'


class ContratoJogador(models.Model):
    numero = models.CharField(primary_key=True, max_length=50)
    idjogador = models.ForeignKey('Jogador', models.DO_NOTHING, db_column='idjogador', blank=True, null=True)
    idtime = models.ForeignKey('Time', models.DO_NOTHING, db_column='idtime', blank=True, null=True)
    datarescisao = models.DateField(blank=True, null=True)
    dataassinatura = models.DateField(blank=True, null=True)
    multarescisoria = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contratojogador'


class ContratoTecnico(models.Model):
    numero = models.AutoField(primary_key=True)
    idtecnico = models.ForeignKey('Tecnico', models.DO_NOTHING, db_column='idtecnico', blank=True, null=True)
    idtime = models.ForeignKey('Time', models.DO_NOTHING, db_column='idtime', blank=True, null=True)
    dataassinatura = models.DateField(blank=True, null=True)
    datarescisao = models.DateField(blank=True, null=True)
    multarescisoria = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contratotecnico'


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


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EquipeArbitragem(models.Model):
    equipearbitragem = models.AutoField(primary_key=True)
    idpartida = models.ForeignKey('Partida', models.DO_NOTHING, db_column='idpartida', blank=True, null=True)
    idarbitro = models.ForeignKey(Arbitro, models.DO_NOTHING, db_column='idarbitro', blank=True, null=True)
    idfuncaoarbitro = models.ForeignKey('Funcaoarbitro', models.DO_NOTHING, db_column='idfuncaoarbitro', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipearbitragem'


class Escalacao(models.Model):
    escalacao = models.AutoField(primary_key=True)
    idpartida = models.ForeignKey('Partida', models.DO_NOTHING, db_column='idpartida', blank=True, null=True)
    idjogador = models.ForeignKey('Jogador', models.DO_NOTHING, db_column='idjogador', blank=True, null=True)
    idposicao = models.ForeignKey('Posicao', models.DO_NOTHING, db_column='idposicao', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalacao'


class Estadio(models.Model):
    idestadio = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    capacidade = models.IntegerField(blank=True, null=True)
    idcidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='idcidade', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadio'


class Evento(models.Model):
    idevento = models.AutoField(primary_key=True)
    tipoevento = models.IntegerField(blank=True, null=True)
    minuto = models.IntegerField(blank=True, null=True)
    idpartida = models.ForeignKey('Partida', models.DO_NOTHING, db_column='idpartida', blank=True, null=True)
    idjogador = models.ForeignKey('Jogador', models.DO_NOTHING, db_column='idjogador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento'


class Federacao(models.Model):
    idfederacao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'federacao'


class FuncaoArbitro(models.Model):
    idfuncaoarbitro = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funcaoarbitro'


class Jogador(models.Model):
    idjogador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    datanascimento = models.DateField(blank=True, null=True)
    idnacionalidade = models.ForeignKey('Nacionalidade', models.DO_NOTHING, db_column='idnacionalidade', blank=True, null=True)
    idposicao = models.ForeignKey('Posicao', models.DO_NOTHING, db_column='idposicao', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogador'


class Nacionalidade(models.Model):
    idnacionalidade = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nacionalidade'


class Participacao(models.Model):
    participacao = models.AutoField(primary_key=True)
    idtime = models.ForeignKey('Time', models.DO_NOTHING, db_column='idtime', blank=True, null=True)
    idtemporada = models.ForeignKey('Temporada', models.DO_NOTHING, db_column='idtemporada', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participacao'


class Partida(models.Model):
    idpartida = models.AutoField(primary_key=True)
    datahora = models.DateTimeField(blank=True, null=True)
    publico = models.IntegerField(blank=True, null=True)
    renda = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    idrodada = models.ForeignKey('Rodada', models.DO_NOTHING, db_column='idrodada', blank=True, null=True)
    idestadio = models.ForeignKey(Estadio, models.DO_NOTHING, db_column='idestadio', blank=True, null=True)
    idtimemandante = models.ForeignKey('Time', models.DO_NOTHING, db_column='idtimemandante', blank=True, null=True)
    idtimevisitante = models.ForeignKey('Time', models.DO_NOTHING, db_column='idtimevisitante', related_name='partida_idtimevisitante_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partida'


class Posicao(models.Model):
    idposicao = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posicao'


class Rodada(models.Model):
    idrodada = models.AutoField(primary_key=True)
    numerorodada = models.IntegerField(blank=True, null=True)
    idtemporada = models.ForeignKey('Temporada', models.DO_NOTHING, db_column='idtemporada', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rodada'


class Tecnico(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    datanascimento = models.DateField(blank=True, null=True)
    idnacionalidade = models.ForeignKey(Nacionalidade, models.DO_NOTHING, db_column='idnacionalidade', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico'


class Temporada(models.Model):
    idtemporada = models.AutoField(primary_key=True)
    quantidaderodadas = models.IntegerField(blank=True, null=True)
    datainicio = models.DateField(blank=True, null=True)
    datafim = models.DateField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    idcampeonato = models.ForeignKey(Campeonato, models.DO_NOTHING, db_column='idcampeonato', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporada'


class Time(models.Model):
    idtime = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    idcidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='idcidade', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time'
