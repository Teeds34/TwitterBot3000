#!/usr/bin/env python3
#
# TwitterBot3000
# by,
# Mike Tieden (@miketieden)
#
import tweepy
import config
import random
import time
from datetime import datetime

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.ckey, config.csecret)
auth.set_access_token(config.atoken, config.asecret)

# Create API object
api = tweepy.API(auth)

# Timestamp Format
f = "%d.%^b.%Y %H:%M:%S"

#Set Tweet Count
tc = 0

#Calculate Sleep time
sleep = config.m*60


def rt(api, screen_name):
    try:
        global tc
        tc = 0
        api.retweet(screen_name)
        t = datetime.now()
        timestamp = t.strftime(f)
        print(timestamp + " Retweeting: " + str(screen_name))
        tc = tc + 1
    except:
        pass
    

print()
print()
print(" +---------------------+")
print(" |                     |")
print(" |   TwitterBot3000    |")
print(" |                     |")
print(" +---------------------+")

time.sleep(3)
print()
print()
t = datetime.now()
timestamp = t.strftime(f)
print(timestamp + " Scanning...")
while True:
    for username in config.usernames:
        tweets = api.user_timeline(screen_name=username, count=1)
        for tweet in tweets:
                rt(api, tweet.id)
    if tc == 0:
        t = datetime.now()
        timestamp = t.strftime(f)
        print(timestamp + " No tweets found during this scan.")
    else:
        pass
    t = datetime.now()
    timestamp = t.strftime(f)
    print(timestamp + " Pausing for " + str(m) + " minutes.")
    time.sleep(sleep)
    print()
    print("New Scan")
    t = datetime.now()
    timestamp = t.strftime(f)
    print(timestamp + " Scanning...")
