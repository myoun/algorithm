k = int(input())
c = int(input())

for i in range(c):
    m, n = map(int, input().split())
    if m == n:
        print(1)
    else:
        gap = abs(m-n)
        rem = k - max(m,n)

        # 동수가 더 많은 경우에는 점수와 남은 라운드수 1점은 극복 가능
        if m < n:
            if gap - rem <= 1:
                print(1)
            else:
                print(0)
        # 영희가 더 많은 경우에는 2점까지 극복 가능
        else:
            if gap - rem <= 2:
                print(1)
            else:
                print(0)