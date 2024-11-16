import sys

input = lambda: sys.stdin.readline().rstrip()

n,k = map(int, input().split())
numbers = [*map(int, input().split())]
cards = [None] * n

def chr2int(c): return ord(c)-65

for i in range(n):
    ti, ui = input().split()
    cards[i] = (ti,int(ui))
deck = [[], [], [],[]]

for card in cards:
    i = chr2int(card[0])
    deck[i].append(card)

for i in range(4):
    deck[i].sort(reverse=True)

for i in range(k):
    large = numbers
    card = ('E', 0)
    for i in range(4):
        if len(deck[i]) == 0:
            continue
        v = deck[i][0] # ex) ('A', 1)
        t = chr2int(v[0]) # 'A' -> 0

        temp = [*numbers]
        temp[t] += v[1]

        if temp[0]*temp[1]*temp[2]*temp[3] > large[0]*large[1]*large[2]*large[3]:
            large = temp
            card = v

    print(card[0], card[1])

    n = chr2int(card[0])
    deck[n].pop(0)
    numbers = large