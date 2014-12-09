from django.conf.urls import patterns, include, url
from django.contrib import admin
import forum.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', include(forum.urls)),
)
