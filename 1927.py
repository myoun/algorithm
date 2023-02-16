from heapq import heappop, heappush
import sys

input = sys.stdin.readline

heap = []

n = int(input())

for i in range(n):
    c = int(input())

    if c == 0:
        print(0 if len(heap) == 0 else heappop(heap))
    else:
        heappush(heap, c)
