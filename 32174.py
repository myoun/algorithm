N, M = map(int, input().split())

procedure = [tuple(map(int, input().split())) for _ in range(M)]

history = [1]

for p, i in procedure:
    match p:
        case 1:
            c  = history[-1]+i
            if c > N:
                c -= N*(c//N)
            history.append(c)
        case 2:
            c = history[-1]-i
            if c < 1:
                c += N*(-c//N+1)
            history.append(c)
        case 3:
            history.append(history[i])

print(history[-1])