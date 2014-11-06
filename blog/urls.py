from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
import views


urlpatterns = patterns('',

    url(r'^$', views.index, name="home"),
    url(r'^blog/(?P<slug>[\w-]+)/$', views.blog_entry, name="blog_entry"),
    url(r'^blog/$', views.blog_entries, name="blog_entries"),
    url(r'^photo/(?P<slug>[\w-]+)/$', views.photo, name="photo"),
    url(r'^photography/$', views.all_photos, name="all_photos"),
    url(r'^about/$', direct_to_template, {'template': 'about.html'}, name="about"),
    url(r'^cv/$', direct_to_template, {'template': 'cv.html'}, name="cv"),
)
