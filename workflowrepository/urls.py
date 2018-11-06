# workflowrepository URL Configuration

from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from data import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base/', views.base),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)