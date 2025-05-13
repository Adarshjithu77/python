# class A:
#     def a(self):
#         print('A is a method')

# class B(A):
#     def b(self):
#         print('B is b method')

# class C(A):
#     def c(self):
#         print('C is c method')

# class D(A):
#     def d(self):
#         print('D is d method')

# obj = B()
# obj1 = C()
# obj2 = D()
# obj1.a()


class Bangloreuniversity():
    def exampreparing(self):
        print('exam preparing')
    def resultpublishing(self):
        print('result maintaing')
    def syllabusmaintaing(self):
        print('syllabusmaintaing')
    def overallmaintance(self):
        print('overallmaintance')

class HKBK(Bangloreuniversity):
    def exam(self):
        print('exam ')
    def sylabus(self):
        print('syllabus conducting')
    def teacher(self):
        print('classes taken and exam coordinator ')

class Acharya(Bangloreuniversity):
    def exams(self):
        print('exams')
    def syllabus(self):
        print('syllabus conducting')
    def teachers(self):
        print('classes taken and exam coordinator')

class seacollege(Bangloreuniversity):
    def examss(self):
        print('examss')
    def syllabuss(self):
        print('syllabuss conducting')
    def teacherss(self):
        print('classes taken and exam coordinator')

student=HKBK()
students=Acharya()
studentss=seacollege()
student.exam()
student.sylabus()
student.teacher()
students.exams()
students.syllabus()
students.teachers()
studentss.examss()
studentss.syllabuss()
studentss.teacherss()
