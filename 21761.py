n,k = map(int, input().split())
numbers = [*map(int, input().split())]
cards = [None] * n

for i in range(n):
    ti, ui = input().split()
    cards[i] = (ti,int(ui))
deck = [[], [], [],[]]

for card in cards:
    if card[0] == 'A':
        deck[0].append(card)
    elif card[0] == 'B':
        deck[1].append(card)
    elif card[0] == 'C':
        deck[2].append(card)
    elif card[0] == 'D':
        deck[3].append(card)

for i in range(4):
    deck[i].sort(reverse=True)

for i in range(k):
    large = numbers
    card = ('E', 0)
    for i in range(4):
        if len(deck[i]) == 0:
            continue
        v = deck[i][0]
        temp = numbers.copy()
        if v[0] == 'A':
            temp[0] += v[1]
        elif v[0] == 'B':
            temp[1] += v[1]
        elif v[0] == 'C':
            temp[2] += v[1]
        elif v[0] == 'D':
            temp[3] += v[1]
        if temp[0]*temp[1]*temp[2]*temp[3] > large[0]*large[1]*large[2]*large[3]:
            large = temp
            card = v
    print(card[0], card[1])
    a = card[0]
    n = 'ABCD'.index(a)
    deck[n].pop(0)
    numbers = large