# -*- coding: utf-8 -*-
# all the import
from flask import *
from model import *
from config import app
from flask_mail import Mail, Message
import datetime
import os

app.debug = True

mail = Mail(app)

app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='mis573wpi@gmail.com',
    MAIL_PASSWORD='wpimstbi'
)

mail = Mail(app)


# TODO: If session is running, kill it
# TODO: To test if the session exists.
# @app.route('/login')
# def login():
#     if 'logged' in session:
#         # already logged in
#         return render_template("home.html", page="homepage")
#     else:
#         session['login'] = True
#         return render_template("home.html", page="homepage")

# This is the test for email server


# create the answers instance, which takes all the value of answers.

@app.route('/')
def homepage():
    # initialize the objects in current session
    # global sess
    # session['sess']
    # session['data']
    # global data
    # global read
    # read = read()
    # session['sess'] = visit()
    # session['data'] = answer()

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
                               ans1=session['ans1'],
                               ans2=session['ans2'],
                               ans3=session['ans3'],
                               ans4=session['ans4'],
                               ans5=session['ans5'],
                               ans6=session['ans6'])
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
        # db.engine.execute("INSERT INTO session (ans1) VALUES (session['ans1'])")
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
                               ans1=session['ans1'],
                               ans2=session['ans2'],
                               ans3=session['ans3'],
                               ans4=session['ans4'],
                               ans5=session['ans5'],
                               ans6=session['ans6'],
                               ans7=session['ans7'],
                               ans8=session['ans8'],
                               ans9=session['ans9'],
                               ans10=session['ans10'],
                               ans11=session['ans11'],
                               ans12=session['ans12'],
                               ans13=session['ans13'],
                               ans14=session['ans14'],
                               ans15=session['ans15'],
                               ans16=session['ans16'],
                               email=session['email'])

    else:
        return redirect('/')


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
                               ans1=session['ans1'],
                               ans2=session['ans2'],
                               ans3=session['ans3'],
                               ans4=session['ans4'],
                               ans5=session['ans5'],
                               ans6=session['ans6'],
                               ans8=session['ans8'],
                               ans9=session['ans9'],
                               ans10=session['ans10'],
                               ans11=session['ans11'],
                               ans12=session['ans12'],
                               ans13=session['ans13'],
                               ans14=session['ans14'],
                               ans15=session['ans15'],
                               ans16=session['ans16']
                               )
    else:
        return redirect('/')


@app.route('/preview')
def page_preview():
    if 'logged' in session:
        return render_template('preview.html',
                               page="review",
                               ans1=session['ans1'],
                               ans2=session['ans2'],
                               ans3=session['ans3'],
                               ans4=session['ans4'],
                               ans5=session['ans5'],
                               ans6=session['ans6'],
                               ans8=session['ans8'],
                               ans9=session['ans9'],
                               ans10=session['ans10'],
                               ans11=session['ans11'],
                               ans12=session['ans12'],
                               ans13=session['ans13'],
                               ans14=session['ans14'],
                               ans15=session['ans15'],
                               ans16=session['ans16']
                               )
    else:
        return redirect('/')



@app.route('/report')
def page_report():
    if 'logged' in session:
        # session['end_time'] = datetime.datetime.now()
        # session['is_finished'] = True
        # # creating two objects to add data
        # db.session.add(data)
        # db.session.add(sess)
        # db.session.commit()
        # # test code
        # session['ref_num'] = data.ref_num
        # session['email'] = sess.email
        # db.session.add(data)
        # db.session.add(sess)
        # db.session.commit()
        # test code
        commitdb()
        session.pop('logged')
        # print("the session ends")
        # print(session['mailsent'])
        return render_template("report.html",
                               ref_num=session['ref_num'],
                               start=session['start'],
                               end=session['end'],
                               email=session['email'],
                               ans1=session['ans1'],
                               ans2=session['ans2'],
                               ans3=session['ans3'],
                               ans4=session['ans4'],
                               ans5=session['ans5'],
                               ans6=session['ans6'],
                               ans8=session['ans8'],
                               ans9=session['ans9'],
                               ans10=session['ans10'],
                               ans11=session['ans11'],
                               ans12=session['ans12'],
                               ans13=session['ans13'],
                               ans14=session['ans14'],
                               ans15=session['ans15'],
                               ans16=session['ans16'])
    else:
        return redirect('/')



