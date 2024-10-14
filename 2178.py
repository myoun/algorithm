from collections import deque

n,m = map(int, input().split())
maze = [[*map(int, input())] for _ in range(n)]

queue = deque()

queue.append((0,0,1))

visited = set()

min_t = float('inf')

while queue:
    x, y, t = queue.popleft()

    if (x,y) in visited:
        continue

    visited.add((x,y))
    if (x,y) == (n-1,m-1):
        min_t = t
        break

    if x > 0 and maze[x-1][y]:
        queue.append((x-1, y, t+1))
    if y > 0 and maze[x][y-1]:
        queue.append((x, y-1, t+1))
    if x+1 < n and maze[x+1][y]:
        queue.append((x+1, y, t+1))
    if y+1 < m and maze[x][y+1]:
        queue.append((x, y+1, t+1))

print(min_t)