# For testing
# import db as db
from flask import *
from model import *


# def saveData3(ans8, ans9, ans10, ans11, ans12, ans13, ans14, ans15):
#     vans8 = ans8
#     vans9 = ans9
#     vans10 = ans10
#     vans11 = ans11
#     vans12 = ans12
#     vans13 = ans13
#     vans14 = ans14
#     vans15 = ans15


def putDB(data):
    db.session.add(data)
    db.session.commit()
