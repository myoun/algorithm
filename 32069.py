from collections import deque

l, n, k = map(int, input().split())

A = [*map(int, input().split())]

queue = deque(map(lambda x: (x, 0), A))
visited = set()
result = []

while queue:
    a, b = queue.popleft()
    
    if len(result) == k:
        break

    if a in visited:
        continue
    
    visited.add(a)
    result.append(b)
    
    if a+1 <= l:
        queue.append((a+1, b+1))
    if a-1 >= 0:
        queue.append((a-1, b+1))

for r in result:
    print(r)
