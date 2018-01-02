# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .forms import UploadFileForm
# from .models import ModelWithFileField

# Create your models here.
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
    arquivo = models.TextField(_(u'Caminho do arquivo'), null=True, blank=True)

    # def upload_file(request):
    #     if request.method == 'POST':
    #         form = UploadFileForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             instance = ModelWithFileField(file_field=request.FILES['file'])
    #             instance.save()
    #             return HttpResponseRedirect('/success/url/')
    #     else:
    #         form = UploadFileForm()
    #     return render(request, 'upload.html', {'form': form})

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
