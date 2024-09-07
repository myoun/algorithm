n, m = map(int, input().split())
nums = [*map(int, input().split())]

ijs = []

for _ in range(m):
    ijs.append(tuple(map(int, input().split())))

s = [0] * (n+1)

for i in range(len(nums)):
    s[i+1] = s[i] + nums[i]

for i, j in ijs:
    print(s[j]-s[i-1])