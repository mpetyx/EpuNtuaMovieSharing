from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'epuproject.views.home', name='home'),
    # url(r'^epuproject/', include('epuproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^accounts/', include('allauth.urls')),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html' }),
    url(r'^accounts/profile/$', 'django.views.generic.simple.direct_to_template', {'template': 'profile.html' }),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
