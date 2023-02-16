import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    c = int(input())

    if c == 0:
        print(0 if len(heap) == 0 else heappop(heap)[1])
    else:
        heappush(heap, (abs(c), c))
