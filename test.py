from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '84519851'
app.config['MYSQL_DATABASE_DB'] = 'DP'
app.config['MYSQL_DATABASE_HOST'] = '104.131.52.198'
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

data = cursor.fetchall()



if __name__ == '__main__':
    app.run(debug=True)
