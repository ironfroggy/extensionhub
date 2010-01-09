
import os, sys

sys.path.append("/domains/0.1.v.extensionhub.pantechnoco.com/libs/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'extensionhub.settings'

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
