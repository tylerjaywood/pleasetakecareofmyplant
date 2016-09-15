# Make a thread in the subreddit to get input on water/don't water
import os
import praw
import sys

import config as c
import send_mails as sm
import post_templates as posts
#import gpio_out as g

REDDIT_USERNAME = 'AzureDiamond'
REDDIT_PASSWORD = 'hunter2'

# Set-up
r = c.getReddit()
sr = c.getSubReddit(r)

post_body = posts.body
post_title = posts.title

if c.checkKillSwitch() == 1:
    sys.exit()

# Post Thread
s = sr.submit(post_title, text=post_body)
s.sticky()

# Send message to everyone about the thread
broadcast_title = "Take care of my plant"
broadcast_body = "Do you want to water the plant today? [Vote here!]({})"
broadcast_body = broadcast_body.format(s.short_link)
sm.broadcast(broadcast_title, broadcast_body)

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


