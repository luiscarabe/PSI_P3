# workflowrepository URL Configuration

from django.conf.urls import url
from find import views

# Si algo va mal revisar

app_name = 'find'
urlpatterns = [
    url(r'^$', views.workflow_list, name='workflow_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.workflow_list, name='workflow_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.workflow_detail, name='workflow_detail'),
    url(r'^(?P<name>[-\w]+)/$', views.workflow_search, name='workflow_search'),
]
