# a = open('24-1.txt').read().replace('ad','a d').replace('da','d a').split()
# print(max(list(map(len,a))))
import collections

# a = open('24-2.txt').readlines()
# len5 = []
#
# for s in a:
#     n = 1
#     mx = 0
#
#     for i in range(len(s)-1):
#         if s[i] == s[i + 1]:
#             n += 1
#         else:
#             mx = max(mx, n)
#             n = 1
#     if mx == 5:
#         len5.append(s)
#
# for i in len5:
#     print(i)
# # j = []
# # for s in len5:
# #     for i in range(len(s) - 1):
# #         if s[i] == s[i + 1]:
# #             j.append(s[i + 1])
# # print(collections.Counter(j))
# #
# #

#
# a = open('24 изи 2.txt').read()
#
# s = 0
# n = 1
# mx = 0
# for i in range(len(a) - 1):
#     if a[i] == a[i + 1]:
#         n += 1
#         if n > mx:
#             mx = n
#             s = a[i + 1]
#     else:
#         n = 1
#
# print(s,mx)
# print(a)
#
# A

# a = open('24-3.txt').read().split('.')
# n = []
# mx = 0
#
# for i in a:
#     if i.count('A') >= 3:
#         n.append(i)
# print(max(list(map(len,n))))



# s = 'ABCDSSSSFFFSDADDD'

# if s.count('S') <= 2:
#     print(s)







# a = open('изи-4.txt').read().replace('AB','*').replace('AC','*').replace('A',' ').replace('B',' ').replace('C',' ').split()
# print(max(list(map(len,a))))


# a = open('изи-5.txt').read().replace('XYZ','*').replace('ZYX','*').replace('Z',' ').replace('Y',' ').replace('X',' ').split()
# print(max(list(map(len,a))))
#
#












# for i in a:
#     if len(i) == 754:
#         print(i)
# # print(a)
#
# #
# # print(len(''))
# #
# #
# #
#
#





# a = open('хард-2.txt').read().replace('XIX','XI IX').split()
# print(max(list(map(len,a))))
# # for i in a:
# #     if len(i) == 289:
# #         print(i)



# a = open('хард-3.txt').read().replace('NPO','*').replace('PNO','*').replace('N',' ').replace('O',' ').replace('P',' ').split()
# print(max(list(map(len,a))))

#
# a = open('хард-4.txt').read().replace('ZX','*').replace('ZY','*').replace('Z',' ').replace('Y',' ').replace('X',' ').split()
# print(max(list(map(len,a))))



# a = open('хард-5.txt').read().replace('XVIII','').split()
# print(max(list(map(len,a))))
# # for i in a:
# #     print(i)

