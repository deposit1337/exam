# a = open('хард блок номер 1.txt').read().replace('DD','D D').split()
# # print(a)
# n = []
# mx = 0
# for i in range(len(a)):
#     if a[i].count('FE') >= 1:
#         n.append(a[i])
# n = map(len,n)
# print(max(n))

# a = open('хард блок номер 2.txt').read()
# n = 1
# mx = 0
# for i in range(len(a)-1):
#     if ((a[i] in 'NOP') + (a[i + 1] in 'NOP')) != 2:
#         n += 1
#     else:
#         mx = max(mx,n)
#         n = 1
# print(mx)

# a = open('хард блок номер 3.txt').readlines()
# # print(a)
# n = 0
# for i in a:
#     q = 'QWERTY'
#     k = 0
#     for g in range(len(i)):
#         if i[g] == q[k]:
#             k += 1
#             if k == 6:
#                 break
#     if k == 6:
#         n += 1
# print(n)

# a = open('хард блок номер 4.txt').read()
# n = 1
# mx = 0
# for i in range(len(a)- 1):
#     if ((int(a[i]) % 2) == (int(a[i + 1]) % 2)):
#         n += 1
#     else:
#         mx = max(mx,n)
#         n = 1
# print(mx)

# a = open('хард блок номер 5.txt').read().replace('NEWYEAR','*')
# a.count('*')
# print(a.count('*'))

# a = open('24__12.txt').read().replace('4','2').replace('5','1').replace('3','1').replace('21','*').replace('2',' ').replace('1',' ').split()
# print(max(list(map(len,a))))

# import collections
# a = open('24_14.txt').read()
# m = [0]* 122
# for i in range(len(a) - 2):
#     if a[i] == a[i + 2]:
#         # m.append(a[i + 1])
#         ind = ord(a[i + 1])
#         m[ind] += 1
# print(chr(m.index(max(m))))
# # print(collections.Counter(m))
#
#
# a = open('24_15.txt').read().split('F')
# n = 1
# mx = 0
# for i in a:
#     if i.count('A') <= 2:
#         n += len(i) + 1
#     else:
#         mx = max(n,mx)
#         n = 1
# print(mx)


