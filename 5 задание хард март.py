# for i in range(1, 1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     summ1 = sum(int(x) for x in s)
#     s = s + str(summ1 % 2)
#     summ2 = sum(int(x) for x in s)
#     s = s + str(summ2 % 2)
#     r = int(s,2)
#     if r > 97:
#         print(r)
#         exit()


# for i in range(128,255+1):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     s = s.zfill(8)
#     g = ''
#     for dig in s:
#         if dig == '1':
#             g = g + '0'
#         else:
#             g = g + '1'
#     preR = int(g,2)
#     r = i - preR
#     if r == 185:
#         print(i)

# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     summ1 = sum(int(x) for x in s)
#     s = s + str(summ1 % 2)
#     summ2 = sum(int(x) for x in s)
#     s = s + str(summ2 % 2)
#     r = int(s, 2)
#     if r > 123:
#         print(r)
#         exit()




# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     if i % 2 == 0:
#         s = '1' + s + '0'
#     else:
#         s = '11' + s + '11'
#     r = int(s,2)
#     if r > 52:
#         print(r)
#         exit()

# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     if s.count('0') == s.count('1'):
#         s = s + s[-1]
#     else:
#         if s.count('0') > s.count('1'):
#             s = s + '1'
#         elif s.count('0') < s.count('1'):
#             s = s + '0'
#     if s.count('0') == s.count('1'):
#         s = s + s[-1]
#     else:
#         if s.count('0') > s.count('1'):
#             s = s + '1'
#         elif s.count('0') < s.count('1'):
#             s = s + '0'
#     if s.count('0') == s.count('1'):
#         s = s + s[-1]
#     else:
#         if s.count('0') > s.count('1'):
#             s = s + '1'
#         elif s.count('0') < s.count('1'):
#             s = s + '0'
#     r = int(s, 2)
#     if (i > 104) and (r % 4 == 0):
#         print(i)
#         exit()


# d = []
#
# for n in range(10000):
#     n2 = bin(n) [2:]
#     n2 += n2[-3:] if n%3 == 0 else bin((n % 3) * 3) [2:]
#     r = int(n2, 2)
#     if r < 137:
#         d.append(r)
# print(max(d))

# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     summI = sum(int(x) for x in str(i))
#     if summI % 2 == 0:
#         s += '0'
#     else:
#         s += '1'
#     summ2 = sum(int(x) for x in str(int(s,2)))
#     if summ2 % 2 == 0:
#         s += '0'
#     else:
#         s += '1'
#     summ3 = sum(int(x) for x in str(int(s,2)))
#     if summ3 % 2 == 0:
#         s += '0'
#     else:
#         s += '1'
#     r = int(s,2)
#     if r > 2054:
#         print(r)
#         exit()


"""РАЗБОР ОШИБОК 4 ВОПРОС"""
#
# a = []
# for n in range(1, 100):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 = "1" + n2 + "0"
#     else:
#         n2 = "11" + n2 + "11"
#     if int(n2, 2) > 52:
#         a.append(int(n2, 2))
# print(min(a))

#
# arr = []
# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     if i % 2 == 0:
#         s = '1' + s + '0'
#     else:
#         s = '11' + s + '11'
#     r = int(s,2)
#     if r > 52:
#         print(r)
# # print(min(arr))