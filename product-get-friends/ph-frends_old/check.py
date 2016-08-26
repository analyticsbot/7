import hashlib, sqlite3, tweepy, requests, time
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from threading import Thread
from bs4 import BeautifulSoup
import pandas as pd

def checkPH(name):
    url = 'https://www.producthunt.com/@'+name
    resp = requests.get(url)
    print resp.status_code
    exists = 0
    data_user = []
    if 'profile on Product Hunt' in resp.text:
        soup = BeautifulSoup(resp.text)
        try:
            name = soup.find(attrs = {'class':'page-header--title'}).getText()
        except:
            name = ''
        try:
            user_id = soup.find(attrs = {'class':'page-header--id'}).getText()
        except:
            user_id = ''
        try:
            img = soup.find(attrs = {'class':'page-header--avatar'}).find('img')['src']
        except:
            img = ''
        try:
            bio = soup.find(attrs = {'class':'page-header--subtitle'}).getText()
        except:
            bio = ''
        try:
            navtags = soup.findAll(attrs = {'class':'page-header--navigation--tab'})
            try:
                upvotes = navtags[0].find('strong').getText()
            except:
                upvotes = ''
            try:
                made = navtags[1].find('strong').getText()
            except:
                made = ''
            try:
                followers = navtags[2].find('strong').getText()
            except:
                followers = ''
            try:
                following = navtags[3].find('strong').getText()
            except:
                following = ''
        except:
            upvotes = ''
            made = ''
            followers = ''
            following = ''
        
        data_user.append(name)
        data_user.append(user_id)
        data_user.append(img)
        try:
            img_local = download_file(img, user_id)
        except:
            img_local = ''
        data_user.append(img_local)
        data_user.append(bio)
        data_user.append(upvotes)
        data_user.append(made)
        data_user.append(followers)
        data_user.append(following)
        exists = 1
    return exists, data_user

print checkPH('gauravbhogale')
print checkPH('dharmu89')
print checkPH('gauravsha93')

access_token = "700557896677875713-GY6Dg12eZhw94iASBoqbPOy1eZdDHzL"
access_token_secret = "Nbh8FTPhO1yT69lpgx82FNXYQkaLT2aGBhOaKT5qdi0Iw"
consumer_secret = "Qi4N4I1MTEtlDkWK112dEGCu9ZT2ot6fSzIQNDe8UyAo1xU5IX"
consumer_key = "3gKCZwdPDbigcJyMvS3A86kB7"
'''
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit_notify = True, wait_on_rate_limit=True)

user_name = 'i__Ravi'

users = tweepy.Cursor(api.followers, screen_name=user_name).items()
screen_names = []

while True:
    try:
        twitter_friends = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        twitter_friends = next(users)
    except StopIteration:
        break
    print twitter_friends.screen_name
    screen_names.append(twitter_friends.screen_name)

for name in screen_names:
    time.sleep(1)
    exists, data_user = checkPH(name)
    print data_user
'''
