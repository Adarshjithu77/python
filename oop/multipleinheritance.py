# class A:
#     def a(self):
#         print("A is a method")

# class B:
#     def b(self):
#         print("B is b method ")

# class C(A,B):
#     def c(self):
#         print("C is c method")

# obj=C()
# obj.a()
# obj.b()
# obj.c()

class school():
    def hour(self):
        print("8hours")
    def daywise(self):
        print("class taken 8subjects")
    def teachers(self):
        print("school teachers")

class tution():
    def hours(self):
        print("2 hour,morning and evening")
    def daywises(self):
        print("2 subjects class taken")
    def teacher(self):
        print("tution teachers")

class student(school,tution):
    def studying(self):
        print("study in school and tution classes")
    def exam(self):
        print("attend the exams in school and tution")

Adarsh=student()
Adarsh.hour()
Adarsh.daywise()
Adarsh.teachers()
Adarsh.hours()
Adarsh.daywises()
Adarsh.teacher()
Adarsh.studying()
Adarsh.exam()