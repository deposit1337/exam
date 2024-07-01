
# s = '>' + 100 * '432' + '<'
# while '>4' in s or '>3' in s or '>2' in s or '<4' in s or '<3' in s or '<2' in s:
#     if '>4' in s or '>3' in s:
#         s = s.replace('>4','2>3',1)
#         s = s.replace('>3', '1>2', 1)
#     else:
#         if '>4' in s or '<3' in s:
#             s = s.replace('4<', '3<2', 1)
#             s = s.replace('3<', '2<1', 1)
#         else:
#             s = s.replace('>2', '0>', 1)
#             s = s.replace('<2', '0<', 1)
#
#
#
# print(s.count('1') * 1 + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4)



    # if (s.count('5') * 5 + s.count('9') * 9 + s.count('3') * 3) % len(s) == n:
    #     print(n)






# r = 0




for x in range(1,100):
    for y in range(1, 100):
        for z in range(1, 100):
            s = '0' + '1' * x + '2' * y + '3' * z
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01','30',1)
                s = s.replace('02', '101', 1)
                s = s.replace('03','202',1)
            if s.count('1') == 15 and s.count('2') == 10 and s.count('3') == 60:
                print(x)


















