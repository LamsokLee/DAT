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

    def __init__(self, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
        # def __init__(self, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10, ans11, ans12, ans13,
        #              ans14, ans15, ans16, ans17):
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.ans5 = ans5
        self.ans6 = ans6
        self.ans7 = ans7
        self.ans8 = ans8
        self.ans9 = ans9
        self.ans10 = ans10
        # self.ans11 = ans11
        # self.ans12 = ans12
        # self.ans13 = ans13
        # self.ans14 = ans14
        # self.ans15 = ans15
        # self.ans16 = ans16
        # self.ans17 = ans17

    def __repr__(self):
        return '<User %r>' % self.ans_id





