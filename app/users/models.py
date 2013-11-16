import datetime
from app import db


class User(db.Model):
    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    vk_id = db.Column(db.String(80), unique=True)
    access_token = db.Column(db.String(80))
    expires = db.Column(db.DateTime)
    groups = db.relationship('Group', backref='user', lazy='dynamic') 

    def is_expired(self):
        if datetime.datetime.now() > self.expires:
            return True
        else:
            return False


class AdminUser(db.Model):
    __tablename__ = 'users_admin_user'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))