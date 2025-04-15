def update(student):
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