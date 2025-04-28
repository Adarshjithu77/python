def register(employ):
    if len(employ)==0:
        emp=1
    else:
        emp=employ[-1]['emp_id']+1
    name=input("enter name:")
    age=int(input("enter age"))
    pos=input("enter position:")
    salary=int(input("enter salary"))
    employ.append({"emp_id":emp,"name":name,"age":age,"position":pos,"salary":salary})
