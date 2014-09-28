__author__ = 'Roy'
from django.conf.urls import url, patterns
urlpatterns = patterns('',
   url(r'^login/$', 'backend.views.user_login'),
   url(r'^logout/$', 'backend.views.user_logout'),
   url(r'^backend/$', 'backend.views.backend'),
   )