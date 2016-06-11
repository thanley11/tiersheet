import os
import sys


def populate_tiers():
    positions = ['QB','RB', 'WR', 'TE']
    #positions = ['QB']
    for i in positions:
        for j in range(1,8):
            tier_name = '%s Tier %s' % (i, j)
            add_player(tier_name,i,None,None)

def add_player(name,position,bye,url):
    c = Player.objects.get_or_create(name=name,position=position,bye=bye,url=url)
    return c

if __name__== '__main__':
    print "Starting populate tiers script"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sortable.settings')
    import django
    django.setup()
    from tiersheet.models import Player
    populate_tiers()
