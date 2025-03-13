a=int(input("enter a cost price of bike:"))
if a>100000:
    tax=0.15*a
    print("road tax  to be paid:",tax)
elif a>50000:
    tax=0.10*a
    print("road tax to be paid:",tax)
else:
    tax=0.05*a
    print("road tax to be paid:",tax)
