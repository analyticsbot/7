from pffriends_v1 import db

class Users(db.Model):

    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    friends = db.relationship('Friends', cascade="all, delete-orphan" , lazy='dynamic')
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def is_anonymous(self):
        return False

    def __repr__(self):
        return '<username {}'.format(self.username)


class Friends(db.Model):

    __tablename__ = 'Friends'

    id = db.Column(db.Integer, primary_key=True)
    friendname = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    img_local = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=False)
    upvotes = db.Column(db.String, nullable=False)
    made = db.Column(db.String, nullable=False)
    followers = db.Column(db.String, nullable=False)
    following = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def is_anonymous(self):
        return False

    def __repr__(self):
        return '<name {}'.format(self.friendname)

class TwitterKeys(db.Model):

    __tablename__ = 'twitterkeys'

    Username = db.Column(db.String, nullable=False)
    Password = db.Column(db.String, nullable=False)
    ConsumerKey = db.Column(db.String, nullable=False)
    ConsumerSecret = db.Column(db.String, nullable=False)
    AccessToken = db.Column(db.String, nullable=False)
    TokenSecret = db.Column(db.String, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    inUse = db.Column(db.Integer, nullable=False)

