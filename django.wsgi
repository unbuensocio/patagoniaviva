#!/opt/python2.7/bin/python
import os, sys
sys.path.insert(0,'/var/www/patagonia/sitio/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'sitio.settings'
os.environ['PYTHON_EGG_CACHE'] = '/var/www/patagonia/.python-eggs'
# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()