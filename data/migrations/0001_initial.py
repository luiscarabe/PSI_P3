# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 19:01
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tooltip', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(default='', max_length=512)),
                ('views', models.IntegerField()),
                ('downloads', models.IntegerField()),
                ('versionInit', models.CharField(max_length=128)),
                ('client_ip', models.GenericIPAddressField()),
                ('keywords', models.CharField(default='', max_length=256)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='data.Category')),
            ],
        ),
    ]
