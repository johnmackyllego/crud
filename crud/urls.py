from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^', include('servers.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^servers/', include('servers.urls')),
]
