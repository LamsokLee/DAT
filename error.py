from config import app
from flask import render_template

@app.route('/error')
def error():
    return render_template("error.html")
