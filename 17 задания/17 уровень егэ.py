# a = list(map(int, open('изи1.txt').readlines()))
# m = []
# for i in range(len(a) - 1):
#     if ((abs(a[i]) % 3 == 0) + (abs(a[i+1]) % 3 == 0)) >= 1:
#         m.append(a[i] + a[i+1])
# print(len(m),max(m))


#
# a = list(map(int,open('изи блок номер 2.txt').readlines()))
# m = []
# MID = []
# for i in range(len(a)):
#     if a[i] % 2 != 0:
#         MID.append(a[i])
# sr = sum(MID) / len(MID)
#
# for i in range(len(a) - 1):
#     if ((a[i] % 5 == 0) or (a[i + 1] % 5 == 0)) and (a[i] < sr or a[i + 1] < sr):
#         m.append(a[i] + a[i + 1])
# print(len(m),max(m))


# a = list(map(int,open('изи блок номер 3.txt').readlines()))
# m = []
# for i in range(len(a) - 1):
#     for j in range(i + 1,len(a)):
#         if (a[i] + a[j]) % 126 == 0:
#             m.append(a[i] + a[j])
# print(len(m),max(m))

#
# a = list(map(int,open('изи блок номер 4.txt').readlines()))
# m = []
# for i in range(len(a) - 1):
#     for j in range(i + 1,len(a)):
#         if (a[i] * a[j]) % 34 != 0:
#             m.append(a[i] + a[j])
# print(len(m),max(m))


# a = list(map(int,open('изи блок номер 5.txt').readlines()))
# m = []
# for i in range(len(a)- 1):
#     for j in range(i + 1,len(a)):
#         if (a[i] - a[j]) % 80 == 0:
#             m.append(a[i] - a[j])
#
# print(len(m),max(m))


# a = list(map(int,open('изи блок номер 6.txt').readlines()))
# MINPOSLED = []
# for i in range(len(a)):
#     if a[i] % 21 == 0:
#         MINPOSLED.append(a[i])
# DELITEL = min(MINPOSLED)
# m = []
# for i in range(len(a) - 1):
#     if (a[i] % DELITEL == 0) or (a[i + 1] % DELITEL == 0):
#         m.append(a[i] + a[i + 1])
#
# print(len(m),max(m))
#


# a = list(map(int, open('изи блок номер 7.txt').readlines()))
# m = []
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if ((a[i] + a[j]) % 2 != 0) and (a[i] * a[j]) % 3 == 0:
#             m.append(a[i] + a[j])
# print(len(m), max(m))
