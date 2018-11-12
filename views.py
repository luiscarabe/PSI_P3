# workflowrepository URL Configuration

from django.conf.urls import url

# Si algo va mal revisar

urlpatterns = [
	url(r'^find/', include('find.urls', namespace='find')),
	url(r'^admin/', admin.site.urls),
	url(r'', include('data.urls')),
]
