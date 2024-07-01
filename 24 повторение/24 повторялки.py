#
#
# a = open('24.1.txt').read().replace('DD','D D').split()
#
# m = []
#
# for i in a:
#     if 'FE' in i:
#         m.append(i)
#
# print(max(list(map(len,m))))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# a = open('24.2.txt').read().replace('O','N').replace('P','N').replace('NN','N N')
#
# while 'NN' in a:
#     a = a.replace('NN','N N')
# a = a.split()
#
# print(max(list(map(len,a))))
#
#


# a = list(open('24.3.txt').readlines())
# print(a)
# a= ['BBF6YH9XONWIWWR4UXTB41Y442TONGBI766S4KGL7GTWW5W89PJK7I9IL\n','QW1ERTY5EEQW','QW1ERTY5EEQW','YT6XAWQTW154HFERU6MBTWRL1LJKHYMXR4RLS6ETWYQC0EN\n', 'DQRUBM8Q9CHI945WTTXKE6E2RHCKEBJ4T9KATT8CYXTJP286A3\n', '1TE2XGQRQEHNIJTN3IWEZSR406T4X3GYF\n', 'FNQIIXBRX5FPCH38QXJUGL8QWK9ARF8JGIW3WJ4DTYG3EJW9E827XRC\n', '515PNCH1MNLAW5NULBLNBZNA3GX7NTWP6LXN6BX\n', '75JKZ0IA3PCZB263HM9BYI22SZ2YAMUJ9IIB6V0XL5\n', 'TJRZSURERLXFA7BLN05FZG2NCWJ71G9\n', '2ET9EZFZ4QC92CWNZOM86G9IEVM4SERTLIZO2Q7VS3YN52\n', 'P53JPGW1U51HJ8TSIY9JVUI0SOI0U60RBXDPKVH6CH40HKRB1A\n', '9VMKHKJDJIPTX5TKP82P6VG4PG8UAPZE2H073EA7VMM6N4YK9ASF\n', '9KGNYOGY81GADJTYF78D7H9VH1G99H\n', '98JG47S5XEDIVU1P66F0GSC3WXCY7KFLUAFHEGW6EVGPWH9\n', 'HKLOTP9A0DWQJH926SWI9IZNR6DGRRT5IB5FUDGPF\n', 'XQQBWHNEQNGMYR5GHHT9M229P8Y0ZHL5IIDQCQ2BE9ZD893T\n', 'LQ6HWZWEVJGUC8RJTF84DT5OG7TYRHOYGJTZSYWYHJKJPIZS\n', 'IHW8SY235BBJ9XZ316PAQECFIYRG69\n', 'I1BM6QQ6UR7GZO7J13BOZAYOUWE0K6PRLTBYQC5YVPO\n', 'TWFG793F25FXWFTTW8ZOGJQCFXDCC0PWTPYEQQHDDB4XIR0JS\n', 'X53QGKUT7W30E0ERU8T25H5UM7FILQLT938RW7YVVTNX6\n', 'HXK2QAMBUFG2WBOSEQT3SVCRBHTMPG2LYZY5BOSGY7KRM9HMN\n', 'OIYQE2WATKKGWV46S3VNXJNEKV4SLTERVCUNT19YRAYU\n', '8N8NPGTB6WSZ3IRDHOIQC7TWE7M1SRTNFXY9HZSYLGLZAYQJG\n', '1IHKU9MCLF5JK079VST73XY7NHIGMG13PXP7PBEX50WUUP7TU0AWC3B34F\n', 'Z45YIRE1MV6QIB185OTMWBDOZY5NO08FRUCF\n', '3QIHLWW5EBN42LBKMEKREFLT1YFXVZ357Z3BA4RGUW1Y\n', '1BKTQS5VIWEE8SKBRSER6W9TKTZZ43JYXQA\n', 'X4M5A2URGPQWWVUMN05KT8LHYB0794SBQUI8GTJ0YEONL8VKJZ4EFU80QR\n', 'Q1V0V49TYCMA1V8K3KUO5IC5KPY2VTJPHDGRXRCODPH3E7GL3KVQ\n', 'YE3QXLJWYEXF3EIDQ7QDJZRNTBY5U0KCEPW\n', 'NC3DAFCC5YD6G4BIYIKQLLMMQLLLUVCVH8U59ZXOPDJ5J77O6YSBTF60R\n', 'QWA0PEL9RKA32F086KUTG13T998WF3BCKT47E0KY6R1R509\n', 'C9BNYW5FWYKL6G7DUBAK84YNRGB56BKTRZQ0NLLOKE0YATVOT\n', '0DEAXVFPA1SWLVW96K1DNC5A6AKN8ZLN0D7ZENKF8G3MPXS\n', 'SDQ7EXY44WCZ4SPWEXSWZEE45R9U5ELUYU10TXY2376R\n', '7RJEZ0NL9NB1Q71QBFV9DU0XNOGV68Y145V0Q1HZT8AWZS1\n', 'RQY6R4E5JEGWD62TNT5MV7EYRHTG6JYUM9\n', 'C5184R86CASDJRUFKYL4OSR9E2G3COGZ3720HQBLO7U5BJRJOWQZV3\n', '8KHS6BC0NGFVHNAOU1R781H1IN7IAADO5OWVSMCOIDNO7QD\n',]


