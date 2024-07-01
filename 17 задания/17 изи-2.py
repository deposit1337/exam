# a = list(map(int,open('17-1-1.txt').readlines()))
# m = []
# for i in range(len(a) -1):
#     for j in range(i + 1,len(a)):
#         if (a[i] + a[j]) % 120 == 0:
#             m.append(a[i] + a[j])
# print(len(m),max(m))

# a = list(map(int,open('17-2-2.txt').readlines()))
# arrMIN = []
#
# m = []
# # sqrtMIN = (min(arrMIN)) ** 2
# for i in range(len(a) - 1):
#     if str(a[i])[-1] == '7':
#         arrMIN.append(a[i])
# sqrtMIN = (min(arrMIN) ** 2)
# for i in range(len(a) - 1):
#     if (((str(a[i])[-1] == '7') + (str(a[i+1])[-1] == '7')) == 1) and (a[i] ** 2 + a[i + 1]**2) < sqrtMIN:
#         m.append((a[i]**2) + ((a[i + 1]) ** 2))
# print(len(m),max(m))

# a = list(map(int, open('17-3-3.txt').readlines()))
#
# minARR = []
# for i in range(len(a) - 1):
#     if (str(a[i])[-1]) == '6':
#         minARR.append(a[i])
# sqrtMIN = (min(minARR)**2)
# m = []
# for i in range(len(a) - 1):
#     if (((str(a[i])[-1]) == '6') + ((str(a[i + 1])[-1]) == '6'))  == 1 and (a[i] ** 2 + a[i + 1]**2) < sqrtMIN:
#         m.append((a[i]**2 + a[i + 1]**2))
# print(len(m), max(m))

# a = list(map(int, open('17-4-4.txt').readlines()))
# m = []
# for i in range(len(a) - 1):
#     for j in range(i + 1,len(a)):
#         if ((a[i] - a[j]) % 60 == 0):
#             m.append(a[i] - a[j])
# print(len(m),max(m))

# a = list(map(int,open('17-5-5.txt').readlines()))
# m = []
# for i in range(len(a)-1):
#     for j in range(i + 1,len(a)):
#         if (a[i] * a[j]) % 26 == 0:
#             m.append(a[i] + a[j])
# print(len(m),max(m))
