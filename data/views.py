# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from find import views

# Create your views here.
def base(request):
	if request.method == 'POST':
		return views.workflow_search(request)
		#return redirect('workflow_search', name=request.POST['name'])
		# return redirect('find:workflow_search',  name=request.POST['name'])
	return render(request, 'data/base.html')
