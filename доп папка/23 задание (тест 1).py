def f(x,y):
    if x == y:
        return 1
    elif x < y or (x == 20):
        return 0
    else:
        return f(x - 2,y) + f(x // 2,y)


print(f(80,40) * f(40,1))
#print(f(3,9)* f(9,20))
