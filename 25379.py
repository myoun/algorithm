n = int(input())

arr = list(map(int,input().split()))

even = list(filter(lambda x: x % 2 == 0, arr))
odd = list(filter(lambda x: x % 2 == 1, arr))

result1 = even + odd
result2 = odd + even

evenn = 0
oddn = 0

i1 = 0
i2 = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        if arr[i] == result1[i1]:
            evenn += i - i1
            i1 += 1
    else:
        if arr[i] == result2[i2]:
            oddn += i - i2
            i2 += 1

print(min(evenn, oddn))