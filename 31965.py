import bisect
import sys

input = sys.stdin.readline
print = sys.stdout.write

N, Q = map(int, input().split())
H = [*map(int, input().split())]

prefix = [0]*(N+1)
for i in range(N):
    prefix[i+1] = prefix[i] + H[i]

def calculate_cost(i, L, R):
    k = R - L
    A_i = H[L+i]
    left_sum = prefix[L+i] - prefix[L]
    right_sum = prefix[R] - prefix[L+i+1]

    return i * A_i - left_sum + right_sum - (k-1-i) * A_i

def calculate_fatigue(L, R):
    k = R - L
     
    # 구간합
    total = prefix[R] - prefix[L]
     
    # 구간 내 첫 집의 비용
    cost0 = total - k*H[L]
    cost_last = k*H[R-1] -  total

    max_cost = max(cost0, cost_last)
    m = (k-1) // 2
    cost_m = calculate_cost(m, L, R)
    if k % 2 == 0:
        cost_m1 = calculate_cost(m+1, L, R)
        min_cost = min(cost_m, cost_m1)
    else:
        min_cost = cost_m
    
    return max_cost - min_cost

for _ in range(Q):
    L, R = map(int, input().split())
    li, ri = bisect.bisect_left(H, L), bisect.bisect(H, R)
    if ri-li <= 1:
        fat = 0
    else:
        fat = calculate_fatigue(li, ri)
    print(str(fat)+"\n")