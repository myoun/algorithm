import bisect

T = int(input())
n = int(input())
A = [*map(int, input().split())]
m = int(input())
B = [*map(int, input().split())]

apsum = [0] * (n+1)
bpsum = [0] * (m+1)

for i in range(1, n+1):
    apsum[i] = apsum[i-1] + A[i-1]

for i in range(1, m+1):
    bpsum[i] = bpsum[i-1] + B[i-1]

asum = []
bsum = []


for i in range(n+1):
    for j in range(i+1, n+1):
        sum_sub_A = apsum[j] - apsum[i]
        asum.append(sum_sub_A)

for i in range(m+1):
    for j in range(i+1, m+1):
        sum_sub_B = bpsum[j] - bpsum[i]
        bsum.append(sum_sub_B)

bsum.sort()

ans = 0

for i in range(len(asum)):
    f = T - asum[i]

    up = bisect.bisect_right(bsum, f)
    lp = bisect.bisect_left(bsum, f)

    ans += up - lp

print(ans)