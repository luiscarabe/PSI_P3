# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.template.defaultfilters import slugify
from datetime import date

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True, blank=False)
	slug = models.SlugField(unique=True)
	created = models.DateField(default=date.today)
	tooltip = models.CharField(max_length=128)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural='Categories'

	def __str__(self):# For Python 2, use __unicode__ too
		return self.name

class Workflow(models.Model):
	name = models.CharField(max_length=128, unique=True, blank=False)
	slug = models.SlugField(unique=True)
	descrciption = models.CharField(max_length=512, default="")
	views = models.IntegerField()
	downloads = models.IntegerField()
	versionInit = models.CharField(max_length=128)
	category = models.ManyToManyField(Category)
	client_ip = models.GenericIPAddressField()
	keywords = models.CharField(max_length=256, default="")
	json = JSONField()
	created = models.DateField(default=date.today)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Workflow, self).save(*args, **kwargs)


	def __str__(self):# For Python 2, use __unicode__ too
		return self.name

