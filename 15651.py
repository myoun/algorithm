N, M = map(int, input().split())

def a(idx, now):
    if idx == M:
        print(" ".join(now))
        return
    else:
        for i in range(1, 1+N):
            a(idx + 1, now + [str(i)])
a(0, [])