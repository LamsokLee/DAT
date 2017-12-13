from flask_mail import Mail, Message
from config import app
from flask import session, render_template, request, flash
from database import *

mail = Mail(app)
#Send report to the client.
@app.route("/mail")
def sendmail():
    if session['email'] != '':
        # Email: Subject, sender, recipient
        msg = Message('Your report from Traumatic Brain Injury Decision Aid Tool -- Report ID: ' + str(session['ref_num']),
            sender='mis573wpi@gmail.com',
            recipients=[session['email']])
        # Email: Body
        msg.html = render_template('sections/textreport.html', session = session)
        try:
            mail.send(msg)
        except Exception:
            session['alertmsg'] = "E-mail sent unsuccessfully, Please try again."
            return render_template("summary.html",
                                   session=session)
        session['alertmsg'] = 'The report has been sent.'
        return render_template("summary.html",
                               session = session)

#
@app.route("/mailid", methods=['POST'])
def mailid():
    if request.form.get('input_email') != '':
        # tablelist = visit.query.filter_by(email=request.form.get('input_email')).first()
        visitquery = db.engine.execute("SELECT * FROM session WHERE email = '" + request.form.get('input_email') + "'")
        # testing
        if visitquery.rowcount != 0:
            # Has user record
            for record in visitquery:
                retrieve_mail = Message(
                    'Your report ID from Traumatic Brain Injury Decision Aid Tool',
                    sender='mis573wpi@gmail.com',
                    recipients=[request.form.get('input_email')])
                retrieve_mail.html = render_template("email/forget_mail.html", record = record)
            mail.send(retrieve_mail)
            alertmsg = 'The Report ID has been sent to your E-mail.'
            print("mail has been sent")
            return render_template("pages/home.html",
                                   alertmsg=alertmsg)
        else:
            alertmsg = "No matched record"
            return render_template("pages/home.html",
                                   alertmsg=alertmsg)
    else:
        alertmsg = "You have to input your E-mail address"
        return render_template("pages/home.html",
                               alertmsg=alertmsg)

@app.route('/sendcontact', methods=['POST'])
def sendcontact():
    msg = Message(
        'User Feedback: ' + request.form.get('subject'),
        sender='mis573wpi@gmail.com',
        recipients=['lilinshuo1110@gmail.com'])
    msg.html = "<p> Name: " + request.form.get('name') + "</p><p> Email: " + request.form.get(
        'email') + "</p><p>" + request.form.get('message')
    mail.send(msg)
    # flash("Your feedback has been sent to us, we'll reply you as soon as possible. Thank you!")
    # return ('', 204)
    return render_template("pages/home.html", feedback ="Your feedback has been sent to us, we'll reply you as soon as possible. Thank you!")