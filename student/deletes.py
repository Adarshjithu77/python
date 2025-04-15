def delete(student):
    adm=int(input("enter adm no:"))
    f=0
    for std in student:
        if std['adm_no']==adm:
            f=1
            student.remove(std)
            print("record deleted")
        if f==0:
            print("no record found")