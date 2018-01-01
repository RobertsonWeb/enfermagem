# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class Midia(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS = (
        ('TEXTO', 'Texto'),
        ('IMAGEM', 'Imagem'),
        (u'ÁUDIO', u'Áudio')
    )
    legenda = models.CharField('Legenda', max_length=250)
    tipo = models.CharField(_(u'Tipo de mídia'), max_length=7, choices=TIPOS, default='TEXTO')
    arquivo = models.FileField(_(u'Arquivo anexo'), upload_to='uploads/midias',null=True, blank=True)
    
    class Meta:
        ordering = ['tipo']

    def __unicode__(self):
        return '%s - %s ' % (self.tipo, self.legenda)

    def save(self, *args, **kwargs):
        self.tipo = self.tipo.upper()
        super(Midia, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('midia_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('midia_delete', args=[str(self.id)])


#deleta os arquivo fisico ao excluir o item midia
@receiver(models.signals.post_delete, sender=Midia)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.arquivo:
        if os.path.isfile(instance.arquivo.path):
            os.remove(instance.arquivo.path)


#deleta o arquivo fisico ao alterar o arquivo do item midia
@receiver(models.signals.pre_save, sender=Midia)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        obj = Midia.objects.get(pk=instance.pk)

        if not obj.arquivo:
            return False

        old_file = obj.arquivo
    except Midia.DoesNotExist:
        return False

    new_file = instance.arquivo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)