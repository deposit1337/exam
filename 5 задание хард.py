"""for i in range(1,1000):
    n = i
    s = ''
    while n != 0:
        s = str(n % 2) + s
        n = n // 2
    s = s + s[0:2][::-1]
    r = int(s,2)
    if r > 74:
        print(i)
        break
"""
# s = '13245'
# s = s + s[0:2][::-1] #1324531
# print(s)

"""q = 0
for i in range(1000, 9999):
    s = str(i)
    if int(s[0]) % 2 != 0 and int(s[1]) % 2 != 0 and int(s[2]) % 2 != 0 and int(s[3]) % 2 != 0:
        arr = []
        sum1 = int(str(i)[0]) + int(str(i)[1])
        sum2 = int(str(i)[2]) + int(str(i)[3])
        arr.append(sum1), arr.append(sum2)
        r = (str(min(arr)) + str(max(arr)))
        # print(i)
        # print(r)
        # print(arr)
        if r == '616':
            q += 1
print(q)
    # print(q)"""






#
# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     summary = sum(int(x) for x in s)
#     e = s + str(summary % 2)
#     summary2 = sum(int(x) for x in e)
#     b = e + str(summary2 % 2)
#     r = int(b,2)
#     print(r)
#



# summary = 1101
# e = str(summary) + str(summary % 2)
# s = '12345'
# print(type(sum(int(x) for x in s)))

# arr = []
# for i in range(1,1000):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     if i % 2 == 0:
#         s = s + '00'
#     else:
#         s = s + '11'
#     r = int(s, 2)
#     if r < 94:
#         arr.append(i)
#     # while r < 94:
#     #     arr.append(n)
# print(max(arr))


#
# for i in range(10000,99999):
#     arr = []
#     sum1 = int(str(i)[0]) + int(str(i)[2]) + int(str(i)[4])
#     sum2 = int(str(i)[1]) + int(str(i)[3])
#     arr.append(sum2),arr.append(sum1)
#     r = str(min(arr)) + str(max(arr))
#     if r == '723':
#         print(i)
#
#


# for i in range(1000,9999):
#     arr = []
#     sum1 = int(str(i)[0]) + int(str(i)[1])
#     sum2 = int(str(i)[1]) + int(str(i)[2])
#     sum3 = int(str(i)[2]) + int(str(i)[3])
#     arr.append(sum1),arr.append(sum2),arr.append(sum3)
#     arr.remove(min(arr))
#     r = (str(min(arr)) + str(max(arr)))
#     if r == '613':
#         print(i)
#
#
#



#
# for i in range(0,255+1):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     s = '0' * (8 - len(s)) + s
#     g = ''
#     for dig in s:
#         if dig == '1':
#             g += '0'
#         else:
#             g += '1'
#     r1 = int(g,2)
#     result = int(r1) - int(i)
#     if result == 133:
#         print(i)
#









# s = '1010'
# g = ''
# for dig in s:
#     if dig == '1':
#         g += '0'
#     else:
#         g += '1'
# print(g)

# s = '0' * (8 - len(s)) + s
#
# print(s)
#
# s = '1010'
# s = s.zfill(8)
#
# print(s)
#













