import sqlite3
con = sqlite3.connect("qstn8.db")
# con.execute("create table product(id int,name text,price int)")  
# con.commit() 

# id=int(input("enter id"))
# name=input("enter name")
# price=int(input("enter price"))
# con.execute("insert into product(id,name,price)values(?,?,?)",(id,name,price))
# con.commit()

data = con.execute("select * from product ")

for i in data:
    print(i)
