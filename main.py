# For testing
# import db as db
from flask import *
from model import *


def putDB(comments1,comments2,comments3,comments4,comments5,comments6,comments7,comments8,comments9,comments10):

    admin = answers(comments1, comments2,comments3, comments4, comments5, comments6, comments7, comments8,comments9,comments10)
    db.session.add(admin)
    db.session.commit()
