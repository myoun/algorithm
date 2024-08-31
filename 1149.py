n = int(input())
costs = [[0,0,0]]

for i in range(n):
    costs.append(list(map(int, input().split())))

dp = [[0 for i in range(3)] for i in range(n+1)]

dp[0][0] = dp[0][1] = dp[0][2] = 0

for i in range(n+1):    
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(min(dp[n][0], dp[n][1]), dp[n][2]))