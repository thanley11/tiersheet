import os
import urllib2
import re, mmap
from bs4 import BeautifulSoup
from django.db import IntegrityError

html_to_parse = ""
html_dir ="/home/thanley/python/tiersheet/rotoworld/"
positions = ['qb','rb','wr','te','k','dst']
fantasypros_url = "http://www.fantasypros.com/nfl/rankings/"
#+ position +"-cheatsheets.php"
def loop():
    for position in positions:
        url = fantasypros_url + position +"-cheatsheets.php"
        soup_file = scrape(url)
        bsoup(soup_file)

def bsoup(soup_file):
    for table in soup_file.findAll('div', {'class': 'mobile-table'}):
        for tbody in table.findAll('tbody'):
            for row in tbody.findAll('tr'):
                col = row.findAll('td')
                rank = col[0].text
                for link in row.findAll('a'):
                    if hasNflPrefix(link.get('href')):
                        name = link.text
                        print "%s, %s" % (rank, name)
                        add_fantasy_rank(name, rank)
                #print rank
                #div =td_list[1].findAll('div')
                #for element in div.findAll('tr',{"class":""}):
                #    print element
                #    for atag in div.findAll('a'):
                #        name = atag.text
                #        print "%s, %s" % (name, rank)
                        #add_fantasy_rank(atag.text, prefix + atag.get('href'))

def scrape(file):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(file,headers=hdr)
    page = urllib2.urlopen(req)
    fantasypros = BeautifulSoup(page)
    return fantasypros

def hasNflPrefix(string):
    url_regex = re.compile("nfl")
    match = re.search(url_regex, string)
    return match

def regexTableAd(string):
    class_regex = re.compile("table-ad")
    match = re.search(class_regex, string)
    return match

def add_fantasy_rank(fantasy_name, fantasy_rank):
    # Get player object based on name
    # When you find the object, update the rank to what is scraped
    c = FantasyProRank.objects.get_or_create(name=fantasy_name, rank=fantasy_rank)
    return c

if __name__== '__main__':
    print "Starting populate script"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sortable.settings')
    from tiersheet.models import FantasyProRank
    loop()
