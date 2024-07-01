# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and (n % 2 == 0):
#         return f(n / 2)
#     if n % 2 != 0:
#         return 1 + f(n - 1)
#
# # print(f(10))
#
# # k = 0
# for n in range(10000):
#     if f(n) == 11:
#         print(n)
#         exit()
#
# # print(k)


# def g(n):
#     if n == 1:
#         return 1
#     elif n >= 2:
#         return f(n - 1) + g(n - 1)
#
#
# def f(n):
#     if n == 1:
#         return 1
#     elif n >= 2:
#         return f(n - 1) - g(n - 1)
#
# print(f(5)/g(5))


# def f(n):
#     if n == 0:
#         return 0
#     elif n > 0 and (n % 2 == 0):
#         return f(n / 2)
#     elif n % 2 != 0:
#         return 1 + f(n - 1)
#
# k = 0
# for n in range(1,1000+1):
#     if f(n) == 3:
#         k += 1
#
# print(k)

# def g(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return f(n - 1) + 2 * n
#
#
# def f(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return 2 * g(n - 1) + 5 * n
#
# print(f(4)+g(4))


# def f(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 3
#     elif n > 1:
#         return f(n - 1) - f(n - 2) + 3 * n
#
# print(f(40))
