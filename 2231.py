N = int(input())

for i in range(0, N):
    num = str(i)
    n = len(num)
    a = 0
    total = 0

    while a < n:
        total = total + int(num[a])
        a = a + 1
    
    if total + i == N:
        print(i)
        break
else:
    print(0)