# class Demo:
#     def display(self):
#         print('demo class dispaly fun')

# class Demo1(Demo):
#     def display(self):
#         print('demo1 class display fun')

# obj = Demo1()
# obj.display()

# class Demo:
#     def display(self):
#         print('demo class display fun')

# class Demo1(Demo):
#     def display(self):
#         print('demo1 class display fun')
#         super().display()

# obj=Demo1()
# obj.display()

# class Demo:
#     def __init__(self):
#         print('diplay fun')

# class Demo1(Demo):
#     def __init__(self):
#         super().__init__()
#         print('display fun2')   


# obj=Demo1()

class Demo:
    def __init__(self,a):
        print('diplay fun',a)

class Demo1(Demo):
    def __init__(self,b):
        print('display fun2',b)
        super().__init__(10)

obj=Demo1(25)   

        
