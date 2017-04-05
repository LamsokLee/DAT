from flask import Flask, render_template

from flask import *

from main import *

from model import app

# app = Flask(__name__)
data = answers()


@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/1')
def page_1():
    return render_template("1.html")


@app.route('/2')
def page_2():
    return render_template("2.html")


@app.route('/3')
def page_3():
    return render_template("3.html")


@app.route('/4')
def page_4():
    return render_template("4.html")


@app.route('/5')
def page_5():
    data.ans1 = request.form.get('ans1')
    data.ans2 = request.form.get('ans2')
    data.ans3 = request.form.get('ans3')
    data.ans4 = request.form.get('ans4')
    data.ans5 = request.form.get('ans5')
    data.ans6 = request.form.get('ans6')
    return render_template("5.html")


@app.route('/6')
def page_6():
    return render_template("6.html")


@app.route('/7')
def page_7():
    return render_template("7.html")


@app.route('/8')
def page_8():
    return render_template("8.html")


@app.route('/9')
def page_9():
    return render_template("9.html")


@app.route('/10')
def page_10():
    return render_template("10.html")


@app.route('/11')
def page_11():
    return render_template("11.html")


@app.route('/12')
def page_12():
    return render_template("12.html")


@app.route('/13')
def page_13():
    return render_template("13.html")


@app.route('/14')
def page_14():
    return render_template("14.html")


@app.route('/15')
def page_15():
    return render_template("15.html")


@app.route('/16')
def page_16():
    return render_template("16.html")


@app.route('/17')
def page_17():
    return render_template("17.html")


@app.route('/18')
def page_18():
    return render_template("18.html")


@app.route('/preview', methods=['POST'])
def page_preview():
    data.ans8 = request.form.get('ans8')
    data.ans9 = request.form.get('ans9')
    data.ans10 = request.form.get('ans10')
    data.ans11 = request.form.get('ans11')
    data.ans12 = request.form.get('ans12')
    data.ans13 = request.form.get('ans13')
    data.ans14 = request.form.get('ans14')
    data.ans15 = request.form.get('ans15')
    data.ans16 = request.form.get('ans16')
    putDB(data)

    return render_template('preview.html', a1=data.ans1, a2=data.ans2, a3=data.ans3, a4=data.ans4, a5=data.ans5,
                           a6=data.ans6, a8=data.ans8, a9=data.ans9, a10=data.ans10,
                           a11=data.ans11, a12=data.ans12, a13=data.ans13, a14=data.ans14, a15=data.ans15, a16=data.ans16)


@app.route('/report')
def page_report():
    # TODO: commit all the data into the database
    # TODO: retrieve the reference number from database and show it on this page.
    return render_template("report.html")


if __name__ == "__main__":
    app.run()
