#!/usr/bin/env python3

import json
from datetime import datetime
from time import sleep

from praw import Reddit

import scheduler

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

subreddit = reddit.subreddit('Uruguay_beta')


def schedulePost(title, body=None, sticky=False):
    post = subreddit.submit(title, selftext=body)
    if sticky:
        post.mod.sticky()


def auto_unsticky():
    username = reddit.user.me().name
    for post in subreddit.search(query='author:{}'.format(username),
                                 time_filter='week'):
        created_date = datetime.fromtimestamp(post.created)
        midnight = datetime.now().replace(hour=0, minute=0, second=0,
                                          microsecond=0)
        if created_date <= midnight:
            post.mod.sticky(False)


scheduler.every().day.at('00:00').do(auto_unsticky)

scheduler.every().friday.at('09:00').do(
    schedulePost, title='UPT: Uruguay Pro Tips')

scheduler.every().saturday.at('09:00').do(
    schedulePost, title='Sabado de deportes')

scheduler.every().sunday.at('09:00').do(
    schedulePost, title='Domingo de noticias y politica')

while True:
    scheduler.run_pending()
    sleep(60)
