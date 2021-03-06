# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

# from webanayluis.admin import admin_site as admin

from django.conf import settings
import os


from django.views.generic import TemplateView

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}),

                       url(r'^maquetado/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MAQUETADO_ROOT}),

                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),

                       url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': os.path.join(settings.STATIC_ROOT, 'css')}),

                       url(r'^files/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': os.path.join(settings.STATIC_ROOT, 'files')}),

                       url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': os.path.join(settings.STATIC_ROOT, 'fonts')}),

                       url(r'^img/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': os.path.join(settings.STATIC_ROOT, 'img')}),

                       url(r'^js/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': os.path.join(settings.STATIC_ROOT, 'js')}),


                       url(r'^ckeditor/', include('ckeditor.urls')),

                       url(r'^contenidos/', include("contenidos.urls")),
                       url(r'^contacto/', include('contact_form.urls')),

                       url(r'^$', TemplateView.as_view(
                           template_name="index.html")),

                       )


admin.site.site_title = u'Administración del sitio AnayLuisTango.com.ar'
admin.site.site_header = u'Administración de Ana y Luis'
admin.site.index_title = u'Administración del Sitio Ana y Luis'

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     )
