# def f(n):
#     if n == 0:
#         return 0
#     elif n % 2 == 0 and n > 0:
#         return f(n/2)
#     else:
#         return 1 + f(n - 1)
#
# k = 0
# for n in range(1,501):
#     if f(n) == 3:
#         k +=1
#
# print(k)


# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n > 2 and n % 2 == 0:
#         return int((3 * n + f(n - 3)) / 3)
#     else:
#         return int((7 * n + f(n - 1) - f(n - 2)) / 5)
#
#
# print(f(35))


# def f(n):
#     if n < 3:
#         return 1
#     elif n > 2:
#         return sum(f(i) for i in range(1,n))

#
# print(f(18))
#
# import sys
# sys.setrecursionlimit(10000)
# def f(n):
#     if n >= 10000:
#         return n
#     elif n < 10000 and n % 2 == 0:
#         return f(n + 2) - 3
#     elif n < 10000 and n % 2 != 0:
#         return f(n + 2) + 1
# print(f(94)-f(80))
#


# def f(n):
#     if n < 3:
#         return 1
#     elif n > 2 and n % 2 != 0:
#         return f(n-1) + 3 * f(n-2)
#     else:
#         return sum(f(i) for i in range(1,n))
#
# print(f(28))



# print(len(range(1,1000,2)))
# print(len(range(123456796, 1234567889, 2)))



# def f(n):
#     if n > 1000000:
#         return n
#     elif n <= 1000000:
#         return n + f(2*n)
#     else:
#         return g(n)
#
# def g(n):
#     return f(n) / n
#
# k = 0
# for n in range(1,2000+1):
#     if g(n) == 2000:
#         k += 1
# print(k)