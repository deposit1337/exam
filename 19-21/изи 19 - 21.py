# def f(x, h):
#     if h == 3 and x >= 88:
#         return 1
#     elif h == 3 and x < 88:
#         return 0
#     elif h < 3 and x >= 88:
#         return 0
#     else:
#         if h % 2 == 0:#V
#             return f(x + 1,h + 1) or f(x + 4,h + 1) or f(x * 3,h + 1)
#         else:
#             return f(x + 1,h + 1) and f(x + 4,h + 1) and f(x * 3,h + 1)
#
# # for x in range(1,88+1):
#     # if f(x,1) == 1:
#         # print(x)


# def f(x, h):
#     if (h == 3 or h == 5) and x >= 63:
#         return 1
#     elif h == 5 and x < 63:
#         return 0
#     elif h < 5 and x >= 63:
#         return 0
#     else:
#         if h % 2 == 0:  #P
#             return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)
#         else:
#             return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)
#
#
# for x in range(1, 63+1):
#     if f(x,1) == 1:
#         print(x)


# def f(x, h):
#     if (h == 4 or h == 2) and x >= 42:
#         return 1
#     elif h == 4 and x < 42:
#         return 0
#     elif h < 4 and x >= 42:
#         return 0
#     else:
#         if h % 2 == 0:  # VANYA
#             return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 2, h + 1)
#         else:
#             return f(x + 1, h + 1) and f(x + 2, h + 1) and f(x * 2, h + 1)
#
#
# for x in range(1, 41 + 1):
#     if f(x, 1) == 1:
#         print(x)

# def f(x,h):
#     if (h == 3 or h == 5) and x >= 54:
#         return 1
#     elif h == 5 and x < 54:
#         return 0
#     elif h < 5 and x >= 54:
#         return 0
#     else:
#         if h % 2 == 0: #VANYA
#             return f(x + 1,h + 1) or f(x + 2,h + 1) or f(x * 3,h + 1)
#         else:
#             return f(x + 1, h + 1) and f(x + 2, h + 1) and f(x * 3, h + 1)
#
# for x in range(1,54+1):
#     if f(x,1) == 1:
#         print(x)


# def f(x,h):
#     if h == 4 and x >= 29:
#         return 1
#     elif h == 4 and x < 29:
#         return 0
#     elif h < 4 and x >= 29:
#         return 0
#     else:
#         if h % 2 == 1:#P
#             return f(x + 1,h + 1) or f(x + 2,h + 1) or f(x * 2,h + 1)
#         else:
#             return f(x + 1,h + 1) and f(x + 2,h + 1) and f(x * 2,h + 1)
#
# for x in range(1,29):
#     if f(x,1) == 1:
#         print(x)
#
#
#
# def f(x, y, h):
#     if h == 3 and (x + y <= 20):
#         return 1
#     elif h == 3 and (x + y > 20):
#         return 0
#     elif h < 3 and (x + y <= 20):
#         return 0
#     else:
#         if h % 2 == 0:  # V
#             return f(x - 1, y, h + 1) or f(((x // 2) + (x % 2)), y, h + 1) or f(x, y - 1, h + 1) or f(x, (
#             ((y // 2) + (y % 2))), h + 1)
#         else:
#             return f(x - 1, y, h + 1) or f(((x // 2) + (x % 2)), y, h + 1) or f(x, y - 1, h + 1) or f(x, (
#                 ((y // 2) + (y % 2))), h + 1)
#         # n = 8
# # print((n // 2) + (n % 2))
#
# for x in range(10,10000):
#     if f(x,10,1) == 1:
#         print(x)


# def f(x, y, h):
#     if (h == 3 or h == 5) and (x + y >= 93):
#         return 1
#     elif h == 5 and (x + y < 93):
#         return 0
#     elif h < 5 and (x + y >= 93):
#         return 0
#     else:
#         if h % 2 == 0:  # P
#             return f(x + 1, y, h + 1) or f(x * 2, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1)
#         else:
#             return f(x + 1, y, h + 1) and f(x * 2, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 2, h + 1)
#
#
# for x in range(1, 80):
#     if f(x, 12, 1) == 1:
#         print(x)


# def f(x, y, h):
#     if (h == 3 or h == 5) and (x + y >= 82):
#         return 1
#     elif h == 5 and (x + y < 82):
#         return 0
#     elif h < 5 and (x + y >= 82):
#         return 0
#     else:
#         if h % 2 == 0:  #V
#             return f(x + 1, y, h + 1) or f(x * 4, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 4, h + 1)
#         else:
#             return f(x + 1, y, h + 1) and f(x * 4, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 4, h + 1)
#
# for x in range(1,77+1):
#     if f(x,4,1) == 1:
#         print(x)


# def f(x, y, h):
#     if (h == 3 or h == 5) and (x + y >= 74):
#         return 1
#     elif h == 5 and (x + y < 74):
#         return 0
#     elif h < 5 and (x + y >= 74):
#         return 0
#     else:
#         if h % 2 == 0:  # V
#             return f(x + 1, y, h + 1) or f(x * 2, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1)
#         else:
#             return f(x + 1, y, h + 1) and f(x * 2, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 2, h + 1)
#
# for x in range(1,61+1):
#     if f(x,12,1) == 1:
#         print(x)


# def f(x, h):
#     if (h == 3 or h == 5) and (x >= 38):
#         return 1
#     elif h == 5 and (x < 38):
#         return 0
#     elif h < 5 and (x >= 38):
#         return 0
#     else:
#         if h % 2 == 0:  # V
#             return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 2, h + 1)
#         else:
#             return f(x + 1, h + 1) and f(x + 2, h + 1) and f(x * 2, h + 1)
#
#
# for x in range(1, 37 + 1):
#     if f(x, 1) == 1:
#         print(x)


# def f(x, h):
#     if (h == 3 or h == 5) and x >= 47:
#         return 1
#     elif h == 5 and x < 47:
#         return 0
#     elif h < 5 and x >= 47:
#         return 0
#     else:
#         if h % 2 == 0:  # V
#             return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 2, h + 1)
#         else:
#             return f(x + 1, h + 1) and f(x + 2, h + 1) and f(x * 2, h + 1)
#
#
# for x in range(1, 46 + 1):
#     if f(x, 1) == 1:
#         print(x)


# def f(x, y, h):
#     if (h == 3 or h == 5) and (x + y >= 61):
#         return 1
#     elif h == 5 and (x + y < 61):
#         return 0
#     elif h < 5 and (x + y >= 61):
#         return 0
#     else:
#         if h % 2 == 0:  #P
#             return f(x + 1, y, h + 1) or f(x * 4, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 4, h + 1)
#         else:
#             return f(x + 1, y, h + 1) and f(x * 4, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 4, h + 1)
#
#
# for x in range(1, 57 + 1):
#     if f(x, 3, 1) == 1:
#         print(x)


