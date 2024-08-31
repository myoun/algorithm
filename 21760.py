t = int(input())
case = [[*map(int, input().split())] for i in range(t)]

for i in range(t):
    n, m, k, d = case[i]
    j = -1

    for b in range(1, d+1):
        a = b*k
        dif = (n-1)*m*b*n*m
        sam = (m-1)*a*n*m
        all = (dif+sam) // 2
        if all <= d:
            j = max(j, all)
        else:
            break
    print(j)