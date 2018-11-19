

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

import django, os
from data.models import Category, Workflow
from populate import Command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workflowrepository.settings')
django.setup()
populate = Command()
# populate.handle()

def workflow_given_category(categoryname):
	try:
		c = Category.objects.get(name = "category 1")
		q = Workflow.objects.filter(category = c)
		return q
	except ObjectDoesNotExist:
		return "Category named '" + categoryname + "' does not exist"


def category_given_workflow(workflowslug):
	try:
		q = Workflow.objects.get(slug = workflowslug)
		return q.category.all()
	except ObjectDoesNotExist:
		return "Workflow with slug '"+ workflowslug +"'  does not exist"

for i in range(1, 3):
	print "Creating category " + str(i) + "..."
	try:
		c = Category.objects.get(name = "category " + str(i))
	except ObjectDoesNotExist:
		c = Category(name = "category " + str(i))
		c.save()

for i in range(1, 4):
	for j in range(1, 3):
		print "Creating workflow " + str(j) + str(i) + "..."
		try:
			w = Workflow.objects.get(name = "workflow " + str(j) + str(i))
			w.category.add(Category.objects.get(name = "category " + str(j)))
		except ObjectDoesNotExist:
			w = Workflow(name = "workflow " + str(j) + str(i), json = Command.getJson(populate))
			w.save()
			w.category.add(Category.objects.get(name = "category " + str(j)))

print "--------------------------------------------"
print "Searching workflow associated to category 1..."
query = workflow_given_category("category 1")
for q in query:
	print q.name

print "Searching category of workflow-11..."
query = category_given_workflow("workflow-11")
for q in query:
	print q.slug

# In our case workflow-10 does exist
print "Searching category of workflow-10..."
query = category_given_workflow("workflow-10")
for q in query:
	print q.slug

