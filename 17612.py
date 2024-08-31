from heapq import heappop, heappush

n, k = map(int, input().split())

customers = [tuple(map(int, input().split())) for i in range(n)]
heap = []

ci = [0] * k

a = 1

for (i, w) in customers:
    if a <= k:
        heappush(heap, (w, -a, i))
        ci[a-1] = w
    else:
        m = min(enumerate(ci), key=lambda x: x[1])
        heappush(heap, (m[1]+w, -(m[0]+1), i))
        ci[m[0]] = m[1]+w
    a += 1

r = 0
rn = 1

for i in range(len(heap)):
    r += rn * heappop(heap)[2]
    rn += 1
print(r)