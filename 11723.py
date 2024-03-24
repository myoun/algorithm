import sys

M = int(input())

S = 0

for i in range(M):
    r = sys.stdin.readline().rstrip().split()

    if len(r) > 1:
        n = int(r[1])-1
        match r[0]:
            case 'add':
                S |= (1<<n)
            case 'remove':
                if (S & (1<<n)):
                    S &= ~(1<<n)
            case 'check':
                print(1 if S & (1<<n) != 0 else 0)
            case 'toggle':
                S ^= (1<<n)
    else:
        match r[0]:
            case 'all':
                S = (1<<20)-1
            case 'empty':
                S = 0
