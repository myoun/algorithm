import heapq
import sys

n = int(sys.stdin.readline())

pq = []

com = [-1] * n

for i in range(n):
    inp = int(sys.stdin.readline())
    com[i] = inp
    
for c in com:
    if c == 0:
        n = 0 if len(pq) == 0 else heapq.heappop(pq)[1]
        print(n)
    else:
        heapq.heappush(pq, (-c, c))
