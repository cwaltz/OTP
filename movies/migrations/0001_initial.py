# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('release_year', models.IntegerField(blank=True)),
                ('locations', models.CharField(max_length=200, blank=True)),
                ('fun_facts', models.CharField(max_length=500, blank=True)),
                ('production_company', models.CharField(max_length=200, blank=True)),
                ('distributor', models.CharField(max_length=200, blank=True)),
                ('director', models.CharField(max_length=100, blank=True)),
                ('writer', models.CharField(max_length=100, blank=True)),
                ('actor_1', models.CharField(max_length=100, blank=True)),
                ('actor_2', models.CharField(max_length=100, blank=True)),
                ('actor_3', models.CharField(max_length=100, blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
