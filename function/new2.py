# # loop control statement
# # #
# #  for i in range(10):
# # #     print(i)
# # # # # # #     if i==5:
# # # # # # #         break
# # # # # # # print('hai')
# # # # # for i in range(10):
# # # # #     if i==5:
# # # # #         continue
# # # # #     print(i)
# # # # def data():
# # # #     print('hello')
# # # #     print('world')
# # # #     print('python')

# # # # data()
# # # # print("function completed")
# # # # data()
# # # # print("fun completed")
# # # # data()
# # # a=10 #global variable
# # # def data():
# # #     b=20  #loacal variable
# # #     print('hello',a)
# # #     print('hello',b)

# # # print('before fun ',a)
# # # data()
# # # print('after fun', a)
# # a=10
# # def data():
# #     b=20
# #     a=25
# #     global c
# #     c=5
# #     print("hello",a)
# #     print("hello",b)

# # print("before fun ",a)
# # data()
# # print('after fun',c)
# # def demo():
# #     return 'hello','world'

# # a,b=demo()
# # print(a)
# # def data(a,b):
# #     print(a)

# # data("hello",123)


# # def data(name,age):
# #     print('name',name)
# #     print('age',age)

# # data('manu',20)
# # data('ram',22)

# # data(age=20,name='akhil')


# # def data(name,age=20):
# #     print('name',name)
# #     print('age',age)

# # data(name='akhil')
# # data('akhil',22)

# # def fun(*a):
# #     print(a)

# # fun('sample',123)

# # def fun1(**a):
# #     print(a)
# # fun1(name='manu',age=22)


# calculaor using function

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

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
        add(a,b)
    elif choice==2:
        a,b=numbers()
        sub(a,b)
    elif choice==3:
        a,b=numbers()
        mul(a,b)
    elif choice==4:
        a,b==numbers()
        div(a,b)
    else:
        print("invalid choice")
        break