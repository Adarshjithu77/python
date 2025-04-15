library=[]

def delete():
    lib_id=int(input("enter lib_id"))
    f=0
    for lib in library:
        if lib['lib_id']==lib:
            f=1
            library.remove(lib)
            print("record deleted")
    if f==0:
        print("no record found")