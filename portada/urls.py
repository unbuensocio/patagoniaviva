from django.conf.urls import patterns, url

urlpatterns = patterns('portada.views',
	# url(r'^portada/$','portada',name='portada'),
    url(r'^$','portada', name='portada'),
)
 
