from django.conf.urls import patterns, include, url
from posts.views import *

urlpatterns = patterns('posts.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<lang>\w+)/(?P<cat>\w)/(?P<mode>\w)/$', 'get', name='get'),
    url(r'^u/(?P<id>\d+)/$', 'upvote', name='upvote'),
    url(r'^s/$', 'submit', name='submit'),
)

