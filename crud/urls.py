from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from app import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^servers/', include('servers.urls')),
]
