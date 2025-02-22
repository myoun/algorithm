<<<<<<< HEAD
import heapq

N, M = map(int, input().split())

field = [[*map(int, input().split())] for _ in range(N)]
box = [[0 for _ in range(M)] for _ in range(N)]
box[0][0] = 1
v = {}
v[(0,0)] = 1

pq = []
pq.append((-field[0][0], (0, 0,), (-1, -1)))

while pq:
    h, (x,y), (ox, oy) = heapq.heappop(pq)
    box[x][y] += box[ox][oy]

    if v[(x,y)] > 1:
        v[(x,y)] -= 1
        continue

    for a, b in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        if 0 <= x+a < N and 0 <= y+b < M:
            fh = field[x+a][y+b]
            if -fh > h:
                heapq.heappush(pq, (-fh, (x+a, y+b,), (x,y,)))
                if (x+a, y+b) not in v:
                    v[(x+a,y+b)] = 1
                else:
                    v[(x+a,y+b)] += 1

print(box[N-1][M-1])
=======
from collections import deque

M, N = map(int, input().split())

field = [[*map(int, input().split())] for _ in range(N)]

queue = deque()

queue.append((0, 0))

r = 0

while queue:
    x, y = queue.popleft()

    if (x,y) == (M-1, N-1):
        r += 1

    ch = field[x][y]

    for a, b in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        if 0 <= x+a < M and 0 <= y+b < N:
            fh = field[x+a][y+b]
            if ch > fh:
                queue.append((x+a, y+b))

print(r)
>>>>>>> 5348f9d31aa50e3c60c966b9fc60b5495ca9389b
