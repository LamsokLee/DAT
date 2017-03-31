#import mysql module
import mysql.connector

#Connecting to our database
con = mysql.connector.connect(user='root',password='84519851',host='104.131.52.198',database='DP')

#creating cursor to use its various methods further
cur = con.cursor()

#this is our mysql query
cur.execute("""select * from Answers""")

#It is going to fetch the executed mysql query into rows.
#Hence assigning it to row
row = cur.fetchall()

#printing the result
print(row)

#closing the function
cur.close()

import MySQLdb
conn = MySQLdb.connect(host= "104.131.52.198.",
                  user="root",
                  passwd="84519851",
                  db="DP")
x = conn.cursor()

try:
   x.execute("""INSERT INTO anooog1 VALUES (%s,%s)""",(188,90))
   conn.commit()
except:
   conn.rollback()

conn.close()