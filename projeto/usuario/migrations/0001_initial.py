# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-27 18:02
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=70, verbose_name='nome')),
                ('email', models.EmailField(db_index=True, max_length=70, unique=True, verbose_name='email')),
                ('is_active', models.BooleanField(default=False, help_text='Se ativo o usu\xe1rio tem permiss\xe3o para acessar o sistema', verbose_name='ativo')),
                ('tipo', models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('COMUM', 'Comum')], default='COMUM', max_length=15, verbose_name='tipo do usu\xe1rio')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'usu\xe1rio',
                'verbose_name_plural': 'usu\xe1rios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
