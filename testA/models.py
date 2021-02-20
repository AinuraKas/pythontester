# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Faculty(models.Model):
    facultyid = models.CharField(db_column='FacultyID', primary_key=True, max_length=10)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Faculty'


class Glossar(models.Model):
    idgloss = models.AutoField(db_column='idGloss', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    urlgl = models.CharField(max_length=50)
    har = models.CharField(db_column='Har', max_length=300, blank=True, null=True)  # Field name made lowercase.
    iduch = models.ForeignKey('Ucheb', models.DO_NOTHING, db_column='iduch', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Glossar'


class Gruppa(models.Model):
    idgruppy = models.AutoField(db_column='IdGruppy', primary_key=True)  # Field name made lowercase.
    gruppan = models.CharField(db_column='GruppaN', max_length=50)  # Field name made lowercase.
    facultyid = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='FacultyID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gruppa'


class Kafedra(models.Model):
    idkaf = models.AutoField(db_column='IdKaf', primary_key=True)  # Field name made lowercase.
    kafedra = models.CharField(db_column='Kafedra', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kafedra'


class Nast(models.Model):
    idnastr = models.AutoField(db_column='IdNastr', primary_key=True)  # Field name made lowercase.
    idtest = models.IntegerField(db_column='IdTest')  # Field name made lowercase.
    idgruppa = models.IntegerField(db_column='IdGruppa')  # Field name made lowercase.
    idtestir = models.OneToOneField('Testir', models.DO_NOTHING, db_column='IdTestir')  # Field name made lowercase.
    kvop = models.IntegerField(db_column='KVop')  # Field name made lowercase.
    vremprt = models.IntegerField(db_column='VremPrT')  # Field name made lowercase.
    obkolbal = models.IntegerField(db_column='ObKolBal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nast'


class Otvet(models.Model):
    idotvet = models.AutoField(db_column='IdOtvet', primary_key=True)  # Field name made lowercase.
    idvopr = models.ForeignKey('Vopros', models.DO_NOTHING, db_column='IdVopr')  # Field name made lowercase.
    otvet = models.CharField(db_column='Otvet', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ball = models.IntegerField(db_column='Ball', blank=True, null=True)  # Field name made lowercase.
    ris = models.BooleanField(db_column='Ris')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Otvet'


class Predm(models.Model):
    idpredm = models.AutoField(db_column='IdPredm', primary_key=True)  # Field name made lowercase.
    predm = models.CharField(db_column='Predm', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idkaf = models.ForeignKey(Kafedra, models.DO_NOTHING, db_column='IdKaf')  # Field name made lowercase.
    idsemestr = models.ForeignKey('Semestr', models.DO_NOTHING, db_column='IdSemestr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Predm'


class Rezultat(models.Model):
    idrez = models.AutoField(db_column='IdRez', primary_key=True)  # Field name made lowercase.
    idotvet = models.ForeignKey(Otvet, models.DO_NOTHING, db_column='IdOtvet')  # Field name made lowercase.
    idstyd = models.ForeignKey('Stydent', models.DO_NOTHING, db_column='IdStyd')  # Field name made lowercase.
    idtestir = models.ForeignKey('Testir', models.DO_NOTHING, db_column='IdTestir', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rezultat'


class Semestr(models.Model):
    idsemestr = models.AutoField(db_column='IdSemestr', primary_key=True)  # Field name made lowercase.
    semestr = models.CharField(db_column='Semestr', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Semestr'


class Stvesa(models.Model):
    idstyd = models.IntegerField(db_column='IdStyd')  # Field name made lowercase.
    idtestir = models.IntegerField(db_column='IdTestir')  # Field name made lowercase.
    ves = models.IntegerField(db_column='Ves')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StVesa'


class Stydent(models.Model):
    idstyd = models.AutoField(db_column='IdStyd', primary_key=True)  # Field name made lowercase.
    fam = models.CharField(db_column='Fam', max_length=50)  # Field name made lowercase.
    im = models.CharField(db_column='Im', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otsh = models.CharField(db_column='Otsh', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idgruppy = models.ForeignKey(Gruppa, models.DO_NOTHING, db_column='IdGruppy')  # Field name made lowercase.
    nzah = models.CharField(db_column='Nzah', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stydent'


class Test(models.Model):
    idtest = models.AutoField(db_column='IdTest', primary_key=True)  # Field name made lowercase.
    idpredm = models.ForeignKey(Predm, models.DO_NOTHING, db_column='IdPredm')  # Field name made lowercase.
    nazvtest = models.CharField(db_column='NazvTest', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Test'


class Testir(models.Model):
    idtestir = models.AutoField(db_column='IdTestir', primary_key=True)  # Field name made lowercase.
    datapr = models.DateTimeField(db_column='DataPr')  # Field name made lowercase.
    ob = models.BooleanField(db_column='Ob')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Testir'


class Ucheb(models.Model):
    iduch = models.OneToOneField(Predm, models.DO_NOTHING, db_column='iduch', primary_key=True)
    uch_n = models.CharField(max_length=100)
    papka = models.CharField(max_length=20)
    prep = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ucheb'


class Vr(models.Model):
    idstyd = models.IntegerField(db_column='IdStyd')  # Field name made lowercase.
    idtestir = models.IntegerField(db_column='IdTestir')  # Field name made lowercase.
    ves = models.IntegerField(db_column='Ves')  # Field name made lowercase.
    kvop = models.IntegerField(db_column='KVop')  # Field name made lowercase.
    obkolbal = models.IntegerField(db_column='ObKolBal')  # Field name made lowercase.
    bally = models.IntegerField(db_column='Bally')  # Field name made lowercase.
    nzah = models.CharField(db_column='Nzah', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VR'


class Vopros(models.Model):
    idvopr = models.AutoField(db_column='IdVopr', primary_key=True)  # Field name made lowercase.
    idtest = models.ForeignKey(Test, models.DO_NOTHING, db_column='IdTest')  # Field name made lowercase.
    vopros = models.CharField(db_column='Vopros', max_length=1000)  # Field name made lowercase.
    explanation = models.CharField(max_length=1000, blank=True, null=True)
    putrisunka = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vopros'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class Indexis(models.Model):
    id_index = models.AutoField(primary_key=True)
    stat = models.TextField()  # This field type is a guess.
    sait = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'indexis'


class Otkazvobsluge(models.Model):
    idsess = models.AutoField(primary_key=True)
    idstyd = models.IntegerField(db_column='IdStyd')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otkazVObsluge'


class PollsKafedra(models.Model):
    kafedra = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'polls_kafedra'


class Pos(models.Model):
    idpos = models.AutoField(primary_key=True)
    pos = models.CharField(max_length=100)
    idtype = models.ForeignKey('Typemat', models.DO_NOTHING, db_column='idtype')
    strsaita = models.CharField(max_length=50, blank=True, null=True)
    target = models.BooleanField()
    iduch = models.ForeignKey(Ucheb, models.DO_NOTHING, db_column='iduch')

    class Meta:
        managed = False
        db_table = 'pos'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Typemat(models.Model):
    idtype = models.AutoField(primary_key=True)
    typem = models.CharField(db_column='typeM', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typeMat'


class U1(models.Model):
    col001 = models.CharField(db_column='Col001', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col002 = models.CharField(db_column='Col002', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col003 = models.CharField(db_column='Col003', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col004 = models.CharField(db_column='Col004', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col005 = models.CharField(db_column='Col005', max_length=255, blank=True, null=True)  # Field name made lowercase.
    col006 = models.CharField(db_column='Col006', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u1'
