A, B, V = map(int, input().split())

n = (V - B) / (A - B)

if (int(n) == n):
    print(int(n))
else:
    print(int(n)+1)