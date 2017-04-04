# For testing
# import db as db
from flask import *
from model import *


def putDB(ans8,ans9,ans10,ans11,ans12,ans13,ans14,ans15):

    admin = answers(ans8,ans9,ans10,ans11,ans12,ans13,ans14,ans15)
    db.session.add(admin)
    db.session.commit()
