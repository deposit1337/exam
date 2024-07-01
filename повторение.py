# a = '0123456789'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     s = a1 + a2 + a3 + a4 + a5
#                     if s != '00001':
#                         n += 1
#                         print(s)
#
# print(n)

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = not(y <= w) or (x <= z) or (not x)
#                 if not Af:
#                     print(x,y,z,w)

# arr = []
# for AL in range(1, 300):
#     for AR in range(AL, 300):
#         flag = True
#         for x in range(1, 300):
#             a = 13 <= x <= 19
#             b = 17 <= x <= 23
#             c = AL <= x <= AR
#             f = (not(not(a) <= b)) <= (c <= (not(b) <= a))
#             if f == 0:
#                 flag = False
#         if flag == True:
#             arr.append(AR-AL)
# print(max(arr))


# for A in range(0, 300):
#     flag = True
#     for x in range(1, 300):
#         for y in range(1, 300):
#             a = ((7 * y) + x) < A
#             b = ((2 * x) + (3 * y)) > 98
#             f = (a) or (b)
#             if f == 0:
#                 flag = False
#     if flag == True:
#         arr.append(A)
#
# print(min(arr))


# for A in range(1,1000):
#     flag = True
#     for x in range(1,1000):
#         a = x & 52 != 0
#         b = x & 36 == 0
#         c = x & A == 0
#         f = (a and b) <= (not(c))
#         if f == 0:
#             flag = False
#     if flag == True:
#         print(A)


# def dell(n,m):
#     return n % m == 0
#
# for A in range(0,200):
#     flag = True
#     for x in range(1,200):
#         for y in range(1,200):
#             a = dell(108,x)
#             b = dell(x,y)
#             c = x + y > 80
#             d = A - y > x
#             f = (a <= (not(b))) or (c) or d
#             if f == 0:
#                 flag = False
#     if flag == True:
#         arr.append(A)
# print(min(arr))


# def dell(n,m):
#     return n % m == 0
#
# for A in range(1,1000):
#     flag = True
#     for x in range(1,1000):
#         a = dell(x,A)
#         b = 70 <= x <= 80
#         c = dell(x,18)
#         f = a or (b <= (not(c)))
#         if f == 0:
#             flag = False
#     if flag == True:
#         arr.append(A)
# print(arr)


# for i in range(1,200):
#     if 0.45 * (320 * 512 * i) <= 50 * 1024 * 8:
#         print(i)
# n = 0
# k = 0
# for i in range(1,100):
#     n = n + 2 + 1
#     if n <= 64:
#         k += 1
#     else:
#         # exit()
# print(k)


# for  i in range(1,100):
#     if (320 * 512 * i) * 0.45 <= 50 * 1024 * 8:
#         print(i)
#
#

# for i in range(1, 100):
#     if (192 * 960 * i) <= 90 * 1024 * 8:
#         print(i)


# for n in range(1, 100):
#     if
#         print(n)


# a = 'АВОРТ'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         s = a1 + a2 + a3 + a4 + a5 + a6
#                         n += 1
#                         # print(n,s)
#                         if s == 'ВОРОТА':
#                             print(n)

# a = 'МАРИН'
# a = sorted(a)
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         for a7 in a:
#                             for a8 in a:
#                                 s = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
#                                 n += 1
#                                 if s == 'МАРИАННА':
#                                     print(n)


# a = 'ВАЛЕРИЯ'
# a = sorted(a)
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             s = a1 + a2 + a3
#             if s.count('В') == 1:
#                 n += 1
#                 print(n,s)


# arr = []
#
# for AL in range(1,200):
#     for AR in range(AL,200):
#         flag = True
#         for x in range(1,200):
#             P = 13 <= x <= 19
#             Q = 17 <= x <= 23
#             A = AL <= x <= AR
#             f = (not((not P) <= Q)) <= (A <= (not(Q) <= P))
#             if f == 0:
#                 flag = False
#         if flag == True:
#             arr.append(AR - AL)
# print(max(arr))

#
# for i in range(1, 200):
#     if
#         print(i)

#
# a = 4 * 100 / 80


#
#
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = not(y <= (x == w)) and (z <= x)
#                 if f:
#                     print(x,y,z,w)


# def f(x, h):
#     if (h == 3 or h == 5) and x >= 55:
#         return 1
#     elif h == 5 and x < 55:
#         return 0
#     elif h < 5 and x >= 55:
#         return 0
#     else:
#         if h % 2 == 0:  #V
#             return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 3, h + 1)
#         else:
#             return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 3, h + 1)
#
#
# for x in range(1, 54 + 1):
#     if f(x, 1) == 1:
#         print(x)
# #13


