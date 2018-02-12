from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)

# configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:melomelo@localhost:3306/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
mail = Mail(app)
