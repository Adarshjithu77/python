library=[]

def update():
    lib_id=int(input("enter lib_id:"))
    f=0
    for lib in library:
        if lib['lib_id']==lib_id:
            f=1
            updatedbookname=input("enter updatedbook name")
            lib['book_name']=updatedbookname
            newstock=int(input("enter new stock:"))
            lib['stock']=newstock
            newprice=int(input("enter newprice"))
            lib['price']=newprice
            print('bookname updated')
            print('stock updated')
            print('price updated')
            
    if f==0:
        print("no record found")