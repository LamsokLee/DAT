from flask import session, request, render_template, redirect
from config import *
from database import *


@app.route('/sus')
def sus():
    return render_template('sus.html')


@app.route('/submitsus', methods=['POST'])
def submitsus():
    session['sus'] = {}
    for i in range(1, 11):
        key = 'sus' + str(i)
        session['sus'].update({key: 0})
    session['sus'].update({'sus11':''})
    session['sus'].update({'version': session['version']})
    session['sus'].update({'time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

    print(session['sus'])

    for sus in request.form:
        value = request.form.get(sus)
        if value is None and type(value) is not str:
            session['sus'].update({sus: value})
        elif type(value) is str:
            session['sus'].update({sus: value})
    commitsus()
    return redirect('/')
