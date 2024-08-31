N, K = map(int, input().split())
table = list(input())

eaten = [False] * 20000

ep = 0

for s in range(N):
    if table[s] == "P":
        for i in range(s-K, s+K+1):
            if i < 0 or i >= N:
                continue

            sf = (s, i)
            v = 1
            if table[i] == "H" and not eaten[i]:
                eaten[i] = True
                ep += 1
                break
        
print(ep)