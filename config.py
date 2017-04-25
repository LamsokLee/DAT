from flask import Flask

# create the Flask application instance
app = Flask(__name__)

# configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:84519851@104.131.52.198/DP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# configure the Email server
app.config['MAIL_SERVER']   =   'smtp.gmail.com'
app.config['MAIL_PORT']     =   465
app.config['MAIL_USE_SSL']  =   True,
app.config['MAIL_USERNAME'] =   'mis573wpi@gmail.com',
app.config['MAIL_PASSWORD'] =   'Mis573umass'