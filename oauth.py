import os
from requests_oauthlib import OAuth1Session
import json
from lxml import etree
def populate():
    key = os.environ['YAHOO_CONSUMER_KEY']
    secret = os.environ['YAHOO_SECRET_KEY']

    # OAuth URLs given on the application page
    request_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
    authorization_base_url = 'https://api.login.yahoo.com/oauth/v2/request_auth'
    access_token_url = 'https://api.login.yahoo.com/oauth/v2/get_token'

    #Use any redirect page here, you  leave it as it, we just need extract the query params (see below)
    yahoo = OAuth1Session(key, client_secret=secret, callback_uri='www.google.com')

    yahoo.fetch_request_token(request_token_url)

    # Link user to authorization page
    authorization_url = yahoo.authorization_url(authorization_base_url)
    print "Please go here and click 'Agree',", authorization_url

    # Get the verifier code from the URL
    redirect_response = raw_input('Paste the full redirect URL here: ')
    yahoo.parse_authorization_response(redirect_response)

    # Fetch the access token
    access_token_data = yahoo.fetch_access_token(access_token_url)

    print '\n\nYour access token data:', access_token_data

    QB1 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=QB;sort=OR;start=0?format=json').json()
    QB2 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=QB;sort=OR;start=25?format=json').json()
    RB1 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=RB;sort=OR;start=0?format=json').json()
    RB2 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=RB;sort=OR;start=25?format=json').json()
    RB3 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=RB;sort=OR;start=50?format=json').json()
    WR1 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=WR;sort=OR;start=0?format=json').json()
    WR2 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=WR;sort=OR;start=25?format=json').json()
    WR3 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=WR;sort=OR;start=50?format=json').json()
    WR4 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=WR;sort=OR;start=75?format=json').json()
    TE1 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=TE;sort=OR;start=0?format=json').json()
    TE2 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=TE;sort=OR;start=25?format=json').json()
#DEF1 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/teams;start=0?format=json').json()
#DEF2 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/teams;start=25?format=json').json()
    K1 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=K;sort=OR;start=0?format=json').json()
    K2 = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=K;sort=OR;start=25?format=json').json()
    TEAMS = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games;game_keys=nfl/teams?format=json').json()

#    data = json.dumps(QB2, sort_keys=True, indent=4, separators=(',', ': '))
#    print data
# SELECT * FROM fantasysports.players WHERE league_key="331.l.249215" and sort="AR" and sort_type="season" and sort_season="2014"
posArray = [QB1,QB2,RB1,RB2,RB3,WR1,WR2,WR3,TE1,TE2,K1,K2,TEAMS]
     for y in posArray:
        myResult = y["fantasy_content"]["league"][1]["players"]
        for x in myResult.keys():
            if x == "count":
                pass
            else:
                try:
                    name = myResult[x]["player"][0][2]["name"]["full"]
                    position = "QB"
                    #bye  = myResult[x]["player"][0][7]["bye_weeks"]["week"]
                    bye = None
                    url  = "http://sports.yahoo.com/nfl/players/" + myResult[x]["player"][0][1]["player_id"] +"/"
                    team = myResult[x]["player"][0][7]["editorial_team_abbr"]
                    add_player(name,position,bye,url,team)

                except KeyError:
                    name = myResult[x]["player"][0][2]["name"]["full"]
                    position = "QB"
                    #bye  = myResult[x]["player"][0][8]["bye_weeks"]["week"]
                    bye = None
                    url  = "http://sports.yahoo.com/nfl/players/" + myResult[x]["player"][0][1]["player_id"] +"/"
                    team = myResult[x]["player"][0][8]["editorial_team_abbr"]
                    add_player(name,position,bye,url,team)

