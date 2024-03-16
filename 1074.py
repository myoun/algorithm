N, r, c = map(int, input().split())

def board(n, r, c):
    if n == 1:
        return [[0,1], [2,3]][r][c]


    if r > (2**(n-1))-1:
        # 3, 4번째
        if c > (2**(n-1))-1:
            # 4번째
            return (2**(2*n-2))*3 + board(n-1, r-int((2**(n))/2), c-int((2**(n))/2))
        else:
            # 3번째
            return (2**(2*n-2))*2 + board(n-1, r-int((2**(n))/2), c)
            # 2^1에서 3열 1행 => 3-int(1)=2열 1행으로 변환
    else:
        # 1, 2번째
        if c > (2**(n-1))-1:
            # 2번째
            return (2**(2*n-2)) + board(n-1, r, c-int((2**(n))/2))
        else:
            # 1번째
            return board(n-1, r, c)

print(board(N, r, c))   