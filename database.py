import datetime

from flask import session, request
from flask_sqlalchemy import SQLAlchemy
from config import app

# create an instance of SQLAlchemy class with the Flask object as the parameter
db = SQLAlchemy(app)


def commitdb():
    if session['ref_num'] != -1:
        # session exists
        session['end'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.engine.execute(
            "UPDATE session SET end  = '" + session['end'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET email  = '" + session['email'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET end    = '" + session['end'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans1   = '" + session['ans1'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans2   = '" + session['ans2'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans3   = '" + session['ans3'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans4   = '" + session['ans4'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans5   = '" + session['ans5'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans6   = '" + session['ans6'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans7   = '" + session['ans7'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans8   = '" + session['ans8'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans9   = '" + str(session['ans9']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans10  = '" + session['ans10'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans11  = '" + session['ans11'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans12  = '" + session['ans12'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans13  = '" + session['ans13'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans14  = '" + session['ans14'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans15  = '" + session['ans15'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans16  = '" + str(session['ans16']) + "' WHERE session_id = " + str(session['ref_num']))
    else:
        ex = db.engine.execute("INSERT INTO session (start) VALUES ('" + session['start'] + "')")
        session['ref_num'] = ex.lastrowid
        session['end'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.engine.execute(
            "UPDATE session SET email  = '" + session['email'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET end    = '" + session['end'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans1   = '" + session['ans1'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans2   = '" + session['ans2'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans3   = '" + session['ans3'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans4   = '" + session['ans4'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans5   = '" + session['ans5'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans6   = '" + session['ans6'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans7   = '" + session['ans7'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans8   = '" + session['ans8'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans9   = '" + str(session['ans9']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans10  = '" + session['ans10'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans11  = '" + session['ans11'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans12  = '" + session['ans12'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans13  = '" + session['ans13'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans14  = '" + session['ans14'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans15  = '" + session['ans15'] + "' WHERE session_id = " + str(session['ref_num']))
        # db.engine.execute(
        #     "UPDATE session SET ans16  = '" + str(session['ans16']) + "' WHERE session_id = " + str(session['ref_num']))
    return
