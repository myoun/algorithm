N = int(input())

def b(li, k):
    if k == N:
        return 1
    ans = 0
    for i in range(N):
        ok = True
        for i2 in range(k):
            if k + i == i2 + li[i2] or k - i == i2 - li[i2] or li[i2] == i:
                ok  = False
                break
        if ok:
            ans += b(li+[i], k+1)
    return ans

print(b([], 0))