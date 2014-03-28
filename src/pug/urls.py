from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pug.apps.homepage.views.index', name='index'),
    url(r'^contact$', 'pug.apps.homepage.views.contact', name='contact'),
    url(r'^blog$', 'pug.apps.homepage.views.blog', name='blog'),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT, 'show_indexes' : False}),


    # url(r'^pug/', include('pug.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


# ... the rest of your URLconf goes here ...
urlpatterns += staticfiles_urlpatterns()
