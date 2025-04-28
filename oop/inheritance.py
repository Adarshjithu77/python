class A:
    def a(self):
        print('A class a method')

class B(A):
    def b(self):
        print('B class b method')

obj=B()
obj.a()