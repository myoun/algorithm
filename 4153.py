while True:
    a, b, c = sorted(map(int, input().split()))

    if a == 0 and b == 0 and c == 0:
        break

    aq, bq, cq = a * a, b * b, c* c

    if aq + bq == cq:
        print('right')
    else:
        print('wrong')