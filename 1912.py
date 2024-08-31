n = int(input())
arr = list(map(int, input().split()))

li = [0] * n

for i in range(n):
    if i == 0:
        li[i] = arr[i]
    else:
        if li[i-1] > 0:
            li[i] = arr[i] + li[i-1]
        else:
            li[i] = arr[i]

print(max(li))