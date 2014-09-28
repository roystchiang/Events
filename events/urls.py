__author__ = 'Roy'
from django.conf.urls import url, patterns
urlpatterns = patterns('',
   url(r'^$', 'events.views.index'),
   url(r'^events/$', 'events.views.event', name='event'),
   url(r'^events/(?P<event_id>\d+)/$', 'events.views.event_detail')
   )