# for n in range(100,999+1):
"""for n in range(100,999+1):
    first_sum = int(str(n)[0]) + int(str(n)[1])
    second_sum = int(str(n)[1]) + int(str(n)[2])
    if first_sum < second_sum:
        r = (str(second_sum) + str(first_sum))
        if r == '1412':
            print(n)
    elif first_sum > second_sum:
        r = (str(first_sum) + str(second_sum))
        if r == '1412':
            print(n)"""


"""for i in range(1,1000+1):
    n = i
    s = ''
    while n != 0:
        s = str(n % 2) + s
        n = n // 2
    s = s + s[:2][::-1]
    r = int(s,2)
    if r > 90:
        print(i)
        break"""




# for i in range(1,10000+1):
#     n = i
#     s = ''
#     while n != 0:
#         s = str(n % 2) + s
#         n = n // 2
#     s = s[0:-1]
#     if i % 2 != 0:
#         s = s + '10'
#     else:
#         s = s + '01'
#     r = int(s, 2)
#     if r == 2017:
#         print(i)
#


# print(bin(1000)[2:])



""""
# for i in range(1000,9999):
#     arr = []
#     sum1 = int(str(i)[0]) + int(str(i)[1])
#     sum2 = int(str(i)[1]) + int(str(i)[2])
#     sum3 = int(str(i)[2]) + int(str(i)[3])
#     arr.append(sum1), arr.append(sum2), arr.append(sum3)
#     # print(arr)
#     arr.remove(min(arr))
#     r = (str(min(arr)) + str(max(arr)))
#     # print(r)
#     if r == '1215':
#         print(i)
#         print(arr)
#         break

# arr = [3,3,3]
# if min(arr) == max(arr):
#     arr.remove(min(arr))
# print(arr)
#

"""




# for i in range(100,999):
#     arr = []
#     mult1 = int(str(i)[0]) * int(str(i)[1])
#     mult2 = int(str(i)[1]) * int(str(i)[2])
#     arr.append(mult1), arr.append(mult2)
#     r = (str(max(arr)) + str(min(arr)))
#     if r == '205':
#         print(i)
#

