# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x == y) <= ((x and w) == (z and (not w)))
#                 if not f:
#                     print(x,y,z,w)

# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 f = (x and y) or (y == z) or w
#                 if not f:
#                     print(x, y, z, w)
#
# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 f = (x or (not y)) and (not(x == z)) and (not w)
#                 if f:
#                     print(x, y, z, w)





# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if not(((x and (not y)) == (z or (not w))) <= (x and z)):
#                     print(x, y, z, w)
#






# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((w <= (not x)) == (z <= y)) and (y or w)
#                 if not f:
#                     print(x, y, z, w)
#

print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((not(z == w)) <= (w and not(x))) or (x and not(y))):
                    print(x, y, z, w)