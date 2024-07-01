# a = list(map(int, open('17 - 7.txt').readlines()))
# maxARR = []
# for i in range(len(a)):
#     if a[i] % 246 == 0:
#         maxARR.append(a[i])
# mx = max(maxARR)
# m = []
# for i in range(len(a) - 1):
#     if ('aa' in (hex(a[i])[2:])) and ('aa' in (hex(a[i + 1])[2:])) and (a[i] + a[i + 1]) < mx:
#         m.append(a[i] + a[i + 1])
# print(len(m),max(m))

# a = list(map(int, open('изи блок №1.txt').readlines()))
# m = []
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if ((a[i] % 160) != (a[j] % 160)) and ((a[i] % 7 == 0) or (a[j] % 7 == 0)):
#             m.append(a[i] + a[j])
# print(len(m), max(m))
#

# a = list(map(int, open('изи блок №2.txt').readlines()))
# minARR = []
# for i in range(len(a)):
#     if a[i] % 21 == 0:
#         minARR.append(a[i])
# minx = min(minARR)
# m = []
# for i in range(len(a) - 1):
#     if (a[i] % minx == 0) or (a[i + 1] % minx == 0):
#         m.append(a[i] + a[i + 1])
# print(len(m),max(m))

#
# a = list(map(int, open('изи блок №3.txt').readlines()))
# DIG35 = []
# for i in range(len(a)):
#     if a[i] % 35 == 0:
#         DIG35.append(a[i])
# SUMOFDIG = 0
# for i in DIG35:
#     SUMOFDIG += sum(int(x) for x in str(i))
# # print(SUMOFDIG)
#
# m = []
# for i in range(len(a)-1):
#     if ((a[i] > SUMOFDIG) and ((hex(a[i + 1])[2:])[-2:] == 'ef')) or ((a[i + 1] > SUMOFDIG) and ((hex(a[i])[2:])[-2:] == 'ef')):
#         m.append(a[i] + a[i + 1])
# print(len(m), min(m))
#
"""
# a = [11,47,5,9]
# summa = 0
# for i in a:
#     summa += sum(int(x) for x in str(i))
#
# print(summa)
"""
#
# a = list(map(int, open('изи блок №4.txt').readlines()))
# m = []
# for i in range(len(a)):
#     if sum(int(x) for x in (str(a[i])[-2:])) >= 15:
#         if (a[i] % 3 != 0) and (a[i] % 4 != 0) and (a[i] % 7 != 0):
#             m.append(a[i])
# print(min(m),sum(m))


# a = list(map(int, open('изи блок №5.txt').readlines()))
# m = []
# for i in range(len(a)):
#     if (bin(a[i])[2:])[-4:] == '1001':
#         n = a[i]
#         s = ''
#         while n != 0:
#             s = str(abs(n) % 5) + s
#             n = abs(n) // 5
#             # print(n)
#         if s[-2:] == '11':
#             m.append(a[i])
#             print(a[i])
# print(max(m),sum(m))
#
#
#
# # s = '123456789'
# # print((s[2:])[-4:])
#
# n = -9081
# s = ''
# while abs(n) != 0:
#     s = str(abs(n) % 5) + s
#     n = abs(n) // 5
#     # print(n)
# print(s)

# a = list(map(int, open("изи блок №5.txt").readlines()))
# k = 0
# b = []
# for i in range(len(a)):
#     x = a[1]
#     st = ''
#     while x > 0:
#         st + str(x % 5)
#         x //= 5
#     st = st[::-1]
#     if bin(a[i]) [-4::] == '1001' and st[-2::] == '11':
#         b.append(a[i])
# print(max(b), sum(b))

#
# a = list(map(int, open('изи блок №3.txt').readlines()))
# DIG35 = []
# for i in range(len(a)):
#     if a[i] % 35 == 0:
#         DIG35.append(a[i])
# SUMOFDIG = 0
# for i in DIG35:
#     SUMOFDIG += sum(int(x) for x in str(i))
# # print(SUMOFDIG)
#
# m = []
# for i in range(len(a)-1):
#     if ((a[i] > SUMOFDIG) and (((hex(a[i + 1])[2:])[-2:] == 'ef') and a[i + 1] < SUMOFDIG)) or ((a[i + 1] > SUMOFDIG) and (((hex(a[i])[2:])[-2:] == 'ef') and a[i] < SUMOFDIG)):
#         m.append(a[i] + a[i + 1])
# print(len(m), min(m))


# a = list(map(int, open('изи блок №3.txt')))
# k = 0
# sumch = 0
# minsum = 1000000000
# for i in range(len(a)):
#     if a[i] % 35 == 0:
#         while a[i] > 0:
#             sumch += a[i] % 10
#             a[i] //= 10
#
# for j in range(len(a) - 1):
#     if (a[j] > sumch > a[j + 1] and hex(a[j + 1])[-2::] == 'ef') or \
#  \
#             (a[j + 1] > sumch > a[j] and hex(a[j])[-2::] == 'ef'):
#         k += 1
#         minsum = min(minsum, a[j] + a[j + 1])
# print(k, minsum)
