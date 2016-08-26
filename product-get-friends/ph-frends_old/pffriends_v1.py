from flask import Flask, render_template, request, flash, session, url_for, redirect
from flask.ext.login import login_user, login_required, logout_user, LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
import hashlib, sqlite3, tweepy, requests, time
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from threading import Thread
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from text_unidecode import unidecode

try:
    from pyvirtualdisplay import Display
    from selenium import webdriver

    display = Display(visible=0, size=(800, 600))
    display.start()
except:
    pass
app = Flask(__name__)

# config
app.secret_key = 'my precious'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECURITY_PASSWORD_SALT'] = 'somepassword'

# create the sqlalchemy object
db = SQLAlchemy(app)

# email server
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = 'product.hunt.bot12@gmail.com'  ## CHANGE THIS
app.config["MAIL_PASSWORD"] = 'producthunt1234'

# create the mail object
mail = Mail(app)

# administrator list
ADMIN = 'product.hunt.bot12@gmail.com'

# import db schema. this should always be done after initializing the app
from models import *

def getFriends(user_name, email, app, mail):
    ## access tokens from twitter
    access_token = "700557896677875713-GY6Dg12eZhw94iASBoqbPOy1eZdDHzL"
    access_token_secret = "Nbh8FTPhO1yT69lpgx82FNXYQkaLT2aGBhOaKT5qdi0Iw"
    consumer_secret = "Qi4N4I1MTEtlDkWK112dEGCu9ZT2ot6fSzIQNDe8UyAo1xU5IX"
    consumer_key = "3gKCZwdPDbigcJyMvS3A86kB7"

    tkeys = TwitterKeys.query.filter_by(inUse = 0).first()
    access_token = tkeys.AccessToken
    access_token_secret = tkeys.TokenSecret
    consumer_secret = tkeys.ConsumerSecret
    consumer_key = tkeys.ConsumerKey

    tkeys.inUse = 1
    db.session.commit()

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit_notify = True, wait_on_rate_limit=True)
    
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

    df = pd.DataFrame(columns = ['Username', 'id', 'image_url', 'bio', '#upvotes', '#made', '#followers', '#following'])

    driver = webdriver.Firefox()
    for name in screen_names:
        time.sleep(1)
        exists, data_user = checkPH(name, driver)
        if exists:            
            
            try:
                user = Users.query.filter_by(username = user_name).first()
                users_id = user.id
            except:
                user = Users()
                user.username = user_name
                db.session.add(user)
                db.session.commit()
                users_id = user.id
            name_, user_id, img, img_local, bio, upvotes, made, followers, following = data_user
            print 'Adding user to friends' , unidecode(name_)
            user.friends.append(
                            Friends(friendname=name_,\
                                    bio = bio,
                                    img = img,
                                    img_local = img_local,
                                    user_id = user_id,
                                    upvotes = upvotes,
                                    made = made,
                                    users_id = users_id,
                                    followers = followers,
                                    following = following))
            nrows = df.shape[0]
            df.loc[nrows+1] = [name_, user_id, img, bio, upvotes, made, followers, following]
            db.session.commit()
    df.to_csv(user_name+'_friends_on_ph.csv', index = False)
    driver.close()
    url = 'http://127.0.0.1:5000/friends/'+user_name.replace('@','')
    msg = Message("Your friend list if ready", sender = ADMIN, recipients = [email])        
    msg.html = "<p>Hello " + user_name + ", <br> Thank you. Please click on " + url + " to see your friends <br>Regards,<br>Admin</p>"
    try:
        with app.open_resource(user_name+'_friends_on_ph.csv') as fp:
            msg.attach(user_name+'_friends_on_ph.csv', "text/csv", fp.read())
    except:
        pass

    with app.app_context():
       mail.send(msg)
    tkeys.inUse = 0
    db.session.commit()
        
def download_file(url, id):
    """ function to download the files to local"""
    r = requests.get(url, stream=True)
    with open('images//'+ str(id) + '.jpg', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return 'images//'+ str(id) + '.jpg'

def checkPH(name, driver):
    url = 'https://www.producthunt.com/@'+name
    print url
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
        
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/friends/<user>", methods =['GET'])
def profile(user=None):
    user = Users.query.filter_by(username=user).first()
    if user:
        id = user.id
        friends = Friends.query.filter_by(users_id=id).all()
        return render_template('profile.html', user = user.username, friends = friends)
    return render_template('index.html')
    
@app.route("/go", methods = ['GET', "POST"])
def go():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        if '@' not in username:
            user = username
        elif '@' in username:
            user = username.replace('@','')
        print user, email
        if user != '':
            threads= []
            threads.append(Thread(target = getFriends, args=(user,email,app, mail, )))
     
            for t in threads:
                t.start()
                print 'thread started'

            return render_template('wait.html', username = username.replace('@',''))
 
        return render_template('index.html', username = username) 
        
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
