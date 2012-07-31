import bulk.views

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    #url(r'^bulk/$', 'bulk.views.post_list'),
    url(r'^schedule/$', 'bulk.views.schedule'), 
    url(r'^sendsms/$', 'bulk.views.send_sms'),
    url(r'^aboutUs/$', 'bulk.views.aboutUs'),
    #url(r'^customer/(?P<id>.*?)/$', 'bulk.views.customerprofile'),
    #url(r'^optout/$', 'bulk.views.optout'),
    #url(r'^message/(?P<id>.*?)/$', 'bulk.views.editmessage'),
)
