# for i in range(1,11):
#     # print(i)
#     print('hello')
# a=int(input("enter starting:"))
# b=int(input("enter ending:"))
# for i in range(a,b+1):
#     print(i)
# a=int(input("enter starting:"))
# b=int(input("enter ending: "))
# sum=10
# for i in range (a,b+1):
#     # sum=sum+i
#     sum+=i
# print("sum",sum)
# a=int(input("enter starting:"))
# b=int(input("enter ending"))
# prd=1
# for i in range(a,b+1):
#     prd*=i
# print("prd",prd)
# 
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
#         sum=sum+i
# print("sum",sum)
   
a=int(input("enter starting"))
b=int(input("enter ending"))
sum1=0
sum2=0
sum3=0
for i in range(a,b+1):
    if i%2==0:
        sum1+=i
    else:
        sum2+=i    
else:
    sum3+=i
    print(sum1,sum2,sum3)

   