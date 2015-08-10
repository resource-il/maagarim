# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0008_auto_20150809_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='address',
            field=models.CharField(verbose_name='Address', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='street',
            field=models.CharField(verbose_name='Street', max_length=64, null=True, blank=True),
        ),
    ]
