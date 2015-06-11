# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='desiderata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField()),
                ('tipoDesiderata', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='specializzando',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=20)),
                ('CF', models.CharField(max_length=16)),
                ('sesso', models.CharField(max_length=1)),
                ('anno_iscrizione', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='desiderata',
            name='spec',
            field=models.ForeignKey(to='specializzando.specializzando'),
        ),
    ]
