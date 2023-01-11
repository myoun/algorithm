n = int(input())

graph = [[0] * (n+2)]

for i in range(n):
    graph.append([0] + list(map(int, input())) + [0])

graph.append([0] * (n+2))

visited = [[False for i in range(n+2)] for i in range(n+2)]


def dfs(row, column):
    visited[row][column] = True

    a = 1

    if graph[row][column+1] != 0:
        if not visited[row][column+1]:
            a += dfs(row, column + 1)
    if graph[row][column-1] != 0:
        if not visited[row][column-1]:
            a += dfs(row, column -1)
    if graph[row+1][column] != 0:
        if not visited[row+1][column]:
            a += dfs(row +1, column)
    if graph[row-1][column] != 0:
        if not visited[row-1][column]:
            a += dfs(row-1, column)

    return a

danji = []

for row in range(1, n+1):
    for column in range(1, n+1):
        if graph[row][column] == 1 and not visited[row][column]:
            danji.append(dfs(row, column))

danji.sort()

print(len(danji))
for d in danji:
    print(d)