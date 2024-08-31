n = int(input())

dp = [-1] * 1000001

dp[0] = 0
dp[1] = 0

for x in range(2, n+1):
    v = dp[x-1]
    if x % 3 == 0:
        v = min(v, dp[x // 3])
    if x % 2 == 0:
        v = min(v, dp[x // 2])
    dp[x] = v + 1

print(dp[n])