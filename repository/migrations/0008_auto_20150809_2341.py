# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0007_auto_20150809_2306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='zipcode',
            options={'verbose_name_plural': 'Zip Codes', 'ordering': ['zip_code']},
        ),
    ]
