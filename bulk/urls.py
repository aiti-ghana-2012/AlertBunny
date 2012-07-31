import bulk.views

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    #url(r'^bulk/$', 'bulk.views.post_list'),
    url(r'^schedule/$', 'bulk.views.schedule'), 
    url(r'^sendsms/(?P<uname>.*?)/$$', 'bulk.views.send_sms'),
    url(r'^schedulesms/$', 'bulk.views.schedule_sms'),
    url(r'^customer/(?P<id>.*?)/$', 'bulk.views.customerprofile'),
    url(r'^optout/$', 'bulk.views.optout'),
    url(r'^message/(?P<id>.*?)/$', 'bulk.views.editmessage'),
)
