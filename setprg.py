# {1, 2, 3, 4}
# s={1,2,3,4,3,2}
# print(s)

# {'hello'}
# s={'hello'}
# print(s)

# {1, (2, 3), 4}
# s={1,(2,3),4}
# print(s)

# s={1,2,3,4,[1,2]}
# print(s)

# 1
# 2
# 3
# 4
# s={1,2,3,4}
# for i in s:
#     print(i)

# yes
# s={1,2,3,4}
# if 4 in s:
#      print('yes')
# else:
#       print('no')

s={1,2,3,4}
# print(s)
# s.add(10)
# s.add('6')
# s.remove(13)
# s.discard(12)
# print(s)

# print(s.difference({3,4,5,6,7}))
# print(s.intersection({3,4,5,6,7}))
# print(s.union({3,4,5,6,7}))
# print(s.isdisjoint({6,7}))
# print(s.issubset({1,2,3,4,5,6,7}))
# print(s.issuperset({1,2,3}))
# s.pop()
# print(s)

# s.intersection_update({3,4,5,6,7,1})
# print(s)
# (s.sprintymmetric_difference({2,3,4,6,7,8}))

# enter a number:5
# enter name:adarsh
# {'adarsh'}
# enter name:ajith
# {'adarsh', 'ajith'}
# enter name:jithu
# {'adarsh', 'ajith', 'jithu'}
# enter name:nanadhu
# {'nanadhu', 'adarsh', 'ajith', 'jithu'}
# enter name:anandhu
# {'anandhu', 'jithu', 'nanadhu', 'adarsh', 'ajith'}
# s=set()
# a=int(input("enter a number:"))
# for i in range(0,a):
#     b=input("enter name:")
#     s.add(b)
#     print(s)

python=set()
php=set()
java=set()
a=int(input("enter how many students in python:"))
for i in range(0,a):
    b=input("enter python students name")
    python.add(b)
c=int(input("enetr how many students in php"))
for j in range(0,c):
    d=input("enter php students name:")
    php.add(d)
e=int(input("eneter how many students in java:"))
for k in range(0,e):
    f=input("enter java students name:")
    java.add(f)
print("python",python)
print("php",php)
print("java",java)
