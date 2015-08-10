# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20150809_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='house',
            field=models.CharField(verbose_name='House', blank=True, null=True, max_length=8),
        ),
    ]
