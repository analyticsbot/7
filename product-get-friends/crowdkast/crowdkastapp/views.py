from flask import render_template, flash,redirect, url_for
from crowdkastapp import mypage

from authentication.models import * #.. therefore we need the auth models


from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required

## add the login required handler
@login_required
@mypage.route('/')
@mypage.route('/<username>')
def index(username=None):
    if username is None:
        return redirect(url_for('authentication.AuthenticationView:signup'))

    user = Users.query.filter_by(username=username).first()
    if user is None:
	# return to the sign up page with a message, the user does not exist
        return redirect(url_for('authentication.AuthenticationView:signup'))
    else:
        return render_template('crowdkast/index.html', page_title= user.username + " | Your friends")
