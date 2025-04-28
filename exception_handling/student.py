student=[]
while True:
    print("""
1.Register
2.view
3.update
4.delete
5.search
6.exit""")
    while True:
        try:
            ch=int(input("enter your choice:"))
            break
        except:
            print("enter a number")
            
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
        adm=int(input("enter adm no:"))
        f=0
        for std in student:
            if std['adm_no']==adm:
                f=1
                newfee=int(input("enter new fee:"))
                std['fee']=newfee
                print('fee updated')
        if f==0:
            print("no record found")
    elif ch==4:
        adm=int(input("enter adm no:"))
        f=0
        for std in student:
            if std['adm_no']==adm:
                f=1
                student.remove(std)
                print("record deleted")
        if f==0:
            print("no record found")
    elif ch==5:
        adm=int(input("enter adm no:"))
        f=0
        for std in student:
            if std['adm_no']==adm:
                print("std",std)
                f=1
        if f==0:
            print("no record found")
    elif ch==6:
        print("exit")
        break
    else:
        print("invalid choice:")