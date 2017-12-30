# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from utils.decorators import LoginRequiredMixin
from .models import Instituicao

# Create your views here.

class InstituicaoListView(LoginRequiredMixin, ListView):
	model = Instituicao


class InstituicaoCreateView(LoginRequiredMixin, CreateView):
	model = Instituicao
	fields = ['nome', 'sigla']
	success_url = 'instituicao_list'


class InstituicaoUpdateView(LoginRequiredMixin, UpdateView):
	model = Instituicao
	fields = ['nome', 'sigla']
	success_url = 'instituicao_list'


class InstituicaoDeleteView(LoginRequiredMixin, DeleteView):
	model = Instituicao
	success_url = 'instituicao_list'