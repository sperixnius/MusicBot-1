"""Global configuration variables."""

########################
#   GENERAL SETTINGS   #
########################

driver = None

CHANNEL_ID = '460228909590380554'

########################
#   DISCORD SETTINGS   #
########################

DISCORD_TOKEN = 'NDYwMjExNDkxODg3NTEzNjAx.DhBc3A.Cp4cciutO1kojbscT6hk8hGmFi0'
########################
#   SPOTIFY SETTINGS   #
########################

S_CLIENT_ID = 'e564c45fbef04272bd3e71dd5f49764a'
S_CLIENT_SECRET = '4efd17b4242e4ee3823bd07dd2ee2feb'
S_REDIRECT_URI = 'https://discordapp.com/channels/@me'

S_URL = f"https://accounts.spotify.com/authorize/?" \
        f"client_id={S_CLIENT_ID}&" \
        f"response_type=code&" \
        f"redirect_uri={S_REDIRECT_URI}&" \
        f"scope=user-read-birthdate%20user-read-private%20" \
        f"user-read-email%20user-read-currently-playing&" \
        f"state=34fFs29kd09"

S_SCOPE = """user-read-birthdate
             user-read-private
             user-read-email
             user-read-currently-playing
             user-modify-playback-state"""

S_TOKEN = ''