# m = ''
# k = 0
# for j in range(len(a)):
#     s = ''
#     for letter in a[j]:
#         if letter in 'QWERTY':
#             s = s + letter
#     if 'QWERTY' in s:
#         k += 1
# print(k)

#
# a = open('24.3.txt').readlines()
# print(a)
# count = 0
# for f in a:
#     q = 'QWERTY'
#     k = 0
#     for i in range(len(f)):
#         if f[i] == q[k]:
#             k += 1
#             # print(f[i])
#             if k == 6:
#                 break
#     if k == 6:
#         count += 1
# print(count)
# #
#
#
#
#
#
#
#
#
#
# a = 'QW1ERTY5EEQW'
# result = ''  # Определение переменной за пределами цикла
# for i in a:
#     if i in 'QWERTY':
#         result += i  # Добавление символов к переменной
#
# print(result)
#
#
#
#
#
#
# a = open('24.4.txt').read()
# m = []
# for i in range(len(a)-4):
#     if (a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4]) == (a[i+ 4] + a[i + 3] + a[i + 2] + a[i + 1] + a[i]):
#         m.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4])
#
# print(len(m))
#
#


# a = open('zadanie24_1.txt').read().replace('A','C').replace('C',' ').split()
#
#
# print(max(list(map(len,a))))
#


a = open('24_13866.txt').read().replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
# while '111' in a:
# a = a.replace('111','*')

# a = a.split('*')
# print(a)

# k = 2
# mx = 0
# for i in range(len(a) - 2):
#     if ((a[i] == '1') + (a[i + 1] == '1') + (a[i + 2] == '1')) < 3:
#         k += 1
#     else:
#         mx = max(mx,k)
#         k = 2
#
# print(mx)


# print(max(list(map(len,a)))  + 4)


# 25
# import fnmatch
# for n in range(2024,10**10,2024):
#     if fnmatch.fnmatch(str(n),'112?57*4') and (sum(int(x) for x in str(n)) % 2 != 0):
#         print(n,n // 2024)
#
#


# a = open('24_7 (2).txt').readline().replace('ad','a d').replace('da','d a').split()
# print(max(list(map(len,a))))


# a = open('24_15.txt').read().split('F')
# c = 1
# mx = 0
# for i in a:
#     if i.count('A') <= 2:
#         c += len(i) + 1
#     else:
#         mx = max(c,mx)
#         c = 1
# print(mx)


# a = open('24_9791 (2).txt').read().split('X')
# mx = -10000
# c = 0
#
# for i in range(len(a) - 500):
#     s = 'X'.join(a[i:i + 501])
#     if s.count('Y') == 0:
#         mx = min(len(s) - len(a[i]) - len(a[i + 500]), mx)
# print(mx)




