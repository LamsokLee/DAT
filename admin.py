# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#                                         #
#  Following part is under construction   #
#                                         #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #
from flask import render_template, request, session, redirect
from config import app
from database import db


@app.route('/admin')
def admin_login():
    if 'adminlogged' in session:
        session.pop('adminlogged')
    return render_template("admin/admin.html")


@app.route('/admin/main', methods=['POST'])
def admin_main():
    if 'adminlogged' in session:
        return render_template('admin/admin_main.html')
    else:
        if (request.form.get('username') == 'admin') & (request.form.get('password') == 'umass'):
            session['adminlogged'] = 'y'
            return render_template('admin/admin_main.html')
        else:
            alertmsg = 'Username or Password Wrong!'
            return render_template('admin/admin.html', alertmsg = alertmsg)


@app.route('/admin/main')
def admin_listall():
    if 'adminlogged' in session:
        return render_template('admin/admin_main.html', tablelist=db.engine.execute("SELECT * FROM session ORDER BY id DESC"))
    else:
        return redirect('/admin')


@app.route('/admin/main/result', methods=['POST'])
def search_result():
    if (request.form.get('ref_num') != '') and (request.form.get('email') == ''):
        # only ref_num input
        return render_template('admin/admin_main.html',
                               tablelist=db.engine.execute("SELECT * FROM session WHERE id = " + request.form.get('ref_num')))
    elif (request.form.get('ref_num') == '') and (request.form.get('email') != ''):
        # only email input
        return render_template('admin/admin_main.html',
                               tablelist=db.engine.execute("SELECT * FROM session WHERE email = '" + request.form.get('email') +"' ORDER BY id DESC"))
    elif (request.form.get('ref_num') != '') and (request.form.get('email') != ''):
        return render_template('admin/admin_main.html', tablelist=db.engine.execute("SELECT * FROM session WHERE id = " + request.form.get('ref_num') + " AND email = '" + request.form.get('email') + "' ORDER BY id DESC"))
    else:
        return render_template('admin/admin_main.html', no_result=True)

@app.route('/admin/main/report/<int:ref_num>', methods=['GET','POST'])
def admin_report(ref_num):
    if 'adminlogged' in session:
        visitquery = db.engine.execute("SELECT * FROM session WHERE id = " + str(ref_num))
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
            session['ref_num'] = ans['id']
            session['email'] = ans['email']
            session['start'] = ans['start']
            session['end'] = ans['end']
        return render_template("admin/admin_report.html", session=session)
    else:
        return redirect('/admin')

@app.route('/admin/main/report/delete')
def admin_report_delete():
    if 'adminlogged' in session:
        db.engine.execute("DELETE FROM session WHERE id = " + str(session['ref_num']))
        return redirect('/admin/main')
    else:
        return redirect('/admin')