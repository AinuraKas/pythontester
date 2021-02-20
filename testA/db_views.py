from django.db import models
from testA.models import Test


class fullyVopros(models.Model):
    fv_idvopr = models.AutoField(db_column='fv_IdVopr', primary_key=True)  # Field name made lowercase.
    fv_idtest = models.ForeignKey(Test, models.DO_NOTHING, db_column='fv_IdTest')  # Field name made lowercase.
    fv_vopros = models.CharField(db_column='fv_Vopros', max_length=1000)  # Field name made lowercase.
    fv_explanation = models.CharField(max_length=1000, blank=True, null=True)
    fv_putrisunka = models.CharField(max_length=50, blank=True, null=True)
    ccnt = models.IntegerField(db_column='ccnt')

    class Meta:
        managed = False
        db_table = 'fullyVopros'

class v_Otvet(models.Model):
    idotvet = models.AutoField(db_column='IdOtvet', primary_key=True)  # Field name made lowercase.
    idvopr = models.ForeignKey('fullyVopros', models.DO_NOTHING, db_column='IdVopr')  # Field name made lowercase.
    otvet = models.CharField(db_column='Otvet', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ball = models.IntegerField(db_column='Ball', blank=True, null=True)  # Field name made lowercase.
    ris = models.BooleanField(db_column='Ris')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'v_Otvet'