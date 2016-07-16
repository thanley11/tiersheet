import os, sys
import csv
from django.db import IntegrityError

POSITIONS = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
def loop():
    for position in POSITIONS:
        populate(position)

def populate(position):
    path = '/home/tom/dev_projects/python/tiersheet/parse_urls/csv/'
    filename = path + position + '.csv'
    with open(filename) as players:
        player_reader = csv.reader(players)
        #hello = csv.excel_tab
        try:
            next(player_reader)
            for row in player_reader:
                rank = row[0]
                name = row[1]
                position = position.upper()
                bye = row[3]
                if bye == '':
                    bye = 0
                url = None
                team = row[2]
                print ("%s, %s, %s, %s, %s" % (position,bye,rank, name, team))
                add_player(name, position, bye, url, team, rank)
        except csv.Error as e:
            sys.exit('file %s, line %d' % (filename, player_reader.line_num, e))

def add_player(name, position, bye, url, team, rank):
    try:
        c = Player.objects.get_or_create(name=name,position=position,bye=bye,url=url,team=team, rank=rank)
    except IntegrityError:
        return False
    return c

if __name__ == '__main__':
    print("Starting populate script")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sortable.settings')
    import django
    django.setup()
    from tiersheet.models import Player
    loop()
