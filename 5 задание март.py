# s = '12345'
# print(s + s[0:2][::-1])

# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     s = s + s[0:2][::-1]
#     r = int(s, 2)
#     if r > 90:
#         print(i)


#
# for i in range(1,10000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     s = s[0:-1]
#     if i % 2 == 0:
#         s = s + '01'
#     else:
#         s = s + '10'
#     r = int(s, 2)
#     if r == 2017:
#         print(i)


#
# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     digitsum = sum(int(x) for x in s)
#     s = s + str(digitsum % 2)
#     digitsum2 = sum(int(x) for x in s)
#     s = s + str(digitsum2 % 2)
#     r = int(s,2)
#     if r > 77:
#         print(i)
#         exit()
#


# for i in range(2,1000):
#     n = i
#     s = ''
#     while n != 0:
#          s = str(n % 2) + s
#          n = n // 2
#     s = s + s[-2]
#     s = s + s[1]
#     r = int(s,2)
#     if r > 150:
#         print(i)


# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     if int(s) % 2 == 0:
#         s += '10'
#     else:
#         s += '01'
#     r = int(s,2)
#     if r < 109:
#         print(r)


# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     if s.count('1') > s.count('0'):
#         s += '1'
#     else:
#         s += '0'
#     r = int(s,2)
#     if r > 80:
#         print(r)
#         exit()


# for i in range(1, 1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 3) + s
#         n = n // 3
#     s = s + str(i % 3)
#     r = int(s, 3)
#     if r >= 100:
#         print(r)
