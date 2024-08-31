n = int(input())
weight = [*map(int, input().split())]

weight.sort()
min_sum = 1
for num in weight:
    if num > min_sum:
        break
    min_sum += num

print(min_sum)