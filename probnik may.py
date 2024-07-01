#2 задание
"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = y and (x or z) or (not(y or z)) or w
#                 if not f:
#                     print(x,y,z,w)
"""



# 5 задание

# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     if i % 2 == 0:
#         s = s + s[-2:]
#     else:
#         s = '1' + s + '0'
#     r = int(s,2)
#     if r < 100:
#         print(i)


# 8 задание




# a = '012345678'
# k = 0
# for a1 in '12345678':
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     s = a1 + a2 + a3 + a4 + a5
#                     if s.count('5') == 1 and a1 != a2 and a2 != a3 and a3 != a4 and a4 != a5:
#                         k += 1
#                         print(s)
# print(k)



arr = []
#12 задание
for i in range(4,10000):
    s = '3' + '5' * i
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555','3',1)
        else:
            s = s.replace('333','5',1)
    arr.append(int(s))
print(max(arr))




# 14 задание
#
# n = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338
#
# s = ''
#
# while n != 0:
#     s = str(n % 9) + s
#     n = n // 9
# r = s.count('1') + s.count('2') + s.count('3') + s.count('4') + s.count('5') + s.count('6') + s.count('7') + s.count('8')
# print(r)
#
#


# 15 задание
# arr = []
# for A in range(1,1000):
#     flag = True
#     for x in range(1,1000):
#         a = x & A == 0
#         b = x & 37 == 0
#         c = x & 12 == 0
#         f = a or (not (b)) or (not(c))
#         if f == 0:
#             flag = False
#     if flag == True:
#         arr.append(A)
# print(max(arr))



# 16 задание
#
# import sys
# sys.setrecursionlimit(10000)
# def f(n):
#     if n <= 3:
#         return 1
#     else:
#         return (n + 3) * f(n - 2)
# print(f(2028)/f(2024))


# 19 - 21 задания
# def f(s, n):
#     if (s > 300) or (n > 4):
#         return n == 2 or n == 4
#     else:
#         if (n % 2 != 0):
#             return f(s+3, n+1) or f(s*5, n+1)
#         else:
#             return f(s+3, n+1) and f(s*5, n+1)
#
# for s in range(1, 300+1):
#     if (f(s, 0) == True):
#         print(s)
#
#

#23 задание
#
# def f(x,y):
#     if x == y:
#         return 1
#     elif x > y or x == 16:
#         return 0
#     else:
#         return f(x +1,y) + f(x + 3,y) + f(x ** 2,y)
#
# print(f(3,20) * f(20,26))
