from collections import deque

n, m = map(int, input().split())

graph = [[0] * (n+2)]

for i in range(n):
    graph.append(list(map(int, input())))

graph.append([0] * (n+2))



visited = [[False for i in range(m+2)] for i in range(n+2)]

queue = deque()

queue.append((1,1))

move = 0


while queue:
    u = queue.popleft()
    if u == (n, m):
        print(move)
        break

    move += 1

    # visited[u[0]][u[1]] = True

    if u[0] == 0 or u[1] == 0 or u[0] == n or u[1] == m:    
        continue

    print(u)

    if graph[u[0]][u[1]+1] != 0:
        queue.append((u[0], u[1]+1))
    if graph[u[0]][u[1]-1] != 0:
        queue.append((u[0], u[1]-1))
    if graph[u[0]+1][u[1]] != 0:
        queue.append((u[0]+1, u[1]))
    if graph[u[0]-1][u[1]] != 0:
        queue.append((u[0]-1, u[1]))
    
