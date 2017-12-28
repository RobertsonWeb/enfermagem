# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Instituicao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Nome', max_length=20)

    def __unicode__(self):
        return '%s - %s ' % (self.sigla, self.nome)