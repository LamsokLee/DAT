# all the import
from flask import *
from model import *
from config import app
import datetime
import os

app.debug = True


# TODO: If session is running, kill it
# TODO: To test if the session exists.

# create the answers instance, which takes all the value of answers.

@app.route('/')
def homepage():
    # initialize the objects in current session
    global sess
    global data
    # global read
    # read = read()
    sess = visit()
    data = answer()
    # default value of data attributes
    data.ans1 = ''
    data.ans2 = ''
    data.ans3 = ''
    data.ans4 = ''
    data.ans5 = ''
    data.ans6 = ''
    data.ans7 = 'Did not make any choice'
    data.ans8 = ''
    data.ans9 = ''
    data.ans10 = ''
    data.ans11 = ''
    data.ans12 = ''
    data.ans13 = ''
    data.ans14 = ''
    data.ans15 = ''
    data.ans16 = 50
    # default value of sess attributes
    sess.email = ''
    sess.start_time = datetime.datetime.now()
    # TODO: Is_finish is not funcitoning
    sess.is_finished = False
    # mark the session as logged
    session['logged'] = 'y'
    session['accordion1'] = False;
    session['accordion2'] = False;
    session['accordion3'] = False;
    session['accordion4'] = False;
    session['accordion5'] = False;
    session['accordion6'] = False;
    session['accordion7'] = False;
    session['accordion8'] = False;
    session['accordion9'] = False;
    session['accordion10'] = False;
    return render_template("home.html")


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
    # TODO: When user click start, the session starts.
    # TODO: Set the session time
    if 'logged' in session:
        return render_template("3.html", page=3)
    else:
        return redirect('/')


@app.route('/4')
def page_4():
    if 'logged' in session:
        return render_template("4.html",
                               page=4,
                               ans1=data.ans1,
                               ans2=data.ans2,
                               ans3=data.ans3,
                               ans4=data.ans4,
                               ans5=data.ans5,
                               ans6=data.ans6)
    else:
        return redirect('/')


@app.route('/post5', methods=['POST'])
def post_5():
    if 'logged' in session:
        # get the user input from the form in the html
        data.ans1 = request.form.get('ans1')
        data.ans2 = request.form.get('ans2')
        data.ans3 = request.form.get('ans3')
        data.ans4 = request.form.get('ans4')
        data.ans5 = request.form.get('ans5')
        data.ans6 = request.form.get('ans6')
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
        data.ans7 = request.form.get('option')
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
                               ans1=data.ans1,
                               ans2=data.ans2,
                               ans3=data.ans3,
                               ans4=data.ans4,
                               ans5=data.ans5,
                               ans6=data.ans6,
                               ans7=data.ans7,
                               ans8=data.ans8,
                               ans9=data.ans9,
                               ans10=data.ans10,
                               ans11=data.ans11,
                               ans12=data.ans12,
                               ans13=data.ans13,
                               ans14=data.ans14,
                               ans15=data.ans15,
                               ans16=data.ans16,
                               email=sess.email)

    else:
        return redirect('/')


@app.route('/postpreview', methods=['POST'])
def post_preview():
    if 'logged' in session:
        # get the user input from the form
        data.ans8 = request.form.get('ans8')
        data.ans9 = request.form.get('ans9')
        data.ans10 = request.form.get('ans10')
        data.ans11 = request.form.get('ans11')
        data.ans12 = request.form.get('ans12')
        data.ans13 = request.form.get('ans13')
        data.ans14 = request.form.get('ans14')
        data.ans15 = request.form.get('ans15')
        data.ans16 = request.form.get('ans16')
        sess.email = request.form.get('email')

        return render_template('preview.html',
                               page="review",
                               ans1=data.ans1,
                               ans2=data.ans2,
                               ans3=data.ans3,
                               ans4=data.ans4,
                               ans5=data.ans5,
                               ans6=data.ans6,
                               ans8=data.ans8,
                               ans9=data.ans9,
                               ans10=data.ans10,
                               ans11=data.ans11,
                               ans12=data.ans12,
                               ans13=data.ans13,
                               ans14=data.ans14,
                               ans15=data.ans15,
                               ans16=data.ans16
                               )
    else:
        return redirect('/')


@app.route('/preview')
def page_preview():
    if 'logged' in session:
        return render_template('preview.html',
                               page="review",
                               ans1=data.ans1,
                               ans2=data.ans2,
                               ans3=data.ans3,
                               ans4=data.ans4,
                               ans5=data.ans5,
                               ans6=data.ans6,
                               ans8=data.ans8,
                               ans9=data.ans9,
                               ans10=data.ans10,
                               ans11=data.ans11,
                               ans12=data.ans12,
                               ans13=data.ans13,
                               ans14=data.ans14,
                               ans15=data.ans15,
                               ans16=data.ans16
                               )
    else:
        return redirect('/')


@app.route('/report')
def page_report():
    if 'logged' in session:
        sess.end_time = datetime.datetime.now()
        sess.is_finished = True
        db.session.add(data)
        db.session.add(sess)
        db.session.commit()
        # test code
        data.ref_num = sess.ref_num
        db.session.add(data)
        db.session.add(sess)
        db.session.commit()
        # test code
        session.pop('logged')
        # TODO: retrieve the reference number from database and show it on this page.
        return render_template("report.html",
                               ref_num  =data.ref_num,
                               start    =sess.start_time,
                               end      =sess.end_time,
                               email    =sess.email,
                               ans1     =data.ans1,
                               ans2     =data.ans2,
                               ans3     =data.ans3,
                               ans4     =data.ans4,
                               ans5     =data.ans5,
                               ans6     =data.ans6,
                               ans8     =data.ans8,
                               ans9     =data.ans9,
                               ans10    =data.ans10,
                               ans11    =data.ans11,
                               ans12    =data.ans12,
                               ans13    =data.ans13,
                               ans14    =data.ans14,
                               ans15    =data.ans15,
                               ans16    =data.ans16)
    else:
        return redirect('/')


@app.route('/printable', methods=['POST'])
def printable():
    visitquery = visit.query.filter_by(ref_num=request.form.get('ref'),
                                       email=request.form.get('input_email')).first()
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
        msg = 'No matched record'
        return render_template('home.html', msg=msg)


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
        # TODO: Show the SQL query results of all the data
        return render_template('admin_main.html', tablelist=visit.query.all())
    else:
        return redirect('/admin')


@app.route('/admin/main')
def admin_return_main():
    if 'adminlogged' in session:
        return render_template('admin_main.html', tablelist=visit.query.all())
    else:
        return redirect('/admin')
        # , tablelist = visit.query.filter_by(ref_num=ref_post).all()


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


if __name__ == "__main__":
    app.secret_key = os.urandom(32)
    app.run()
