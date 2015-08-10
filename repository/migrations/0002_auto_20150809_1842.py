# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='owner_serial',
            field=models.BigIntegerField(verbose_name='Owner Serial'),
        ),
    ]
