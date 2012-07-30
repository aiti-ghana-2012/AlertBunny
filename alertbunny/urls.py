from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings	
import dj_simple_sms

admin.autodiscover()



import django_cron
django_cron.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alertbunny.views.home', name='home'),
    # url(r'^alertbunny/', include('alertbunny.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg/',include('reg.urls')),
    url(r'^bulk/',include('bulk.urls')),
    url(r'^sms/', include(dj_simple_sms.urls)),
   
    #url(r'^$', direct_to_template,{ 'template': 'index.html' }, 'index'),
    url(r'^accounts/',include('reg.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_ROOT,}),
)
