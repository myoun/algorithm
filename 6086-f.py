from collections import deque

N = int(input())

INF = float("inf")

graph = {}

result = 0
c = [[0 for _ in range(52)] for _ in range(52)]
f = [[0 for _ in range(52)] for _ in range(52)]
d = [-1] * 52

a = [[] for _ in range(52)]

def maxFlow(start, end):
    global result
    while 1:
        d = [-1] * 52
        q = deque()
        q.append(start)
        while q:
            x = q.popleft()
            for y in a[x]:
                if c[x][y] - f[x][y] > 0 and y not in d:
                    q.append(y)
                    d[y] = x
                    if y == end: break
        if d[end] == -1: break
        flow = INF
        i = end
        while i != start:
            flow = min(flow, c[d[i]][i] - f[d[i]][i])
            i = d[i]
        
        i = end
        while i != start:
            f[d[i]][i] += flow
            f[i][d[i]] -= flow
            i = d[i]
        result += flow

table = {}
b = 0
for i in range(N):
    x, y, cap = input().split()
    if x not in table:
        table[x] = b
        table[b] = x
        b += 1
    
    if y not in table:
        table[y] = b
        table[b] = y
        b += 1
    m, n = table[x], table[y]
    a[m].append(n)
    a[m].append(n)

    c[m][n] += int(cap)
    c[n][m] += int(cap)


maxFlow(table["A"], table["Z"])
print(result)