from django.conf.urls.defaults import *
from django.conf import settings
import django.views.static
from westiseast.blog.feeds import LatestEntriesFeed
from westiseast.blog.models import BlogEntry
from django.contrib.sitemaps import GenericSitemap
from django.views.generic.simple import direct_to_template


from django.contrib import admin
admin.autodiscover()


info_dict = {
    'queryset': BlogEntry.objects.all(),
    'date_field': 'date_added',
}

sitemaps = {
    'blog': GenericSitemap(info_dict, priority=0.6),
}



urlpatterns = patterns('',
    (r'^', include('westiseast.blog.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^feeds/latest/$', LatestEntriesFeed()),
    (r'^robots\.txt$', 'direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)

urlpatterns += patterns('',

    # CSS, Javascript and IMages
    (r'^photos/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT + '/photos',
        'show_indexes': settings.DEBUG}),
    (r'^images/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT + '/images',
        'show_indexes': settings.DEBUG}),
    (r'^cache/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT + '/cache',
        'show_indexes': settings.DEBUG}),
    (r'^css/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT + '/css',
        'show_indexes': settings.DEBUG}),
    (r'^css/fonts/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT + '/css/fonts',
        'show_indexes': settings.DEBUG}),
    (r'^js/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT + '/js',
        'show_indexes': settings.DEBUG}),
)
