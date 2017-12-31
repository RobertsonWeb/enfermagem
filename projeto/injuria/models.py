# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

class Injuria(models.Model):
    nome = models.CharField(_(u'Nome principal da injúria'), max_length=250)
    descricao = models.TextField(_(u'Descrição da injúria')) 
    instituicao = models.ForeignKey('instituicao.Instituicao', null=True, blank=True)
    midia_texto = models.ForeignKey('midia.Midia', null=True, blank=True)

    class Meta:
        ordering = [u'nome']

    def __unicode__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        super(Injuria, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('injuria_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('injuria_delete', args=[str(self.id)])


