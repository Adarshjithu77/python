# import sqlite3

# # con = sqlite3.connect("sample.db")

# try:
#     con.execute("create table Student(roll int,name text,age int)")  #text-string
#     con.commit() #save
# except:
#     pass

# con.execute("insert into Student(roll,name,age)values(5,'ranu',21),(6,'appuse',22)")
# con.commit()

# import sqlite3
# con = sqlite3.connect("sample.db")

# roll=int(input("enter roll"))
# name=input("enter name")
# age=int(input("enter age"))
# con.execute("insert into Student(roll,name,age)values(?,?,?)",(roll,name,age)) #insert chynda variable-?,?,?

# con.commit()


# import sqlite3

# con = sqlite3.connect("sample.db")

# data =con.execute("select roll,name,age from Student") #read method
# print('{:<10}{:<10}{:<10}'.format('roll','name','age'))

# for i in data:
#     print('{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2]))


# import sqlite3

# con = sqlite3.connect("sample.db")

# data =con.execute("select * from Student where roll=1 or name='manu'") #where use chynth condition kodukn vndi
# for i in data:
#     print(i)


# import sqlite3

# con = sqlite3.connect("sample.db")

# data =con.execute("select * from Student order by roll ") #order by use chyunth ascending decending akn vndi decending akkn last 'desc' use chynm
# for i in data:
#     print(i)


# import sqlite3

# con = sqlite3.connect("sample.db")

# roll = int(input("enter roll"))
# data =con.execute("select * from Student where roll=?",(roll,))
# print('{:<10}{:<10}{:<10}'.format('roll','name','age'))


# con.commit()
# for i in data:
#     print('{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2]))
    

# import sqlite3

# con = sqlite3.connect("sample.db")

# data = con.execute("select * from Student where name like 'a%'")

# for i in data:
#     print(i)

# import sqlite3

# con = sqlite3.connect("sample.db")

# data = con.execute("select * from Student where name like '____'")

# for i in data:
#     print(i)

# import sqlite3

# con = sqlite3.connect("sample.db")

# data=con.execute("update Student set name='Sachu' where roll=8")
# data1=con.execute("select * from Student where roll=8")

# con.commit()

# for i in data1 :
#     print(i)


# import sqlite3  #update

# con = sqlite3.connect("sample.db")

# roll = int(input("enter roll"))
# data=con.execute("update Student set name='abhi' where roll=?",(roll,))
# data1=con.execute("select * from Student where roll=?",(roll,))

# con.commit()

# for i in data1 :
#     print(i)

# import sqlite3  #delete

# con = sqlite3.connect("sample.db")
 
# data=con.execute("delete from Student where roll=5")
# data1=con.execute("select * from Student")
# con.commit()

# for i in data1:
#     print(i)

# import sqlite3  

# con = sqlite3.connect("sample.db")
 
# con.execute("create table mark(roll int,sub text,mark int)")
# con.commit()

# con.execute("insert into mark(roll,sub,mark)values(1,'eng',65),(2,'maths',75)")
# con.commit()


# data= con.execute("select Student.roll,Student.name,Student.age,mark.sub,mark.mark from Student join mark on Student.roll=mark.roll")
# for i in data:
#     print(i)

# aggregation

# import sqlite3  

# con = sqlite3.connect("sample.db")

# data=con.execute("select sum(mark) from mark")
# print(data)
# for i in data:
#     print(i)

# data =con.execute("select count(mark) from mark")
# print(data)
# for i in data:
#     print(i)

# data=con.execute("select min(mark) from mark")
# print(data)
# for i in data:
#     print(i)

# data=con.execute("select max(mark) from mark")
# print(data)
# for i in data:
#     print(i)

# data=con.execute("select avg(mark) from mark")
# print(data)
# for i in data:
#     print(i)

# data=con.execute("select max(roll) from Student")
# print(data)
# for i in data:
#     print(i)

# grouping

import sqlite3  

con = sqlite3.connect("sample.db")

data=con.execute("select roll,name,max(age) from Student group by name")
for i in data:
    print(i)