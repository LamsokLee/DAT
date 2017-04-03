from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:84519851@104.131.52.198/DP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False