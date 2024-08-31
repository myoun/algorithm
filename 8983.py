import bisect

m,n,l = map(int, input().split())
p = [*map(int, input().split())]

animals = []

for i in range(n):
    x, y = map(int, input().split())
    animals.append((x,y))

p.sort()
count = 0
for (x,y) in animals:
    left = bisect.bisect_left(p, x+y-l)

    if left >= len(p):
        continue

    c = p[left]
    d = abs(c-x)+y

    if d <= l:
        count += 1

print(count)