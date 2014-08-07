import os, sys, site, django.core.handlers.wsgi

SITE_DIR = '/home/ubuntu/web/www.tcharleshanley.com/app/tiersheet'
site.addsitedir(SITE_DIR)
sys.path.append(SITE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'sortable.settings'
application = django.core.handlers.wsgi.WSGIHandler()
