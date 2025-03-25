# a=int(input('enter the salary:'))
# b=int(input('enter the year of experience:'))
# if b>5:
#     bonus=a*0.05
#     print("eligible for bonus",bonus)
# else:
#     print("not eligible for bonus")


# a=int(input("enetr number of units:"))
# if a<=100:
#     charge=a*0
#     print("the unit price is zero",charge)
# elif a<=200:
#     charge=(a-100)*5
#     print("the unit price is 5",charge)
# else:
#     charge=((a-200)*10)+(100*5)
#     print("the unit charge is 10 rs")

# a=int(input("eneter the number between 1 to 7:"))
# if a==1:
#     print("sunday")
# elif a==2:
#     print("monday")
# elif a==3:
#     print("tuesday")
# elif a==4:
#     print("wenesday")
# elif a==5:
#     print("thursday")
# elif a==6:
#     print("friday")
# elif a==7:
#     print("saturday")

# a=input("enter the city name:")
# if a=="delhi":
#     print("red fort")
# elif a=="agra":
#     print("taj mahal")
# elif a=="jaipur":
#     print("jal mahal")
# else:
#     print("city name is not defined:")

# a=int(input("enter the  number"))
# b=a%10
# print(b)
# if b%3==0:
#     print("the last number is divisible by 3")
# else:
#     print("the last number is not divisible by 3")

# a=int(input("enter a cost price of bike:"))
# if a>100000:
#     tax=0.15*a
#     print("road tax  to be paid:",tax)
# elif a>50000:
#     tax=0.10*a
#     print("road tax to be paid:",tax)
# else:
#     tax=0.05*a
#     print("road tax to be paid:",tax)

# for i in range(1,11):
#     print('hello')

# a=int(input("starting"))
# b=int(input("ending"))
# for i in range(a,b+1):
#     print(i)

# a=int(input("starting"))
# b=int(input("ending"))
# sum=0
# for i in range(a,b+1):
#     sum+=i
# print("sum",sum)

# a=int(input("starting"))
# b=int(input("ending"))
# prd=1
# for i in range(a,b+1):
#     prd*=i
# print("prd",prd)

# a=int(input('starting'))
# b=int(input("ending"))
# for i in range(a,b+1):
#     if i%2==1:
#         print(i)
# a=int(input('starting'))
# b=int(input("ending"))
# for i in range(a,b+1):
#     if i%2==0:
#         print(i)
# a=int(input("starting"))
# b=int(input("ending"))
# sum=0
# for i in range(a,b+1):
#     if i%2==1:
#         sum+=i
# print("sum",sum)
# a=int(input("starting"))
# b=int(input("ending"))
# sum=0
# for i in range(a,b+1):
#     if i%2==0:
#         sum+=i
# print("sum",sum)

# a=int(input("starting"))
# b=int(input("ending"))
# sum1=0
# sum2=0
# sum3=0
# for i in range(a,b+1):
#     if i%2==0:
#         sum1+=i
#     else:
#         sum2+=i
#     sum3=sum3+i
# print(sum1,sum2,sum3)
# a=int(input("enter a number:"))
# prd=1
# for i in range(1,a+1):
#     prd=prd*i
# print("prd",prd)
# a=int(input("first number"))
# b=int(input("second number"))
# for i in range(a,b+1):
#     if i%3==0:
#         print(i)

# a=int(input("enter a number"))
# for i in range(1,11):
#     print(i,'*',a,'=',i*a)
# a='python' 
# rev=''
# for i in a:
#     rev=i+rev
# print(rev)

# i=1
# while i<=10:
#     print(i)
#     i+=1

# i=0
# while i<=10:
#     print('hello')
#     i+=1

# a=int(input('starting'))
# b=int(input('ending'))
# while a<=b:
#     print(a)
#     a+=1

# a=int(input('starting'))
# b=int(input('ending'))
# sum=0
# while a<=b:
#     sum+=a
#     a+=1
# print(sum)

# a=int(input("enter starting:"))
# b=int(input("enter ending"))
# prd=1
# while a<=b:
#     prd*=a
#     a+=1
# print("prd",prd)
    
# a=int(input("starting"))
# b=int(input("ending"))
# while a<=b:
#     if a%2==1:
#         print(a)
#     a+=1

# a=int(input("starting"))
# b=int(input("ending"))
# while a<=b:
#     if a%2==0:
#         print(a)
#     a+=1

# a=int(input("starting"))
# b=int(input("ending"))
# sum=0
# while a<=b:
#     if a%2==1:
#         sum+=a
#     a+=1
# print("sum",sum)

# a=int(input("starting"))
# b=int(input("ending"))
# sum=0
# while a<=b:
#     if a%2==0:
#         sum+=a
#     a+=1
# print("sum",sum)

# a=int(input("starting"))
# b=int(input("ending"))
# sum1=0
# sum2=0
# sum3=0
# while a<=b:
#     if a%2==1:
#         sum1+=a
#     else:
#         sum2+=a
#     sum3+=a
#     a+=1
# print("sum1,sum2,sum3",sum1,sum2,sum3)

# a=int(input("starting"))
# b=int(input("ending"))
# while a<=b:
#     if a%3==0:
#         print(a)
#     a+=1

# i=1
# a=int(input("enter a number: "))
# while i<=10:
#     print(i,"*",a,"=",i*a)
#     i+=1

# a=int(input("enter a number"))
# count=0
# while a>0:
#     count+=1
#     a//=10
# print("number of digits",count)