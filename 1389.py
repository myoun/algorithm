N, M = [*map(int, input().split())]

INF = float('inf')
graph = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for i in range(M):
    A, B = map(int, input().split())
    graph[A-1][B-1] = 1
    graph[B-1][A-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

smallest = INF
smallest_idx = INF

for i in range(N):
    s = sum(graph[i])
    if s <= smallest:
        if s == smallest:
            smallest_idx = min(i, smallest_idx)
        else:
            smallest = s
            smallest_idx = i

print(smallest_idx+1)
