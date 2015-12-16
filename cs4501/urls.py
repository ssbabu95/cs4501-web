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
    url(r'^login/$', main.login),
    url(r'^logout/$', main.log_out),
    url(r'^logoutsuccess$', main.logoutsuccess),
    url(r'^profile/$', main.profile),
    url(r'^create_listing/$', main.createListing),
    url(r'^create_listing_success/$', main.createListingSuccess),
    url(r'^searchresults/$', main.searchresults),
    url(r'^base1/$', main.base1),
    url(r'^base2/$', main.base2),
    url(r'^base3/$', main.base3),
#    url(r'^search/$', main.search),
)
