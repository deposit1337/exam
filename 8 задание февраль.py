# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     n += 1
#                     s = a1 + a2 + a3 + a4 + a5
#                     print(n,s)



# a = 'АВОРТ'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 n += 1
#                 s = a1 + a2 + a3 + a4
#                 # print(n,s)
#                 if s == 'ТАРА':
#                     print(n)
#
# a = 'АЕКР'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 n += 1
#                 s = a1 + a2 + a3 + a4
#                 # print(n,s)
#                 if s.count('А') == 0:
#                     print(n)
#                     exit()
#

# a = 'КАТЕР'
# arr = []
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         s = a1 + a2 + a3 + a4 + a5 + a6
#                         if s[0] == 'Р' and s[-1] == 'К':
#                             n += 1
#                             print(s)
# print(n)



# a = 'МЕТРО'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 s = a1 + a2 + a3 + a4
#                 if a1 in 'МТР' and a4 in 'ЕО':
#                     n += 1
#                     print(s)
# print(n)

# a = 'ШКОЛА'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             s = a1 + a2 + a3
#             if s.count('К') == 1:
#                 n += 1
# print(n)

# a = 'ОЛЬГА'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     s = a1 + a2 + a3 + a4 + a5
#                     if a1 != 'Ь' and 'ОЬ' not in s and 'АЬ' not in s and len(set(s)) == 5:
#                         n += 1
#
# print(n)



# a = 'АКЛОШ'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     n += 1
#                     s = a1 + a2 + a3 + a4 + a5
#                     if s == 'ШКОЛА':
#                         print(n)
#
#


# a = 'АПРСУ'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 s = a1 + a2 + a3 + a4
#                 n += 1
#                 # print(n,s)
#                 if a1 == 'У':
#                     print(n)
#                     print(s)
#                     exit()


#
# a = 'БКФ'
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
#                         if n == 342:
#                             print(s)


#
#
# a = 'АНДРЕЙ'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 s = a1 + a2 + a3 + a4
#                 if a1 != 'Й' and (s.count('А') >= 1 or s.count('Е') >= 1) :
#                     n += 1
#
# print(n)


#
# a = 'РУСЛАН'
# n = 0
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         s = a1 + a2 + a3 + a4 + a5 + a6
#                         if len(set(s)) == 6 and 'УА' not in s and 'АУ' not in s:
#                             n += 1
#
# print(n)



# a = "АВСХ"
# b = 'АВС'
# n = 0
# for a1 in a:
#     for a2 in b:
#         for a3 in b:
#             for a4 in b:
#                 for a5 in b:
#                     s = a1 + a2 + a3 + a4 + a5
#                     if a1 == 'Х' or s.count('Х') == 0:
#                         n += 1
# print(n)


# a = 'АНДРЕЙ'
# n = 0
#
# for a1 in a:
#     for a2 in a:
#         for a3 in a:
#             for a4 in a:
#                 for a5 in a:
#                     for a6 in a:
#                         s = a1 + a2 + a3 + a4 + a5 + a6
#                         if s.count('Й') <= 1 and a1 != 'Й' and a6 != 'Й' and 'ЙЕ' not in s and 'ЕЙ' not in s:
#                             n += 1
#
# print(n)


