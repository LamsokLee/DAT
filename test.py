from flask import Flask,session,render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('1.html')

if __name__ == 'main':
    app.run(debug=True)