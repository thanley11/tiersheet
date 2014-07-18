import os
from requests_oauthlib import OAuth1Session

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
print '\n\nExample: All the games the user has competed in:', yahoo.get('http://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games?format=json').json()
