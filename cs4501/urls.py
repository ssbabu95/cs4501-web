from django.conf.urls import patterns, include, url
from django.contrib import admin
from cs4501 import main

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cs4501.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', main.render_home),
    url(r'^item/(\d+)$', main.item_det),
    url(r'^about/$', main.about, name='about'),
    url(r'^create_user/$', main.create_user),
)
