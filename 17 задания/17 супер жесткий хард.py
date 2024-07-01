# a = list(map(int, open('хард блок №1.txt').readlines()))
# # print(a)
# arr = []
# for i in range(len(a)):
#     if str(a[i])[-2:] == '17':
#         arr.append(a[i])
# mx = max(arr)
#
#
# m = []
# for i in range(len(a)-2):
#     if ((len(str(a[i])) == 4) + (len(str(a[i + 1])) == 4) + (len(str(a[i + 2])) == 4)) == 2 and ((a[i] % 5 == 0) or (a[i + 1] % 5 == 0) or (a[i + 2] % 5 == 0)) and (a[i] + a[i + 1] + a[i + 2]) > mx :
#         # if (a[i] + a[i + 1] + a[i + 2]) > mx:
#         m.append(a[i] + a[i + 1] + a[i + 2])
# print(len(m),max(m))


# a = list(map(int, open('хард блок №2.txt').readlines()))
# arr = []
# for i in range(len(a)):
#     if (len(str(abs(a[i]))) == 4) and (str(a[i])[-1]) == '1':
#         arr.append(a[i])
# mx = max(arr)
# arr2 = []
# for i in range(len(a)):
#     if len(str(abs(a[i]))) == 2:
#         arr2.append(a[i])
# minx = min(arr2)**2
#
# m = []
# for i in range(len(a) - 2):
#     if ((a[i] > minx) + (a[i + 1] > minx) + (a[i + 2] > minx)) == 2:
#         if ((abs(a[i])) * (abs(a[i + 1])) * (abs(a[i + 2]))) % mx == 0:
#             m.append((abs(a[i])) + (abs(a[i + 1])) + (abs(a[i + 2])))
# print(len(m),max(m))


a = list(map(int, open('хард блок №3.txt').readlines()))
m = []
for i in range(len(a) - 1):
    for j in range(i + 1,len(a)):
        if ((a[i] + a[j]) % 18 == 0) + ((a[i] * a[j]) % 18 == 0) == 1:
            m.append(a[i] + a[j])
            print(a[i],a[j])

print(len(m),max(m))

# a = list(map(int, open('хард блок №4.txt').readlines()))
# arr = []
# for i in range(len(a)):
#     if str(a[i])[-1] == '7':
#         arr.append(a[i])
# minxsqrt = min(arr) ** 2
# m = []
# for i in range(len(a) - 1):
#     if (str(a[i])[-1]) == (str(a[i + 1])[-1]):
#         if (((abs(a[i]) % 7) == 0) + ((abs(a[i + 1]) % 7) == 0)) == 1:
#             if ((a[i] ** 2) + (a[i + 1] ** 2)) <= minxsqrt:
#                 m.append(a[i] ** 2 + a[i + 1] ** 2)
# print(len(m), max(m))


# a = list(map(int, open('хард блок №5.txt').readlines()))
# # summa = 0
# # for i in range(len(a)):
# #     summa += a[i]
# # sr = summa / len(a)
# sr = sum(x for x in a) / len(a)
#
# m = []
# for i in range(len(a) - 2):
#     if ((a[i] > sr) + (a[i + 1] > sr) + (a[i + 2] > sr)) >= 2:
#         m.append(a[i] + a[i + 1] + a[i + 2])
# print(len(m),max(m))
