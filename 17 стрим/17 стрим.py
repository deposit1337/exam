# a = list(map(int, open('17.1').readlines()))
# maxsqrt = []
# for i in a:
#     if abs(i % 10) == 3:
#         maxsqrt.append(i)
#
# mx = max(maxsqrt) ** 2
# ans = []
# for i in range(len(a)-1):
#     if (((str(a[i])[-1] == '3') + (str(a[i + 1])[-1] == '3')) == 1) and (((a[i]**2) + (a[i + 1]**2)) >= mx):
#         ans.append((a[i]**2) + (a[i + 1]**2))
#
# print(len(ans),max(ans))

# a = list(map(int,open('17_9993 (1).txt').readlines()))

# def f(n):
#     if n < 2:
#         return 0
#     for d in range(2,int(n**0.5) + 1):
#         if n % d == 0:
#             return 0
#     return 1
#
#
# temp = []
# for i in a:
#     if str(i)[-2:] == '17':
#         temp.append(i)
#
# mx17 = max(temp)
# m = []
# for i in range(len(a) - 1):
#     if ((f((a[i])) == 1) + (f((a[i + 1])) == 1)) == 1:
#         if (a[i] + a[i + 1]) % mx17 == 0:
#             m.append(a[i] * a[i + 1])
#
# print(len(m),max(m))

#
# a = list(map(int, open("17.3").readlines()))
#
# max4 = []
# A = -100000
# for i in range(len(a) - 3):
#     if (str(a[i])[-1] == str(a[i + 1])[-1] == str(a[i + 2])[-1] == str(a[i + 3])[-1]):
#         A = max((a[i] + a[i + 1] + a[i + 2] + a[i + 3]), A)
#
# # print(A)
# #
# mxdvuznach = 0
# for i in range(len(a)):
#     if len(str(abs(a[i]))) == 2:
#         mxdvuznach = max(mxdvuznach,a[i])
#
# # print(mxdvuznach)
# m = []
#
# for i in range(len(a) - 4):
#     if ((((a[i] < A) + (a[i + 1] < A) + (a[i + 2] < A) + (a[i + 3] < A) + (a[i + 4] < A)) == 1)):
#         if (a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4]) % mxdvuznach == 0:
#             m.append((a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4]))
#
# print(len(m),min(m))


a = list(map(int, open('17.4').readlines()))

mxsqrt = []

for i in range(len(a)):
    if len(str(abs(a[i]))) == 5 and str(a[i])[-2:] == '21':
        mxsqrt.append(a[i])

mx = max(mxsqrt)
m = []
for i in range(len(a) - 1):
    if (((len(str(abs(a[i]))) == 5) and (str(a[i])[-2:] == '21')) + (
            (len(str(abs(a[i + 1]))) == 5) and (str(a[i + 1])[-2:] == '21'))) == 1:
        if (a[i]**2 + a[i+1]**2) >= mx**2:
            m.append(a[i] + a[i + 1])

print(len(m), max(m))
