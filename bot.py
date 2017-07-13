import praw
import json
import datetime
import time

if time.strftime("%d/%m/%Y") == open("/Users/jblanco/reddit-bot/last_run",'r').read():
    exit()
else:
    f = open("/Users/jblanco/reddit-bot/last_run",'w')
    f.write(time.strftime("%d/%m/%Y"))


json_str = open("/Users/jblanco/reddit-bot/params.json",'r').read()
params = json.loads(json_str)

reddit = praw.Reddit(client_id='YRLrk60hAOy0IA',
                     client_secret= params['client_secret'],
                     user_agent= 'uruguay-bot-user-agent',
                     username= params['username'],
                     password= params['password'])

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
