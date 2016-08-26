from flask import render_template, request, flash, request, redirect, url_for, session, flash, g, \
     render_template

from flask.ext.classy import FlaskView, route
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from models import *
from crowdkastapp.authentication import authentication
from crowdkastapp import application
import md5, os
from flask_oauth import OAuth
from flask_oauthlib.client import OAuth
import datetime
from crowdkastapp.email import send_email

oauth = OAuth(application)

twitter = oauth.remote_app(
    'twitter',
    consumer_key=application.config['CONSUMER_KEY'],
    consumer_secret=application.config['CONSUMER_SECRET'],
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
)

@twitter.tokengetter
def get_twitter_token():
    if 'twitter_oauth' in session:
        resp = session['twitter_oauth']
        return resp['oauth_token'], resp['oauth_token_secret']

@application.before_request
def before_request():
    g.user = None
    if 'twitter_oauth' in session:
        g.user = session['twitter_oauth']

facebook = oauth.remote_app(
    'facebook',
    consumer_key=application.config['FACEBOOK_APP_ID'],
    consumer_secret=application.config['FACEBOOK_APP_SECRET'],
    request_token_params={'scope': 'email'},
    base_url='https://graph.facebook.com',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    access_token_method='GET',
    authorize_url='https://www.facebook.com/dialog/oauth'
)

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

## method to hash the password before storing in db. Never ever store passwords as it is. 
def hash_string(string):
    password_hash = string
    return password_hash
    #return md5.new(password_hash).hexdigest()

class AuthenticationView(FlaskView):
    @route('signin', methods=['GET', 'POST'])
    def signin(self):
        return render_template('signin.html', page_title='Sign In')
    
    
    @route('twitterlogin', methods=['GET', 'POST'])
    def twitterlogin(self):
        """Calling into authorize will cause the OpenID auth machinery to kick
        in.  When all worked out as expected, the remote application will
        redirect back to the callback URL provided.
        """
        return twitter.authorize(callback=url_for('authentication.AuthenticationView:oauthorized',
            next=request.args.get('next') or request.referrer or None))

    @route('oauthorized', methods=['GET', 'POST'])
    def oauthorized(self):
        resp = twitter.authorized_response()
        username = resp['screen_name']
        if resp is None:
            flash('You denied the request to sign in.')
        else:
            session['twitter_oauth'] = resp
            session['login_method'] = 'twitter'
            
        login_user(username)
        return redirect(url_for('mypage.index', username = username))

##    @route('twitterlogout', methods=['GET', 'POST'])
##    def logout():
##        session.pop('user_id', None)
##        flash('You were signed out')
##        return redirect(request.referrer or url_for('mypage.index'))

    @route('logout')
    @login_required
    def logout(self):
        session.clear()
        logout_user()
        return redirect(url_for('mypage.index'))

    @route('facebooklogin', methods=['GET', 'POST'])
    def facebooklogin(self):
        callback = url_for(
            'authentication.AuthenticationView:facebook_authorized',
            next=request.args.get('next') or request.referrer or None,
            _external=True
        )
        return facebook.authorize(callback='http://localhost:8000/')

    @route('authorized')
    def facebook_authorized(self):
        resp = facebook.authorized_response()
        if resp is None:
            return 'Access denied: reason=%s error=%s' % (
                request.args['error_reason'],
                request.args['error_description']
            )
        if isinstance(resp, OAuthException):
            return 'Access denied: %s' % resp.message

        session['oauth_token'] = (resp['access_token'], '')
        me = facebook.get('/me')
        return 'Logged in as id=%s name=%s redirect=%s' % \
            (me.data['id'], me.data['name'], request.args.get('next'))

    
        return redirect(url_for('mypage.index'))
    
    @route('signup', methods=['GET', 'POST'])
    def signup(self):
        return render_template('signup.html',
                               title='Signup')

AuthenticationView.register(authentication)
