# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from utils.decorators import LoginRequiredMixin
from .models import Pergunta

class PerguntaListView(LoginRequiredMixin, ListView):
	model = Pergunta

class PerguntaCreateView(LoginRequiredMixin, CreateView):
	model = Pergunta
	fields = ['numero', 'descricao', 'numero_exibicoes', 'injuria', 'midia_texto']
	# fields = ['descricao', 'injuria', 'midia_texto']
	success_url = 'pergunta_list'

class PerguntaUpdateView(LoginRequiredMixin, UpdateView):
	model = Pergunta
	fields = ['numero', 'descricao', 'numero_exibicoes', 'injuria', 'midia_texto']
	# fields = ['descricao', 'injuria', 'midia_texto']
	success_url = 'pergunta_list'

class PerguntaDeleteView(LoginRequiredMixin, DeleteView):
	model = Pergunta
	success_url = 'pergunta_list'