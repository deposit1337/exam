#
# for i in range(2,1000):
#     s = bin(i)[2:]
#     s = s + s[-2] + s[1]
#     r = int(s,2)
#     if r > 180:
#         print(i)
#
# # s = '12345678'
# # s = s + s[-2] + s[1]
# # print(s)


# for i in range(1, 1000):
#     s = bin(i)[2:]
#     s = s + str(sum(int(x) for x in s) % 2)
#     s = s + str(sum(int(x) for x in s) % 2)
#     r = int(s,2)
#     if r > 43:
#         print(r)
#
# for i in range(1,1000):
#     s = bin(i)[2:]
#     if i % 2 == 0:
#         s += '01'
#     else:
#         s += '10'
#     r = int(s,2)
#     if r > 102:
#         print(r)

#
# for i in range(1, 1000):
#     s = bin(i)[2:]
#     if s.count('1') == s.count('0'):
#         s += s[-1]
#     elif s.count('1') > s.count('0'):
#         s += '0'
#     else:
#         s += '1'
#     if s.count('1') == s.count('0'):
#         s += s[-1]
#     elif s.count('1') > s.count('0'):
#         s += '0'
#     else:
#         s += '1'
#     if s.count('1') == s.count('0'):
#         s += s[-1]
#     elif s.count('1') > s.count('0'):
#         s += '0'
#     else:
#         s += '1'
#     r = int(s,2)
#     # print(r)
#     # print(r)
#     if (i > 104) and (r % 4 == 0):
#         print(i)
#

# #
# a = 'БОРИС'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         s = a1 + a2 + a3 + a4 + a5 + a6
#                         if ((s.count('Б') == 1) and (s.count('Р') == 1)) and s.count('С') <= 1:
#                             n += 1
# print(n)
#


# a = 'ЕГЭ'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             s = a1 + a2 + a3
#             if (len(set(s)) == 3) and (a1 != 'Э') and s.count('ЕЭ') == 0:
#                 n += 1
#                 print(s)
#
# print(n)


# a = 'БАШНЯ'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         s = a1 + a2 + a3 + a4 + a5 + a6
#                         if (s.count('Б') <= 1) and (a1 != 'Н') and(a6 not in 'АЯ'):
#                             n += 1
#                             print(s)
# # print(n)
# a = 'АНДРЕЙ'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     s = a1 + a2 + a3 + a4 + a5
#                     if (s.count('А') >= 1) and (s.count('Й') <= 1):
#                         n += 1
#                         print(s)
# print(n)


# a = '0123456'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         for a7 in a:
#                             s = a1 + a2 + a3 + a4 + a5 + a6 + a7
#                             if (a1 not in '035') and ((s.count('22') == 0) or (s.count('44') == 0)):
#                                 n += 1
#                                 print(s)
# print(n)


#
# for i in range(410,411):
#     s = bin(i)[2:]
#     if (sum(int(x) for x in s)) % 2 == 0:
#         s += '0'
#         s = s.replace(s[:2], '10', 1)
#     else:
#         s += '1'
#         s = s.replace(s[:2], '11', 1)
#     r = int(s,2)
#     print(r)


#
# for i in range(1,1000):
#     s = bin(i)[2:]
#     # print(s)
#     if (sum(int(x) for x in s)) % 2 == 0:
#         s += '0'
#         s = s.replace(s[:2], '10', 1)
#         # print(s)
#     else:
#         s += '1'
#         s = s.replace(s[:2], '11', 1)
#     r = int(s,2)
#     if r > 40:
#         print(i)
# # r = int(s,2)
#
#
#
#
#

# arr = []
# for i in range(1, 1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 3) + s
#         n = n // 3
#     if (sum(int(x) for x in s) % 4) == 0:
#         s = '1' + s
#         s = s[0:-2]
#     else:
#         g = ((sum(int(x) for x in s) % 4) * 3)
#         temp = ''
#         while g != 0:
#             temp = str(g % 3) + temp
#             g = g // 3
#         s = s + temp
#     r = int(s, 3)
#     print(r)
#     if r > 353:
#         arr.append(r)
# print(min(arr))
#

# a = 'ОНИКС'
# n = 0
# k = 0
# g = 0
# r = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         sN = a1 + a2 + a3 + a4 + a5 + a6
#                         sK = a1 + a2 + a3 + a4 + a5
#                         sG = a1 + a2 + a3 + a4
#                         if ((sN.count('С') == 3) and (sN.count('О') == 1)):
#                             n += 1
#                             if ((sK.count('С') == 3) and (sK.count('О') == 1)):
#                                 k += 1
#                                 if ((sG.count('С') == 3) and (sG.count('О') == 1)):
#                                     g += 1
#
# print(n + k + g)


# a = 'КЛН'
# b = 'ОУ'
# n = 0
# for a1 in b:
#     for a2 in a:
#         for a3 in b:
#             for a4 in a:
#                 for a5 in b:
#                     s = a1 + a2 + a3 + a4 + a5
#                     # if len(set(s)) == 5:
#                     n += 1
#                     print(s)
# print(n)


# #
# a = 'ЛЕГКО'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         s = a1 + a2 + a3 + a4 + a5 + a6
#                         if (s.count('О') <= 1) and a1 != 'Г' and (a6 not in 'ЕО'):
#                             n += 1
#                             print(s)
# print(n)
#
#


#
# a = '01234567'
# n = 0
# for a1 in '1234567':
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     s = a1 + a2 + a3 + a4 + a5
#                     if (s.count('6') == 1) and (('16' not in s) and ('36' not in s) and ('56' not in s) and ('76' not in s)) and (('61' not in s) and ('63' not in s) and ('65' not in s) and ('67' not in s)):
#                         n += 1
#                         print(s)
#
# print(n)
#


# a = 'МИТРОФАН'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         s = a1 + a2 + a3 + a4 + a5 + a6
#                         if ((s.count('М') + s.count('Т') + s.count('Р') + s.count('Ф') + s.count('Н')) > (
#                                 s.count('И') + s.count('О') + s.count('А'))) and (
#                                 ('ИО' not in s) and ('ОИ' not in s) and ('ИА' not in s) and ('АИ' not in s)) and (
#                                 len(set(s)) == 6):
#                             n += 1
#                             print(s)
# print(n)
