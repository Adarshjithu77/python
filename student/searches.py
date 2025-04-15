def search(student):
    adm=int(input("enter adm no:"))
    f=0
    for std in student:
        if std['adm_no']==adm:
            print("std",std)
            f=1
        if f==0:
            print("no record found")