import os
from requests_oauthlib import OAuth1Session
import json

def populate():
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
    myResult = QB1["fantasy_content"]["league"][1]["players"]
    for x in myResult.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult[x]["player"][0][2]["name"]["full"]
                position = "QB"
                bye  = myResult[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult[x]["player"][0][1]["player_id"] +"/"
                team = myResult[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name,position,bye,url,team)

            except KeyError:
                name = myResult[x]["player"][0][2]["name"]["full"]
                position = "QB"
                bye  = myResult[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult[x]["player"][0][1]["player_id"] +"/"
                team = myResult[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

    myResult2 = QB2["fantasy_content"]["league"][1]["players"]
    for x in myResult2.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult2[x]["player"][0][2]["name"]["full"]
                position = "QB"
                bye  = myResult2[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult2[x]["player"][0][1]["player_id"] +"/"
                team = myResult2[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
            except:
                name = myResult2[x]["player"][0][2]["name"]["full"]
                position = "QB"
                bye  = myResult2[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult2[x]["player"][0][1]["player_id"] +"/"
                team = myResult2[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
    myResult3 = RB1["fantasy_content"]["league"][1]["players"]
    for x in myResult3.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult3[x]["player"][0][2]["name"]["full"]
                position = "RB"
                bye  = myResult3[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult3[x]["player"][0][1]["player_id"] +"/"
                team = myResult3[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult3[x]["player"][0][2]["name"]["full"]
                position = "RB"
                bye  = myResult3[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult3[x]["player"][0][1]["player_id"] +"/"
                team = myResult3[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

    myResult4 = RB2["fantasy_content"]["league"][1]["players"]
    for x in myResult4.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult4[x]["player"][0][2]["name"]["full"]
                position = "RB"
                bye  = myResult4[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult4[x]["player"][0][1]["player_id"] +"/"
                team = myResult4[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult4[x]["player"][0][2]["name"]["full"]
                position = "RB"
                bye  = myResult4[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult4[x]["player"][0][1]["player_id"] +"/"
                team = myResult4[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
    myResult5 = WR1["fantasy_content"]["league"][1]["players"]
    for x in myResult5.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult5[x]["player"][0][2]["name"]["full"]
                position = "WR"
                bye  = myResult5[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult5[x]["player"][0][1]["player_id"] +"/"
                team = myResult5[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult5[x]["player"][0][2]["name"]["full"]
                position = "WR"
                bye  = myResult5[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult5[x]["player"][0][1]["player_id"] +"/"
                team = myResult5[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
    myResult6 = WR2["fantasy_content"]["league"][1]["players"]
    for x in myResult6.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult6[x]["player"][0][2]["name"]["full"]
                position = "WR"
                bye  = myResult6[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult6[x]["player"][0][1]["player_id"] +"/"
                team = myResult6[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult6[x]["player"][0][2]["name"]["full"]
                position = "WR"
                bye  = myResult6[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult6[x]["player"][0][1]["player_id"] +"/"
                team = myResult6[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
    myResult7 = WR3["fantasy_content"]["league"][1]["players"]
    for x in myResult7.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult7[x]["player"][0][2]["name"]["full"]
                position = "WR"
                bye  = myResult7[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult7[x]["player"][0][1]["player_id"] +"/"
                team = myResult7[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult7[x]["player"][0][2]["name"]["full"]
                position = "WR"
                bye  = myResult7[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult7[x]["player"][0][1]["player_id"] +"/"
                team = myResult7[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
    myResult8 = TE1["fantasy_content"]["league"][1]["players"]
    for x in myResult8.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult8[x]["player"][0][2]["name"]["full"]
                position = "TE"
                bye  = myResult8[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult8[x]["player"][0][1]["player_id"] +"/"
                team = myResult8[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult8[x]["player"][0][2]["name"]["full"]
                position = "TE"
                bye  = myResult8[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult8[x]["player"][0][1]["player_id"] +"/"
                team = myResult8[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
    myResult9 = TE2["fantasy_content"]["league"][1]["players"]
    for x in myResult9.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult9[x]["player"][0][2]["name"]["full"]
                position = "TE"
                bye  = myResult9[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult9[x]["player"][0][1]["player_id"] +"/"
                team = myResult9[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult9[x]["player"][0][2]["name"]["full"]
                position = "TE"
                bye  = myResult9[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult9[x]["player"][0][1]["player_id"] +"/"
                team = myResult9[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
    myResult10 = WR4["fantasy_content"]["league"][1]["players"]
    for x in myResult10.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult10[x]["player"][0][2]["name"]["full"]
                position = "WR"
                bye  = myResult10[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult10[x]["player"][0][1]["player_id"] +"/"
                team = myResult10[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult10[x]["player"][0][2]["name"]["full"]
                position = "WR"
                bye  = myResult10[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult10[x]["player"][0][1]["player_id"] +"/"
                team = myResult10[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
    myResult11 = K1["fantasy_content"]["league"][1]["players"]
    for x in myResult11.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult11[x]["player"][0][2]["name"]["full"]
                position = "K"
                bye  = myResult11[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult11[x]["player"][0][1]["player_id"] +"/"
                team = myResult11[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult11[x]["player"][0][2]["name"]["full"]
                position = "K"
                bye  = myResult11[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult11[x]["player"][0][1]["player_id"] +"/"
                team = myResult11[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
    myResult12 = K2["fantasy_content"]["league"][1]["players"]
    for x in myResult12.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult12[x]["player"][0][2]["name"]["full"]
                position = "K"
                bye  = myResult12[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult12[x]["player"][0][1]["player_id"] +"/"
                team = myResult12[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult12[x]["player"][0][2]["name"]["full"]
                position = "K"
                bye  = myResult12[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult12[x]["player"][0][1]["player_id"] +"/"
                team = myResult12[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

    myResult13 = QB1["fantasy_content"]["league"][1]["players"]
    for x in myResult13.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult13[x]["player"][0][5]["editorial_team_full_name"]
                position = "DEF"
                bye  = myResult13[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult13[x]["player"][0][1]["player_id"] +"/"
                team = myResult13[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult13[x]["player"][0][6]["editorial_team_full_name"]
                position = "DEF"
                bye  = myResult13[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult13[x]["player"][0][1]["player_id"] +"/"
                team = myResult13[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

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

    myResult15 = RB3["fantasy_content"]["league"][1]["players"]
    for x in myResult15.keys():
        if x == "count":
            pass
        else:
            try:
                name = myResult15[x]["player"][0][2]["name"]["full"]
                position = "RB"
                bye  = myResult15[x]["player"][0][7]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult15[x]["player"][0][1]["player_id"] +"/"
                team = myResult15[x]["player"][0][6]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)

            except KeyError:
                name = myResult15[x]["player"][0][2]["name"]["full"]
                position = "RB"
                bye  = myResult15[x]["player"][0][8]["bye_weeks"]["week"]
                url  = "http://sports.yahoo.com/nfl/players/" + myResult15[x]["player"][0][1]["player_id"] +"/"
                team = myResult15[x]["player"][0][7]["editorial_team_abbr"]
                add_player(name, position, bye, url, team)
def add_player(name,position,bye,url,team):
    c = Player.objects.get_or_create(name=name,position=position,bye=bye,url=url,team=team)
    return c

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




