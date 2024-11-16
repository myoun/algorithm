from itertools import*
def t(b,c):
    for i in c:b^=7<<3*i if i<3 else 73<<(i-3)if i<6 else 273 if i<7 else 84
    return b
def s(b):
    for r in range(9):
        if any(t(b,x)in{0,511}for x in combinations(range(8),r)):print(r);return
    print(-1)
for _ in range(int(input())):s(sum(1<<(3*i+j)for i in range(3)for j,x in enumerate(input().split())if x=="T"))