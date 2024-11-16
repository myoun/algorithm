n = int(input())
seq = [*map(int, input().split())]

next = "B"

for a in range(-200, 201):
    for b in range(-20000, 20000):
        check = True
        for i in range(1, len(seq)):
            if seq[i] != a*seq[i-1]+b:
                check = False
                break
        if check and next != a*seq[-1]+b:
            if next == "B":
                next = a*seq[-1]+b
            else:
                next = "A"

print(next)