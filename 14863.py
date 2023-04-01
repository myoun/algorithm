n, k = map(int, input().split())

sections = [list(map(int, input().split())) for _ in range(n)]


# 구간 i까지 봤을 때, 최대 j분의 행군으로 얻을 수 있는 최대 금액
dp = [[(0,0) for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(0, k+1):
        walk_time, walk_money, ride_time, ride_money = sections[i-1]

        pride = dp[i-1][j-ride_time]
        pwalk = dp[i-1][j-walk_time]

        if pwalk[1] + walk_time > j:
            dp[i][j] = (pride[0]+ride_money, pride[1]+ride_time)
        elif pride[1] + ride_time > j:
            dp[i][j] = (pwalk[0]+walk_money, pwalk[1]+walk_time)
        else:
            dp[i][j] = max((pride[0]+ride_money, pride[1]+ride_time), (pwalk[0]+walk_money, pwalk[1]+walk_time))

print(dp[n][k][0])