from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns(
	'',
#	url(r'^', post_all),
	url(r'^$', post_all),
	url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
	url(r'^posts/tag/(?P<tag>\w+)$', post_list_by_tag, name='list_by_tag'),
	url(r'^posts/category/(?P<cg>\w+)$', post_list_by_category, name='list_by_cg'),
	url(r'^post/new/$', post_new, name = 'pose_new'),
)
