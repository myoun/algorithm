# import time

# start = time.time()

n = int(input())
nums = list(map(int, input().split()))

ns = [0] * 10001


for i in nums:
    ns[i] += 1

mn = float('inf')
mns = float('inf')

mni = mnsi = 987654321

for a in range(1, 10001):
    nd1 = 0
    nd2 = 0
    for b in range(1, 10001):
        nb = ns[b]
        t = abs(b-a)
        nd1 += t*nb
        nd2 += t*t*nb

    s1 = nd1
    s2 = nd2

    if s1 < mn:
        mn = s1
        mni = a

    if s2 < mns:
        mns = s2
        mnsi = a

print(mni, mnsi)

# print(time.time() - start)