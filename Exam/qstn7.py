import sqlite3
con = sqlite3.connect("qstn7.db")
con.execute("create table products(id int,name text,price int)")  
con.commit() 

id=int(input("enter id"))
name=input("enter name")
price=int(input("enter price"))
con.execute("insert into products(id,name,price)values(?,?,?)",(id,name,price))
con.commit()


