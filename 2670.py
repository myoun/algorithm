N = int(input())

nums = [float(input()) for _ in range(N)]

m = nums[0]
a = nums[0]

for i in range(1, N):
    if a < 1:
        a = 1

    a *= nums[i]
    if a > m:
        m = a

s = "{:.3f}".format(m)
print(s)