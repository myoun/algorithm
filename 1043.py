N, M = map(int, input().split()) # 사람의 수, 파티의 수

parties = [] # 파티들
parent = [i for i in range(N+1)] # 사람 노드의 부모 노드

def find(x):
    if x == parent[x]: return x
    return find(parent[x])

def union(x, y):
    nx = find(x)
    ny = find(y)
    if nx != ny:
        parent[nx] = ny

raw = [*map(int, input().split())]
if len(raw) == 1: # 거짓말을 아는 사람이 없다면
    for i in range(M):
        input()
    print(M)
    exit()

if len(raw) > 2:
    for i in range(2, raw[0]+1):
        union(raw[i-1], raw[i])

tr = raw[1]

for i in range(M):
    raw = [*map(int, input().split())]
    parties.append(raw[1:])

for p in parties:
    if len(p) > 1:
        for i in range(1, len(p)):
            union(p[i-1], p[i])
    
troot = find(tr)
s = 0
for p in parties:
    fail = False
    for e in p:
        if find(e) == troot:
            fail = True
    
    if not fail:
        s += 1

print(s)