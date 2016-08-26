import hashlib, sqlite3, tweepy, requests, time
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from threading import Thread
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

def checkPH(name, driver):
    url = 'https://www.producthunt.com/@'+name
    driver.get(url)
    time.sleep(3)
    exists = 0
    data_user = []
    if 'profile on Product Hunt' in driver.title:
        try:
            name = driver.find_element_by_tag_name('h1').text.split('#')[0]
        except:
            name = ''
        try:
            user_id = '#'+driver.find_element_by_tag_name('h1').text.split('#')[1]
        except:
            user_id = ''
        try:
            img = driver.find_element_by_tag_name('img').get_attribute('src')
        except:
            img = ''
        try:
            bio = driver.find_element_by_tag_name('h2').text
        except:
            bio = ''
        upvotes = ''
        made = ''
        followers = ''
        following = ''
        try:
            navtags = driver.find_elements_by_tag_name('li')
            try:
                for nav in navtags:
                    if 'Upvotes' in nav.text:
                        upvotes = nav.text.split('\n')[0]
            except:
                upvotes = ''
            try:
                for nav in navtags:
                    if 'Made' in nav.text:
                        made = nav.text.split('\n')[0]
            except:
                made = ''
            try:
                for nav in navtags:
                    if 'Followers' in nav.text:
                        followers = nav.text.split('\n')[0]
            except:
                followers = ''
            try:
                for nav in navtags:
                    if 'Following' in nav.text:
                        following = nav.text.split('\n')[0]
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
driver = webdriver.Firefox()
print checkPH('gauravbhogale',driver)
print checkPH('dharmu89', driver)
print checkPH('gauravsha93', driver)


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
