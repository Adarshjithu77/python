employ=[]
from registers import register
from views import view
from updates import update
from deletes import delete
from searches import search
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
        register(employ)
    elif choice==2:
        view(employ)
    elif choice==3:
        update(employ)
    elif choice==4:
        delete(employ)
    elif choice==5:
        search(employ)
    else:
        print("exit")
        break