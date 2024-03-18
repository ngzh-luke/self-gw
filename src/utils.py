""" Global utilities functions """

from fastapi.templating import Jinja2Templates
from config import ALGORITHMS
from random import choice


# Template
TEMPLATES = Jinja2Templates(directory="templates")


def getALG(algorithmsList: list | str = ALGORITHMS) -> str:  # Algorithm related function
    """ Return 1 of the default or given algorithms list """
    if type(ALGORITHMS) == list:
        return str(choice(algorithmsList))
    elif type(ALGORITHMS) == str:
        return algorithmsList
    else:
        return "HS256"
