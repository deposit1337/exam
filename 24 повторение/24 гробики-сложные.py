# a = open('24_3099 (3).txt').read()
#
# m = [0] * 122
# for i in range(len(a)):
#     m[ord(a[i])] += 1
# k = 0
# for i in range(len(m)):
#     if m[i] != 0:
#         print(chr(i), m[i])
#         if m[i] % 2 != 0:
#             k += 1
# print(k // 2)
#
#

# a = open('24__3091 (1).txt').readlines()
#
#
# def f(line):
#     for i in range(len(line) - 6):
#         s = line[i: i + 7]
#         if s == s[::-1]:
#             return 1
#         else:
#             for i in range(len(s)):
#                 for j in range(i + 1, len(s)):
#                     a = list(s)
#                     a[i], a[j] = a[j], a[i]
#                     if a == a[::-1]:
#                         return 1
#     return 0
#
#
# k = 0
# for line in a:
#     k += f(line)
#
# print(k)


a = open('24_2578 (1).txt').read().replace('E','A').replace('I','A').replace('O','A').replace('U','A').replace('Y','A').split('.')
# print(a)
mx = 0
for line in a:
    lenofline = 0
    k = 0
    for i in range(len(line)):
        if k <= 7:
            if line[i] == 'A':
                k += 1
            lenofline += 1
        else:
            mx = max(lenofline,mx)
            lenofline = 0
print(mx)