from django.conf.urls import patterns, include, url
from django.contrib import admin
# import forum.urls
from forum.views import TopicView, ProfileView

urlpatterns = patterns(
    '',
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),
    url(r'^section/(?P<section_id>\d+)/$', 'forum.views.section', name='section'),
    url(r'^topic/(?P<topic_id>\d+)/$', TopicView.as_view(), name='topic'),
    url(r'^add_topic/(?P<section_id>\d+)/$', 'forum.views.add_topic', name='add_topic'),
    url(r'^$', 'forum.views.index', name='index'),
)
