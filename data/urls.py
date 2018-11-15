# workflowrepository URL Configuration

from django.conf.urls import url

# Si algo va mal revisar
urlpatterns = [
    url(r'^base/', views.base, name='base'),
]
