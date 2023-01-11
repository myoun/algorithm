# 시간 초과

X = int(input())

line = 1
count = 0

while X > count + line:
    count += line
    line += 1

if line % 2 == 0:
    print(f"{X-count}/{line+count-X+1}")
else:
    print(f"{line+count-X+1}/{X-count}")
