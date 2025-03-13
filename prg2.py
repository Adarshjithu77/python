a=int(input("enter number of unit"))
if a<=100:
    charge=a*0
    print("price of the unit is 0",charge)
elif a<=200:
    charge=(a-100)*5
    print("per unit is  5rs",charge)
else:
    charge=((a-200)*10)+(100*5)
    print("print unit is 10rs",charge)
