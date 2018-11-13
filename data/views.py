# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from data.forms import BaseForm

# Create your views here.
def base(request):
	if request.method == 'POST':
		#return redirect('workflow_search', name=request.POST['name'])
		return redirect('/workflow_search/' + request.POST['name'])
	return render(request, 'data/base.html')
