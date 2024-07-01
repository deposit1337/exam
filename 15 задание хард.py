# arr = []
#
# def dell(n,m):
#     return n % m == 0
#
# for A in range(1,1000):
#     flag = True
#     for x in range(1,1000):
#         a = dell(120,A)
#         b = dell(x,36)
#         c = not(dell(x,A))
#         d = not(dell(x,45))
#         f = a and (b <= (c <= d))
#         if f == 0:
#             flag = False
#     if flag == True:
#         arr.append(A)
# print(max(arr))







# def dell(n,m):
#     return n % m == 0
#
#
# for A in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         a = dell(72, x)
#         b = dell(90, x)
#         c = A - x > 80
#         f = (a <= (not b)) or c
#         if f == 0:
#             flag = False
#     if flag == True:
#         print(A)
#         break
#
# arr = []
# for A in range(0,300):
#     flag = True
#     for x in range(0,300):
#         for y in range(0,300):
#             a = 2 * x + 3 * y < 30
#             b = x + y >= A
#             f = a or b
#             if f == 0:
#                 flag = False
#     if flag == True:
#         arr.append(A)
# print(max(arr))







# #
# for A in range(0,200):
#     flag = True
#     for x in range(0,200):
#         for y in range(0, 200):
#             a = 2 * x + 3 * y > 30
#             b = x + y <= A
#             f = a or b
#             if f == 0:
#                 flag = False
#     if flag == True:
#         print(A)
#         break
#








# for A in range(0,1000):
#     flag = True
#     for x in range(0,1000):
#         a = x & 51 == 0
#         b = x & 41 == 0
#         c = x & A == 0
#         f = (x & 51 == 0) or ( (x & 41 == 0) <= (x & A == 0))
#         if f == 0:
#             flag = False
#     if flag == True:
#         print(A)


























