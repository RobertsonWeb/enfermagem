# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-29 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_instituicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(db_index=True, max_length=100, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
    ]