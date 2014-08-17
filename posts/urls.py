from django.conf.urls import patterns, include, url
from posts.views import *

urlpatterns = patterns('posts.views',
    url(r'^$', 'index', name='index'),
    url(r'^t/$', 'get', {'cat': 't', 'language': None, 'mode': 't'}),
)

