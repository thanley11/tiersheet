import os
import re, mmap
from os.path import join, getsize
from bs4 import BeautifulSoup
from django.db import IntegrityError

html_to_parse = ""
html_dir ="/home/tom/dev_projects/python/tiersheet/parse_urls/"

def bsoup():
    for root, dirs, files in os.walk(html_dir):
        for html_file in files:
            soup_file = BeautifulSoup(open(html_dir + html_file))
            for table in soup_file.findAll('table',id ="cp1_tblDepthCharts"):
                for row in table.findAll('td'):
                    for atag in row.findAll('a'):
                        if not hasHttp(atag.get('href')):
                            prefix = "http://www.rotoworld.com"
                        else:
                            prefix = ""
                        print "%s, %s" % (atag.text, prefix + atag.get('href'))
                        try:
                            add_roto_url(atag.text, prefix + atag.get('href'))
                        except IntegrityError:
                            add_roto_url(atag.text + " (dup)", prefix + atag.get('href'))

def hasHttp(string):
    url_regex = re.compile(r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>\[\]]+|\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\))+(?:\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\)|[^\s`!(){};:'".,<>?\[\]]))""")
    match = re.search(url_regex, string)
    return match

def add_roto_url(name,roto_url):
    c = Rotoworld_Url.objects.get_or_create(name=name,roto_url=roto_url)
    return c

if __name__== '__main__':
    print "Starting populate script"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sortable.settings')
    import django
    django.setup()
    from tiersheet.models import Rotoworld_Url
    bsoup()
