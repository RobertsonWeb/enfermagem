# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from utils.decorators import LoginRequiredMixin
from .models import Midia

# Create your views here.

class MidiaListView(LoginRequiredMixin, ListView):
	model = Midia

class MidiaCreateView(LoginRequiredMixin, CreateView):
	model = Midia
	fields = ['tipo', 'legenda']
	success_url = 'midia_list'


class MidiaUpdateView(LoginRequiredMixin, UpdateView):
	model = Midia
	fields = ['tipo', 'legenda']
	success_url = 'midia_list'


class MidiaDeleteView(LoginRequiredMixin, DeleteView):
	model = Midia
	success_url = 'midia_list'