n = 0
a = 'АГМНСТУ'
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    for a6 in a:
                        n += 1
                        s = a1 + a2 + a3 + a4 + a5 + a6
                        if s[0] != 'У' and s.count('М') == 2 and s.count('Г') <= 1:
                            print(n,s)