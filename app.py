# all the functions are written here
from flask import *

from main import *

from model import app


@app.route('/')
def worksheet1():
    return render_template('18.html')


@app.route('/worksheet2', methods=['POST'])
def worksheet2():
    # print(request.form.get('comment1'))
    putDB(request.form.get('ans8'),request.form.get('ans9'),
          request.form.get('ans10'),request.form.get('ans11'),
          request.form.get('ans12'),request.form.get('ans13'),
          request.form.get('ans14'),request.form.get('ans15'))

    return render_template('preview.html')
#
#
if __name__ == '__main__':
    app.run()
# def main():
#     return render_template('index.html')
#
# def get_db():
#     """Opens a new database connection if there is none yet for the
#     current application context.
#     """
#     if not hasattr(g, 'sqlite_db'):
#         g.sqlite_db = connect_db()
#     return g.sql1b