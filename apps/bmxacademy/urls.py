from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
    url(r'^$',
        index_view,
        name="bmxacademy.index"),
    url(r'^intro/$',
        intro_view,
        name="bmxacademy.intro"),
    url(r'^registration/$',
        registration_view,
        name="bmxacademy.registration"),
    url(r'^contact/$',
        contact_view,
        name="bmxacademy.contact"),
    url(r'^intro/$',
        intro_view,
        name="bmxacademy.intro"),
    url(r'^json/gallery-(?P<gallery_pk>\d+).json$',
        gallery_json,
        name="bmxacademy.json.gallery"),
)