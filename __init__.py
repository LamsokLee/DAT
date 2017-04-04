from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run()