@app.route("/mail")
def sendmail():
    print(session['email'])
    if session['email'] != '':
        msg = Message(
            'Your report from Traumatic Brain Injury Decision Aid Tool -- Report ID: ' + str(session['ref_num']),
            sender='mis573wpi@gmail.com',
            recipients=
            [session['email']])
        # msg.body = "1) What is most important for your loved one right now?"
        msg.html = "<div style='line-height:20px'><p>Hello,</p><p>This is an auto-generate report from Goals-of-Care after Traumatic Brain Injury Decision Aid Prototype.</p> <p>Start Time:" + str(
            session['start']) + "<p>End Time: " + str(session[
                                                               'end']) + "<ol><li>What is your loved one’s outlook for getting better and how independent will he/she be with further medical care after the ICU?</li><ul><li>" + session['ans8'] + "</li></ul><li> Do you understand what your loved one’s life will be like based on the two different treatment goals?</li><ul><li>" + session['ans9'] + "</li></ul><li>Is this quality of life acceptable to your loved one?</li><ul><li>" + session['ans10'] + "</li></ul><li> Do you understand the pros and cons of the two treatment goals/choices?</li><ul><li>" + session['ans11'] + "</li></ul><li>What are their wishes for medical treatments when illness is severe or possibly leave them disabled? Have they mentioned it to you? Do they have a living will?</li><ul><li>" + session['ans12'] + "</li></ul><li>If your loved one could look at the choices right now, what would they choose?</li><ul><li>" + session['ans13'] + "</li></ul><li>How is this choice making you feel?</li><ul><li>" + session['ans14'] + "</li></ul><li>Make a list and ask. Bring the list of questions to the meeting with the doctor, too.</li><ul><li>" + session['ans15'] + "</li></ul><li> Where do you think your loved one would put themselves on the line below? (Number from 0-100, smaller number represents survival, greater number represents comfort)</li><ul><li>" + str(
            session['ans16']) + "</li></ul></div>"
        session['mailsent'] = True
        mail.send(msg)
        alertmsg = 'The report has been sent.'
        print(session['mailsent'])
        print("mail has been sent")
        return render_template("report.html",
                               ref_num=session['ref_num'],
                               start=session['start'],
                               end=session['end'],
                               email=session['email'],
                               ans1=session['ans1'],
                               ans2=session['ans2'],
                               ans3=session['ans3'],
                               ans4=session['ans4'],
                               ans5=session['ans5'],
                               ans6=session['ans6'],
                               ans8=session['ans8'],
                               ans9=session['ans9'],
                               ans10=session['ans10'],
                               ans11=session['ans11'],
                               ans12=session['ans12'],
                               ans13=session['ans13'],
                               ans14=session['ans14'],
                               ans15=session['ans15'],
                               ans16=session['ans16'],
                               alertmsg=alertmsg
                               )
    else:
        alertmsg = "You didn't input your E-mail address"
        return render_template("report.html",
                               ref_num=session['ref_num'],
                               start=session['start'],
                               end=session['end'],
                               email=session['email'],
                               ans1=session['ans1'],
                               ans2=session['ans2'],
                               ans3=session['ans3'],
                               ans4=session['ans4'],
                               ans5=session['ans5'],
                               ans6=session['ans6'],
                               ans8=session['ans8'],
                               ans9=session['ans9'],
                               ans10=session['ans10'],
                               ans11=session['ans11'],
                               ans12=session['ans12'],
                               ans13=session['ans13'],
                               ans14=session['ans14'],
                               ans15=session['ans15'],
                               ans16=session['ans16'],
                               alertmsg=alertmsg)


