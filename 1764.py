N, M = map(int, input().split())

neverheard = set()
neverseen = set()

for i in range(N):
    neverheard.add(input())

for i in range(M):
    neverseen.add(input())

neverheardseen = list(neverheard.intersection(neverseen))

neverheardseen.sort()

print(len(neverheardseen))
for p in neverheardseen:
    print(p)