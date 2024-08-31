from collections import deque
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

def dfs():
    visited = [False] * (n+1)
    order = []

    def idfs(s):
        visited[s] = True
        order.append(s)

        for x in graph[s]:
            if not visited[x]:
                idfs(x)

    idfs(r)

    print(" ".join(map(str, order)))

def bfs():
    visited = [False] * (n+1)
    queue = deque()

    order = [r]

    visited[r] = True
    queue.append(r)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                order.append(v)
                queue.append(v)

    print(" ".join(map(str, order)))


dfs()
bfs()