import math

n = int(input())

div1 = []
for i in range(1, int(math.sqrt(n))+1):
    if n%i==0:
        div1.append(i)
div2 = []
for i in range(1, int(math.sqrt(n+2))+1):
    if (n+2)%i==0:
        div2.append(i)


for i1 in div1:
    i2 = n//i1
    for j1 in div2:
        j2 = (n+2)//j1
        
        a = -i1*j1+i2*j2 == (n+1)
        b = i1*j1-i2*j2 == (n+1)
        c = -i1*j2+i2*j1 == (n+1)
        d = i1*j2-i2*j1 == (n+1)

        if a:
            print(i1, j2, i2, -j1)
            exit()
        elif b:
            print(i1, -j2, i2, j1)
            exit()
        elif c:
            print(i1, j1, i2, -j2)
            exit()
        elif d:
            print(i1, -j1, i2, j2)
            exit()

print(-1)