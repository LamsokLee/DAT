from flask_sqlalchemy import SQLAlchemy
from config import app

db = SQLAlchemy(app)

# the class to store all the answers from user
class answers(db.Model):
    ans_id  = db.Column(db.Integer, primary_key=True)
    ans1    = db.Column(db.String(150))
    ans2    = db.Column(db.String(150))
    ans3    = db.Column(db.String(150))
    ans4    = db.Column(db.String(150))
    ans5    = db.Column(db.String(150))
    ans6    = db.Column(db.String(150))
    ans7    = db.Column(db.Integer)
    ans8    = db.Column(db.String(150))
    ans9    = db.Column(db.String(150))
    ans11   = db.Column(db.String(150))
    ans12   = db.Column(db.String(150))
    ans13   = db.Column(db.String(150))
    ans14   = db.Column(db.String(150))
    ans15   = db.Column(db.String(150))
    ans16   = db.Column(db.Integer)

    def __init__(self):
        return

    def __repr__(self):
        return '<User %r>' % self.ans_id

# the class to store all the attribute of one session
class session(db.Model):
    ref_num     = db.Column(db.Integer, primary_key=True)
    ans_id      = db.Column(db.Integer)
    email       = db.Column(db.String(254))
    start_time  = db.Column(db.DateTime)
    is_finished = db.Column(db.Boolean)

    def __init__(self):
        return

    def __repr__(self):
        return '<User %r>' % self.ref_num