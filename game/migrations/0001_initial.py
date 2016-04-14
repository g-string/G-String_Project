# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveSubstance',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False, db_column='PrimaryKey')),
                ('substance', models.CharField(max_length=64, db_column='Substance', unique=True)),
                ('description', models.CharField(null=True, max_length=255, blank=True, db_column='Description')),
            ],
            options={
                'db_table': 'active_substance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ActiveSubstances',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False, db_column='PrimaryKey')),
            ],
            options={
                'db_table': 'active_substances',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False, db_column='PrimaryKey')),
                ('brand', models.CharField(max_length=32, db_column='Brand', unique=True)),
                ('description', models.CharField(null=True, max_length=255, blank=True, db_column='Description')),
            ],
            options={
                'db_table': 'brand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False, db_column='PrimaryKey')),
                ('classification', models.CharField(max_length=64, db_column='Classification', unique=True)),
                ('description', models.CharField(null=True, max_length=255, blank=True, db_column='Description')),
            ],
            options={
                'db_table': 'classification',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False, db_column='PrimaryKey')),
                ('difficulty', models.IntegerField(db_column='Difficulty')),
                ('description', models.CharField(max_length=20, db_column='Description')),
            ],
            options={
                'db_table': 'difficulty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False, db_column='PrimaryKey')),
                ('form', models.CharField(max_length=32, db_column='Form', unique=True)),
                ('description', models.CharField(null=True, max_length=255, blank=True, db_column='Description')),
            ],
            options={
                'db_table': 'form',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False, db_column='PrimaryKey')),
                ('group', models.IntegerField(db_column='Group', unique=True)),
                ('description', models.CharField(max_length=20, db_column='Description')),
            ],
            options={
                'db_table': 'group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Highscores',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False, db_column='PrimaryKey')),
                ('points', models.IntegerField(db_column='Points')),
                ('group', models.IntegerField(db_column='Group')),
                ('difficulty', models.IntegerField(db_column='Difficulty')),
            ],
            options={
                'db_table': 'highscores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False, db_column='PrimaryKey')),
                ('dosage', models.CharField(max_length=32, db_column='Dosage')),
                ('indication', models.CharField(null=True, max_length=255, blank=True, db_column='Indication')),
            ],
            options={
                'db_table': 'medicine',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('primarykey', models.AutoField(primary_key=True, serialize=False, db_column='PrimaryKey')),
                ('username', models.CharField(max_length=20, db_column='Username', unique=True)),
                ('password', models.CharField(max_length=50, db_column='Password')),
                ('salt', models.CharField(max_length=50, db_column='Salt')),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
