# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_auto_20150809_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owner',
            options={'ordering': ['name'], 'verbose_name_plural': 'Owners'},
        ),
        migrations.AlterField(
            model_name='owner',
            name='address_line2',
            field=models.CharField(max_length=128, blank=True, null=True, verbose_name='Address line 2'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='pob',
            field=models.CharField(max_length=8, blank=True, null=True, verbose_name='P.O.B'),
        ),
    ]
