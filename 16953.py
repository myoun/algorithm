from collections import deque

A, B = map(int, input().split())

queue = deque()

queue.append((A, 0))

p = False
r = -1

while queue:
    n, i = queue.popleft()

    if n == B:
        p = True
        r = i+1
        break
    elif n > B:
        continue
    
    queue.append((n*2, i+1))
    queue.append((n*10+1, i+1))

print(r)