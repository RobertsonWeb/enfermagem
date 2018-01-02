# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

class Pergunta(models.Model):
    numero = models.IntegerField(_(u'Número da pergunta'), null=True, blank=True)
    descricao = models.TextField(_(u'Descrição da pergunta')) 
    numero_exibicoes = models.IntegerField(_(u'Quantidade de vezes que a pergunta foi realizada'), null=True, blank=True)
    injuria = models.ForeignKey('injuria.Injuria', null=True, blank=True)
    midia_texto = models.ForeignKey('midia.Midia', null=True, blank=True)

    class Meta:
        ordering = [u'descricao']

    def __unicode__(self):
        return self.descricao   #'%d - %s ' % (self.numero, self.descricao)

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()
        super(Pergunta, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('pergunta_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('pergunta_delete', args=[str(self.id)])


