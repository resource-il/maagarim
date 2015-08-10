# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('serial', models.BigIntegerField(verbose_name='Serial')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('address', models.CharField(max_length=128, verbose_name='Address')),
                ('address_line2', models.CharField(max_length=128, verbose_name='Address line 2')),
            ],
            options={
                'verbose_name_plural': 'Owners',
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('serial', models.BigIntegerField(verbose_name='Serial')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('marketing', models.BooleanField(default=False, verbose_name='Marketing')),
                ('status', models.CharField(max_length=16, verbose_name='Status', null=True)),
                ('date', models.CharField(max_length=16, verbose_name='Date', blank=True, null=True)),
                ('owner_serial', models.BigIntegerField(verbose_name='Owner')),
                ('owner_name', models.CharField(max_length=255, verbose_name='Owner name')),
                ('city', models.CharField(max_length=64, verbose_name='City')),
                ('street', models.CharField(max_length=64, verbose_name='Street')),
                ('house', models.CharField(max_length=8, verbose_name='House')),
                ('pob', models.CharField(max_length=8, verbose_name='P.O.B')),
                ('zip_code', models.CharField(max_length=8, verbose_name='Zip code')),
                ('owner', models.ForeignKey(null=True, to='repository.Owner', blank=True, verbose_name='Owner')),
            ],
            options={
                'verbose_name_plural': 'Repositories',
            },
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=8, verbose_name='Zip code')),
                ('city', models.ForeignKey(to='repository.City', verbose_name='City')),
            ],
            options={
                'verbose_name_plural': 'Zip Codes',
            },
        ),
        migrations.AddField(
            model_name='owner',
            name='zip_code',
            field=models.ForeignKey(null=True, to='repository.ZipCode', blank=True, verbose_name='Zip code'),
        ),
    ]
