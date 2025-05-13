import mysql.connector

con =mysql.connector.connect(
    host="localhost",
    user="abhi",
    password="abhi",
    port=3306,
    database="abhi"
)

cur =con.cursor()
con.autocommit =True

data = cur.fetchall()
for i in data:
    print(i)
