add=lambda a,b:a+b
print(add(10,5))



add =lambda a,b:(a+b)

sub=lambda a,b:(a-b)

mul=lambda a,b:(a*b)

div=lambda a,b:(a/b)

def numbers():
    a=int(input("enter a:"))
    b=int(input("enetr b:"))
    return a,b

while True:
    print("""
1.add
2.substract
3.multiplication
4.division """)
    choice=int(input("enter your choice:"))
    if choice==1:
        a,b=numbers()
        print(add(a,b))
    elif choice==2:
        a,b=numbers()
        print(sub(a,b))
    elif choice==3:
        a,b=numbers()
        print(mul(a,b))
    elif choice==4:
        a,b=numbers()
        print(div(a,b))
    else:
        print("invalid choice")
        break



