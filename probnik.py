n = 134
s = ''
while n != 0:
    s = str(n % 5) + s
    n = n // 5
print(s)