import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())
K = int(input())

graph = {}

inf = float('inf')

queue = []
visited = [0] * (V+1)
distance = { K : 0 }

def calculate_distance(node):
    if node not in distance:
        distance[node] = inf
    return distance[node]

for _ in range(E):
    u, v, w = map(int, input().split())
    if u in graph:
        graph[u].append((v, w)) # (node, weight)
    else:
        graph[u] = [(v, w)]

heapq.heappush(queue, (0, K)) # (distance, node)

while queue:
    d, node = heapq.heappop(queue)
    
    if visited[node]:
        continue

    visited[node] = 1

    if calculate_distance(node) < d:
        continue
    
    if node not in graph:
        continue

    connected_nodes = graph[node]

    acc = calculate_distance(node)

    for i, w in connected_nodes:
        cd = calculate_distance(i)
        nd = min(acc+w, cd)
        heapq.heappush(queue, (nd, i))
        distance[i] = nd

for i in range(1, V+1):
    d = calculate_distance(i)
    if d == inf:
        print("INF")
    else:
        print(d)