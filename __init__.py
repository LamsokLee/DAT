# -*- coding: utf-8 -*-
# all the import
from admin import *
from mail import *
from error import *
from navigation import *
from sus import *
import os

app.debug = True


# TODO: If session is running, kill it
# TODO: To test if the session exists.
@app.route('/testportal')
def testhomepage():
    # initialize the objects in current session
    session['test'] = 1
    session['ans1'] = 'Did not make any choice'
    session['ans2'] = ''
    session['ans3'] = ''
    session['ans4'] = 0
    session['ans5'] = 0
    session['ans6'] = 0
    session['ans7'] = 0
    session['ans8'] = 0
    session['ans9'] = 50
    session['ans10'] = ''
    session['ref_num'] = -1
    session['email'] = ''
    session['start'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session['end'] = -1
    session['logged'] = 'y'
    session['opt1'] = 0
    session['opt2'] = 0
    session['opt3'] = 0
    session['opt4'] = 0
    return render_template("pages/home.html", session = session)

@app.route('/')
def homepage():
    # initialize the objects in current session
    session['test'] = 0
    session['ans1'] = 'Did not make any choice'
    session['ans2'] = ''
    session['ans3'] = ''
    session['ans4'] = 0
    session['ans5'] = 0
    session['ans6'] = 0
    session['ans7'] = 0
    session['ans8'] = 0
    session['ans9'] = 50
    session['ans10'] = ''
    session['ref_num'] = -1
    session['email'] = ''
    session['start'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session['end'] = -1
    session['logged'] = 'y'
    session['opt1'] = 0
    session['opt2'] = 0
    session['opt3'] = 0
    session['opt4'] = 0
    return render_template("pages/home.html", session = session)


# Report Preview Page
@app.route('/postreport', methods=['POST'])
def post_report():
    if 'logged' in session:
        # get the user input from the form
        session['ans2'] = request.form.get('ans2')
        session['ans3'] = request.form.get('ans3')
        if request.form.get('ans4') is not None:
            session['ans4'] = int(request.form.get('ans4'))
        if request.form.get('ans5') is not None:
            session['ans5'] = int(request.form.get('ans5'))
        if request.form.get('ans6') is not None:
            session['ans6'] = int(request.form.get('ans6'))
        if request.form.get('ans7') is not None:
            session['ans7'] = int(request.form.get('ans7'))
        if request.form.get('ans8') is not None:
            session['ans8'] = int(request.form.get('ans8'))
        session['ans9'] = request.form.get('ans9')
        session['ans10'] = request.form.get('ans10')
        session['email'] = request.form.get('email')
        if request.form.get('opt1') == "on":
            session['opt1'] = 1
        if request.form.get('opt2') == "on":
            session['opt2'] = 1
        if request.form.get('opt3') == "on":
            session['opt3'] = 1
        if request.form.get('opt4') == "on":
            session['opt4'] = 1
        return redirect('/report')
    else:
        return redirect('/')


@app.route('/report')
def page_report():
    if 'logged' in session:
        return render_template('report.html',
                               page="review",
                               session=session)
    else:
        return redirect('/')


# Submit the report and commit to database
@app.route('/summary')
def page_summary():
    if 'logged' in session:
        commitdb()
        session.pop('logged')
        return render_template("summary.html",
                               session=session)
    else:
        return redirect('/')


# if user click the retrieve report button
@app.route('/printable', methods=['POST'])
def printable():
    # TODO: check the input format
    if request.form.get('input_email') != '' and request.form.get('ref') != '':
        visitquery = db.engine.execute(
            "SELECT * FROM session WHERE session_id = " + request.form.get('ref') + " and email = '" + request.form.get(
                'input_email') + "'")
        if visitquery.rowcount == 0:
            return render_template('pages/home.html', alertmsg="No matched record")
        else:
            result = visitquery.fetchall()
            for ans in result:
                session['ans1'] = ans['ans1']
                session['ans2'] = ans['ans2']
                session['ans3'] = ans['ans3']
                session['ans4'] = ans['ans4']
                session['ans5'] = ans['ans5']
                session['ans6'] = ans['ans6']
                session['ans7'] = ans['ans7']
                session['ans8'] = ans['ans8']
                session['ans9'] = ans['ans9']
                session['ans10'] = ans['ans10']
                session['opt1'] = ans['opt1']
                session['opt2'] = ans['opt2']
                session['opt3'] = ans['opt3']
                session['opt4'] = ans['opt4']
                session['ref_num'] = ans['session_id']
                session['email'] = ans['email']
                session['start'] = ans['start']
                session['end'] = ans['end']
            return render_template("printable.html", session=session)
    return render_template("pages/home.html", alertmsg="Please input complete information")


@app.route('/getreport')
def getreport():
    return render_template('pages/home.html', page="getreport")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.run()
