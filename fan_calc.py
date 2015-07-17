import os, sys
import csv

def populate():
    filename = 'adp_csv.csv'
    with open(filename,'rb') as players:
        player_reader = csv.reader(players)
        try:
            for row in player_reader:
               name = row[2]
               position = row[3]
               bye = row[6]
               url = None
               team = row[4]
               add_player(name, position, bye, url, team)
        except csv.Error as e:
            sys.exit('file %s, line %d' % (filename, player_reader.line_num, e))

def add_player(name,position,bye,url,team):
    c = Player.objects.get_or_create(name=name,position=position,bye=bye,url=url,team=team)
    return c

if __name__== '__main__':
    print "Starting populate script"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sortable.settings')
    from tiersheet.models import Player
    populate()
