# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from utils.decorators import LoginRequiredMixin
from .models import Injuria

class InjuriaListView(LoginRequiredMixin, ListView):
	model = Injuria

class InjuriaCreateView(LoginRequiredMixin, CreateView):
	model = Injuria
	fields = ['nome', 'descricao', 'midia_texto' ,'instituicao']
	success_url = 'injuria_list'

class InjuriaUpdateView(LoginRequiredMixin, UpdateView):
	model = Injuria
	fields = ['nome', 'descricao', 'midia_texto', 'instituicao']
	success_url = 'injuria_list'

class InjuriaDeleteView(LoginRequiredMixin, DeleteView):
	model = Injuria
	success_url = 'injuria_list'