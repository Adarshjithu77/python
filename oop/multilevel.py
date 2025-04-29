# class A:
#     def a(self):
#         print("A is a method")

# class B(A):
#     def b(self):
#         print("B is b method ")

# class C(B):
#     def c(self):
#         print("C is c method")

# obj=C()
# obj.b()
# obj.c()


class principal:
    def collegehead(self):
        print('principal of the college')
    def maintanceofcollege(self):
        print("college maintaining")
    def staffsalary(self):
        print("staff salary calculating")

class HOD(principal):
    def examcreation(self):
        print("examcreation")
    def batcharrangemt(self):
        print("batcharrangement")

class Teacher(HOD):
    def examhandling(self):
        print("exam maintaing")
    def resultvalidating(self):
        print("result validating")

Ajitha=Teacher()
Ajitha.examcreation()
Ajitha.resultvalidating()


    