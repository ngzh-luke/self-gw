""" Global config of the app """

import dotenv as env

# App info
TITLE = 'GW By LukeCreated'
VERSION = '0.1.4'
DESCRIPTION = 'Redirector application to any given URL'
ISSUER = "https://gw.lukecreated.com"
AUDIENCE = "https://gw.lukecreated.com/auth"

# .env
envPath = env.find_dotenv(filename='.env')
envDict = env.dotenv_values(dotenv_path=envPath)

# handle def values for .env
try:
    SECRET_KEY = envDict['SECRET_KEY']
except KeyError:
    SECRET_KEY = "c9b0fb4504ca8631f65742429424b802"  # 16 bytes hex encoded value
try:
    ALGORITHMS = envDict['ALGORITHMS_LIST']  # algorithms used
except KeyError:
    ALGORITHMS = ['HS256', 'HS512', 'RS256', 'RS512']
try:
    ACCESS_TOKEN_VALID_PERIOD_IN_MINS = int(
        envDict['ACCESS_TOKEN_VALID_PERIOD_IN_MINS'])
except KeyError:
    ACCESS_TOKEN_VALID_PERIOD_IN_MINS = 30
try:
    REDISHOST = envDict['REDISHOST']
except KeyError:
    print("'REDISHOST' key is referenced but not defined")
    exit(code=1)
try:
    REDISPASSWORD = envDict['REDISPASSWORD']
except KeyError:
    print("'REDISPASSWORD' key is referenced but not defined")
    exit(code=1)
try:
    REDISPORT = envDict['REDISPORT']
except KeyError:
    print("'REDISPORT' key is referenced but not defined")
    exit(code=1)
try:
    REDISUSER = envDict['REDISUSER']
except KeyError:
    print("'REDISUSER' key is referenced but not defined")
    exit(code=1)

# fake credentials
credentials = {
    "luke": {
        'username': 'luke',
        'hased_password': "",
        'disabled': False
    }
}
