n = int(input())

li = [-1] * 1000001

li[1] = 1
li[2] = 2
li[3] = 3

for i2 in range(4, n+1):
    li[i2] = (li[i2-2] + li[i2-1]) % 15746

print(li[n])