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
    putDB(request.form.get('comment1'),request.form.get('comment2'),
          request.form.get('comment3'),request.form.get('comment4'),
          request.form.get('comment5'),request.form.get('comment6'),
          request.form.get('comment7'),request.form.get('comment8'),
          request.form.get('comment9'),request.form.get('comment10'))

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