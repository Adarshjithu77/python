import sqlite3

con = sqlite3.connect("qstn6.db")
con.execute("create table employ(users text,id int,name text,email text)")  
con.commit() 


