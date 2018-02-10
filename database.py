import datetime

from flask import session, request
from flask_sqlalchemy import SQLAlchemy
from config import app

# create an instance of SQLAlchemy class with the Flask object as the parameter
db = SQLAlchemy(app)


def commitdb():
    if session['id'] != 0:
        # session exists, update datetime
        session['end'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for value in session:
            if value not in ['logged', 'page', 'test', 'id', 'version']:
                if type(session[value]) is int:
                    db.engine.execute(
                        "UPDATE session SET " + str(value) + " = " + str(session[value]) + " WHERE id = " + str(
                            session['id']))

                else:
                    db.engine.execute(
                        "UPDATE session SET " + str(value) + " = '" + str(session[value]) + "' WHERE id = " + str(
                            session['id']))


    else:
        ex = db.engine.execute("INSERT INTO session (start) VALUES ('" + session['start'] + "')")
        session['id'] = ex.lastrowid
        session['end'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for value in session:
            if value not in ['logged', 'page', 'test', 'id', 'start', 'version']:
                if type(session[value]) is int:
                    db.engine.execute(
                        "UPDATE session SET " + str(value) + " = " + str(session[value]) + " WHERE id = " + str(
                            session['id']))
                else:
                    db.engine.execute(
                        "UPDATE session SET " + str(value) + " = '" + str(session[value]) + "' WHERE id = " + str(
                            session['id']))
    return


def commitsus():
    susscore = [session['sus'].get(sus) for sus in session['sus']]

    db.engine.execute("INSERT INTO sus VALUES (" +
                      str(susscore[0]) + ',' +
                      str(susscore[1]) + ',' +
                      str(susscore[2]) + ',' +
                      str(susscore[3]) + ',' +
                      str(susscore[4]) + ',' +
                      str(susscore[5]) + ',' +
                      str(susscore[6]) + ',' +
                      str(susscore[7]) + ',' +
                      str(susscore[8]) + ',' +
                      str(susscore[9]) + ",'" +
                      str(susscore[10]) + "'," +
                      str(susscore[11]) + ",'" +
                      str(susscore[12]) + "')")
