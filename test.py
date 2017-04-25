# from flask import Flask
# from flask_mail import Mail, Message
#
# app = Flask(__name__)
# mail = Mail(app)
#
# app.config.update(
#     DEBUG=True,
#     # EMAIL SETTINGS
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_PORT=465,
#     MAIL_USE_SSL=True,
#     MAIL_USERNAME='mis573wpi@gmail.com',
#     MAIL_PASSWORD='Mis573umass'
# )
#
# mail = Mail(app)
#
#
# @app.route("/")
# def index():
#     msg = Message(
#         'Hello',
#         sender='mis573wpi@gmail.com',
#         recipients=
#         ['lli5@wpi.edu'])
#     msg.body = "This is the email body"
#     mail.send(msg)
#     return "Sent"
#
#
# if __name__ == "__main__":
#     app.run()
