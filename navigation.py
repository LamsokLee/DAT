from flask import render_template, session, redirect
from config import app

@app.route('/1')
def page_1():
    if 'logged' in session:
        return render_template("main.html", page = 1)
    else:
        return redirect('/')


@app.route('/2')
def page_2():
    if 'logged' in session:
        return render_template("main.html", page = 2)
    else:
        return redirect('/')


@app.route('/3')
def page_3():
    if 'logged' in session:
        return render_template("main.html", page = 3)
    else:
        return redirect('/')


@app.route('/4')
def page_4():
    if 'logged' in session:
        return render_template("main.html",
                               page=4,
                               session = session)
    else:
        return redirect('/')

#
# @app.route('/post5', methods=['POST'])
# def post_5():
#     if 'logged' in session:
#         # get the user input from the form in the html
#         session['ans1'] = request.form.get('ans1')
#         session['ans2'] = request.form.get('ans2')
#         session['ans3'] = request.form.get('ans3')
#         session['ans4'] = request.form.get('ans4')
#         session['ans5'] = request.form.get('ans5')
#         session['ans6'] = request.form.get('ans6')
#         return redirect('/5')
#     else:
#         return redirect('/')
#

@app.route('/5')
def page_5():
    if 'logged' in session:
        return render_template("main.html", page=5)
    else:
        return redirect('/')


@app.route('/6')
def page_6():
    if 'logged' in session:
        return render_template("main.html", page=6)
    else:
        return redirect('/')


@app.route('/7')
def page_7():
    if 'logged' in session:
        return render_template("main.html", page=7)
    else:
        return redirect('/')


@app.route('/8')
def page_8():
    if 'logged' in session:
        return render_template("main.html", page=8)
    else:
        return redirect('/')


@app.route('/9')
def page_9():
    if 'logged' in session:
        return render_template("main.html", page=9)
    else:
        return redirect('/')


@app.route('/10')
def page_10():
    if 'logged' in session:
        return render_template("main.html", page=10)
    else:
        return redirect('/')


@app.route('/11')
def page_11():
    if 'logged' in session:
        return render_template("main.html", page=11)
    else:
        return redirect('/')


@app.route('/12')
def page_12():
    if 'logged' in session:
        return render_template("main.html", page=12)
    else:
        return redirect('/')


@app.route('/13')
def page_13():
    if 'logged' in session:
        return render_template("main.html", page=13)
    else:
        return redirect('/')


@app.route('/14')
def page_14():
    if 'logged' in session:
        return render_template("main.html", session = session, page=14)
    else:
        return redirect('/')


@app.route('/post15', methods=['POST'])
def post_15():
    if 'logged' in session:
        if request.form.get('option') != None:
            session['ans1'] = request.form.get('option')
        return redirect('/15')
    else:
        return redirect('/')


@app.route('/15')
def page_15():
    if 'logged' in session:
        return render_template("main.html", page=15, session = session)
    else:
        return redirect('/')


@app.route('/16')
def page_16():
    if 'logged' in session:
        return render_template("main.html", page=16)
    else:
        return redirect('/')


@app.route('/17')
def page_17():
    if 'logged' in session:
        return render_template("main.html", page=17)
    else:
        return redirect('/')


@app.route('/18')
def page_18():
    if 'logged' in session:
        return render_template("main.html", page=18)
    else:
        return redirect('/')
