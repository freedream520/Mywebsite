from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns(
	'',
#	url(r'^', post_all),
	url(r'^$', post_all),
	url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
)
