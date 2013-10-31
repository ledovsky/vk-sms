# -*- coding: utf-8 -*-

# from app import db


# class Group(db.Model):
#     #User
#     __tablename__ = "service_groups"
#     id = db.Column(db.Integer, primary_key=True)
#     vk_id = db.Column(db.Integer)
#     numbers = db.relationship('Number', backref='group', lazy='dynamic')


# class Number(db.Model):
#     __tablename__ = "service_numbers"
#     id = db.Column(db.Integer, primary_key=True)
#     group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
#     number = db.Column(db.String(50))
#     comment = db.Column(db.String(250))
#     sendings = db.relationship('Sending', backref='number', lazy='dynamic')


# class Post(db.Model):
#     __tablename__ = "service_posts"
#     id = db.Column(db.Integer, primary_key=True)
#     sendings = db.relationship('Sending', backref='post', lazy='dynamic')


# class Sending(db.Model):
#     __tablename__ = "service_sendings"
#     id = db.Column(db.Integer, primary_key=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
#     number_id = db.Column(db.Integer, db.ForeignKey('number.id'))
