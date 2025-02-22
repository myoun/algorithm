import math
import random

N = int(input())
A = [*map(int, input().split())]


m, t = 1, 0

for i in range(N):
    a = A[i]

    if a >= m:
        m = a
        continue

    r = math.ceil(math.log2(m)-math.log2(a))
    print(r)
    t += r
    m = a*2**r

print(t)
