#
# a = open('24_8 (3).txt').read().split('A')
# c = 0
# for i in a:
#     if len(i) + 2 >= 10:
#         if i.count('B') == 0:
#             c += 1
#
# print(c)
import collections

# a = open('24_8 (3).txt').read().split('A')
# c = 0
# for i in a:
#     if len(i) + 2 >= 10:
#         if i.count('B') == 0:
#             c += 1
# print(c)
#
#

# import collections
# a = open('24_3099.txt').readline()
#
# letters = collections.Counter(a)
# c = 0
# for key in letters:
#     if letters[key] % 2 != 0:
#         c += 1
# print(c//2)


# # print(len(a))
#
# import collections
#
# c = collections.Counter(a)
# k = 0
# for key in c:
#     value = c[key]
#     if value % 2 != 0:
#         k +=1
# print(k/2)

#
# a = open('24__3091.txt').readlines()
#
#
# def f(line):
#     for i in range(len(line) - 6):
#         cs = line[i: i + 7]
#         if cs == cs[::-1]:
#             return 1
#         else:
#             for i in range(len(cs)):
#                 for j in range(i + 1, len(cs)):
#                     a = list(cs)
#                     a[i], a[j] = a[j], a[i]
#                     if a == a[::-1]:
#                         return 1
#     return 0
#
#
# counter = 0
# for i in a:
#     counter += f(i)
# print(counter)

# # a = ['ADGHADGOJAJAG','ADGHADGOJAJAG']
# k = 0
# for j in a:
#     for i in range(len(j)):
#         s = j[i:i + 7]
#         # print(s)
#         letters = collections.Counter(s)
#         # print(letters)
#         c = list(letters.values())
#         nechet = c.count(1)
#         if len(j[i:i + 7]) == 7:
#             if nechet == 1:
#                 bukva = next(key for key, value in letters.items() if value == 1)
#                 if s[3] == bukva:
#                     k += 1
# print(k)

#
# c = ({'A': 2, 'D': 2, 'G': 2, 'H': 1})
#
# key = next(key for key, value in c.items() if value == 1)
# print(key)


# print(k)


# first_half = a[:-500000]
# second_half = a[500000:]
#
# c1 = collections.Counter(first_half)
# c2 = collections.Counter(second_half)
#
# for key in c1:
#     value = c1[key]
#     print(key,value)
#
# for key in c2:
#     value = c2[key]
#     print(key,value)
#


# a = open('24_12476.txt').read().replace('ORO', ' ').replace('ROR', ' ')

# while 'ORO' in a or 'ROR' in a:
#     a = a.replace('ORO', 'O RO')
#     a = a.replace('ROR', 'R OR')


# print(len('')


import collections

a = open('24_7981.txt').read().replace('B','A').replace('C','A').replace('AA','A A')
while 'AA' in a:
    a = a.replace('AA','A A')
a = a.split()
m = []
for i in a:
    if len(i) >=2:
        m.append(i)
print(len(m))