def register(student):
    if len(student)==0:
        adm=1
    else:
        adm=student[-1]['adm_no']+1
    name=input("enter name:")
    age=int(input("enter age"))
    cur=input("enter course name:")
    fee=int(input("enter fees"))
    student.append({"adm_no":adm,"name":name,"age":age,"course":cur,"fee":fee})