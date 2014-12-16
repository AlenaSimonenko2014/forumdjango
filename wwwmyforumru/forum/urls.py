from django.conf.urls import patterns, include, url
from django.contrib import admin
# import forum.urls

urlpatterns = patterns(
    '',
    url(r'^section/(?P<section_id>\d+)/$', 'forum.views.section', name='section'),
    url(r'^topic/(?P<topic_id>\d+)/$', 'forum.views.topic', name='topic'),
    url(r'^send_message/(?P<topic_id>\d+)/$', 'forum.views.send_message', name='send_message'),
    url(r'^$', 'forum.views.index', name='index'),
)
