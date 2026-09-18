from heapq import heappop, heappush

n, k = map(int, input().split())

customers = [tuple(map(int, input().split())) for i in range(n)]
# i(고객 번호), w(물건의 수)

heap1 = [] # (비는 시간, 계산대 번호)
heap2 = [] # (물건의 수 = 종료 시간, -계산대 번호, 고객 번호)

a = 1

for (i, w) in customers:
    if a <= k:
        heappush(heap2, (w, -a, i))
        heappush(heap1, (w, a))
    else:
        m_w, m_a = heappop(heap1)
        heappush(heap2, (m_w+w, -m_a, i))
        heappush(heap1, (m_w+w, m_a))
    a += 1

r = 0
rn = 1

for i in range(len(heap2)):
    r += rn * heappop(heap2)[2]
    rn += 1

print(r)
