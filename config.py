from flask import Flask

# create the Flask application instance
app = Flask(__name__)

# configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:84519851@104.131.52.198/DP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# configure the Email server
# app.config['']