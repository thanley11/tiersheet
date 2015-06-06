import os
import re, mmap
from os.path import join, getsize
from bs4 import BeautifulSoup

player_list ="player_list.txt"
html_to_parse = ""
html_dir ="/home/thanley/python/tiersheet/rotoworld/"

def bsoup():
    with open(player_list, 'wb') as write_file:
        print "Hello"
        for root, dirs, files in os.walk(html_dir):
            print "Next"
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
                            write_file.write("%s, %s \n" % (atag.text, prefix + atag.get('href')))

def hasHttp(string):
    url_regex = re.compile(r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>\[\]]+|\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\))+(?:\(([^\s()<>\[\]]+|(\([^\s()<>\[\]]+\)))*\)|[^\s`!(){};:'".,<>?\[\]]))""")
    match = re.search(url_regex, string)
    return match



if __name__== '__main__':
    print "Starting populate script"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sortable.settings')
    from tiersheet.models import Rotoworld_Url
    bsoup()
