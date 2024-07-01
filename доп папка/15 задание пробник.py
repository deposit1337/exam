arr = []

def dell(n,m):
    return n % m == 0


for A in range(1,1000):
        flag = True
        for x in range(0,1000):
            a = dell(x,12)
            b = 70 <= x <= 80
            c = not(dell(x,A))
            f = a and b and c
            if f != 0:
                flag = False
                break
        if flag == True:
            print(A)

            
