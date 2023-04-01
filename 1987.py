r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = set()
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 0

def dfs(x, y, cnt):
    global ans

    ans = max(ans, cnt)
    visited.add(board[x][y])

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] not in visited:
                dfs(nx, ny, cnt + 1)

    visited.remove(board[x][y])

dfs(0, 0, 1)

print(ans)