@app.route("/mailid", methods=['POST'])
def mailid():
    if request.form.get('input_email') != '':
        tablelist = visit.query.filter_by(email=request.form.get('input_email')).first()
        # testing
        if tablelist:
            print(type(tablelist))
            print(type(tablelist.ref_num))
            print(type(str(tablelist.ref_num)))
            print(str(tablelist.ref_num))
            print(str(tablelist.start_time))
            print(str(tablelist.end_time))
            retrieve_mail = Message(
                'Your report ID from Traumatic Brain Injury Decision Aid Tool',
                sender='mis573wpi@gmail.com',
                recipients=[request.form.get('input_email')])
            retrieve_mail.html = "<p>Hello, <p>You sent a request to request your report ID from Traumatic Brain Injury Decision Aid Tool. These are the reports you finished before: </p><p>Report ID: " + str(
                tablelist.ref_num) + "</p><p>Start Time: " + str(tablelist.start_time) + "</p><p>End Time: " + str(
                tablelist.end_time)
            mail.send(retrieve_mail)
            alertmsg = 'The Report ID has been sent to your E-mail.'
            print("mail has been sent")
            return render_template("home.html",
                                   alertmsg=alertmsg)
        else:
            alertmsg = "No matched record"
            return render_template("home.html",
                                   alertmsg=alertmsg)
    else:
        alertmsg = "You have to input your E-mail address"
        return render_template("home.html",
                               alertmsg=alertmsg)


# if user click the retrieve report button
@app.route('/printable', methods=['POST'])
def printable():
    visitquery = visit.query.filter_by(ref_num=request.form.get('ref'),
                                       email=request.form.get('input_email')).first()
    print(type(visitquery))
    if visitquery:
        answerquery = answer.query.filter_by(ref_num=request.form.get('ref')).first()
        return render_template("printable.html",
                               start=visitquery.start_time,
                               end=visitquery.end_time,
                               email=visitquery.email,
                               ans1=answerquery.ans1,
                               ans2=answerquery.ans2,
                               ans3=answerquery.ans3,
                               ans4=answerquery.ans4,
                               ans5=answerquery.ans5,
                               ans6=answerquery.ans6,
                               ans7=answerquery.ans7,
                               ans8=answerquery.ans8,
                               ans9=answerquery.ans9,
                               ans10=answerquery.ans10,
                               ans11=answerquery.ans11,
                               ans12=answerquery.ans12,
                               ans13=answerquery.ans13,
                               ans14=answerquery.ans14,
                               ans15=answerquery.ans15,
                               ans16=answerquery.ans16)
    else:
        alertmsg = 'No matched record'
    return render_template('home.html', alertmsg=alertmsg)


# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#                                         #
#  Following part is under construction   #
#                                         #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

@app.route('/admin')
def admin_login():
    return render_template("admin.html")


@app.route('/admin/main', methods=['POST'])
def admin_main():
    if (request.form.get('username') == 'admin') & (request.form.get('password') == 'umass'):
        session['adminlogged'] = 'y'
        return render_template('admin_main.html', tablelist=visit.query.all())
    else:
        return redirect('/admin')


@app.route('/admin/main')
def admin_return_main():
    if 'adminlogged' in session:
        return render_template('admin_main.html', tablelist=visit.query.all())
    else:
        return redirect('/admin')


