import mysql.connector

con =mysql.connector.connect(
    host="localhost",
    user="adarsh",
    password="adarsh",
    port=3306,
    database="adarsh"
)

cur =con.cursor()
con.autocommit =True

# cur.execute("create table Student(roll int,name text,age int)")

cur.execute("insert into Student(roll,name,age)values(2,'arjun',22)")

# cur.execute("update Student set name='aravind' where roll=1")

# cur.execute("delete from Student where roll=1 ")

cur.execute("select * from Student")
data = cur.fetchall()
for i in data:
    print(i)





