from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),    
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',    
    # Examples:
    # url(r'^$', 'sitio.views.home', name='home'),
    url(r'^$', include('portada.urls') ),  
    # url(r'^docente/', include('docente.urls') ),
    # url(r'^alumno/', include('alumno.urls')),
    # url(r'^usuario/', include('usuario.urls')),
    # url(r'^contacto/', include('contacto.urls')),
    # url(r'^biblioteca/', include('biblioteca.urls')),
    # url(r'^formulario/', include('formulario.urls')),
    # #usuarios
    # url(r'^accounts/', include('allauth.urls')),
)