
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT}),
	url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_FILE_ROOT}),

]
