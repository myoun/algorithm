import sys

sys.setrecursionlimit(2000000000)

n = int(input())
mix = [*map(int, input().split())]
visited = [False] * 20001

def find(f, a=1):
    visited[f] = True
    if visited[mix[f]-1]:
        return a
    return find(mix[f]-1, a+1)

def gcd(a, b):
    tmp = 0
    while b:
        tmp = a % b
        a = b
        b = tmp
    return a

r = 1
for i in range(n):
    d = find(i)
    r = r * d // gcd(r, d)
    

print(r)
