# For testing
# import db as db
from flask import *
from model import *


def putDB(comments):

    admin = answers(comments)
    db.session.add(admin)
    db.session.commit()
