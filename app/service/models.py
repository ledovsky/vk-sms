# -*- coding: utf-8 -*-

from app import db


class Group(db.Model):
    #User
    __tablename__ = "service_groups"
    id = db.Column(db.Integer, primary_key=True)
    vk_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    user_status = db.Column(db.String(50))
    numbers = db.relationship('Number', backref='group', lazy='dynamic')
    active = db.Column(db.Boolean)
    #sending settings
    send_first_line = db.Column(db.Boolean)

    def __init__(self, *args, **kwargs):
        super(Group, self).__init__(*args, **kwargs)
        self.active = False
        self.send_first_line = False


class Number(db.Model):
    __tablename__ = "service_numbers"
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('service_groups.id'))
    number = db.Column(db.String(50))
    comment = db.Column(db.String(250))
    # sendings = db.relationship('Sending', backref='number', lazy='dynamic')


# class Post(db.Model):
#     __tablename__ = "service_posts"
#     id = db.Column(db.Integer, primary_key=True)
#     sendings = db.relationship('Sending', backref='post', lazy='dynamic')


# class Sending(db.Model):
#     __tablename__ = "service_sendings"
#     id = db.Column(db.Integer, primary_key=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
#     number_id = db.Column(db.Integer, db.ForeignKey('number.id'))
