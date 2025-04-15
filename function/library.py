library=[]

def register():
    if len(library)==0:
        lib=1
    else:
        lib=library[-1]['lib_id']+1
    bookname=input("enter book name:")
    authorname=input("enter author name ")
    stock=int(input("enter the stock:"))
    price=int(input("enter price"))
    library.append({"lib_id":lib,"bookname":bookname,"authorname":authorname,"stock":stock,"price":price})

def view():
    print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format('lib_id','bookname','authorname','stock','price'))#for formatting the output to a table structure
    print('-'*70)
    for lib in library:
        print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format(lib['lib_id'],lib['bookname'],lib['authorname'],lib['stock'],lib['price']))

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

def search():
    search=input("enter lib_id or bookname or authorname:")
    if search.isdigit():#digit aanonn check chyn
        search=int(search)
    f=0
    for lib in library:
         if lib['lib_id']==search or lib['bookname']==search or lib['authorname']==search:#id anno name anno author name anno equal akunnth enn chck chyn condition
            print("lib",lib)
            f=1
    if f==0:
        print("no record found")

while True:
    print("""
1.register
2.view
3.update
4.delete
5.search
6.exit""")
    choice=int(input("enter your choice:"))
    if choice==1:
        register()
    elif choice==2:
        view()
    elif choice==3:
        update()
    elif choice==4:
        delete()
    elif choice==5:
        search()
    else:
        print("exit")
        break
        





