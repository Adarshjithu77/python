# a=10
# b=20
# print(a+b)
# a=[1,2,3]
# b=[2,4,6]
# print(a+b)
# a=10
# a+=20
# print(a)
# a=20
# a-=10
# print(a)
# a=10
# a*=10
# print(a)
# a=10
# a/=3
# print(a)
# a=10
# a//=3
# print(a)
# a=10
# b=20
# print(a==b)
# a=10
# b=20
# print(a<b)
# a=10
# b=20
# print(a>b)
# a=10
# b=20
# print(a<=b)
# a=10
# b=20
# print(a>=b)
# a=[1,2,3]
# b=[1,2,3]
# print(a)
# a=[1,2,3]
# b=[1,2,3]
# print(b)
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
# a=[1,2,3]
# b=[1,2,3]
# print(a is not b)
# a='hello'
# print('e'in a)
# print('o'in a)
# a=10
# b=11
# if a==b:
#     print('equal')
# a=10
# b=11
# if a==b:
#     print(' equal')
# else:
#     print('not equal')

# a=10
# b=5
# if a>b:
#     if a<20:
#         print('value greater than 5 and less than 20')
#     else:
#         print('value greater than 5 and not less than 20')
# else:
#     print('not greater than 5')
# Roll_no=12
# name="achu"
# weight=56
# print("Roll_no")
# print("name")
# print("weight")
# Roll_no=12
# name="achu"
# weight=56
# print("Roll_no",Roll_no)
# print("name",name)
# print("weight",weight)
# a=int(input("enter a first number:"))
# b=int(input("enter a second number:"))
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")
# a=int(input("enter a first number:"))
# b=int(input("enter a second number:"))
# c=int(input("enter a third number:"))
# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater")
# a=int(input("enter a number between 1 to 7"))
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
# else:
#     print("days is not defined")
# a=int(input("enter a number"))
# b=a%10
# print(b)
# if b%3==0:
#     print(" last digit is divisible by 3")
# else:
#     print("last is not divisible by 3")
# a=input("enter the city name:")
# if a=="delhi":
#     print("Redfoert")
# elif a=="agra":
#     print("Taj Mahal")
# elif a=="jaipur":
#     print("Jal mahal")

# a=int(input("enter a the unit"))
# if a<=100:
#     charge=a*0
#     print("the unit is 0",charge)
# elif a<=200:
#     charge=(a-100)*5
#     print("per unit 5 rs",charge)
# else:
#     charge=((a-200)*10+(100*5))
#     print("per unit is 10rs",charge)
# a=int(input("enter a price of bike"))
# if a>100000:
#     tax=0.15*a
#     print("tax paid",tax)
# elif a>50000:
#     tax=0.10*a
#     print("tax is paid",tax)
# else:
#     tax=0.05*a
#     print("tax is not paid",tax)
# a=int(input("enter the salary"))
# b=int(input("enter the year of experience"))
# if b>5:
#     bonus=a*0.05
#     print("eligible for bonus",bonus)
# else:
#     print("not eligible for bonus")
# a=int(input("enter the number between 1 to 12"))
# if a==1:
#     print("january")
# elif a==2:
#     print("february")
# elif a==3:
#     print("march")
# elif a==4:
#     print("april")
# elif a==5:
#     print("may")
# elif a==6:
#     print("june")
# elif a==7:
#     print("july")
# elif a==8:
#     print("august")
# elif a==9:
#     print("september")
# elif a==10:
#     print("october")
# elif a==11:
#     print("november")
# elif a==12:
#     print("december")
# else:
#     print("the is not defined")
# for i in range(1,11):
#     print('hello')
# a=int(input("enter starting"))
# b=int(input("enter ending"))
# for i in range(a,b+1):
#     print(i)

# a=int(input("enter starting"))
# b=int(input("enter ending"))
# sum=0
# for i in range(a,b+1):
#     sum+=i
# print("sum",sum)
# a=int(input("enter starting"))
# b=int(input("enter ending"))
# prd=1
# for i in range(a,b+1):
#     prd*=i
# print("product",prd)
# a=int(input("enter starting"))
# b=int(input("enter ending"))
# for i in range(a,b+1):
#     if i%2==1:
#         print(i)
# a=int(input("enter starting"))
# b=int(input("enter ending"))
# sum=0
# for i in range(a,b+1):
#     if i%2==1:
#         sum+=i
# print("sum",sum)
# a=int(input("enter starting"))
# b=int(input("enter ending"))
# sum1=0
# sum2=0
# sum3=0
# for i in range(a,b+1):
#     if i%2==1:
#         sum1+=i
#     else:
#         sum2+=i
#     sum3+=i
# print(sum1,sum2,sum3)

# a=int(input("enter a number:"))
# prd=1
# for i in range(1,a+1):
#     prd=prd*i
# print("prd",prd)
# a=int(input("enter a first number:"))
# b=int(input("enter a second number"))
# for i in range(a,b+1):
#     if i%3==0:
#         print(i)
# a=int(input("enter a number: "))
# for i in range(1,11):
#     print(i,"*",a,"=",i*a)
# a="python"
# for i in a:
#     print(i)
# rev=''
# a="python"
# for i in a:
#     rev=i+rev
# print(rev)
# i=1
# while i<=10:
#     print(i)
#     i+=1
# i=1
# while i<=10:
#     print('hello')
#     i+=1
# a=int(input("enter starting"))
# b=int(input("enter ending"))
# while a<=b:
#     print(a)
#     a+=1
# a=int(input("enter starting"))
# b=int(input("enter ending"))
# sum=0
# while a<=b:
#     sum+=a
#     a+=1
# print("sum",sum)
# a=int(input("enter starting"))
# b=int(input("enter ending"))
# prd=1
# while a<=b:
#     prd*=a
#     a+=1
# print("product",prd)
# a=int(input("enter starting"))
# b=int(input("enter ending"))
# while a<=b:
#     if a%2==1:
#         print(a)
#     a+=1
# a=int(input("enter starting"))
# b=int(input("enter ending"))
# sum=0
# while a<=b:
#     if a%2==1:
#         sum+=a
#     a+=1
# print("sum",sum)
# a=int(input("enter starting"))
# b=int(input("enter ending"))
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
# print(sum1,sum2,sum3)
# a=int(input("enter a first number:"))
# b=int(input("enter a second number"))
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
# a=int(input("enter a number"))
# rev=0
# while a>0:
#     d=a%10
#     a=a//10
#     rev=(rev*10)+d
# print(rev)

# a=int(input("enter a number"))
# sum=0
# while a>0:
#     d=a%10
#     a//=10
#     sum=sum+d
# print("sum of the digit",sum)

   

  

   