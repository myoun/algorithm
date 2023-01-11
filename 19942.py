N = int(input())
mp, mf, ms, mv = map(int, input().split())

mat = [[0,0,0,0]]+[list(map(int, input().split())) for _ in range(N)]

# 재료 3개 -> 가격

def solve(*nums):
    sp, sf, ss, sv, p = 0,0,0,0,0

    for n in nums:
        m = mat[n]
        sp += m[0]
        sf += m[1]
        ss += m[2]
        sv += m[3]
        p += m[4]
    
    if sp < mp or sf < mf or ss < ms or sv < mv:
        return -1
    
    return p

mini = (987654321, [])


for i in range(2**N):
    has = []
    for n in range(N):
        if i & (i<<n) == i<<n:
          has.append(n+1)
    
    v = solve(*has)

    if v == -1:
        continue
    elif v == mini[0]:
        if has < mini[1]:
            mini = (v, has)
    elif v < mini[0]:
        mini = (v, has)

if mini[0] == 987654321:
    print(-1)
else:
    print(mini[0])
    print(*mini[1])