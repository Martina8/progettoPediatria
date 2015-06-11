# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specializzando', '0002_auto_20150611_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='specializzando',
            name='mat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='specializzando',
            name='neo',
            field=models.BooleanField(default=False),
        ),
    ]
