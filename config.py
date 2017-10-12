from flask import Flask

# create the Flask application instance
app = Flask(__name__)

# configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:melomelo@localhost:3306/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# configure the Email server
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='mis573wpi@gmail.com',
    MAIL_PASSWORD='wpimstbi'
)
