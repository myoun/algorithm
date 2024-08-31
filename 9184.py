li = {}
def w(a: int, b: int, c: int) -> int:
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if (a,b,c) in li.keys():
        return li[(a,b,c)]
    if a > 20 or b > 20 or c > 20:
        li[(a,b,c)] = w(20, 20, 20)
        return li[(a,b,c)]
    if a < b and b < c:
        li[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return li[(a,b,c)]

    li[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return li[(a,b,c)]

while True:
    a,b,c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")