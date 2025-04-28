

def search(library):
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
