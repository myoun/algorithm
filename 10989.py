import sys

input = sys.stdin.readline

n = int(input())

nums = [0] * 10001

for i in range(n):
    d = int(input())
    nums[d] += 1

for i in range(10001):
    num = nums[i]
    for _ in range(num):
        print(i)