from flask_sqlalchemy import SQLAlchemy
from config import app


db = SQLAlchemy(app)

class answers(db.Model):
    ans_id = db.Column(db.Integer, primary_key=True)
    ans1 = db.Column(db.String(150))
    ans2 = db.Column(db.String(150))
    ans3 = db.Column(db.String(150))
    ans4 = db.Column(db.String(150))
    ans5 = db.Column(db.String(150))
    ans6 = db.Column(db.String(150))
    ans7 = db.Column(db.Integer)
    ans8 = db.Column(db.String(150))
    ans9 = db.Column(db.String(150))
    ans11 = db.Column(db.String(150))
    ans12 = db.Column(db.String(150))
    ans13 = db.Column(db.String(150))
    ans14 = db.Column(db.String(150))
    ans15 = db.Column(db.String(150))
    ans16 = db.Column(db.Integer)
    ans17 = db.Column(db.String(150))

    def __init__(self):
        return

    def __repr__(self):
        return '<User %r>' % self.ans_id





