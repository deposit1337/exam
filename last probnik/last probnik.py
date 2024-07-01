# 2
# print('a b c d')
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             for d in range(2):
#                 f = (a <= b) and (b <= (not c)) and ((not c) <= d)
#                 if f:
#                     print(a,b,c,d)

# 5
# m = []
# for i in range(1, 1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 3) + s
#         n = n // 3
#     if i % 2 == 0:
#         if s[-1] == '2':
#             s = '2' + s + '11'
#         else:
#             s = '2' + s + str(int(s[-1]) * 2)
#     else:
#         if s[0] == '2':
#             s = '11' + s + '2'
#         else:
#             s = str(int(s[0]) * 2) + s + '2'
#     r = int(s, 3)
#     if r > 100:
#         m.append(r)
# print(min(m))

# 7
# for p in range(1,1000):
#     if 0.8 * (1600 * 1200 * (10 +p)) <= 3 * 1024 * 1024 * 8:
#         print(p)

# 8

# a = '012345678'
# k = 0
# for a1 in '2468':
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         for a7 in a:
#                             s = a1 + a2 + a3 + a4 + a5 + a6 + a7
#                             if int(a7) % 3 != 0:
#                                 if s.count('6') >= 1:
#                                     k += 1
# print(k)

# 12
# for n in range(4, 1000):
#     s = '5' + '2' * n
#     while '52' in s or '222' in s or '122' in s:
#         s = s.replace('52', '11', 1)
#         s = s.replace('222', '15', 1)
#         s = s.replace('122', '21', 1)
#     if (sum(int(x) for x in s))**0.5 == int((sum(int(x) for x in s))**0.5):
#         print(s)
#         print(n)
#         print(sum(int(x) for x in s))


# 13
# k = 1
# while k != 0:
#     n = input('число :')
#     s = bin(int(n))[2:].zfill(8)
#     print(s)
#
# def f(n):
#     if n < 2:
#         return 0
#     for d in range(2,int(n**0.5) + 1):
#         if n % d == 0:
#             return 0
#     return 1
#
#


# a = '01'
# k = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         for a7 in a:
#                             for a8 in a:
#                                 address = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
#                                 sum1 = sum(int(x) for x in address)
#                                 if address != '00000000' or address != '11111111':
#                                     if f(sum1 + 10) == 1:
#                                         k += 1
# print(k)


# 14

# t = 'QWERTYUIOPASDFGHJKLZXCVBNM'
# alph = '0123456789ABCDEFGHIJKLMNOPQRSTUV'
# # print(sorted(t))
# for x in alph:
#     n = (int('72' + x, 32) + int('1C' + x + '7', 32) + int('572' + x, 32) + int('1C' + x + '7', 32) + ((int(x, 32)) ** 5))
#
#     if n % 2 == 0:
#         try:
#             print(n // int(x,32))
#         except ZeroDivisionError:
#             print(0)


# 15
# def dell(n,m):
#     return n % m == 0
#
#
# for A in range(1,1000):
#     flag = True
#     for x in range(1,1000):
#         a = dell(x,12)
#         b = x & 4 == 0
#         c = (x + 1 )> A
#         f =(a and (b)) <= (c)
#         if f == 0:
#             flag = False
#             break
#     if flag == True:
#         print(A)


# 16
# import sys
#
# sys.setrecursionlimit(10000)
# def h(x):
#     if x <= 2:
#         return 2**x
#     elif (x > 2) and (x % 2 == 0):
#         return h(x / 2)
#     elif (x > 2) and (x % 2 != 0):
#         print(1)
#         return h(x + 1) + h(x - 4)
#
# print(h(4202))


# 17

# a = list(map(int, open('№17.txt').readlines()))
# #
# m = []
# mx = 99894
# # for i in a:
# #     n = abs(i)
# #     alph = '0123456789ABC'
# #     s = ''
# #     while n != 0:
# #         s = alph[n % 13] + s
# #         n = n // 13
# #     if s[-2:] == '12':
# #         mx.append(i)
# #
# # print(max(mx))
#
# for i in range(len(a) - 2):
#     # print((len(str(abs(a[i])))))
#     if ((len(str(abs(a[i]))) == 3) + (len(str(abs(a[i + 1]))) == 3) + (len(str(abs(a[i + 2]))) == 3)) == 2:
#         if (a[i] + a[i + 1] + a[i + 2]) < mx:
#             m.append(a[i] * a[i + 1] * a[i + 2])
# print(len(m),max(m))


# 19 - 21


# def f(x, h):
#     if (h == 3 or h == 5) and x >= 72:
#         return 1
#     elif h == 5 and x < 72:
#         return 0
#     elif h < 5 and x >= 72:
#         return 0
#     else:
#         if h % 2 == 0:  # V
#             return f(x + 3, h + 1) or f(x + 5, h + 1) or f(x * 2, h + 1)
#         else:
#             return f(x + 3, h + 1) and f(x + 5, h + 1) and f(x * 2, h + 1)
#
# for x in range(1,71+1):
#     if f(x,1) == 1:
#         print(x)


# 23

# def f(x, y ):
#     if x == y:
#         return 1
#     elif x > y:
#         return 0
#     else:
#         return f(x + 1, y) + f(x * 2, y) + f(x + 5, y)
# print(f(5,62))
#



# 24

# a = open('№24.txt').read()
#
# c = 0
# b = 0
# k = 0
# s = ''
# for i in range(len(a)):
#     k += 1
#     s += a[i]
#     if a[i] == 'B':
#         b += 1
#     elif a[i] == 'C':
#         c += 1
#     if b >= 127 and c >= 127:
#         break
#
# print(k,s)


# 25

# import fnmatch
#
# for n in range(13705, 10 ** 8):
#     if ((n + 1) % 2024) == 0:
#         ds = []
#         if fnmatch.fnmatch(str(n), '13*7?5'):
#             for d in range(2,int(n ** 0.5) + 1):
#                 if n % d == 0:
#                     print(n,n // d)
#                     break


