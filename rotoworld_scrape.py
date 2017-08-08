import os
import urllib2
from bs4 import BeautifulSoup

def loop_dir():
    rootdir = '/rotoworld/2017/'
    for file in os.walk(rootdir):
        print (file)
        scraped = BeautifulSoup(file)
        for table in scraped.findAll('table', id='cp1_tblDepthCharts'):
            for row in table.findAll('td'):
                for atag in row.findAll('a'):
                    prefix = "http://www.rotoworld.com"
                    print ("%s, %s") % (atag.text, prefix + atag.get('href'))

def populate(scraped):
    for table in scraped.findAll('table', id='cp1_tblDepthCharts'):
        for row in table.findAll('td'):
            for atag in row.findAll('a'):
                prefix = "http://www.rotoworld.com"
                print ("%s, %s") % (atag.text, prefix + atag.get('href'))

def scrape(file):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(file,headers=hdr)
    page = urllib2.urlopen(req)
    rotoworld = BeautifulSoup(file)
    return rotoworld

def add_roto_url(name,url):
    c = Player.objects.get_or_create(name=name, position=position, bye=bye,
                                     url=url, team=team)
    return c

if __name__== '__main__':
    print ("Starting populate script")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sortable.settings')
    from tiersheet.models import Player
    loop_dir()
