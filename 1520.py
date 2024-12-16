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