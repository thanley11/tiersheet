import os
from requests_oauthlib import OAuth1Session
import json

key = os.environ['YAHOO_CONSUMER_KEY']
secret = os.environ['YAHOO_SECRET_KEY']

# OAuth URLs given on the application page
request_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
authorization_base_url = 'https://api.login.yahoo.com/oauth/v2/request_auth'
access_token_url = 'https://api.login.yahoo.com/oauth/v2/get_token'

#Use any redirect page here, you  leave it as it, we just need extract the query params (see below)
yahoo = OAuth1Session(key, client_secret=secret, callback_uri='www.tcharleshanley.com')

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
QBA = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=QB;sort=OR;start=0?format=json').json()
QBB = yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/league/331.l.249215/players;position=QB;sort=OR;start=25?format=json').json()


#data = json.dumps(QBA, sort_keys=True, indent=4, separators=(',', ': '))
#print data

myResult = QBA["fantasy_content"]["league"][1]["players"]
for x in myResult.keys():
    if x == "count":
        pass
    else:
        try:
            print myResult[x]["player"][0][2]["name"]["full"]+", " + myResult[x]["player"][0][7]["bye_weeks"]["week"]
        except KeyError:
            print myResult[x]["player"][0][2]["name"]["full"]+", " + myResult[x]["player"][0][8]["bye_weeks"]["week"]

myResult2 = QBB["fantasy_content"]["league"][1]["players"]
for x in myResult2.keys():
    if x == "count":
        pass
    else:
        try:
            print myResult2[x]["player"][0][2]["name"]["full"]+", " + myResult2[x]["player"][0][7]["bye_weeks"]["week"]
        except KeyError:
            print myResult2[x]["player"][0][2]["name"]["full"]+", " + myResult2[x]["player"][0][8]["bye_weeks"]["week"]


