n = int(input())

br = list(map(int, input().split()))

m = int(input())


if sum(br) <= m:
    print(max(br))
else:
    maxi = max(br)
    maxb = min(br)
    for i in range(1, maxi):
        new = list(map(lambda x: x if x <= i else i, br))
        if sum(new) <= m:
            maxb = max(new)
    print(maxb)