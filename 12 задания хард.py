# uniq = []
# for n in range(1,500):
#     s = '8' * n
#     while '555' in s or '888' in s:
#         s = s.replace('555','88',1)
#         s = s.replace('888','55',1)
#     uniq.append(s)
#
# print(len(set(uniq)))
#

# for x in range(1,100):
#     for y in range(1,100):
#         for z in range(1,100):
#             s = '0' + '1' * x + '2' * y + '3' * z
#             while '01' in s or '02' in s or '03' in s:
#                 s = s.replace('01', '30', 1)
#                 s = s.replace('02', '3103', 1)
#                 s = s.replace('03', '1201', 1)
#             if s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46:
#                 print


r = 1
s = '7' * 333
while '66' in s or '77777' in s:
    if '66' in s:
        s = s.replace('66', '7', 1)
    else:
        s = s.replace('77777', '676676', 1)
for dig in s:
    if dig != 0:
        r *= int(dig)

print(r)

# r = 0
# for n in range(4, 50):
#     s = '>' + '1' * n + '2' * n + '3' * n
#     while '>1' in s or '>2' in s or '>3' in s:
#         s = s.replace('>1','22>3', 1)
#         s = s.replace('>2', '2>', 1)
#         s = s.replace('>3', '11>2', 1)
#     ans = s.count('1') + s.count('2') * 2 + s.count('3') * 3
#     if ans % 7 == 0:
#         r += 1
#
# print(r)


# def f(n):
#     for d in range(2,n):
#         if n % d == 0:
#             return False
#     return True


# for n in range(1, 1000):
#     s = '>' + 40 * '0' + n * '1' + 40 * '2'
#     while '>1' in s or '>2' in s or '>0' in s:
#         s = s.replace('>1', '22>', 1)
#         s = s.replace('>2', '2>', 1)
#         s = s.replace('>0', '1>', 1)
#     ans = s.count('1') + s.count('2') * 2 + s.count('3') * 3
#     if len(str(ans)) == 3 and str(ans)[0] == str(ans)[1] == str(ans)[2]:
#         print(n)
#
#
#


# ans = s.count('2') * 2 + s.count('1') * 1
# if f(ans):
#     print(n)
#     break


# for i in range(3,51):
#     print(i)
