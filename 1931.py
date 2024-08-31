N = int(input())

times = []

for i in range(N):
    times.append(tuple(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))
last_idx = 0
count = 0

for i in range(len(times)):
    if times[i][0] >= last_idx:
        last_idx = times[i][1]
        count += 1
        continue
    else:
        continue

print(count)