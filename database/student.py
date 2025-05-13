import sqlite3

con = sqlite3.connect("student.db")
try:
    con.execute("create table student(adm_no int,name text,age int,course text,fee int)") 
    con.commit()
except:
    pass


while True:
    print("""
1.Register
2.view
3.update
4.delete
5.search
6.exit""")
    ch=int(input("enter your choice:"))
    if ch ==1:
        adm=int(input("enter adm_no"))
        name=input("enter name:")
        age=int(input("enter age:"))
        cur=input("enter course:")
        fee=int(input("enter fee:"))
        con.execute("insert into student(adm_no,name,age,course,fee)values(?,?,?,?,?)",(adm,name,age,cur,fee)) 
        con.commit()
    elif ch==2:
        student=con.execute("select * from student ")
        print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format('adm_no','name','age','course','fee'))
        print('-'*70)
        for std in student:
            print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format(std[0],std[1],std[2],std[3],std[4]))
    elif ch==3:
        adm=int(input("enter adm no:"))
        newfee=int(input("enter newfee:"))
        con.execute("update student set fee=? where adm_no=?",(newfee,adm))
        
        con.commit()
    elif ch==4:
        adm=int(input("enter adm_no"))
        con.execute("delete from student where adm_no=?",(adm,))
        con.commit()
    
    elif ch==5:
        adm=int(input("enter adm_no"))
        student=con.execute("select * from student where adm_no=?",(adm,))

        for std in student:
            print(std)

    elif ch==6:
        print("exit")
        break
    else:
        print("invalid")
        
            


        
