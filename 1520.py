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