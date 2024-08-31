n = int(input())
spots = list(map(int, input().split()))

ps = [0] * (n+1)

for i in range(n):
    ps[i+1] = spots[i] + ps[i]

mh = 0

for i in range(2, n):
    mh = max(ps[i-1] + ps[-2] - ps[i] + ps[i-1], ps[-1] - ps[1] + ps[-1] - ps[i] - ps[i] + ps[i-1], ps[i] - ps[1] + ps[-2] - ps[i-1], mh)

print(mh)