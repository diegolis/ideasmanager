"""
WSGI config for ideas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append("/home/marioandres/repos/ideasmanager/")
sys.path.append("/home/marioandres/.virtualenvs/ideas/lib/python2.7/site-packages")

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()
