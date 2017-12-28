# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Instituicao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Nome', max_length=20)

    class Meta:
        ordering = ['sigla']
        verbose_name        =   _(u'instituição')
      	verbose_name_plural =   _(u'instituições')

    def __unicode__(self):
        return '%s - %s ' % (self.sigla, self.nome)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.sigla = self.sigla.upper()
        super(Instituicao, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('instituicao_update', args=[str(self.id)])