def f(n):
    for d in range(2,n):
        if n % d == 0:
            return False
    return True
             


for n in range(1,10):
    s = '>' + 39 * '0' + n * '1' + 39 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        s = s.replace('>1','22>',1)
        s = s.replace('>2','2>',1)
        s = s.replace('>0','1>',1)
    if f(s.count('2') * 2 + s.count('1') * 1):
        print(n)
