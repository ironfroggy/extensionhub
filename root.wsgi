
import sys, os
import __main__

os.chdir("/domains/extensionhub.pantechnoco.com/0.1.v.extensionhub.pantechnoco.com/")
sys.path.append("/domains/extensionhub.pantechnoco.com/0.1.v.extensionhub.pantechnoco.com/libs/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'extensionhub.settings'

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
