from flask_sqlalchemy import SQLAlchemy
from config import app

# create an instance of SQLAlchemy class with the Flask object as the parameter
db = SQLAlchemy(app)


# the class to store all the attribute of one session
# class session(db.Model):
#     session_id = db.Column(db.String(1000),primary_key=True,autoincrement=True)
#     email = db.Column(db.String(254))
#     start = db.Column(db.DateTime)
#     end = db.Column(db.DateTime)
#     ans1 = db.Column(db.String(1000))
#     ans2 = db.Column(db.String(1000))
#     ans3 = db.Column(db.String(1000))
#     ans4 = db.Column(db.String(1000))
#     ans5 = db.Column(db.String(1000))
#     ans6 = db.Column(db.String(1000))
#     ans7 = db.Column(db.String(30))
#     ans8 = db.Column(db.String(1000))
#     ans9 = db.Column(db.String(1000))
#     ans10 = db.Column(db.String(1000))
#     ans11 = db.Column(db.String(1000))
#     ans12 = db.Column(db.String(1000))
#     ans13 = db.Column(db.String(1000))
#     ans14 = db.Column(db.String(1000))
#     ans15 = db.Column(db.String(1000))
#     ans16 = db.Column(db.Integer)

# class visit(db.Model):
#     ref_num = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(254))
#     start_time = db.Column(db.DateTime)
#     end_time = db.Column(db.DateTime)
#     is_finished = db.Column(db.Boolean)
#     answers = db.relationship('answer', backref='visit', lazy='dynamic')
#
#     def __init__(self):
#         return
#
#     def __repr__(self):
#         return '<visit %r>' % self.ref_num
#
#
# # the class to store all the answers from user
# class answer(db.Model):
#     ans_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     ans1 = db.Column(db.String(1000))
#     ans2 = db.Column(db.String(1000))
#     ans3 = db.Column(db.String(1000))
#     ans4 = db.Column(db.String(1000))
#     ans5 = db.Column(db.String(1000))
#     ans6 = db.Column(db.String(1000))
#     ans7 = db.Column(db.String(30))
#     ans8 = db.Column(db.String(1000))
#     ans9 = db.Column(db.String(1000))
#     ans10 = db.Column(db.String(1000))
#     ans11 = db.Column(db.String(1000))
#     ans12 = db.Column(db.String(1000))
#     ans13 = db.Column(db.String(1000))
#     ans14 = db.Column(db.String(1000))
#     ans15 = db.Column(db.String(1000))
#     ans16 = db.Column(db.Integer)
#     ref_num = db.Column(db.Integer, db.ForeignKey('visit.ref_num'))
#

# class read():
#     accordion1 = False
#     accordion2 = False
#     accordion3 = False
#     accordion4 = False
#     accordion5 = False
#     accordion6 = False
#     accordion7 = False
#     accordion8 = False
#     accordion9 = False
#     accordion10 = False
#
#     def __init__(self):
#         return
#
#     def __repr__(self):
#         return '<answer %r>' % self.ans_id
