a, b, c = map(int, input().split())

sorted_dice = sorted([a,b,c])

money = 0

if a == b and b == c:
    money = 10000 + a * 1000
elif a != b and b != c and c != a:
    money = sorted_dice[-1] * 100
else:
    money = 1000 + sorted_dice[1] * 100

print(money)