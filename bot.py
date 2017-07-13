import praw
import json

json_str = open("params.json",'r').read()
params = json.loads(json_str)

reddit = praw.Reddit(client_id='YRLrk60hAOy0IA',
                     client_secret= params['client_secret'],
                     user_agent= 'uruguay-bot-user-agent',
                     username= params['username'],
                     password= params['password'])

reddit.subreddit('Uruguay_beta').submit('Some title', selftext='Some text').mod.distinguish(sticky=True)
