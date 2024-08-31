N = int(input())

times = []

for i in range(N):
    times.append(tuple(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))

q = [0]
blacklist = []

t = 0

while t+1 < N:
    a = times[t]
    v = False

    for i in range(t+1, N):
        b = times[i]
        if i in blacklist:
            continue
        
        if b[0] < a[1]:
            blacklist.append(i)
            continue

        if v:
            continue
        
        t = i
        q.append(i)
        v = True



print(len(q))