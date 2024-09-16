n = int(input())

graph = {}
parent = {}

for i in range(n-1):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
while stack:
    node = stack.pop()
    for i in graph[node]:
        if i not in parent:
            parent[i] = node
            stack.append(i)

for i in range(2, n+1):
    print(parent[i])
