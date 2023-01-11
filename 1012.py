import sys
sys.setrecursionlimit(100000)
T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())
    farm = [[0 for i in range(M+2)] for i in range(N+2)]
    for k in range(K):
        x, y = map(int, input().split())
        farm[y+1][x+1] = 1
        
    visited = [[False for i in range(M+2)] for i in range(N+2)]

    def dfs(row, column):
        visited[row][column] = True

        a = 1
        if farm[row][column+1] != 0:
            if not visited[row][column+1]:
                a += dfs(row, column + 1)
        if farm[row][column-1] != 0:
            if not visited[row][column-1]:
                a += dfs(row, column -1)
        if farm[row+1][column] != 0:
            if not visited[row+1][column]:
                a += dfs(row +1, column)
        if farm[row-1][column] != 0:
            if not visited[row-1][column]:
                a += dfs(row-1, column)

        return a
    
    b = []

    for row in range(1, N+1):
        for column in range(1, M+1):
            if farm[row][column] == 1 and not visited[row][column]:
                r = dfs(row, column)
                b.append(r)

    print(len(b))

    