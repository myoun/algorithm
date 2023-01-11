N = int(input())

cards = list(map(int, input().split()))

m = 987654321
for i in range(N-1):
    for j in range(i+1, N):
        if (cards[i] - cards[j]) % (j-i) == 0:
            d = ((cards[i] - cards[j]) // (j-i))
            cnt = i
            for c in range(i+1, N):
                if cards[i] - cards[c] != d*(c-i):
                    cnt += 1
            m = min(cnt, m)

print(m)