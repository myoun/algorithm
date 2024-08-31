import sys

sys.setrecursionlimit(987654321)

n, m, r = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i, a in enumerate(graph):
    graph[i] = sorted(a)

visited = [False] * (n+1)

cnt = 0
order = [0] * (n+1)

def dfs(s):
    global cnt
    
    visited[s] = True
    cnt += 1
    order[s] = cnt

    for x in graph[s]:
        if not visited[x]:
            dfs(x)

dfs(r)

for i in range(1, n+1):
    print(order[i])