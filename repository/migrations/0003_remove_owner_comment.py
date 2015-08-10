# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_auto_20150809_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='comment',
        ),
    ]
