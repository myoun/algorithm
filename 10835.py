import sys
n = int(input())

dp = [[-1 for i in range(2001)] for i in range(2001)]

l = [*map(int, input().split())]
r = [*map(int, input().split())]

sys.setrecursionlimit(10**5)

def solve(left, right):
    # 둘중에 하나라도 다 바닥나면 끝
    if left == n or right == n:
        return 0
    
    if dp[left][right] != -1:
        return dp[left][right]
    
    dp[left][right] = 0

    # 오른쪽 카드를 버림
    if r[right] < l[left]:
        dp[left][right] += r[right] + solve(left, right+1)
    else:
        # 왼쪽이나 둘다 버리는거 중 큰거
        dp[left][right] += max(solve(left+1, right), solve(left+1, right+1))

    return dp[left][right]

print(solve(0,0))