dp = {}

def fibonacci(n):
    if n in dp:
        return dp[n]
    if (n == 0):
        dp[0] = (0, 1, 0)
        return dp[0]
    elif (n == 1):
        dp[1] = (1, 0, 1)
        return dp[1]
    else:
        l = fibonacci(n-1)
        m = fibonacci(n-2)
        dp[n] = (l[0]+m[0], l[1]+m[1], l[2]+m[2])
        return dp[n]

t = int(input())

for i in range(t):
    n = int(input())
    r = fibonacci(n)
    print(r[1], r[2])

