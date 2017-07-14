import json
import time
from datetime import datetime

from praw import Reddit


try:
    with open('config.json', 'r') as config_data:
        config = json.load(config_data)
except FileNotFoundError:
    print('Could not find config.json file')

reddit = Reddit(username=config.get('username'),
                password=config.get('password'),
                client_id=config.get('client_id'),
                client_secret=config.get('client_secret'),
                user_agent=config.get('user-agent', 'uruguay-bot-user-agent'))


if time.strftime("%d/%m/%Y") == open("/Users/jblanco/reddit-bot/last_run",'r').read():
    exit()
else:
    f = open("/Users/jblanco/reddit-bot/last_run",'w')
    f.write(time.strftime("%d/%m/%Y"))


today_index = datetime.datetime.today().weekday()

subr = reddit.subreddit('Uruguay_beta')
if today_index == 0:
    #tengo que agregar el sticky de hoy
    subr.submit('Lunes de RANT2', selftext='Some text').mod.sticky()
else:
    #si hay un sticky del lunes, hay que removerlo
    for s in subr.submissions():
        if s.title == "Lunes de RANT2":
            s.mod.sticky(False)
