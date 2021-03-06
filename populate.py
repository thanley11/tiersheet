import os
import sys


def populate():
    player_1 = add_player('Chris Polk','RB',9,'http://www.rotoworld.com/player/nfl/7424/chris-polk')

def add_player(name,position,bye,url):
    c = Player.objects.get_or_create(name=name,position=position,bye=bye,url=url)
    return c

if __name__== '__main__':
    print "Starting populate script"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sortable.settings')
    from tiersheet.models import Player
    populate()
