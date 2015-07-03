from django.conf.urls import include, url
from django.contrib import admin

import settings

urlpatterns = [

	url(r'^', include('apps.urls', namespace='apps')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
]
