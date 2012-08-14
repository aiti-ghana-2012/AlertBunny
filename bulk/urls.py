import bulk.views

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    #url(r'^bulk/$', 'bulk.views.post_list'),
    url(r'^scheduled/$', 'bulk.views.scheduled'), 
    url(r'^sendsms/$', 'bulk.views.send_sms'),
    url(r'^profile/$', 'bulk.views.profile'),
    url(r'^sentsms/$', 'bulk.views.sent_sms'),
    url(r'^group/$', 'bulk.views.grouplist'),
   
    
    url(r'^contactUs/$', 'bulk.views.contact_Us'),
    url(r'^aboutUs/$', 'bulk.views.aboutUs'),
    url(r'^buyCredit/$', 'bulk.views.buyCredit'),
    url(r'^features/$', 'bulk.views.abFeatures'),
    url(r'^faqs/$', 'bulk.views.faqs'),
    #url(r'^optout/$', 'bulk.views.optout'),
    #url(r'^message/(?P<id>.*?)/$', 'bulk.views.editmessage'),
    url(r'^optout/$', 'bulk.views.optout'),
    url(r'^optout/(?P<id>.*?)/$', 'bulk.views.editoptout'),
    url(r'^message/(?P<id>.*?)/$', 'bulk.views.editmessage'),
    url(r'^group/(?P<id>.*?)/$', 'bulk.views.groupcontact'),
    url(r'^addcontacts/(?P<id>.*?)/$', 'bulk.views.addcontact'),
    url(r'^addgroup/$', 'bulk.views.addgroup'),
    url(r'^groupcontacts/(?P<id>.*?)/$', 'bulk.views.groupcontacts'),
)
