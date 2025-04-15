employ=[]

def search():
    emp1=int(input("enter emp_id:"))
    f=0
    for emp in employ:
        if emp['emp_id']==emp1:
            print("emp",emp)
            f=1
    if f==0:
        print("no record found")
