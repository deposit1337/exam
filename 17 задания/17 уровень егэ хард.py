# a = list(map(int, open('хард блок номер 1.txt').readlines()))
# d = 160
# p = 7
# m = []
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if ((a[i] % d) != (a[j] % d)) and ((a[i] % p == 0) or (a[j] % p == 0)):
#             m.append(a[i] + a[j])
# print(len(m), max(m))

# a = list(map(int, open('хард блок номер 2.txt').readlines()))
# m = []
# for i in range(len(a) - 1):
#     if ((a[i] * a[i + 1]) % 2 != 0) and ((a[i] + a[i + 1]) / 2) % 7 == 0:
#         m.append((a[i] + a[i + 1])/2)
# print(len(m),min(m))

# a = list(map(int,open('хард блок номер 3.txt').readlines()))
# m = []
# for i in range(len(a)):
#     if ((str(a[i])[-1] == '5') or (str(a[i])[-1] == '7')) and ((a[i] % 9 != 0) and (a[i] % 11 != 0)):
#         m.append(a[i])
# print(len(m),(min(m) + max(m)))


# a = list(map(int, open('хард блок номер 4.txt').readlines()))
# ALLARR = []
# for i in range(len(a)):
#     ALLARR.append(a[i])
# sr = sum(ALLARR) / len(ALLARR)
# m = []
# for i in range(len(a) - 2):
#     if ((a[i] > sr) + (a[i + 1] > sr) + (a[i + 2] > sr)) >= 2:
#         m.append(a[i] + a[i + 1] + a[i + 2])
# print(len(m), max(m))

#
# a = list(map(int, open('хард блок номер 5.txt').readlines()))
# m = []
# m2 = []
# for i in range(len(a) - 1):
#     if 50 <= (abs(a[i]) + abs(a[i + 1])) <= 200:
#         m.append(a[i])
#         m2.append(a[i + 1])
# print(len(m),min(m),min(m2))