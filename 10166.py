import math

D1, D2 = map(int, input().split())

angle = [[0 for i in range(D2+1)] for i in range(D2+1)]

att = 0

for i in range(D1, D2+1):
    for j in range(1, i+1):
        g = math.gcd(i,j)
        a,b = i//g, j//g
        if angle[a][b] == 0:
            angle[a][b] = 1
            att += 1

print(att)
