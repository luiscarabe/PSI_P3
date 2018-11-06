# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json

# TODO
def workflow_list(request, category_slug = False):
	_dict = {'category' : category, 
					 'categories' : categories,
					 'workflows' : workflows,
					 'result' : found,
					 'error' : error}
	return render(request, 'find/list.html', _dict)

# TODO
def workflow_detail(request, id, slug):
	_dict = {}
	_dict['result'] = result
	_dict['workflow'] = workflow
	_dict['error'] = error

	return render(request, 'find/detail.html', _dict)

# TODO
def workflow_search(request, name):
	_dict = {}
	_dict['result'] = result
	_dict['workflow'] = workflow
	_dict['error'] = error

	return render(request, 'find/detail.html', _dict)

