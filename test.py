from flask import render_template, request
from database import *
from config import app


###############
# for testing #
###############

@app.route("/test")
def test():
    return render_template('test.html', session = session)

@app.route("/testresult", methods=['POST'])
def testresult():
    result = db.engine.execute(request.form.get('testvar'))
    return render_template('test.html', result=result)

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
        return render_template("sql.html", result='error')
    return render_template("sql.html", result=result)
