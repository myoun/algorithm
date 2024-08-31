import sys
from collections import deque

computers = int(input())
connections = int(input())

graph = [[] for i in range(computers+1)]

for i in range(connections):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i, a in enumerate(graph):
    graph[i] = sorted(a)

visited = [False] * (computers+1)
queue = deque()

def bfs(s):
    cnt = 0
    visited[s] = True
    queue.append(s)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                cnt += 1
                queue.append(v)
    return cnt

print(bfs(1))