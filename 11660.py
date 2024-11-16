N, M = map(int, input().split())

table = [[*map(int, input().split())] for _ in range(N)]
pretable = []

for i in range(N):
    l = [table[i][0]]
    for j in range(1, N):
        l.append(l[-1]+table[i][j])
    pretable.append(l)

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    s = 0

    for i in range(x1, x2+1):
        a = pretable[i-1][y2-1]
        if y1 < 2:
            b = 0
        else:
            b = pretable[i-1][y1-2]
        s += a-b

    print(s)