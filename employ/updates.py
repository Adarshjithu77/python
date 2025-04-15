employ=[]

def update():
    emp_id=int(input("enter emp_id:"))
    f=0
    for emp in employ:
        if emp['emp_id']==emp_id:
            f=1
            newsalary=int(input("enter new salary:"))
            emp['salary']=newsalary
            print('salary updated')
    if f==0:
        print("no record found")