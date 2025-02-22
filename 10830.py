N, B = map(int, input().split())

A = [[*map(int, input().split())] for _ in range(N)] # N * N 행렬

def matmul(a, b):
    t_b = list(zip(*b))
    mat = [[0]*N for _ in range(N)]

    for i in range(N):
        r = a[i]
        for j in range(N):
            c = t_b[j]
            for k in range(N):
                mat[i][j] += r[k]*c[k]
            mat[i][j] %= 1000
    
    return mat

def matpow(a, b):
    if b == 1:
        # a^1
        return a
    elif b == 2:
        return matmul(a, a)
    elif b % 2 == 1:
        # a^(b-1) * a
        return matmul(matpow(a, b-1), a)
    else:
        # (a^(b/2))^2
        return matpow(matpow(a, b//2), 2)

r = matpow(A, B)

for i in range(N):
    for j in range(N):
        r[i][j] %= 1000

for i in range(N):
    print(*r[i])