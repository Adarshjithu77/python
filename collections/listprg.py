# l=[1,2,3,4]
# print(l[0])
# l=[1,2,3,4]
# print (l[1:4])
# l=[1,2,3,4]
# for i in l:
#     print(i)
# l=[1,2,3,4]
# l[0]=10
# if 10 in l:
#     print('yes')
# else:
#     print('no')
# l=[1,2,'abc']
# l.append(3)
# print(l)
# l=[1,2,'abc',3]
# l.append([1,2])
# print(l)
# l=[1,2,'abc',3,[1,2]]
# l.extend([3,4])
# print(l)
# l=[1,2,'abc',3,[1,2],3,4]
# l.insert(0,100)
# print(l)
# l=[1,2,'abc',3,[1,2],3,4]
# l.clear()
# print(l)
# l=[1,2,'abc',3,[1,2],3,4]
# l.pop()
# print(l)
# l=[1,2,'abc',3,[1,2],3,4]
# l.pop(4)
# print(l)
# l=[1,2,'abc',3,[1,2],3,4]
# l.remove([1,2])
# print(l)
# l=[1,2,3]
# a=l
# a.pop()
# print(a)
# print(l)
# l=[1,2,3]
# a=l.copy()
# a.pop()
# print(a)
# print(l)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l=[]
# a=int(input("starting"))
# b=int(input("ending"))
# for i in range(a,b+1):
#     l.append(i)
# print(l)

# [2, 4, 6, 8, 10]
# l=[]
# a=int(input("starting"))
# b=int(input("ending"))
# for i in range(a,b+1):
#     if i%2==0:
#         l.append(i)
# print(l)

# 1
# 2
# 2
# 3
# 4
# 4
# 4
# 5
# 6
# l=[1,2,2,3,4,4,4,5,6]
# for i in l:
#     print(i)
# 1
# 3
# 5
# l=[1,2,2,3,4,4,4,5,6]
# for i in l:
#     if i%2==1:
#         print(i)

# 22 9 31
# sum1=0
# sum2=0
# sum3=0
# l=[1,2,2,3,4,4,4,5,6]
# for i in l:
#     if i%2==0:
#         sum1+=i
#     else:
#         sum2+=i
#     sum3+=i
# print(sum1,sum2,sum3)


# nohtyp
# avaj
# php
# l=['python','java','php']
# for i in l:
#   rev=''
#   for j in i:
#     rev=j+rev
#   print(rev)
# a='python'
# rev=''
# for i in a:
#     rev=i+rev
# print(rev)

# enter a letter:o
# mango
# l=['apple','mango','kivi']
# a=input("enter a letter:")
# for i in l:
#     if a in i:
#         print(i)

# a
# apple 
# l=['apple','mango','kivi']
# a=input("enter a letter:")
# for i in l:
#     if a==i[0]:
#          print(i[0])
#          print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# l=[1,2,3,4,5,6,2,2,5,6]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
#         print(i)


# [10, 6, 8] [7, 3, 5]
# l=[10,10,6,6,8,8,7,3,7,3,5,5,5]
# l1=[]
# l2=[]
# for i in l:
#     if i%2==0:
#         if i not in l1:
#             l1.append(i)
#     else:
#         if i%2==1:
#             if i not in l2:
#                 l2.append(i)
# print(l1,l2)

# 3
# l=[1,2,2,2,3,4,4,5,5,5]
# a=int(input("enter a number:"))
# print(l.count(a))

# l=[1,2,2,3]
# print(l.count(2))
# a='welcome'
# print(a.index('w'))

# [1, 3, 5, 7]
# [2, 4, 6]
# l=[1,2,3,4,5,6,7]
# odd=[i for i in l if i%2==1]
# even=[i for i in l if i%2==0]
# print(odd)
# print(even)