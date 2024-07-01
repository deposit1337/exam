# arr = []
# for AL in range(200):
#     for AR in range(AL,200):
#         flag = True
#         for x in range(200):
#             P = 2 <= x <= 10
#             Q = 6 <= x <= 14
#             A = AL <= x <= AR
#             f = A <= (P or Q)
#             if f == 0:
#                 flag = False
#         if flag == True:
#             arr.append(AR - AL)
# print(max(arr))
#
#
#

#
# arr = []
# for AL in range(200):
#     for AR in range(AL,200):
#         flag = True
#         for x in range(200):
#             A = AL <= x <= AR
#             P = 19 <= x <= 84
#             Q = 4 <= x <= 51
#             f = Q <= ((not P) <= (not(Q and (not A))))
#             if f == 0:
#                 flag = False
#         if flag == True:
#             arr.append(AR-AL)
# print(min(arr))


#
# for A in range(1,1000):
#     flag = True
#     for x in range(1,1000):
#         a = x & 85
#         b = x & 54
#         c = x & A
#         f = (a == 0) <= ((b != 0) <= c)
#         if f == 0:
#             flag = False
#     if flag == True:
#         print(A)



#
# for A in range(1,1000):
#     flag = True
#     for x in range(1,1000):
#         a = x & 105
#         b = x & 58
#         c = x & A
#         f = (a == 0) <= ( (b != 0) <= (c != 0))
#         if f == 0:
#             flag = False
#     if flag == True:
#         print(A)
#         break







#
# for A in range(1,1000):
#     flag = True
#     for x in range(1000):
#         for y in range(1000):
#             a = (2 * x) + (3 * y)
#             b = A >= x
#             c = A >= y
#             f = (a != 60) or b or c
#             if f == 0:
#                 flag = False
#     if flag == True:
#         print(A)
#         break


# arr = []
# def dell(n,m):
#     return n % m == 0
#
# for A in range(1,1000):
#     flag = True
#     for x in range(1,1000):
#         a = A < 50
#         b = dell(x, A)
#         c = dell(x, 10)
#         d = dell(x, 12)
#         f = (a) and ((not b) <= ((c) <= (not d)))
#         if f == 0:
#             flag = False
#     if flag == True:
#         arr.append(A)
#
# print(arr)



#
# for a in range(100, 0, -1):
#     k = 0
#     for x in range(1, 1000):
#         if (a< 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 12 != 0))):
#             k += 1
#     if k == 999:
#         print(a)
#         break
