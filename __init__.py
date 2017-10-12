# -*- coding: utf-8 -*-
# all the import
from test import *
from admin import *
from database import *
from error import *
from sendmail import *
import os

app.debug = True


# TODO: If session is running, kill it
# TODO: To test if the session exists.

@app.route('/')
def homepage():
    # initialize the objects in current session
    session['ans1'] = ''
    session['ans2'] = ''
    session['ans3'] = ''
    session['ans4'] = ''
    session['ans5'] = ''
    session['ans6'] = ''
    session['ans7'] = 'Did not make any choice'
    session['ans8'] = ''
    session['ans9'] = ''
    session['ans10'] = ''
    session['ans11'] = ''
    session['ans12'] = ''
    session['ans13'] = ''
    session['ans14'] = ''
    session['ans15'] = ''
    session['ans16'] = 50
    session['ref_num'] = -1
    session['email'] = ''
    session['start'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session['end'] = -1

    # default value of sess attributes

    # TODO: Is_finish is not funcitoning
    # session['is_finished'] = False
    # session['mailsent'] = False
    # session['accordion1'] = False;
    # session['accordion2'] = False;
    # session['accordion3'] = False;
    # session['accordion4'] = False;
    # session['accordion5'] = False;
    # session['accordion6'] = False;
    # session['accordion7'] = False;
    # session['accordion8'] = False;
    # session['accordion9'] = False;
    # session['accordion10'] = False;

    # mark the session as logged
    session['logged'] = 'y'
    return render_template("home.html", page="homepage")


@app.route('/1')
def page_1():
    if 'logged' in session:
        return render_template("1.html", page=1)
    else:
        return redirect('/')


@app.route('/2')
def page_2():
    if 'logged' in session:
        return render_template("2.html", page=2)
    else:
        return redirect('/')


@app.route('/3')
def page_3():
    if 'logged' in session:
        return render_template("3.html", page=3)
    else:
        return redirect('/')


@app.route('/4')
def page_4():
    if 'logged' in session:
        return render_template("4.html",
                               page=4,
                               session = session)
    else:
        return redirect('/')


@app.route('/post5', methods=['POST'])
def post_5():
    if 'logged' in session:
        # get the user input from the form in the html
        session['ans1'] = request.form.get('ans1')
        session['ans2'] = request.form.get('ans2')
        session['ans3'] = request.form.get('ans3')
        session['ans4'] = request.form.get('ans4')
        session['ans5'] = request.form.get('ans5')
        session['ans6'] = request.form.get('ans6')
        return render_template("5.html", page=5)
    else:
        return redirect('/')


@app.route('/5')
def page_5():
    if 'logged' in session:
        return render_template("5.html", page=5)
    else:
        return redirect('/')


@app.route('/6')
def page_6():
    if 'logged' in session:
        return render_template("6.html", page=6)
    else:
        return redirect('/')


@app.route('/7')
def page_7():
    if 'logged' in session:
        return render_template("7.html", page=7)
    else:
        return redirect('/')


@app.route('/8')
def page_8():
    if 'logged' in session:
        return render_template("8.html", page=8)
    else:
        return redirect('/')


@app.route('/9')
def page_9():
    if 'logged' in session:
        return render_template("9.html", page=9)
    else:
        return redirect('/')


@app.route('/10')
def page_10():
    if 'logged' in session:
        return render_template("10.html", page=10)
    else:
        return redirect('/')


@app.route('/11')
def page_11():
    if 'logged' in session:
        return render_template("11.html", page=11)
    else:
        return redirect('/')


@app.route('/12')
def page_12():
    if 'logged' in session:
        return render_template("12.html", page=12)
    else:
        return redirect('/')


@app.route('/13')
def page_13():
    if 'logged' in session:
        return render_template("13.html", page=13)
    else:
        return redirect('/')


@app.route('/14')
def page_14():
    if 'logged' in session:
        return render_template("14.html", page=14)
    else:
        return redirect('/')


@app.route('/post15', methods=['POST'])
def post_15():
    if 'logged' in session:
        session['ans7'] = request.form.get('option')
        return render_template("15.html", page=15)
    else:
        return redirect('/')


@app.route('/15')
def page_15():
    if 'logged' in session:
        return render_template("15.html", page=15)
    else:
        return redirect('/')


@app.route('/16')
def page_16():
    if 'logged' in session:
        return render_template("16.html", page=16)
    else:
        return redirect('/')


@app.route('/17')
def page_17():
    if 'logged' in session:
        return render_template("17.html", page=17)
    else:
        return redirect('/')


@app.route('/18')
def page_18():
    if 'logged' in session:
        return render_template("18.html",
                               page=18,
                               session = session)

    else:
        return redirect('/')


#Report Preview Page
@app.route('/postpreview', methods=['POST'])
def post_preview():
    if 'logged' in session:
        # get the user input from the form
        session['ans8'] = request.form.get('ans8')
        session['ans9'] = request.form.get('ans9')
        session['ans10'] = request.form.get('ans10')
        session['ans11'] = request.form.get('ans11')
        session['ans12'] = request.form.get('ans12')
        session['ans13'] = request.form.get('ans13')
        session['ans14'] = request.form.get('ans14')
        session['ans15'] = request.form.get('ans15')
        session['ans16'] = request.form.get('ans16')
        session['email'] = request.form.get('email')

        return render_template('preview.html',
                               page="review",
                               session =session)
    else:
        return redirect('/')


@app.route('/preview')
def page_preview():
    if 'logged' in session:
        return render_template('preview.html',
                               page="review",
                               session = session)
    else:
        return redirect('/')

#Submit the report and commit to database
@app.route('/report')
def page_report():
    if 'logged' in session:
        commitdb()
        session.pop('logged')
        return render_template("report.html",
                               session = session)
    else:
        return redirect('/')


# if user click the retrieve report button
@app.route('/printable', methods=['POST'])
def printable():
    # TODO: check the input format
    if request.form.get('input_email') != '' and request.form.get('ref') != '':
        visitquery = db.engine.execute("SELECT * FROM session WHERE session_id = " + request.form.get('ref') + " and email = '" +request.form.get('input_email')+"'")
        if visitquery.rowcount == 0:
            return render_template('home.html', alertmsg = "No matched record")
        else:
            result = visitquery.fetchall()
            for ans in result:
                session['ans1'] =  ans['ans1']
                session['ans2'] =  ans['ans2']
                session['ans3'] =  ans['ans3']
                session['ans4'] =  ans['ans4']
                session['ans5'] =  ans['ans5']
                session['ans6'] =  ans['ans6']
                session['ans7'] =  ans['ans7']
                session['ans8'] =  ans['ans8']
                session['ans9'] =  ans['ans9']
                session['ans10'] = ans['ans10']
                session['ans11'] = ans['ans11']
                session['ans12'] = ans['ans12']
                session['ans13'] = ans['ans13']
                session['ans14'] = ans['ans14']
                session['ans15'] = ans['ans15']
                session['ans16'] = ans['ans16']
                session['ref_num'] = ans['session_id']
                session['email'] = ans['email']
                session['start'] = ans['start']
                session['end'] = ans['end']
            return render_template("printable.html", session = session)
    return render_template("home.html",alertmsg = "Please input complete information")

@app.route('/getreport')
def getreport():
    return render_template('home.html', page="getreport")

if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.run()
