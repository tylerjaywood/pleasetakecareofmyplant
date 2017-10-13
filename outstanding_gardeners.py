import os
import praw
import sys

import config as c

from collections import Counter

path = c.pathPrefix()

r = c.getReddit()

with open(path+'history.txt', 'r+') as f:
    x = f.readlines()

last_seven = x[-7:]

last_seven = [x.split(',')[2].strip() for x in last_seven]

print(last_seven)

def getResponders(thread):
    s = r.get_submission(submission_id = thread)
    s.replace_more_comments(limit = None, threshold = 0)
    comments = s.comments

    name_list = []
    for x in comments:
       try: 
            name_list.append( x.author.name)
       except:
            continue
    return set(name_list)

name_list = []
for x in last_seven:
    s = r.get_submission(submission_id = x)
    name_list += getResponders(x)

foo = Counter(name_list)

outstanding = []
for x in set(name_list):
    if foo[x] >= 6:
        outstanding.append(x)

print outstanding

for x in outstanding:
    r.get_subreddit('takecareofmyplant').set_flair(x, 'Outstanding Gardener', '')
