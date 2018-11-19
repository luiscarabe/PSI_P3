# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from data.models import Category, Workflow

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    readonly_fields = ('created',)
    prepopulated_fields = {'slug' : ('name',)}

class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'views', 'downloads', 'client_ip', 'created')
    readonly_fields = ('created',)
    prepopulated_fields = {'slug' : ('name',)}


# Register your models here.z

admin.site.register(Category, CategoryAdmin)
admin.site.register(Workflow, WorkflowAdmin)
