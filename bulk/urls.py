import bulk.views

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    #url(r'^bulk/$', 'bulk.views.post_list'),
    #url(r'^bulksms/$', 'bulk.views.sample_send_sms'), 
    url(r'^$', 'bulk.views.send_sms'), 
    url(r'^schedule/$', 'bulk.views.schedule'), 
)
