from django.conf.urls.defaults import patterns, include, url
import os.path
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': os.path.join(settings.PROJECT_DIR, 'static'),
        'show_indexes': True
    }),
    url(r'^xml/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': os.path.join(settings.PROJECT_DIR, 'xml'),
        'show_indexes': True
    }),
)

urlpatterns += patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^kanal/(?P<kanal>.*)/$', 'core.views.kanal', name='kanal'),
    # url(r'^news$', 'core.views.home', name='news'),
    # url(r'^internasional$', 'core.views.home', name='internasional'),
    # url(r'^ekonomi$', 'core.views.home', name='ekonomi'),
    # url(r'^bola$', 'core.views.home', name='bola'),
    url(r'^detail/(?P<url>.*)/$', 'core.views.detail', name='detail'),
)
