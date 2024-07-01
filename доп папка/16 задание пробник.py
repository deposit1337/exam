def f(n):
    if n <=  2:
        return 1
    elif n > 2 and (n % 2 != 0):
        return f(n-1)-n
    elif n > 2 and (n % 2 == 0):
        return f(n-2)-f(n-1)+2
print(f(27))
