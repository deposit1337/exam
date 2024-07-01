a = list(map(int, open('17.1.txt').readlines()))

m = []
for i in range(len(a) - 1):
    if abs(a[i] - a[i + 1]) % 2 == 0 and abs(a[i] - a[i + 1]) % 37 ==0:
        m.append(a[i] + a[i + 1])

print(len(m),max(m))


# a = list(map(int, open('17.2.txt').readlines()))
#
# # temp = []
# summofdigits = 0
# m = []
# for i in range(len(a)):
#     if a[i] % 35 == 0:
#         # print(a[i])
#         summofdigits += sum(int(x) for x in str(a[i]))
#
#
# for i in range(len(a) - 1):
#     if ((a[i] > summofdigits) and (((hex(a[i + 1])[-2:]) == 'ef') and a[i + 1] <= summofdigits)) or  ((a[i + 1] > summofdigits) and (((hex(a[i])[-2:]) == 'ef') and a[i] <= summofdigits)):
#         m.append(a[i] + a[i + 1])
#
# print(len(m),min(m))

# s = '122345EF'
# print(s[-2:])


# a = list(map(int,open('17.3.txt').readlines()))
# m = []
# for i in range(len(a)):
#     if (int(str(a[i])[-1]) + int(str(a[i])[-2])) >= 15:
#         if (a[i] % 3 != 0) and (a[i] % 4 != 0) and (a[i] % 7 != 0):
#             m.append(a[i])
#
# sumofnums = 0
#
# for i in m:
#     sumofnums += i
#
# print(min(m),sumofnums)
#


# a = list(map(int, open('17.4.txt').readlines()))
#
# minx = 1000000000
# m = []
# for i in range(len(a) - 1):
#     if 50 <= (abs(a[i]) + abs(a[i + 1])) <= 200:
#         minx = min(a[i], a[i + 1], minx)
#         m.append(abs(a[i]) + abs(a[i + 1]))
#
# print(len(m),minx)


