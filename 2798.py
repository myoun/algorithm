N, M = map(int, input().split())
cards = list(map(int, input().split()))

list1 = set()

for i1, a in enumerate(cards):
    ca = cards.copy()
    ca.pop(i1)
    for i2, b in enumerate(ca):
        cb = ca.copy()
        cb.pop(i2)
        for i3, c in enumerate(cb):
            cc = cb.copy()
            if (a+b+c <= M):
                list1.add(a+b+c)

print(max(list1))