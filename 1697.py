import heapq

N, K = map(int, input().split())

INF = float('inf')

distance = {}

q = []
v = [0] * 100001
heapq.heappush(q, (0, N))
distance[N] = 0

def calc_distance(node):
    if node not in distance:
        distance[node] = INF
    return distance[node]

shortest = None

while q:
    dist, node = heapq.heappop(q)
    if v[node]:
        continue
    if node == K:
        shortest = dist
        break
    v[node] = 1

    if calc_distance(node) < dist:
        continue

    for next in [1, -1, 2]:
        cost = calc_distance(node) + 1
        if next == 2:
            if cost < calc_distance(node*next):
                distance[node*next] = cost
                if 0 <= node*next <= 100000:
                    heapq.heappush(q, (cost, node*next))
        else:
            if cost < calc_distance(node+next):
                distance[node+next] = cost
                if 0 <= node+next <= 100000:
                    heapq.heappush(q, (cost, node+next))
    
print(shortest)