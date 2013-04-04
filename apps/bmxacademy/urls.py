from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
    url(r'^$',
        index_view,
        name="bmxacademy.index"),
    url(r'^json/gallery-(?P<gallery_pk>\d+).json$',
        gallery_json,
        name="bmxacademy.json.gallery"),
)