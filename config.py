import os
from getpass import getuser
import requests

import praw

from secret import user_agent, password, weather_api, zipcode, test_sub

# PRAW
user_name = 'takecareofmyplant'
subreddit = 'takecareofmyplant'
mailing_list_id = "GoogleId"

def getReddit():
    r = praw.Reddit(user_agent=user_agent)
    r.login(user_name, password)
    return r

def getSubReddit(Reddit, test=False):
    sub = test_sub if test else subreddit
    sr = Reddit.get_subreddit(sub)
    return sr

# Files
def pathPrefix():
    pi = '/home/pi/pleasetakecareofmyplant/'
    tyler = '/Users/tyler_wood/personal/pleasetakecareofmyplant/'
    user = getuser()
    path = tyler if user == 'tyler_wood' else pi
    return path

# Kill Switch
def checkKillSwitch():
    url = "http://www.pleasetakecareofmyplant.com/killswitch.html"
    r = requests.get(url)
    check = int(r.content)
    return check



