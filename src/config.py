""" Global config of the app """
import dotenv as env

# App info
TITLE = 'GW By LukeCreated'
VERSION = '0.1.0'
DESCRIPTION = 'Redirector application to any given URL'

# .env
envPath = env.find_dotenv(filename='.env')
envDict = env.dotenv_values(dotenv_path=envPath)
