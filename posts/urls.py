from django.conf.urls import patterns, include, url
from posts.views import *

urlpatterns = patterns('posts.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<lang>\w+)/(?P<mode>\w)/(?P<cat>\w)/$', 'get', name='get'),
    url(r'^s/$', 'submit', name='submit'),
)

