a=int(input("enter a number:")) 
b=a%10
print(b)
if b % 3==0:
    print("the last digit is divisible by 3")
else:
    print("the last digit is not divisible by 3")