# a = open('24_17dosrok.txt').read().replace('QR','Q R').replace('QS','Q S').replace('RQ','R Q').replace('SQ','S Q').replace('QQ','Q Q').replace('RR','R R').replace('SS','S S').replace('RS','R S').replace('SR','S R').split()
# print(max(list(map(len,a))))
#
# for i in a:
#     if len(i) == 594:
#         print(i)

# ban = 'QRS'
# a = open('24_17dosrok.txt').read()
# n = 1
# mx = 0
#
# for i in range(len(a) - 1):
#     if ((a[i] in ban) + (a[i + 1] in ban)) < 2:
#         n += 1
#     else:
#         mx = max(mx,n)
#         n = 1
# print(mx)
# import sys
# sys.setrecursionlimit(100000)

# a = open('24_9845.txt').read()
# n = 1
# mx = 0
# for i in range(len(a) - 1):
#     if ((a[i] in '89') and (a[i + 1] in 'ABC')) or ((a[i + 1] in '89') and (a[i] in 'ABC')):
#         n += 1
#     else:
#         mx = max(mx, n)
#         n = 1
# print(mx)

# alph = '0123456789ABCDEF'
# a = open('24_9791.txt').read()
# # print(a)
# n = 0
# mx = 0
#
# for i in range(len(a)):
#     if a[i] in alph:
#         n += 1
#     else:
#         mx = max(mx,n)
#         n = 0
# print(mx)


# a = open('24-1-1.txt').read().split('Y')
# mx = 0
# for i in range(len(a)-150):
#     s = 'Y'.join(a[i:i + 151])
#     mx = max(len(s), mx)
# print(mx)

#
# a = open('24-2-2.txt').read().split('W')
# mn = 10 ** 20
#
# for i in range(len(a) - 130):
#     s = 'W'.join(a[i:i + 131])
#     mn = min(mn, len(s) - len(a[i]) - len(a[i - 130]))
#     # if len(s) == 2113:
#     #     print(s)
# # print(mn)

# a = open('24-2-2.txt').read().split('W')
# mn = 10**20
# for i in range(len(a) - 130):
#     s = 'W'.join(a[i:i + 131])
#     mn = min(mn,len(s) - len(a[i]) - len(a[i + 130]))
# print(mn)

# a = open('24-3-3.txt').read().split('T')
# mn = 10**20
# for i in range(len(a) - 100):
#     s = 'T'.join(a[i:i + 101])
#     mn = min(mn,len(s) - len(a[i]) - len(a[i + 100]))
# print(mn)

# a = open('24-4-4.txt').read().split('U')
#
# mn = 10 ** 22
# for i in range(len(a) - 110):
#     s = 'U'.join(a[i:i + 111])
#     mn = min(mn, len(s) - len(a[i]) - len(a[i + 110]))
# print(mn)

# a = open('24-5-5.txt').read().split('A')
# n = 0
# mx = []
# for i in a:
#     if i.count('E') >= 3:
#         mx.append(len(i))
# print(max(mx))

# import collections
#
# a = open('24-6-6.txt').read()
# n = []
#
# for i in range(len(a)-2):
#     if a[i] == a[i + 1]:
#         n.append(a[i + 2])
#
# print(collections.Counter(n))
#


a = open('inf_26_04_21_24.txt').readlines()
# print(a)
n = []
maxxx = []
for i in a:
    if i.count('A') < 25:
        n.append(i)
for string in n:
    for g in string:
        maxxx.append((string.rfind(g) - string.find(g)))
print(max(maxxx))

#         n.append(string.rfind(g) - string.find(g))
# print(max(maxxx))

# print(max(n))


# s = 'NOTEBOOK'
# n = []
# for i in s:
#     n.append(s.rfind(i) - s.find(i))
