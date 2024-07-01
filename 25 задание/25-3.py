# # 1
# for n in range(800001, 800000 + 500):
#     s = set()
#     # mxminx = 0
#     for d in range(2, int(n ** 0.5) + 1):
#         if n % d == 0:
#             s.add(d)
#             s.add(n // d)
#             mxminx = min(s) + max(s)
#     if mxminx % 138 == 0:
#         print(n, mxminx)
#
# # 2
# for n in range(190201, 190260 + 1):
#     s = set()
#     for d in range(1, int(n ** 0.5) + 1):
#         if n % d == 0 and d % 2 == 0:
#             s.add(d)
#         if n % d == 0 and (n // d) % 2 == 0:
#             s.add(n // d)
#         if len(s) > 4:
#             break
#     if len(s) == 4:
#         print(n,list(sorted(s))[2:4+1])
#
#
# # 3
#
# for n in range(220000 + 1, 220043 + 1):
#     s = set()
#     mind = 0
#     for d in range(2, int(n ** 0.5) + 1):
#         if n % d == 0:
#             s.add(d)
#             s.add(n // d)
#             mind = min(s) + max(s)
#     if mind % 10 == 4:
#         print(n, mind)
#
#
# # 4
#
# for n in range(105000000, 106000000 + 1,2):
#     k = 0
#     for d in range(1, int(n ** 0.5) + 1):
#         if n % d == 0 and d % 2 == 0:
#             k += 1
#         if n % d == 0 and (n // d) % 2 == 0:
#             k += 1
#         if k > 3:
#             break
#     if k == 3:
#         print(n)


# 5

# for n in range(846320, 846320+200):
#     s = set()
#     for d in range(2, int(n ** 0.5) + 1):
#         if n % d == 0:
#             s.add(d)
#             s.add(n // d)
#     try:
#         mind = min(s) + max(s)
#     except ValueError:
#         mind = 0
#
#     if mind % 26 == 3:
#         print(n, mind)


for n in range(452022, 452600 + 1):
    summdelitel = 0
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            summdelitel = d + n // d
            break
    if summdelitel % 7 == 3:
        print(n, summdelitel)
