from collections import deque

a, b, c, d = map(int, input().split())

queue = deque()
visited: dict = {}

queue.append((0, (0,0)))
visited[(0,0)] = 1
found = False

answer = float('inf')
while queue:
    (now, (e, f)) = queue.popleft()

    if c==e and d==f:
        answer = min(answer, now)


    temp = []
    temp.append((a, f))
    temp.append((e, b))
    temp.append((0, f))
    temp.append((e, 0))

    # e -> f
    if e >= b-f:
        temp.append((e-(b-f),b))
    else:
        temp.append((0, e+f))
    
    if f >= a-e:
        temp.append((a, f-(a-e)))
    else:
        temp.append((e+f, 0))

    for cc in temp:
        if cc in visited.keys():
            if not visited[cc]:
                visited[cc] = 1
                queue.append((now+1, cc))
        else:
            visited[cc] = 1
            queue.append((now+1, cc))


if answer == float('inf'):
    print(-1)
else:
    print(answer)