@app.route('/admin/main/result', methods=['POST'])
def search_result():
    if (request.form.get('ref_num') != '') and (request.form.get('email') == ''):
        # only ref_num input
        return render_template('admin_main.html',
                               tablelist=visit.query.filter_by(ref_num=request.form.get('ref_num')).all())
    elif (request.form.get('ref_num') == '') and (request.form.get('email') != ''):
        # only email input
        return render_template('admin_main.html',
                               tablelist=visit.query.filter_by(email=request.form.get('email')).all())
    elif (request.form.get('ref_num') != '') and (request.form.get('email') != ''):
        return render_template('admin_main.html', tablelist=visit.query.filter_by(ref_num=request.form.get('ref_num'),
                                                                                  email=request.form.get(
                                                                                      'email')).all())
    else:
        return render_template('admin_main.html', no_result=True)


@app.route('/getreport')
def getreport():
    return render_template('home.html', page="getreport")


@app.route('/sendcontact', methods=['POST'])
def sendcontact():
    msg = Message(
        'User Feedback: ' + request.form.get('subject'),
        sender='mis573wpi@gmail.com',
        recipients=['lilinshuo1110@gmail.com'])
    msg.html = "<p> Name: " + request.form.get('name') + "</p><p> Email: " + request.form.get(
        'email') + "</p><p>" + request.form.get('message')
    mail.send(msg)
    flash("Your feedback has been sent to us, we'll reply you as soon as possible. Thank you!")
    print("mail has been sent")
    return ('', 204)


###############
# for testing #
###############

# add into database
def commitdb():
    ex = db.engine.execute("INSERT INTO session (start) VALUES ('" + session['start'] + "')")
    session['ref_num'] = ex.lastrowid
    session['end'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.engine.execute("UPDATE session SET email  = '" + session['email'] + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET end    = '" + session['end']   + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans1   = '" + session['ans1']  + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans2   = '" + session['ans2']  + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans3   = '" + session['ans3']  + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans4   = '" + session['ans4']  + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans5   = '" + session['ans5']  + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans6   = '" + session['ans6']  + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans7   = '" + session['ans7']  + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans8   = '" + session['ans8']  + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans9   = '" + session['ans9']  + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans10  = '" + session['ans10'] + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans11  = '" + session['ans11'] + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans12  = '" + session['ans12'] + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans13  = '" + session['ans13'] + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans14  = '" + session['ans14'] + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans15  = '" + session['ans15'] + "' WHERE session_id = " + str(session['ref_num']))
    db.engine.execute("UPDATE session SET ans16  = '" + str(session['ans16']) + "' WHERE session_id = " + str(session['ref_num']))
    return


@app.route("/test")
def test():
    commitdb()
    print("Commit successfully")
    return render_template('test.html',
                           ref_num=session['ref_num'],
                           start=session['start'],
                           end=session['end'],
                           email=session['email'],
                           logged=session['logged'],
                           ans1=session['ans1'],
                           ans2=session['ans2'],
                           ans3=session['ans3'],
                           ans4=session['ans4'],
                           ans5=session['ans5'],
                           ans6=session['ans6'],
                           ans8=session['ans8'],
                           ans9=session['ans9'],
                           ans10=session['ans10'],
                           ans11=session['ans11'],
                           ans12=session['ans12'],
                           ans13=session['ans13'],
                           ans14=session['ans14'],
                           ans15=session['ans15'],
                           ans16=session['ans16'])

@app.route("/testresult", methods=['POST'])
def testresult():
    session['form'] = request.form.get('testvar')
    print(type(session['form']))
    ex = db.engine.execute("INSERT INTO session (ans1) VALUES ('" + session['form'] + "')")
    print(ex.lastrowid)
    return render_template('test.html', test = session['form'])


@app.route('/sql')
def sql():
    return render_template("sql.html")


@app.route('/sqlresult', methods=['POST'])
def sqlresult():
    # Get the raw sql query from the form
    query = request.form.get('query')
    # Run it using SQL
    try:
        result = db.engine.execute(query)
    except Exception:
        return render_template("sql.html", result = 'error')
    # for row in result:
    #     print(row)
    # Print the resfiult on the screen
    return render_template("sql.html", result = result)

if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.run()
