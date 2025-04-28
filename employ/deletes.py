def delete(employ):
    emp1=int(input("enter emp_id:"))
    f=0
    for emp in employ:
        if emp['employ_id']==emp1:
            f=1
            employ.remove(emp)
            print("record deleted")
    if f==0:
        print("no record found")