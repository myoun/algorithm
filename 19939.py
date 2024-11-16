n, k = map(int, input().split())

l = [*range(1, k+1)]
if k*(k+1)//2 > n:
    print(-1)
    exit()

emt = len(l)

for i in range((k*(k+1)//2), n):
    if emt == len(l):
        emt -= 1
        l.append(l[-1]+1)
        l[-2] = 0
    else:
        l[emt] = l[emt-1]+1
        l[emt-1] = 0
        emt -= 1
        if emt == 0:
            l.pop(0)
            emt = len(l)
    
print(l[-1]-l[0])