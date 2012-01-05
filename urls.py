from django.conf.urls.defaults import patterns, include, url
from django.views.static import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codex.views.home', name='home'),
    # url(r'^codex/', include('codex.foo.urls')),

    url(r'^articles/$', 'articles.views.index'),
    url(r'^articles/(?P<article_id>\d+)/$', 'articles.views.detail'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','articles.views.frontpage'),
    url(r'^frontpage/', 'articles.views.frontpage'),
)
