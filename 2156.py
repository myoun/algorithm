import sys

sys.setrecursionlimit(10000000)

n = int(input())
juice = []
for i in range(n):
    juice.append(int(input()))

dp = [-1] * 10001

def solve(i):
    if i >= n:
        return -1
    # 마시거나 안마시거나
    if i == 0:
        dp[i] = max(solve(1), solve(2)) + juice[i-1]
        return dp[i]

    if dp[i-1] - dp[i-2] == 1:
        dp[i] = solve(i+2) + juice[i-1]
        return dp[i]

    dp[i] = max(solve(i+1), solve(i+2) + juice[i-1])
    return dp[i]

print(solve(0))