# Make a thread in the subreddit to get input on water/don't water 
import os
import praw
import sys

import config as c
import post_templates as posts
#import gpio_out as g

REDDIT_USERNAME = 'takecareofmyplant'
REDDIT_PASSWORD = 'hunter2'

# Either False or an integer
LIMIT_RETRIES = 18
# If LIMIT_RETRIES, the commands to execute
# Note: this example sucks as a contingency plan 
CONTINGENCY_PLAN = (
"""try:
    q = c.checkKillSwitch()
    print("Internet exists, must be a Reddit issue.")
except Exception as e:
    print("No internet connection exists.\nDetails:\n"+str(e.args))
""")

# Set-up

# Check for internet
from time import sleep
count = 0
while True:
    try:
        r = c.getReddit()
        break
    except Exception as e:
        print("An error occurred connecting to Reddit. Trying again in 10 minutes.\nDetails:\n"+str(e.args))
        sleep(600)
        if count < LIMIT_RETRIES:
            count += 1
        elif LIMIT_RETRIES:
            exec(CONTINGENCY_PLAN)
            break
del sleep

sr = c.getSubReddit(r)

post_body = posts.body
post_title = posts.title

if c.checkKillSwitch() == 1:
    sys.exit()

# Post Thread
s = sr.submit(post_title, text=post_body)
s.sticky()

# Logging
path_prefix = c.pathPrefix()

with open(path_prefix+'daily_thread.txt', 'w') as f:
    f.write(s.id)
    f.close()

with open(path_prefix+'topup.txt', 'r+') as f:
    x = f.read()
    if x == '1':
      g.on_off(10)
      True

# Reset continuous comment files
with open(path_prefix+'/continuous_tally/cont_comment_log.txt', 'w') as f:
    f.write('')
    f.close()
    
with open(path_prefix+'/continuous_tally/cont_comment_id.txt', 'w') as f:
    f.write('')
    f.close()


