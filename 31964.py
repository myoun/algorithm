N = int(input())

homes = list(map(int, input().split()))
times = list(map(int, input().split()))

info = {}

for i, e in enumerate(homes):
    info[e] = times[i]
pos = 1
time = 1
forward = 1
picked = []

while pos != 0:
    if pos in info:
        t = info[pos]

        if pos == homes[-1]:
            forward = -1

        if t <= time:
            picked.append(pos)
        else:
            if forward == -1:
                if time < t:
                    time += t-time
                picked.append(pos)
    pos += 1*forward
    time += 1

print(time)