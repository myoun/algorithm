import sys
from collections import deque

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
queue = deque()

cnt = 1
order = [0] * (n+1)

def bfs(s):
    global cnt
    visited[s] = True
    order[s] = 1
    queue.append(s)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                cnt += 1
                order[v] = cnt
                queue.append(v)

bfs(r)

for i in range(1, n+1):
    print(order[i])