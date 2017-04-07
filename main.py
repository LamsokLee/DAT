from model import *

def putDB(data,sess):
    db.session.add(data)
    db.session.add(sess)
    db.session.commit()
