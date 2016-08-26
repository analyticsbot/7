from collections import OrderedDict
from crowdkastapp import db


class Users(db.Model, object):

    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)

    mode_signup = db.Column(db.Integer)
    friends = db.relationship('Friends')
    
       
    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result


class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    friend_username = db.Column(db.Text)
    profile_pic = db.Column(db.Text)
    user_id = db.Column(db.Text)
    profile_desc = db.Column(db.Text)
    upvotes = db.Column(db.Text)
    made = db.Column(db.Text)
    followers = db.Column(db.Text)
    following = db.Column(db.Text)

    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result

