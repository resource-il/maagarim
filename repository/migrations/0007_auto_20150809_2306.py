# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0006_auto_20150809_2305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repository',
            options={'ordering': ['name'], 'verbose_name_plural': 'Repositories'},
        ),
    ]
