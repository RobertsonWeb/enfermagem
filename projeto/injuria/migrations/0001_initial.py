# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-30 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instituicao', '0003_auto_20171229_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Injuria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='nome')),
                ('descricao', models.CharField(max_length=250, verbose_name='descricao')),
                ('instituicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='instituicao.Instituicao')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
