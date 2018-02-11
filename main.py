# -*- coding: utf-8 -*-
# all the import
from admin import *
from mail import *
from error import *
from sus import *
import test
import data
import os


# TODO: If session is running, kill it
# TODO: To test if the session exists.


@app.route('/testportal')
def testhome():
    session['id'] = 0
    session['email'] = ''
    session['start'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session['end'] = -1
    session['logged'] = 1
    session['test'] = 1
    session['version'] = 4.1

    for i in range(1, 12):
        session['ans' + str(i)] = 0
    session['ans7'] = 50
    session['ans12'] = ''
    session['ans13'] = ''

    return render_template("content/home.html")


@app.route('/')
def home():
    session['id'] = 0
    session['email'] = ''
    session['start'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session['end'] = -1
    session['logged'] = 1
    session['test'] = 0
    session['version'] = 4.1

    for i in range(1, 12):
        session['ans' + str(i)] = 0
    session['ans7'] = 50
    session['ans12'] = ''
    session['ans13'] = ''
    return render_template("content/home.html")


@app.route('/page')
@app.route('/<int:page>')
def showpage(page):
    session['page'] = page
    return render_template('content/' + str(session['page']) + '.html')


# Report Preview Page
@app.route('/post', methods=['POST'])
def post():
    if 'logged' in session:
        for item in session:
            if item in request.form:
                if type(session[item]) == int:
                    session[item] = int(request.form.get(item))
                else:
                    session[item] = request.form.get(item)
            elif item in ['ans8', 'ans9', 'ans10', 'ans11']:
                session[item] = 0
        return redirect('/report')
    else:
        return redirect('/')


@app.route('/report')
def page_report():
    if 'logged' in session:
        return render_template('report.html')
    else:
        return redirect('/')


# Submit the report and commit to database
@app.route('/summary')
def page_summary():
    if 'logged' in session:
        commitdb()
        session.pop('logged')
        return render_template("summary.html")
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
            return render_template('content/home.html', alertmsg="No matched record")
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
                session['id'] = ans['id']
                session['email'] = ans['email']
                session['start'] = ans['start']
                session['end'] = ans['end']
            return render_template("printable.html")
    return render_template("content/home.html", alertmsg="Please input complete information")


@app.route('/getreport')
def getreport():
    return render_template('content/home.html', page="getreport")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.run()
