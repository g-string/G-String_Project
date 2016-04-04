# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class ActiveSubstance(models.Model):
    primarykey = models.AutoField(db_column='PrimaryKey', primary_key=True)  # Field name made lowercase.
    substance = models.CharField(db_column='Substance', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'active_substance'


class ActiveSubstances(models.Model):
    primarykey = models.AutoField(db_column='PrimaryKey', primary_key=True)  # Field name made lowercase.
    brand = models.ForeignKey('Brand', db_column='Brand')  # Field name made lowercase.
    substance = models.ForeignKey(ActiveSubstance, db_column='Substance')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'active_substances'


class Brand(models.Model):
    primarykey = models.AutoField(db_column='PrimaryKey', primary_key=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', unique=True, max_length=32)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brand'


class Classification(models.Model):
    primarykey = models.AutoField(db_column='PrimaryKey', primary_key=True)  # Field name made lowercase.
    classification = models.CharField(db_column='Classification', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classification'


class Difficulty(models.Model):
    primarykey = models.AutoField(db_column='PrimaryKey', primary_key=True)  # Field name made lowercase.
    difficulty = models.IntegerField(db_column='Difficulty')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'difficulty'


class Form(models.Model):
    primarykey = models.AutoField(db_column='PrimaryKey', primary_key=True)  # Field name made lowercase.
    form = models.CharField(db_column='Form', unique=True, max_length=32)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form'


class Group(models.Model):
    primarykey = models.AutoField(db_column='PrimaryKey', primary_key=True)  # Field name made lowercase.
    group = models.IntegerField(db_column='Group', unique=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group'


class Highscores(models.Model):
    primarykey = models.AutoField(db_column='PrimaryKey', primary_key=True)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points')  # Field name made lowercase.
    group = models.IntegerField(db_column='Group')  # Field name made lowercase.
    difficulty = models.IntegerField(db_column='Difficulty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'highscores'


class Medicine(models.Model):
    primarykey = models.AutoField(db_column='PrimaryKey', primary_key=True)  # Field name made lowercase.
    brand = models.ForeignKey(Brand, db_column='Brand')  # Field name made lowercase.
    activesubstance = models.ForeignKey(ActiveSubstances, db_column='ActiveSubstance')  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=32)  # Field name made lowercase.
    classification = models.ForeignKey(Classification, db_column='Classification')  # Field name made lowercase.
    form = models.ForeignKey(Form, db_column='Form')  # Field name made lowercase.
    indication = models.CharField(db_column='Indication', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicine'


class Users(models.Model):
    primarykey = models.AutoField(db_column='PrimaryKey', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    salt = models.CharField(db_column='Salt', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
