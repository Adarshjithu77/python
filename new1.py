student=[]
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
        if len(student)==0:
            adm=1
        else:
            adm=student[-1]['adm_no']+1
        name=input("enter name:")
        age=int(input("enter age:"))
        cur=input("enter course:")
        fee=int(input("enter fee:"))
        student.append({"adm_no":adm,"name":name,"age":age,"course":cur,"fee":fee})
    elif ch==2:
        print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format('adm_no','name','age','course','fee'))#for formatting the output to a table structure
        print('-'*70)
        for std in student:
            print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format(std['adm_no'],std['name'],std['age'],std['course'],std['fee']))
    elif ch==3:
        print("update")
    elif ch==4:
        print("delete")
    elif ch==5:
        print("search")
    elif ch==6:
        print("exit")
        break
    else:
        print("invalid choice:")