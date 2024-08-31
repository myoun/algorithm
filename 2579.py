stair_length = int(input())
stairs = []
for i in range(stair_length):
    stairs.append(int(input()))

li = [[-1 for i in range(301)] for i in range(2)]

def goUp(now, jump):
    if len(stairs) == now+1:
        return stairs[-1]
    if now >= len(stairs):
        return -987654321
    if (li[jump][now] != -1):
        return li[jump][now]
    if jump == 0:
        li[jump][now] = goUp(now+2, 1)+ stairs[now]
    else:
        li[jump][now] = max(goUp(now+1, 0)+stairs[now], goUp(now+2, 1)+stairs[now])
    return li[jump][now]

print(max(goUp(0, 1), goUp(1,1)))