# try:
#     print(a)
# except:
#     print('an error')

# try:
#     print(a)
# except:
#     print('an error')
# else:
#     print('no error')
# finally:
#     a1=10
#     b1=20
#     print(a1)
#     print(b1)

# while True:
#     try:
#         a=int(input("enter a number"))
#         print(a)
#         break
#     except:
#         print("enter a number value")
l=[5,3,'abc',5]
sum=0
for i in l:
    try:
        sum+=i
    except:
        pass
print("sum",sum)

