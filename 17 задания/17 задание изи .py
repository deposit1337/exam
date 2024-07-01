# a = list(map(int, open('17-1.txt').readlines()))
# m = []
# for i in range(len(a) - 1):
#     if ((a[i] % 3 == 0) + (a[i + 1] % 3 == 0)) > 0 and ((a[i] + a[i + 1]) % 5 == 0):
#         m.append(a[i] + a[i + 1])
# print(len(m),max(m))




#
# a = list(map(int,open('17-2.txt').readlines()))
# m = []
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if (a[i] * a[j]) % 10 == 0:
#             m.append(a[i] + a[j])
# print(len(m),max(m))
#



# a = list(map(int,open('17-3.txt').readlines()))
# m = []
# for i in range(len(a) - 1):
#     for j in range(i + 1,len(a)):
#         if ((a[i] + a[j]) % 2 != 0) and ((a[i] * a[j]) % 5 == 0):
#             m.append(a[i] + a[j])
# print(len(m),max(m))



# a = list(map(int,open('17-4.txt').readlines()))
# m = []
# for i in range(len(a)-1):
#     for j in range(i + 1,len(a)):
#         if (a[i] * a[j]) % 14 != 0:
#             m.append(a[i] + a[j])
# print(len(m),max(m))
#




a = list(map(int,open('17-5.txt').readlines()))
m = []
for i in range(len(a) - 1):
    for j in range(i + 1,len(a)):
        if (a[i] * a[j]) % 62 == 0:
            m.append(a[i] + a[j])
print(len(m),max(m))