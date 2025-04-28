

def view(library):
    print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format('lib_id','bookname','authorname','stock','price'))#for formatting the output to a table structure
    print('-'*70)
    for lib in library:
        print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format(lib['lib_id'],lib['bookname'],lib['authorname'],lib['stock'],lib['price']))