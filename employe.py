employ=[]
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
        if len(employ)==0:
            emp=1
        else:
            emp=employ[-1]['emp_id']+1#slicing,last position 
        name=input("enter name:")
        age=int(input("enter age:"))
        pos=input("enter position:")
        salary=int(input("enter salary:"))
        employ.append({"emp_id":emp,"name":name,"age":age,"position":pos,"salary":salary})
    elif ch==2:
        print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format('emp_id','name','age','position','salary'))#for formatting the output to a table structure
        print('-'*70)
        for emp in employ:
            print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format(emp['emp_id'],emp['name'],emp['age'],emp['position'],emp['salary']))#iterating variable of loop(i=emp)
    elif ch==3:
        emp_id=int(input("enter emp id:"))
        f=0
        for emp in employ:
            if emp['emp_id']==emp_id:
                f=1
                newsalary=int(input("enter new salary:"))
                emp['salary']=newsalary
                print('salary updated')
        if f==0:
            print("no record found")
    elif ch==4:
        emp_id=int(input("enter emp_id:"))
        f=0
        for emp in employ:
            if emp['emp_id']==emp_id:
                f=1
                employ.remove(emp)
                print("record deleted")
        
    elif ch==5:
        emp_id=int(input("enter emp_id:"))
        f=0
        for emp in employ:
            if emp['emp_id']==emp_id:
                print("emp",emp)
                f=1
        if f==0:
            print("no record found")
        
    elif ch==6:
        print("exit")
        break
    else:
        print("invalid choice:")