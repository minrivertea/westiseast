from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
import views


urlpatterns = patterns('',

    url(r'^$', views.index, name="home"),
    url(r'^more/$', views.more, name="more"),
    url(r'^even-more/$', views.even_more, name="even_more"),
    url(r'^blog/(?P<slug>[\w-]+)/$', views.blog_entry, name="blog_entry"),
    url(r'^photography/$', views.all_photos, name="all_photos"),
    url(r'^photography/all/$', views.all_photos, name="deprecated"), 
    url(r'^photography/gallery/(?P<slug>[\w-]+)/$', views.gallery, name="gallery"),
    url(r'^about/$', direct_to_template, {'template': 'about.html'}, name="about"),
    url(r'^cv/$', direct_to_template, {'template': 'cv.html'}, name="cv"),
)
