# all the functions are written here
from flask import *

from main import *

from model import app


@app.route('/')
def worksheet1():
    return current_app.send_static_file('18.html')


@app.route('/worksheet2', methods=['POST'])
def worksheet2():
    # print(request.form.get('comment1'))
    putDB(request.form.get('comment1'))
    return current_app.send_static_file('1.html')
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

