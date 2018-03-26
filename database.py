import datetime
from flask import session
from config import db


def commitdb():
    if session['id'] == 0:
        ex = db.engine.execute("INSERT INTO session (start) VALUES ('" + session['start'] + "')")
        session['id'] = ex.lastrowid
    session['end'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query(session)


def query(session):
    set = []
    for i in range(1, 14):
        set.append('ans' + str(i))
    set = set + ['start', 'end', 'id', 'email']
    for value in set:
        if type(session[value]) is int:
            db.engine.execute(
                "UPDATE session SET " + str(value) + " = " + str(session[value]) + " WHERE id = " + str(
                    session['id']))
        else:
            db.engine.execute(
                "UPDATE session SET " + str(value) + " = '" + str(session[value]) + "' WHERE id = " + str(
                    session['id']))

def commitsus():
    # susscore = [session['sus'].get(sus) for sus in session['sus']]

    db.engine.execute("INSERT INTO sus VALUES (" +
                      str(session['sus']['sus1']) + ',' +
                      str(session['sus']['sus2']) + ',' +
                      str(session['sus']['sus3']) + ',' +
                      str(session['sus']['sus4']) + ',' +
                      str(session['sus']['sus5']) + ',' +
                      str(session['sus']['sus6']) + ',' +
                      str(session['sus']['sus7']) + ',' +
                      str(session['sus']['sus8']) + ',' +
                      str(session['sus']['sus9']) + ',' +
                      str(session['sus']['sus10']) + ",'" +
                      str(session['sus']['sus11']) + "'," +
                      str(session['version']) + ",'" +
                      str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "')")
