from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'home.views.index_to_home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^accounts/login/$','django.contrib.auth.views.login'),
#    url(r'^accounts/login/$', 'register.views.index_to_login'),
 #   url(r'^login/', include('register.urls')),
)
