n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

dp = [[-1 for i in range(501)] for i in range(501)]


def solve(now, level):
    if n == 1:
        return triangle[0][0]
    if dp[level][now] != -1:
        return dp[level][now]

    if level == n:
        return triangle[n-1][now]
    
    dp[level][now] = triangle[level-1][now] + max(solve(now, level+1), solve(now+1, level+1))
    return dp[level][now]   

print(solve(0, 1))