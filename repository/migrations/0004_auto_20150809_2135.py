# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_remove_owner_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(unique=True, verbose_name='Name', max_length=64),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='zip_code',
            field=models.CharField(unique=True, verbose_name='Zip code', max_length=8),
        ),
    ]
