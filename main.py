# For testing
# import db as db
from flask import *
from model import *


def putDB(comments):

    admin = answers(comments)
    db.session.add(admin)
    db.session.commit()

# putDB('lllllll')





# conn = MySQLdb.connect(host= "104.131.52.198.",
#                   user="root",
#                   passwd="84519851",
#                   db="DP")
#
#
# cursor = db.cursor()
# sql = "INSERT INTO answers(ans1) VALUES ('jadhfiuaeh')"
# cursor.execute(sql)
# db.commit()
# db.close()



