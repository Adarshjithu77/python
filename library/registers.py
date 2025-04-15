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
