from heapq import heappush, heappop

INF = float('inf')

N, M, X = map(int, input().split())

graph = {i:{} for i in range(1, N+1)}


for _ in range(M):
    i, d, t = map(int, input().split())
    graph[i][d] = t


adist = [0]*(N+1)


def least(f):
    dist = [INF]*(N+1)
    dist[f] = 0
    queue = [(0,f)]
    while queue:
        d, i = heappop(queue)
        connected = graph[i].items()
        for ni, nd in connected:
            if d+nd < dist[ni]:
                dist[ni] = d+nd
                heappush(queue, (d+nd, ni))
    dist[0] = 0
    return dist

bwd = least(X)

for i in range(1, N+1):
    fwd = least(i)
    adist[i] = fwd[X]+bwd[i]

print(max(adist))
