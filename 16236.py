from collections import deque

def bfs(start, shark_size, grid):
    N = len(grid)
    dist = [[-1] * N for _ in range(N)]
    sx, sy = start
    q = deque([(sx, sy)])
    dist[sx][sy] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (0,-1), (0,1), (1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                if grid[nx][ny] > shark_size:
                    continue
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

def find_fish(shark, grid):
    N = len(grid)
    sx, sy = shark[0], shark[1]
    shark_size = shark[2]
    dist = bfs((sx, sy), shark_size, grid)
    
    candidate = []
    for i in range(N):
        for j in range(N):
            # 먹을 수 있는 물고기: 숫자가 0보다 크고 상어 크기보다 작아야 함
            if 0 < grid[i][j] < shark_size and dist[i][j] != -1:
                candidate.append((dist[i][j], i, j))
    
    if not candidate:
        return None
    
    # 규칙에 따라 정렬: 거리, 행 번호, 열 번호 순
    candidate.sort()
    return candidate[0]  # (거리, 행, 열)

# 입력 받기
N = int(input())
grid = []
shark = []  # [x, y, size]
for i in range(N):
    row = list(map(int, input().split()))
    for j, value in enumerate(row):
        if value == 9:
            shark = [i, j, 2]  # 아기 상어 초기 위치 및 크기
            row[j] = 0      # 상어가 있는 칸은 빈 칸으로 처리
    grid.append(row)

time = 0
eat_count = 0

while True:
    result = find_fish(shark, grid)
    if result is None:
        break
    dist_to_fish, fish_x, fish_y = result
    # 상어 이동
    time += dist_to_fish
    shark[0], shark[1] = fish_x, fish_y
    # 물고기 먹기: 해당 칸을 빈 칸으로 만듦
    grid[fish_x][fish_y] = 0
    eat_count += 1
    # 크기 증가 확인
    if eat_count == shark[2]:
        shark[2] += 1
        eat_count = 0

print(time)
