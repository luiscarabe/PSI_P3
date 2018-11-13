# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

import django, os
from data.models import Category, Workflow

import json

def workflow_list(request, category_slug = None):
	workflows = None

	# Search for all categories
	categories = Category.objects.all()
	found = True # Default value of found is true

	# Check if we are searching a specific category
	# In case not...
	if category_slug == None:
		category = None
		# List of all workflows
		workflows = Workflow.objects.all()
		print workflows.count()
		if workflows.count() == 0:
			found = False
			error = "No Workflows found!"
		else:
			error = ""
	# In other case...
	else:
		try:
			# Find category with that slug and its workflows
			category = Category.objects.get(slug = category_slug)
			workflows = Workflow.objects.filter(category = category)
		except ObjectDoesNotExist:
			# Category does not exist
			category = None
			found = False
			error = "Category with slug '" + category_slug + "' does not exist"
		
		# If there is no workflows in some category
		if workflows.count()==0 and found == True:
			found = False
			error = "No Workflows in this category!"
		else:
			found = True
			error = ""

	# Create the dictionary
	_dict = {'category' : category,
					 'categories' : categories,
					 'workflows' : workflows,
					 'result' : found,
					 'error' : error}
	return render(request, 'find/list.html', _dict)

def workflow_detail(request, id, slug):

	# Default values
	found = True
	error=""

	# Find workflow with slug given
	try:
		# Fix, el enunciado habla de id, pero el model Workflow no tiene id!!!
		workflow = Workflow.objects.get(slug = slug)
	except ObjectDoesNotExist:
		# Workflow does not exist
		workflow = None
		found = False
		error = "Workflow with slug '" + slug + "' and id '" + str(id) +  "' does not exist"

	# Create the dictionary
	_dict = {}
	_dict['result'] = found
	_dict['workflow'] = workflow
	_dict['error'] = error

	return render(request, 'find/detail.html', _dict)

def workflow_search(request, name):

	# FIX hay que hacer algo con el POST????????? no entiendo

	# Default values
	found = True
	error=""

	# Find workflow with name given
	try:
		workflow = Workflow.objects.get(name = name)
	except ObjectDoesNotExist:
		# Workflow does not exist
		workflow = None
		found = False
		error = "Workflow with name '" + name + "' does not exist"

	# Create the dictionary
	_dict = {}
	_dict['result'] = found
	_dict['workflow'] = workflow
	_dict['error'] = error

	return render(request, 'find/detail.html', _dict)
