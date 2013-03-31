from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
    url(r'^$',
        index_view,
        name="bmxacademy.index"),
)