n = int(input())

bd = sorted([(lambda x: (int(x[0]), abs(int(x[1]))))(input().split()) for i in range(n)], key=lambda x: x[0])

dp = [0] + [2000001] * 10001

for i in range(0, n):
    ym = 0
    for j in range(i, -1, -1):
        a = bd[j]
        b = bd[i]
        ym = max(ym, a[1], b[1])
        minwidth = abs(a[0]-b[0])

        cw = max(ym * 2, minwidth)

        dp[i+1] = min(dp[i+1], dp[j] + cw)

print(dp[n])