# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n == 3:
#         return 1
#     elif n > 3:
#         return f(n - 3) + f(n - 2)
# print(f(10))

# def f(n):
#     if n <= 2:
#         return n
#     else:
#         return f(n - 1) * f(n - 2)
#
# print(f(6))


# def f(n):
#     if n == 1:
#         return 3
#     elif n == 2:
#         return 3
#     elif n > 2:
#         return 5 * f(n - 1) - 4 * f(n - 2)
#
# print(f(15))


# def f(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return f(n-1) * f(n-1) - f(n-1) * n + 2 * n
#
# print(f(4))


# def f(n):
#     if n == 1:
#         return 1
#     elif n % 2 == 0:
#         return n + f(n - 1)
#     elif n > 1 and (n % 2 != 0):
#         return 2 * f(n - 2)
#
#
# print(f(26))
