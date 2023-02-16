from itertools import permutations

n = int(input())
shapes = [*map(int, input().split())]

perms = permutations({0,1,2})


# 세모 네모 동그라미
scnt = [0,0,0]

for i in range(n):
    if shapes[i] == 1:
        scnt[0] += 1
    elif shapes[i] == 2:
        scnt[1] += 1
    else:
        scnt[2] += 1

mini = float('inf')

for perm in perms:
    cnt = [[0,0,0], [0,0,0], [0,0,0]]

    for i in range(n):
        if i < scnt[perm[0]]:
            cnt[0][shapes[i]-1] += 1
        elif i < scnt[perm[0]] + scnt[perm[1]]:
            cnt[1][shapes[i]-1] += 1
        else:
            cnt[2][shapes[i]-1] += 1

    ans = cnt[0][perm[1]] + cnt[0][perm[2]] + max(cnt[1][perm[2]], cnt[2][perm[1]])
    mini = min(ans, mini)

print(mini)