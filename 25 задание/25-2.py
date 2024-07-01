# 1 задание

# def f(n):
#     for d in range(2, int(n ** 0.5) + 1):
#         if n % d == 0:
#             return 0
#     return 1
#
#
# k = 0
# for n in range(2422000, 2422080 + 1):
#     if f(n) == 1:
#         k += 1
#         print(k, n)
#



# 2 задание


# for n in range(110203,110245+1):
#     li = set()
#     for d in range(1, int(n ** 0.5) + 1):
#         if n % d == 0 and d % 2 == 0:
#             li.add(d)
#         if n % d == 0 and (n//d) % 2 == 0:
#             li.add(n//d)
#     if len(li) == 4:
#         print(sorted(li))


# 3 задание

# for n in range(123456789, 223456789 + 1):
#     k = 0
#     maxD = 0
#     if int(n ** 0.5) == n ** 0.5:
#         k += 1
#         for d in range(2, int(n ** 0.5)):
#             if n % d == 0:
#                 maxD = n // d
#                 k += 2
#                 if k > 3:
#                     break
#     if k == 3:
#         print(n, maxD)


#4 задание

# for n in range(600001, 600030):
#     minD = 10**20
#     for d in range(2, int(n ** 0.5) + 1):
#         if n % d == 0 and ((d % 10) == 7) and d != 7:
#             minD = min(d, minD)
#             print(n,minD)



# 5 задание

# for n in range(200000001, 200000001+19):
#     k = 0
#     multdel = 0
#     s = set()
#     for d in range(2, int(n ** 0.5) + 1):
#         if n % d == 0:
#             s.add(d)
#             s.add(n // d)
#
#     mn = 1
#     for x in range(0, 4 + 1):
#         if len(s) < 5:
#             mn = 0
#         else:
#             mn *= list(sorted(s))[x]
#     if 0 < mn < n:
#         print(n , mn)


# k = 5
# n = 200000001
# while k:
#     mn = 1
#     j = 0
#     for i in range(2, int((n//6)**.5) +1):
#         if not(n%i) :
#             mn *= i
#             j += 1
#             if j == 5:
#                 break
#     if j == 5 and mn < n:
#         print(n, mn)
#         k -= 1
#     n += 1