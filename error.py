from config import app
from flask import render_template

@app.errorhandler(404)
def page_not_fount(error):
    return render_template("error.html", error = error)

