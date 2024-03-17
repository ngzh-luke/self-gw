""" Global config of the app """

import dotenv as env
from fastapi.templating import Jinja2Templates

# App info
TITLE = 'GW By LukeCreated'
VERSION = '0.1.2'
DESCRIPTION = 'Redirector application to any given URL'

# .env
envPath = env.find_dotenv(filename='.env')
envDict = env.dotenv_values(dotenv_path=envPath)

# Template
TEMPLATES = Jinja2Templates(directory="templates")
