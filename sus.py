from flask import session, request, render_template
from config import *

@app.route('/sus')
def sus():
    return render_template('sus.html')

@app.route('/submitsus', methods=['POST'])
def submitsus():
    if request.form.get('q1') is None:
        session['sus1'] = 0
    else:
        session['sus1'] = request.form.get('q1')
    if request.form.get('q2') is None:
        session['sus2'] = 0
    else:
        session['sus2'] = request.form.get('q2')
    if request.form.get('q3') is None:
        session['sus3'] = 0
    else:
        session['sus3'] = request.form.get('q3')
    if request.form.get('q4') is None:
        session['sus4'] = 0
    else:
        session['sus4'] = request.form.get('q4')
    if request.form.get('q5') is None:
        session['sus5'] = 0
    else:
        session['sus5'] = request.form.get('q5')
    if request.form.get('q6') is None:
        session['sus6'] = 0
    else:
        session['sus6'] = request.form.get('q6')
    if request.form.get('q7') is None:
        session['sus7'] = 0
    else:
        session['sus7'] = request.form.get('q7')
    if request.form.get('q8') is None:
        session['sus8'] = 0
    else:
        session['sus8'] = request.form.get('q8')
    if request.form.get('q9') is None:
        session['sus9'] = 0
    else:
        session['sus9'] = request.form.get('q9')
    if request.form.get('q10') is None:
        session['sus10'] = 0
    else:
        session['sus10'] = request.form.get('q10')
    session['sus11'] = request.form.get('q11')
    commitsus()
    return redirect('/')
