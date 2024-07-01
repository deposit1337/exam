import sys

sys.set_int_max_str_digits(10000)

# n = 7 * 512 ** 1912 +(6 * 64 ** 1954) - (5 * 8 ** 1991 ) - (4 * 8  ** 1980) - 2022
# g = ''
# while n != 0:
#     g = str(n % 8) + g
#     n = n // 8
# print(g.count('7'))













#
# n = 3 * 1024 ** 75 + 2 * 256 ** 76 - 16 ** 77 -2023
#
# alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# s = ''
# while n != 0:
#     s = alph[n % 32] + s
#     n = n // 32
# print(s.count('0'))
#
# alph = "0123456789ABCDEF"
#
# for x in alph:
#     n = int('8' + x + '834', 16) + int('44' + x + '27', 16)
#     if n % 23 == 0:
#         print(n // 23)
#
#
#

#
# alph18 = '0123456789ABCDEFGH'
# alph12 = '0123456789AB'
#
# for x in alph18:
#     n1 = int('28' + x + '2',18)
#     for x in alph12:
#         n2 = int('93' + x + '5',12)
#         r = n1 + n2
#         if r % 133 == 0:
#             print(r // 133)



# alph13 = '0123456789ABC'
# for x in alph13:
#     for y in alph13:
#         n = int('8' + x + '78' + y,13) + int('79' + x + y + '7',18)
#         if n % 9 == 0:
#             print(n // 9)
#             break


#
# alph19 = '0123456789ABCDEFGHI'
# for x in alph19:
#     n = int('98' + x + '79641',19) + int('36' + x + '14' ,19) + int('73' + x + '4',19)
#     if n % 18 == 0:
#         print(n // 18)














#

