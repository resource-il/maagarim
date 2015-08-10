# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('content', models.TextField(verbose_name='Content')),
                ('full_name', models.CharField(max_length=128, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('ip_address', models.CharField(max_length=64, verbose_name='IP Address')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('edited_flag', models.BooleanField(default=False, verbose_name='Edited Flag')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('status', models.CharField(max_length=32, verbose_name='Status')),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
            ],
            options={
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerComment',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to='comment.Comment', primary_key=True)),
                ('owner', models.ForeignKey(to='repository.Owner', verbose_name='Owner')),
            ],
            options={
                'verbose_name_plural': 'Owner Comments',
            },
            bases=('comment.comment',),
        ),
        migrations.CreateModel(
            name='RepositoryComment',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to='comment.Comment', primary_key=True)),
                ('repository', models.ForeignKey(to='repository.Repository', verbose_name='Repository')),
            ],
            options={
                'verbose_name_plural': 'Repository Comments',
            },
            bases=('comment.comment',),
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.ForeignKey(to='comment.Status', verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='comment',
            name='type',
            field=models.ForeignKey(to='comment.Type', verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_by',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, verbose_name='Updated By'),
        ),
    ]
