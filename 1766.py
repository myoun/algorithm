from heapq import heappush, heappop

n, m = map(int, input().split())
indegree = [0] * (n+1)

graph = [[] for i in range(n+1)]

for i in range(m):
    first, second = map(int, input().split())
    graph[first].append(second)
    indegree[second] += 1


result = []
q = []

isBreak = False

while len(result) < n:
    for i in range(1, n+1):
        if indegree[i] > 0 or i in result:
            continue
        heappush(q, i)
        while q:
            now = heappop(q)
            result.append(now)
            if graph[now]:
                for g in graph[now]:
                    indegree[g] -= 1
                    if indegree[g] == 0:
                        heappush(q, g)
        if len(result) == n:
            break
    if isBreak:
        break
        
print(" ".join(map(str, result)))