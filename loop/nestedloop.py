# for i in range(1,5):
#     print("*")
# for i in range(1,5):
#     print("*"*i)

# for i in range(4,0,-1):
#     print("*"*i)
# for i in range(1,5):
#     print("a"*i)
# for i in range(1,5):
#     print("1"*i)
# for i in range(4):
#     for j in range(4):
#         print(j,end=" ")
#     print()
# for i in range(4):
#     for j in range(4):
#         print(i,end=" ")
#     print()
# for i in range(1,5):
#     for j in range(4):
#         print(i,end=" ")
#     print()
# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()
# a=0
# for i in range(3):
#     for j in range(3):
#         print(a,end=" ")
#         a+=1
#     print()

# 0 2 4 
# 6 8 10
# 12 14 16
# a=0
# for i in range(3):
#     for j in range(3):
#         print(a,end=" ")
#         a+=2
#     print()

# 3 6 9 
# 12 15 18
# 21 24 27
# a=3
# for i in range(3):
#     for j in range(3):
#         print(a,end=" ")
#         a+=3
#     print()
# a=3
# for i in range(4):
#     for j in range(1,a+1):
#          if i%2==0: #odd row and even row
#              print(j-1,end=" ")
#          else:
#              print(a-j,end=" ")
#     print()
# for i in range(1,4):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()    

# for i in range(1,4):
#     for j in range(i):
#         print(i,end=" ")
#     print()    

# 
# a=1
# for i in range(1,4):
#     for j in range(i):
#         print(a,end=" ")
#         a+=1
#     print()
# # a=1
# for i in range(1,4):
#     for j in range(i):
#         print(a,end=" ")
#         a+=2
#     print()
# a=3
# for i in range(5):
#     for j in range(i):
#         # print(j,end=" ")
#         if i%2==1:
#              print(j,end=" ")
#         else:
#              print(i-j-1,end=" ")
#     print()
# for i in range(3):
#     A=65
#     for j in range(3):
#         print(chr(A),end=" ")
#         A+=1
#     print()
# A=65
# for i in range(3):
#     for j in range(3):
#         print(chr(A+i),end=" ")
#     print()

# a=65
# for i in range(1,4):
#     for j in range(i):
#         print(chr(a),end=" ")
#         a+=1
#     print()
# a=65
# for i in range(1,4):
#     for j in range(3):
#         print(chr(a),end=" ")
#         a+=1
#     print()

# for i in range(1,4):
#     for j in range(3):
#         print(i,end=" ")
#         i+=1
#     print()
# a=1
# for i in range(1,4):
#     for j in range(i):
#         print(a,end=" ")
#         a+=1
#     print()



# 1 
# 2 1
# 3 2 1
# for i in range(1,4):
#     for j in range(i):
#         print(i-j,end=" ")
#     print()



# a=65
# for i in range(1,4):
#     for j in range(i):
#          print(chr(a+1),end=" ")
#     print()

# for i in range(4):
#     a=65
#     for j in range(3):
#         if i%2==0:
#             print(chr(a),end=" ")
#             a+=1
#         else:
#             print(j+1,end=" ")
#     print()
# a=65
# for i in range(4):
#   for i in range(3):
#          if i%2==0:
#              print(chr(a),end=" ")
#          a+=1
#          print(i+1,end=" ")
#          print()

# A 
# B A
# C B A
# a=64
# for i in range(1,4):
#     for j in range(i):
#         print(chr(a+i-j),end=" ")
#     print()65 66 67 


# 67 66 65
# 65 66 67
# 67 66 65
# a=65
# for i in range(1,5):
#     for j in range(3):
#         if i%2==1:
#            print(a+j,end=" ")
#         else:
#             print(a+2-j,end=" ")
#     print()A B C 


# C B A
# A B C
# C B A
# a=65
# for i in range(1,5):
#     for j in range(3):
#         if i%2==1:
#            print(chr(a+j),end=" ")
#         else:
#             print(chr(a+2-j),end=" ")
#     print()