# First is 8, next is 7, next is 6 for team abbrev
#Creates IntegrityError bc it is repeating team names that are grabbed from QB


    #QB Tiers
    qb_tier1 = add_player("QB Tier 1","QB",None,None,None)
    qb_tier2 = add_player("QB Tier 2","QB",None,None,None)
    qb_tier3 = add_player("QB Tier 3","QB",None,None,None)
    qb_tier4 = add_player("QB Tier 4","QB",None,None,None)
    qb_tier5 = add_player("QB Tier 5","QB",None,None,None)
    qb_tier6 = add_player("QB Tier 6","QB",None,None,None)
    qb_tier7 = add_player("QB Tier 7","QB",None,None,None)
    qb_tier8 = add_player("QB Tier 8","QB",None,None,None)
    qb_tier9 = add_player("QB Tier 9","QB",None,None,None)

    rb_tier1 = add_player("RB Tier 1","RB",None,None,None)
    rb_tier2 = add_player("RB Tier 2","RB",None,None,None)
    rb_tier3 = add_player("RB Tier 3","RB",None,None,None)
    rb_tier4 = add_player("RB Tier 4","RB",None,None,None)
    rb_tier5 = add_player("RB Tier 5","RB",None,None,None)
    rb_tier6 = add_player("RB Tier 6","RB",None,None,None)
    rb_tier7 = add_player("RB Tier 7","RB",None,None,None)
    rb_tier8 = add_player("RB Tier 8","RB",None,None,None)
    rb_tier9 = add_player("RB Tier 9","RB",None,None,None)

    wr_tier1 = add_player("WR Tier 1","WR",None,None,None)
    wr_tier2 = add_player("WR Tier 2","WR",None,None,None)
    wr_tier3 = add_player("WR Tier 3","WR",None,None,None)
    wr_tier4 = add_player("WR Tier 4","WR",None,None,None)
    wr_tier5 = add_player("WR Tier 5","WR",None,None,None)
    wr_tier6 = add_player("WR Tier 6","WR",None,None,None)
    wr_tier7 = add_player("WR Tier 7","WR",None,None,None)
    wr_tier8 = add_player("WR Tier 8","WR",None,None,None)
    wr_tier9 = add_player("WR Tier 9","WR",None,None,None)

    te_tier1 = add_player("TE Tier 1","TE",None,None,None)
    te_tier2 = add_player("TE Tier 2","TE",None,None,None)
    te_tier3 = add_player("TE Tier 3","TE",None,None,None)
    te_tier4 = add_player("TE Tier 4","TE",None,None,None)
    te_tier5 = add_player("TE Tier 5","TE",None,None,None)
    te_tier6 = add_player("TE Tier 6","TE",None,None,None)
    te_tier7 = add_player("TE Tier 7","TE",None,None,None)

    def_tier1 = add_player("DEF Tier 1","DEF",None,None,None)
    def_tier2 = add_player("DEF Tier 2","DEF",None,None,None)
    def_tier3 = add_player("DEF Tier 3","DEF",None,None,None)
    k_tier1 = add_player("K Tier 1","K",None,None,None)
    k_tier2 = add_player("K Tier 2","K",None,None,None)
    k_tier3 = add_player("K Tier 3","K",None,None,None)

    myResult14 = QB2["fantasy_content"]["league"][1]["players"]
    for x in myResult14.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult14[x]["player"][0][5]["editorial_team_full_name"]
                position = "DEF"
                bye  = myResult14[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult14[x]["player"][0][1]["player_id"] +"/"
                team = myResult14[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult14[x]["player"][0][6]["editorial_team_full_name"]
                position = "DEF"
                bye  = myResult14[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult14[x]["player"][0][1]["player_id"] +"/"
                team = myResult14[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

def add_player(name,position,bye,url,team):
    c = Player.objects.get_or_create(name=name,position=position,bye=bye,url=url,team=team)
    return c

XMLNS = 'http://docs.openstack.org/identity/api/v2.0'

def serialize(d):
    assert len(d.keys()) == 1, 'Cannot encode more than one element'

    name = d.keys()[0]

    root = etree.Element(name, xmlns=XMLNS)

    populate_element(root, d[name])


def populate_element(element, d):
    for k, v in d.iteritems():
        if type(v) is dict:
            child = etree.Element(k)
            populate_element(child, v)
            element.append(child)
        elif type(v) is list:
            if k[-1] == 's':
                name = k[:-1]
            else:
                name = k

            for item in v:
                child = etree.Element(name)
                populate_element(child, item)
                element.append(child)

        else:
            element.set(k, unicode(v))

if __name__== '__main__':
    print "Starting populate script"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sortable.settings')
    from tiersheet.models import Player
    populate()

# Fetch a games as an example
#print '\n\nExample: All the games the user has competed in:', yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games?format=json').json()
#Gets all QBs from this season
#print '\n\nExample: All the games the user has competed in:', yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games;game_keys=nfl/players;position=QB?format=json').json()
#RBs
#players = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games;game_keys=nfl/players;position=RB;start=0;count=50?format=json').json()
#QBs = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games;game_keys=nfl/players;position=QB;start=0;count=50?format=json').json()
#24 Players
#players = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games;game_keys=nfl/players?format=json').json()
##players = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/game_keys=nfl/players?format=json').json()
#Accessing generic query (not league specific)
#myResult = players["fantasy_content"]["users"]["0"]["user"][1]["games"]["0"]["game"][1]["players"]