# def f(x, y, h):
#     if (h == 3 or h == 5) and (x + y >= 255):
#         return 1
#     elif h == 5 and (x + y < 255):
#         return 0
#     elif h < 5 and (x + y >= 255):
#         return 0
#     else:
#         if h % 2 == 0:  # V
#             return f(x + 1, y, h + 1) or f(x * 2, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1)
#         else:
#             return f(x + 1, y, h + 1) and f(x * 2, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 2, h + 1)
#
#
# for x in range(1, 237 + 1):
#     if f(17, x, 1) == 1:
#         print(x)
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((not x) == y) and ( z <= w )
#                 if not f:
#                     print(x, y, z, w)


# for i in range(2,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n//2
#     s = s + s[-2]
#     s = s + s[1]
#     r = int(s,2)
#     if r > 180:
#         print(i)


# s = "12345"
# print(s[-2])
# print(s[1])
#


# for i in range(1, 1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     if i % 3 == 0:
#         s = s + s[-3:]
#     else:
#         s = s + bin(i % 3)[2:]
#     r = int(s,2)
#     if r < 76:
#         print(i)


# s = '123456'
# print(s[-3:])


# s = '7' * 512
# k = 0
# while '7777' in s or '1111' in s:
#     if '7777' in s:
#         s = s.replace('7777', '1', 1)
#         k += 4
#     else:
#         s = s.replace('1111', '7')
# print(k)

#
# a = '012345'
#
# for x in a:
#     for y in a:
#         if '10' * x * y * x ==
#
#

# a = '0123456789'
# b = 'QWERTYUIOPASDFGHJKLZXCVBNM'
# alph = '0123456789' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# n = 3 * 1024** 75 + 2 * 256**76 - 16**77 - 2023
#
# s = ''
# while n != 0:
#     s = alph[n % 32] + s
#     n = n // 32
# print(s.count('0'))


# a = '012345'
# # b = '0123456'
# for x in a:
#     for y in a:
#         if int('10'+x+y+x,6) == int(y + '11' + x,7):
#             print(x,y)

#
# alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for p in range(16,100 + 1):
#     temp1 = str
#         print(p)

# alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for n in range()
# a = '0123456789ABCDE'
# for x in a:
#     n = int('99658' + x + '29', 15) + int('102' + x + '023', 15)
#     if n % 14 == 0:
#         print(x,n // 14)

# def f(n):
#     if n < 4:
#         return n - 1
#     elif n > 3 and n % 3 == 0:
#         return n + 2 * f(n - 1)
#     elif n > 3 and n % 3 != 0:
#         return f(n - 2) + f(n - 3)
#
# print(f(25))
# print(7 + 3+ 2 + 1)


# import sys
#
# sys.setrecursionlimit(100000)
#
# def f(n):
#     if n >= 2025:
#         return n
#     else:
#         return n + 3 + f(n + 3)
#
# print(f(2018) - f(2022))


# def f(x,y):
#     if x == y:
#         return 1
#     elif x < y:
#         return 0
#     else:
#         return f(x - 2,y )+ f(x - 5,y)
#
# print(f(24,3))


# def f(x,y):
#     if x == y:
#         return 1
#     elif x > y or (x == 17):
#         return 0
#     else:
#         return f(x+1,y) + f(x * 2,y) + f(x**2,y)
#
# print(f(2,16) * f(16,65))

# m = set()
# def f(x,h):
#     if h == 15:
#         m.add(x)
#     else:
#         f(x * 2,h + 1)
#         f(x * 2 + 1,h + 1)
# f(1,0)
# print(len(m))


# def f11(x, y):
#     if x == y:
#         return 1
#     elif x > y or x == 12:
#         return 0
#     else:
#         return f11(x + 1, y) + f11(x * 2, y)
#
#
# def f12(x, y):
#     if x == y:
#         return 1
#     elif x > y or x == 11:
#         return 0
#     else:
#         return f12(x + 1, y) + f12(x * 2, y)
#
#
# print((f11(2, 11) * f11(11, 24)) + (f12(2, 12) * f12(12, 24)))


# def f9(x,y):
#     if x == y:
#         return 1
#     elif x > y or x == 10:
#         return 0
#     else:
#         return f9(x + 1,y) + f9(x * 2,y)
#
# def f10(x,y):
#     if x == y:
#         return 1
#     elif x > y or x == 9:
#         return 0
#     else:
#         return f10(x + 1,y) + f10(x * 2,y)
#
# print((f9(1,9) * f9(9,20)) + f10(1,10) * f10(10,20))

for n in range(2,36):
    try:
        if int('103',n) == int('97',n + 2):
            print(n)
    except ValueError:
        continue
