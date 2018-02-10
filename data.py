# # initialize the objects in current session
# import datetime
# from flask import session
#
# def access():
#     session['ref_num'] = -1
#     session['email'] = ''
#     session['start'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     session['end'] = -1
#     session['logged'] = 1
#     session['test'] = 0
#     session['page'] = 0
#
#     for i in range(12):
#         session['ans' + str(i)] = 0
#     session['ans7'] = 50
#     session['ans12'] = ''
#     session['ans13'] = ''