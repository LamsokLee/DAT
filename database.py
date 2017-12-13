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
            "UPDATE session SET ans1   = '" + str(session['ans1']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans2   = '" + str(session['ans2']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans3   = '" + str(session['ans3']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans4   = '" + str(session['ans4']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans5   = '" + str(session['ans5']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans6   = '" + str(session['ans6']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans7   = '" + str(session['ans7']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans8   = '" + str(session['ans8']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans9   = '" + str(session['ans9']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans10  = '" + session['ans10'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET opt1  = '" + str(session['opt1']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET opt2  = '" + str(session['opt2']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET opt3  = '" + str(session['opt3']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET opt4  = '" + str(session['opt4']) + "' WHERE session_id = " + str(session['ref_num']))

    else:
        ex = db.engine.execute("INSERT INTO session (start) VALUES ('" + session['start'] + "')")
        session['ref_num'] = ex.lastrowid
        session['end'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.engine.execute(
            "UPDATE session SET email  = '" + session['email'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET end    = '" + session['end'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans1   = '" + str(session['ans1']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans2   = '" + str(session['ans2']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans3   = '" + str(session['ans3']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans4   = '" + str(session['ans4']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans5   = '" + str(session['ans5']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans6   = '" + str(session['ans6']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans7   = '" + str(session['ans7']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans8   = '" + str(session['ans8']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans9   = '" + str(session['ans9']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET ans10  = '" + session['ans10'] + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET opt1  = '" + str(session['opt1']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET opt2  = '" + str(session['opt2']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET opt3  = '" + str(session['opt3']) + "' WHERE session_id = " + str(session['ref_num']))
        db.engine.execute(
            "UPDATE session SET opt4  = '" + str(session['opt4']) + "' WHERE session_id = " + str(session['ref_num']))
    return

def commitsus():
    db.engine.execute("INSERT INTO sus VALUES (" +
                      str(session['sus1']) + ',' +
                      str(session['sus2'])+ ',' +
                      str(session['sus3'])+ ',' +
                      str(session['sus4'])+ ',' +
                      str(session['sus5'])+ ',' +
                      str(session['sus6'])+ ',' +
                      str(session['sus7'])+ ',' +
                      str(session['sus8'])+ ',' +
                      str(session['sus9'])+ ',' +
                      str(session['sus10']) + ",'" +
                      str(session['sus11']) + "')")