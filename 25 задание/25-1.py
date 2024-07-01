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


# for n in range(110203, 110245 + 1):
#     s = set()
#     for d in range(1, int(n ** 0.5) + 1):
#         if n % d == 0 and d % 2 == 0:
#             s.add(d)
#         if (n // d) % 2 == 0 and n % d == 0:
#             s.add(n // d)
#
#     if len(s) == 4:
#         print(sorted(s))


# for n in range(312614,312651+1):
#     s = set()
#     for d in range(1,int(n ** 0.5) + 1):
#         if n % d == 0:
#             s.add(d)
#             s.add(n//d)
#     if len(s) == 6:
#         print(sorted(s))
# mx = 0
# for n in range(84052, 84130 + 1):
#     li = set()
#
#     for d in range(1, int(n ** 0.5) + 1):
#         if n % d == 0:
#             li.add(d)
#             li.add(n // d)
#
#     mx = max(len(li), mx)
#     if len(li) == mx:
#         print(n)

#
#
# def f(n):
#     for d in range(2,int(n ** 0.5) + 1):
#         if n % d == 0:
#             return False
#     return True
#
#
#
# k = 0
# for n in range(245690,245756+1):
#     k += 1
#     if f(n) == True:
#         print(k,n)
#
#
#
